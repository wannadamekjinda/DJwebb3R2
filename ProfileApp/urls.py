from django.urls import path
from ProfileApp import views,forms

urlpatterns = [
    path('',views.home,name='home'),
    path('hello',views.helloworld, name='hello'),
    path('firstpage',views.firstpage, name='firstpage'),
    path('secondpage',views.secondpage, name='secondpage'),
    path('thirdpage',views.thirdpage, name='thirdpage'),
    path('happy',views.happypage, name='happypage'),
    path('myData',views.myData, name='myData'),
    path('showEmployee',views.showEmployee,name='showEmployee'),
    path('newEmployee',views.newEmployee,name='newEmployee'),
    path('newEmployeeForm',views.newEmployeeForm,name='newEmployeeForm'),
    path('retrieveAllProduct',views.retrieveAllProduct,name='retrieveAllProduct'),
    path('retrieveOneProduct/<pid>',views.retrieveOneProduct,name='retrieveOneProduct'),
    path('createProduct',views.createProduct,name='createProduct'),
    path('<pid>/updateProduct',views.updateProduct,name='updateProduct'),
    path('<pid>/deleteProduceOk',views.deleteProduceOk,name='deleteProduceOk'),
    path('<pid>/deleteProduce',views.deleteProduce,name='deleteProduce'),
]