from django import forms
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.contrib import messages
from ProfileApp.forms import ProductFrom

# Create your views here.
def helloworld(request):
    return HttpResponse("<H1>Hello World,This is My First Django Web </H1>"
                        "<H2> I Love Python and Django,It's My life </H2>")

def firstpage(request):
    return render(request,"firstpage.html")

def secondpage(request):
    return render(request,"secongpage.html")

def thirdpage(request):
    return render(request,"thirdpage.html")

def happypage(request):
    return render(request,"happypage.html")

def home(request):
    return render(request,"home.html")

def myData(request):
    name = "Wannada"
    surname = "Mekjinda"
    gender = "ผู้หญิง"
    education = "นักศึกษา"
    status = "study"
    work = "study"
    subjects = [
        ["32-406-204-201","Python",3],
        ["32-406-204-201","SA",2],
        ["32-406-204-201","DBMS",3],
        ["32-406-204-201","JAVA",1]
    ]
    context = {'name':name,'surname':surname,'gender':gender,'education':education,
        'status':status,'work':work,'subjects':subjects}
    return render(request,'myData.html',context)

from ProfileApp.models import *
from ProfileApp.forms import *

employeeList = []
def showEmployee(request):

    emp1 = Employee('E001','Sukanya','Panichkul','Digital Dev','admin',25000.00)
    employeeList.append(emp1)
    emp2 = Employee('E002', 'Aricha', 'Winaidee', 'Marketing', 'admin',20000.00)
    emp3 = Employee('E003', 'Jhon', 'Terry', 'Accounting','admin', 30000.00)
    emp4 = Employee('E004', 'Emma', 'Lady', 'Admin', 'admin',15000.00)
    emp5 = Employee('E005', 'wanna', 'Tadee', 'Digital Dev','admin', 18000.00)
    employeeList.append(emp2)
    employeeList.append(emp3)
    employeeList.append(emp4)
    employeeList.append(emp5)
    context = {'employees':employeeList}
    return render(request,'showEmployee.html',context)


def newEmployee(request):
    if request.method == "POST":
        # get data from request
        id = request.POST['id']
        name = request.POST['name']
        surname = request.POST['surname']
        division = request.POST['division']
        status = request.POST['status']
        salary = request.POST['salary']
        emp = Employee(id,name,surname,division,status,salary)
        employeeList.append(emp)
        return redirect('showEmployee')

    else:
        return render(request,'inputEmployee.html')

def newEmployeeForm(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            name = form.get('name')
            surname = form.get('surname')
            division = form.get('division')
            status = form.get('status')
            salary = form.get('salary')
            emp = Employee(id,name,surname,division,status,salary)
            employeeList.append(emp)
            return redirect('showEmployee')
    else:
        form = EmployeeForm()
    context = {'forms': form}
    return render(request, 'inputEmployeeForm.html', context)

#CRUD
def retrieveAllProduct(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'productapp/retrieveAllProduct.html', context)
def retrieveOneProduct(request,pid):
    product = Product.objects.get(pid=pid)
    context = {'product': product}
    return render(request, 'productapp/retrieveOneProduct.html', context)

def createProduct(request):
    if request.method == 'POST':
        form = ProductFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'บันทึกสินค้าใหม่เรียบร้อย')
            return redirect('retrieveAllProduct')
        else:
            product = Product.objects.get(pid=request.POST['pid'])
            if product:
                messages.add_message(request,messages.WARNING ,'รหัสซ้ำกับที่มีอยู่แล้วในระบบ ไม่สามารถบันทึกได้...')
            else:
                messages.add_message(request,messages.WARNING,'ข้อมูลไม่ถูกต้อง / ไม่สมบูรณ์ ไม่สามารถบันทึกได้...')
        # return HttpResponse("Okay")
    else:
        form = ProductFrom()
    context = {'form': form}
    return render(request, 'productapp/createProduct.html', context)

def updateProduct(request,pid):
    obj = get_object_or_404(Product, pid=pid)
    form = ProductFrom(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'ปรับปรุงข้อมูลสินค้าเรียบร้อย')
            return redirect('retrieveAllProduct')
        else:
            messages.add_message(request, messages.SUCCESS, 'ไม่สามารถปรับปรุงข้อมูลสินค้าเรียบร้อย')

    else:
        form.updateForm()
        context = {'form': form}
    return render(request,'productapp/retrieveAllProduct.html',context)

def deleteProduceOk(request,pid):
    product = Product.objects.get(pid=pid)
    if product:
        product.delete()
        messages.add_message(request, messages.SUCCESS, 'ลบข้อมูลสินค้าเรียบร้อย')
        return redirect('retrieveAllProduct')
    else:
        messages.add_message(request, messages.WARNING, 'ไม่พบสินค้าที่เลือก')
        return redirect('retrieveAllProduct')

def deleteProduct(request,pid=None):
    if request.method == 'POST':
        pid = request.POST[pid]
        product = Product.objects.get(pid=pid)
        if product:
            product.delete()
            return redirect('retrieveAllProduct')
    else:
        product = Product.objects.get(pid=pid)
        context = {'product':product}
        return render(request,'productapp/deleteProduct.html',context)


