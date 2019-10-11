from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('product', views.product,name='product'),
    path('productdetails/', views.productdetails,name='productdetails'),
    path('mylogin', views.mylogin,name='mylogin'),
    path('myfpass', views.fpass,name='fpass'),
    path('mysignup', views.insertnewuser,name='insertnewuser'),
    path('myorderview', views.myorderview,name='myorderview'),
    path('mycartview', views.mycartview,name='mycartview'),
    path('feedback', views.insertnewfeedback,name='feedback'),
    path('feedbackpro', views.insertnewfeedbackpro, name="feedbackpro"),
    path('contactd', views.insertnewcontact,name='contactd'),
    path('contactpro', views.insertednewcontactpro, name="contactpro"),
    path('cartprocess/', views.cartprocess, name="cartprocess"),
    
]
