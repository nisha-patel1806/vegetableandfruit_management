# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse

from ecom_app.lib.tb_product import tb_product
from ecom_app.lib.tb_admin import tb_admin
from ecom_app.lib.tb_user import tb_user
from ecom_app.lib.tb_category import tb_category
from ecom_app.lib.tb_product import tb_product
from ecom_app.lib.tb_feedback import tb_feedback
from ecom_app.lib.tb_contact import tb_contact
from ecom_app.lib.tb_orderdetails import tb_orderdetails

#Mail
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):
    return  render(request,'home.html')

def about(request):
    return  render(request,'about.html')

def contact(request):
    return  render(request,'contact.html')

#def product(request):
 #   return  render(request,'product.html')


#Fetch Product Listing
def product(request):
    product = tb_product()
    product.connectToDB('localhost', 'root', '')
    products = product.getAllData()
    product.closeConnection()
    return render(request, 'product.html', {'products': products, 'total': len(products)})
    

#Product Detail user side


def productdetails(request):
    if request.method == 'POST' and request.POST['operation'] == 'edit':
        user_id = request.POST['editThis']
        product1 = tb_product()
        product1.connectToDB('localhost', 'root', '')
        products1 = product1.getData(user_id)
        product1.closeConnection()
        return render(request, 'productdetails.html', {'products': products1})
    else:
        return redirect(home)
     
def editedproduct1(request):
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
        return redirect(home)
    else:
        return redirect(home)

 
 
def mylogin(request):
    if request.method == 'GET':
        return render(request, 'mylogin.html', {})
    if request.method == 'POST':
        user = request.POST['email']
        password = request.POST['password']
        admin = tb_user()
        admin.connectToDB('localhost', 'root', '')
        if admin.authenticate(user, password):
            admin.closeConnection()
            response = redirect(home)
            response.set_cookie('useradmin', user)
            return response
        else:
            admin.closeConnection()
            return redirect(mylogin)

def fpass(request):
    if request.method == 'GET':
        return render(request, 'myfpass.html', {})
    if request.method == 'POST':
        user = request.POST['email']
        admin = tb_user()
        admin.connectToDB('localhost', 'root', '')
        if admin.fprocess(user):
            admin.closeConnection()
            response = redirect(mylogin)
            return response
        else:
            admin.closeConnection()
            return redirect(mylogin)
def insertnewuser(request):
    return render(request, 'signup.html', {})
    

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
        return redirect(mylogin)
    else:
        return redirect(mylogin)


def signout(request):
    response = redirect(mylogin)
    response.delete_cookie('useradmin')
    return response



def insertnewcontact(request):
   # if 'useradmin' in request.COOKIES:
    return render(request, 'give-contact.html', {})
    #else:
     #   return redirect(mylogin)

def insertednewcontactpro(request):
    if request.method == 'POST':
        category = tb_contact()
        category.connectToDB('localhost', 'root', '')
        txt1 = request.POST['txt1']
        txt2 = request.POST['txt2']
        txt3 = request.POST['txt3']
        txt4 = request.POST['txt4']
        category.insertData(txt1,txt2,txt3,txt4)
        category.closeConnection()
        return redirect(home)
    else:
        return redirect(home)

def insertnewfeedback(request):
   # if 'useradmin' in request.COOKIES:
    return render(request, 'give-feedback.html', {})
    #else:
      #  return redirect(mylogin)

def insertnewfeedbackpro(request):
    if  request.method == 'POST':
        category = tb_feedback()
        category.connectToDB('localhost', 'root', '')
        feed = request.POST['txt1']
        email = request.POST['txt2']
        category.insertData(feed,email)
        category.closeConnection()
        return redirect(home)
    else:
        return redirect(mylogin)



def myorderview(request):
    if 'useradmin' in request.COOKIES :
        product = tb_orderdetails()
        product.connectToDB('localhost', 'root', '')
        products = product.getAllDataJoin()
        product.closeConnection()
        return render(request, 'uvieworder.html', {'categories': products, 'total': len(products)})
    else:
        return redirect(mylogin)

def mycartview(request):
    product = tb_orderdetails()
    product.connectToDB('localhost', 'root', '')
    products = product.getAllDataJoin()
    product.closeConnection()
    return render(request, 'uviewcart.html', {'categories': products, 'total': len(products)})
    
def cartprocess(request):
    if request.method == 'POST':
        category = tb_orderdetails()
        category.connectToDB('localhost', 'root', '')
        txt0 = 1
        txt1 = request.POST['pid']
        txt2 = request.POST['qty']
        txt3 = request.POST['amount']
        category.insertProduct(txt0,txt1,txt2,txt3)
        category.closeConnection()
        return redirect(product)
    else:
        return redirect(home)