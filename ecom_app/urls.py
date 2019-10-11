"""startup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.touserhome),
    path('signout/', views.signout, name="signout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('changepassword/', views.cpassword, name="changepassword"),
    path('forgotpassword', views.fpass,name='fpass'),
    path('user/', views.userhome, name="userhome"),
    path('user/insert/', views.insertnewuser, name="insertnewuser"),
    path('user/inserted/', views.insertednewuser, name="insertednewuser"),
    path('user/edit/', views.edituser, name="edituser"),
    path('user/edited/', views.editeduser, name="editeduser"),
    path('user/active/', views.useractive, name="useractive"),

    path('user/signup/', views.touserhome),




    path('order-details/', views.orderdetailshome, name="order-details"),

    path('order-master/', views.ordermasterhome, name="order-master"),

    path('category/', views.categoryhome, name="category"),
    path('category/insert/', views.insertnewcategory, name="insertnewcategory"),
    path('category/inserted/', views.insertednewcategory, name="insertednewcategory"),
    path('category/edit/', views.editcategory, name="editcategory"),
    path('category/edited/', views.editedcategory, name="editedcategory"),

    path('product/', views.producthome, name="product"),
    path('product/active/', views.productactive, name="productactive"),
    path('product/insert/', views.insertnewproduct, name="insertnewproduct"),
    path('product/inserted/', views.insertednewproduct, name="insertednewproduct"),
    path('product/edit/', views.editproduct, name="editproduct"),
    path('product/edited/', views.editedproduct, name="editedproduct"),

    # path('active/', views.active, name="active"),

    #NEw Work 
    
    path('feedback/', views.feedbackview, name="feedback"),
    path('contact/', views.contactview, name="contact"),

    #Vendor CRUD
    
    path('vendor/', views.vendorhome, name="vendorhome"),
    path('vendor/insert/', views.insertnewvendor, name="insertnewvendor"),
    path('vendor/inserted/', views.insertednewvendor, name="insertednewvendor"),
    path('vendor/edit/', views.editvendor, name="editvendor"),
    path('vendor/edited/', views.editedvendor, name="editedvendor"),
    
]