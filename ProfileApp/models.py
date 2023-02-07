from django.db import models
import datetime

class Employee:
    def __init__(self, id, name, surname, division, status, salary):
        self.id = id
        self.name = name
        self.surname = surname
        self.division = division
        self.status = status
        self.salary = salary


    def __str__(self):
        return "ID : {}, Name:{},Surname: {},Division: {},Status: {},Salary:{}" \
            .format(self.id, self.name, self.surname, self.division, self.status, self.salary)

class Category(models.Model):
    name = models.CharField(max_length=50,default='')
    desc = models.CharField(max_length=200,default='')
    def __str__(self):
        return str(self.id)+ " : " + self.name + "  : " +self.desc

class Product(models.Model):
    pid = models.CharField(max_length=13,primary_key=True,default='')
    name = models.CharField(max_length=50,default='')
    brand = models.CharField(max_length=30,default='')
    price = models.FloatField(default=0.00)
    net = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.pid + " : "+self.name + " : " +self.brand + " : " \
            + str (self.price) + " : " + str(self.net) + " : " + self.category.name


class Division(models.Model):
    did = models.CharField(max_length=5,primary_key=True,default='')
    name = models.CharField(max_length=50,default='')
    location = models.CharField(max_length=50,default='')

    def __str__(self):
        return self.did + " : " + self.name + " : " + self.location

class Employee(models.Model):
    eid = models.CharField(max_length=13,primary_key=True,default='')
    name = models.CharField(max_length=35,default='')
    surname = models.CharField(max_length=35,default='')
    birthday = models.DateField(default=datetime.date.today())
    gender = models.BooleanField(default=True)
    salary = models.FloatField(default=15000.00)
    status = models.CharField(max_length=35,default='')
    division = models.ForeignKey(Division,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.eid + " : " + self.name + " : "+ self.surname
