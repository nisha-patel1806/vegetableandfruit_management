from django.shortcuts import render, redirect
from ecom_app.lib.tb_admin import tb_admin
from ecom_app.lib.tb_user import tb_user
from ecom_app.lib.tb_category import tb_category
from ecom_app.lib.tb_product import tb_product
from ecom_app.lib.tb_feedback import tb_feedback
from ecom_app.lib.tb_contact import tb_contact
from ecom_app.lib.tb_vendor import tb_vendor
from ecom_app.lib.tb_ordermaster import tb_ordermaster
from ecom_app.lib.tb_orderdetails import tb_orderdetails


#Mail
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def dashboard(request):
     return  render(request,'dashboard.html')
 
 
def cpassword(request):
    if 'useradmin' in request.COOKIES: 
        if request.method == 'GET':
            print("111111111111111")
            return render(request, 'changepassword.html', {})
        if request.method == 'POST':
            print("33333333")
            admin = tb_admin()
            admin.connectToDB('localhost', 'root', '')
            email = request.COOKIES['useradmin']
            npass = request.POST['npass']
            print(email)
            print(npass)
            admin.cpassword(npass,email)
            admin.closeConnection()
            return redirect(dashboard)
    else:
        return redirect(touserhome)

def touserhome(request):
    if request.method == 'GET':
        if 'useradmin' in request.COOKIES:
            return redirect(userhome)
        return render(request, 'login.html', {})
    if request.method == 'POST':
        user = request.POST['email']
        password = request.POST['password']
        admin = tb_admin()
        admin.connectToDB('localhost', 'root', '')
        if admin.authenticate(user, password):
            admin.closeConnection()
            response = redirect(userhome)
            response.set_cookie('useradmin', user)
            return response
        else:
            admin.closeConnection()
            return redirect(touserhome)

def fpass(request):
    if request.method == 'GET':
        return render(request, 'admin-forgotpass.html', {})
    if request.method == 'POST':
        user = request.POST['email']
        admin = tb_admin()
        admin.connectToDB('localhost', 'root', '')
        if admin.fprocess(user):
            admin.closeConnection()
            response = redirect(userhome)
            return response
        else:
            admin.closeConnection()
            return redirect(touserhome)

def signout(request):
    response = redirect(touserhome)
    response.delete_cookie('useradmin')
    return response
    #return render(request, 'login.html', {})

def userhome(request):
    if 'useradmin' in request.COOKIES:
        user = tb_user()
        user.connectToDB('localhost', 'root', '')
        if request.method == "POST":
            if request.POST['operation'] == 'delete':
                user.deleteUser(request.POST['delThis'])
                user.closeConnection()
                return redirect(userhome)
        users = user.getAllData()
        user.closeConnection()
        return render(request, 'user/home.html', {'users':users, 'total':len(users)})
    else:
        return redirect(touserhome)

def edituser(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST' and request.POST['operation'] == 'edit':
            user_id = request.POST['editThis']
            user = tb_user()
            user.connectToDB('localhost', 'root', '')
            users = user.getData(user_id)
            user.closeConnection()
            return render(request, 'user/edit.html', {'users': users})
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def editeduser(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST':
            user = tb_user()
            user.connectToDB('localhost', 'root', '')
            user_id = request.POST['id']
            user_name = request.POST['uname']
            gender = request.POST['gender']
            email = request.POST['email']
            mobile = request.POST['mobile']
            password = request.POST['password']
            address = request.POST['address']
            filePath = "/user/{}.jpg".format(user_name)
            from os import rename
            rename("ecom_app/static/images/user/{}.jpg".format(user.getData(user_id)[1]), "ecom_app/static/images{}".format(filePath))
            user.editUserWithPhoto(user_id, user_name, gender, email, mobile, password, address, filePath)
            try:
                photo = request.FILES['photo']
                f = open("ecom_app/static/images/user/{}.jpg".format(user_name), 'wb')
                for i in photo:
                    f.write(i)
                f.close()
            except:
                pass
            user.closeConnection()
            return redirect(userhome)
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def insertnewuser(request):
    if 'useradmin' in request.COOKIES:
        return render(request, 'user/insert.html', {})
    else:
        return redirect(touserhome)
 

def insertednewuser(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        user = tb_user()
        user.connectToDB('localhost', 'root', '')
        uname = request.POST['uname']
        gender = request.POST['gender']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']
        address = request.POST['address']
        imgData = request.FILES['photo']
        # imgData = imgData.read().decode()
        filePath = "/user/{}.jpg".format(uname)
        f = open("ecom_app/static/images{}".format(filePath), 'wb')
        for i in imgData:
            f.write(i)
        f.close()
        # sourceEncoding = "ISO-8859-1"
        # targetEncoding = "utf-8"
        # source = open("ecom_app/static/temp/0.jpg")
        # target = open("ecom_app/static/temp/0.jpg", "w")
        # target.write(source.read())
        # source.close()
        # target.close()
        # f = open("ecom_app/static/temp/0.jpg", 'rb')
        # imgData = f.read().decode()
        # f.close()
        user.insertUser(uname, gender, email, mobile, password, address, filePath)
        user.closeConnection()
        return redirect(userhome)
    else:
        return redirect(touserhome)

def useractive(request):
    if 'useradmin' in request.COOKIES:
        stuObj = tb_user()
        stuObj.connectToDB('localhost', 'root', '')
        ID = request.GET['activeThis']
        status = request.GET['toggle1']
        stuObj.updateActive(ID, status)
        stuObj.closeConnection()
        return redirect(userhome)
    else:
        return redirect(touserhome)

def producthome(request):
    if 'useradmin' in request.COOKIES:
        product = tb_product()
        product.connectToDB('localhost', 'root', '')
        if request.method == "POST":
            if request.POST['operation'] == 'delete':
                product.deleteProduct(request.POST['delThis'])
                product.closeConnection()
                return redirect(producthome)
        products = product.getAllData()
        product.closeConnection()
        return render(request, 'product/home.html', {'products': products, 'total': len(products)})
    else:
        return redirect(touserhome)

def productactive(request):
    if 'useradmin' in request.COOKIES:
        product = tb_product()
        product.connectToDB('localhost', 'root', '')
        ID = request.GET['activeThis']
        status = request.GET['toggle1']
        product.updateActive(ID, status)
        product.closeConnection()
        return redirect(producthome)
    else:
        return redirect(touserhome)

def insertnewproduct(request):
    if 'useradmin' in request.COOKIES:
        category = tb_category()
        category.connectToDB('localhost', 'root', '')
        categories = category.getAllCategoryNames()
        category.closeConnection()
        return render(request, 'product/insert.html', {'categories': categories})
    else:
        return redirect(touserhome)

def insertednewproduct(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        product = tb_product()
        product.connectToDB('localhost', 'root', '')
        pname = request.POST['pname']
        pdetails = request.POST['pdetails']
        pprice = request.POST['pprice']
        photo = request.FILES['photo']
        category = request.POST['category']
        filePath = "/product/{}.jpg".format(pname)
        f = open("ecom_app/static/images/{}".format(filePath), 'wb')
        for i in photo:
            f.write(i)
        f.close()
        product.insertProduct(pname, pdetails, pprice, filePath, category)
        product.closeConnection()
        return redirect(producthome)
    else:
        return redirect(touserhome)

def editproduct(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST' and request.POST['operation'] == 'edit':
            user_id = request.POST['editThis']
            product = tb_product()
            product.connectToDB('localhost', 'root', '')
            products = product.getData(user_id)
            product.closeConnection()
            category = tb_category()
            category.connectToDB('localhost', 'root', '')
            categories = category.getAllCategoryNames()
            category.closeConnection()
            return render(request, 'product/edit.html', {'products': products, 'categories': categories})
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def editedproduct(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        product = tb_product()
        product.connectToDB('localhost', 'root', '')
        id = request.POST['id']
        pname = request.POST['pname']
        pdetails = request.POST['pdetails']
        pprice = request.POST['pprice']
        category = request.POST['category']
        filePath = "/product/{}.jpg".format(pname)
        try:
            photo = request.FILES['photo']
            f = open("ecom_app/static/images{}".format(filePath), 'wb')
            for i in photo:
                f.write(i)
            f.close()
        except:
            pass
        product.editProduct(pname, pdetails, pprice, filePath, category, id)
        product.closeConnection()
        return redirect(producthome)
    else:
        return redirect(touserhome)

def categoryhome(request):
    if 'useradmin' in request.COOKIES:
        category = tb_category()
        category.connectToDB('localhost', 'root', '')
        if request.method == 'POST':
            if request.POST['operation'] == 'delete':
                cat_id = request.POST['delThis']
                category.deleteCategory(cat_id)
                category.closeConnection()
                return redirect(categoryhome)
        categories = category.getAllCategories()
        total = len(categories)
        category.closeConnection()
        return render(request, 'category/home.html', {'categories': categories, 'total': total})
    else:
        return redirect(touserhome)

def insertnewcategory(request):
    if 'useradmin' in request.COOKIES:
        return render(request, 'category/insert.html', {})
    else:
        return redirect(touserhome)

def insertednewcategory(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        category = tb_category()
        category.connectToDB('localhost', 'root', '')
        cat = request.POST['category']
        category.insertCategory(cat)
        category.closeConnection()
        return redirect(categoryhome)
    else:
        return redirect(touserhome)

def editcategory(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST' and request.POST['operation'] == 'edit':
            category = tb_category()
            category.connectToDB('localhost', 'root', '')
            cat_id = request.POST['editThis']
            cat = category.getCategory(cat_id)
            category.closeConnection()
            return render(request, 'category/edit.html', {'cat': cat})
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def editedcategory(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST':
            category = tb_category()
            category.connectToDB('localhost', 'root', '')
            cat_id = request.POST['id']
            cat_name = request.POST['category']
            category.editCategory(cat_id, cat_name)
            category.closeConnection()
            return redirect(categoryhome)
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

#OrderMaster


#Fetch Order Data
def ordermasterhome(request):
    if 'useradmin' in request.COOKIES:
        category = tb_ordermaster()
        category.connectToDB('localhost', 'root', '')
         
        categories = category.getAllData()
        total = len(categories)
        category.closeConnection()
        return render(request, 'ordermaster/home.html', {'categories': categories, 'total': total})
    else:
        return redirect(touserhome)        


#Add Order Form 

def insertnewordermaster(request):
    if 'useradmin' in request.COOKIES:
        return render(request, 'ordermaster/insert.html')
    else:
        return redirect(touserhome)

def insertnewordermasterprocess(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        product = tb_ordermaster()
        product.connectToDB('localhost', 'root', '')
        order_date = request.POST['order_date']
        user_id = request.POST['user_id']
        order_status = request.POST['order_status']
        product.insertProduct(order_date, user_id, order_status)
        product.closeConnection()
        return redirect(producthome)
    else:
        return redirect(touserhome)

 

#Edit Order Master 


def editordermaster(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST' and request.POST['operation'] == 'edit':
            user_id = request.POST['editThis']
            product = tb_product()
            product.connectToDB('localhost', 'root', '')
            products = product.getData(user_id)
            product.closeConnection()
            category = tb_category()
            category.connectToDB('localhost', 'root', '')
            categories = category.getAllCategoryNames()
            category.closeConnection()
            return render(request, 'product/edit.html', {'products': products, 'categories': categories})
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def editedordermaster(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        product = tb_product()
        product.connectToDB('localhost', 'root', '')
        id = request.POST['id']
        pname = request.POST['pname']
        pdetails = request.POST['pdetails']
        pprice = request.POST['pprice']
        category = request.POST['category']
        filePath = "/product/{}.jpg".format(pname)
        try:
            photo = request.FILES['photo']
            f = open("ecom_app/static/images{}".format(filePath), 'wb')
            for i in photo:
                f.write(i)
            f.close()
        except:
            pass
        product.editProduct(pname, pdetails, pprice, filePath, category, id)
        product.closeConnection()
        return redirect(producthome)
    else:
        return redirect(touserhome)






#FetchOrderDetails
        
def orderdetailshome(request):
    if 'useradmin' in request.COOKIES:
        category = tb_orderdetails()
        category.connectToDB('localhost', 'root', '')
         
        categories = category.getAllData()
        total = len(categories)
        category.closeConnection()
        return render(request, 'orderdetails/home.html', {'categories': categories, 'total': total})
    else:
        return redirect(touserhome)        


        
#Add Order Details Form 

def insertneworderdetails(request):
    if 'useradmin' in request.COOKIES:
        return render(request, 'orderdetails/insert.html')
    else:
        return redirect(touserhome)

def insertneworderdetailsprocess(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        product = tb_orderdetails()
        product.connectToDB('localhost', 'root', '')
        order_id = request.POST['order_id']
        product_id = request.POST['product_id']
        qty = request.POST['qty']
        amount = request.POST['amount']
        product.insertProduct(order_id, product_id, qty,amount)
        product.closeConnection()
        return redirect(producthome)
    else:
        return redirect(touserhome)




##Feedback Display 
def feedbackview(request):
    if 'useradmin' in request.COOKIES:
        feedback = tb_feedback()
        feedback.connectToDB('localhost', 'root', '')
        categories = feedback.getAllData()
        total = len(categories)
        feedback.closeConnection()
        return render(request, 'feedback/home.html', {'categories': categories, 'total': total})
    else:
        return redirect(touserhome)

##Feedback Display 
def contactview(request):
    if 'useradmin' in request.COOKIES:
        contact = tb_contact()
        contact.connectToDB('localhost', 'root', '')
        categories = contact.getAllData()
        total = len(categories)
        contact.closeConnection()
        return render(request, 'contact/home.html', {'categories': categories, 'total': total})
    else:
        return redirect(touserhome)

#Vendor CRUD


def vendorhome(request):
    if 'useradmin' in request.COOKIES:
        user = tb_vendor()
        user.connectToDB('localhost', 'root', '')
        if request.method == "POST":
            if request.POST['operation'] == 'delete':
                user.deleteUser(request.POST['delThis'])
                user.closeConnection()
                return redirect(vendorhome)
        users = user.getAllData()
        user.closeConnection()
        return render(request, 'vendor/home.html', {'users':users, 'total':len(users)})
    else:
        return redirect(vendorhome)

def editvendor(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST' and request.POST['operation'] == 'edit':
            user_id = request.POST['editThis']
            user = tb_user()
            user.connectToDB('localhost', 'root', '')
            users = user.getData(user_id)
            user.closeConnection()
            return render(request, 'vendor/edit.html', {'users': users})
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def editedvendor(request):
    if 'useradmin' in request.COOKIES:
        if request.method == 'POST':
            user = tb_user()
            user.connectToDB('localhost', 'root', '')
            user_id = request.POST['id']
            user_name = request.POST['uname']
            gender = request.POST['gender']
            email = request.POST['email']
            mobile = request.POST['mobile']
            
            address = request.POST['address']
           
            from os import rename
            rename("ecom_app/static/images/user/{}.jpg".format(user.getData(user_id)[1]), "ecom_app/static/images{}".format(filePath))
            user.editUserWithPhoto(user_id, user_name, gender, email, mobile, password, address, filePath)
            try:
                photo = request.FILES['photo']
                f = open("ecom_app/static/images/user/{}.jpg".format(user_name), 'wb')
                for i in photo:
                    f.write(i)
                f.close()
            except:
                pass
            user.closeConnection()
            return redirect(userhome)
        else:
            return redirect(touserhome)
    else:
        return redirect(touserhome)

def insertnewvendor(request):
    if 'useradmin' in request.COOKIES:
        return render(request, 'vendor/insert.html', {})
    else:
        return redirect(touserhome)
 

def insertednewvendor(request):
    if 'useradmin' in request.COOKIES and request.method == 'POST':
        user = tb_vendor()
        user.connectToDB('localhost', 'root', '')
        uname = request.POST['uname']
        gender = request.POST['gender']
        email = request.POST['email']
        mobile = request.POST['mobile']
      
        address = request.POST['address']
       
        # imgData = imgData.read().decode()
       # filePath = "/user/{}.jpg".format(uname)
        #f = open("ecom_app/static/images{}".format(filePath), 'wb')
        #for i in imgData:
        #    f.write(i)
       # f.close()
        # sourceEncoding = "ISO-8859-1"
        # targetEncoding = "utf-8"
        # source = open("ecom_app/static/temp/0.jpg")
        # target = open("ecom_app/static/temp/0.jpg", "w")
        # target.write(source.read())
        # source.close()
        # target.close()
        # f = open("ecom_app/static/temp/0.jpg", 'rb')
        # imgData = f.read().decode()
        # f.close()
        user.insertUser(uname, gender, email, mobile, address)
        user.closeConnection()
        return redirect(vendorhome)
    else:
        return redirect(touserhome)



