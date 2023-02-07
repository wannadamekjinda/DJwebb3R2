from django import forms
from .models import *
class EmployeeForm(forms.Form):
    DIVISION_LIST = [('Digital Development','Digital Development'),
                     ('R&D', 'Research and Development'),
                     ('Marketing', 'Marketing'),
                     ('HR', 'Human Resource'),]

    STATUS_LIST = [('Programmer', 'Programmer'),
                     ('Staff', 'Staff'),
                     ('Admin', 'Admin'),
                     ('Accounting', 'Accounting'),]

    id = forms.CharField(max_length=30, label="รหัสพนักงาน"
                         ,required=True,widget=forms.TextInput(attrs={'size' : '35'}))

    name = forms.CharField(max_length=30, label="ชื่อพนักงาน"
                         , required=True, widget=forms.TextInput(attrs={'size': '35'}))

    surname = forms.CharField(max_length=30, label="นามสกุลพนักงาน",
                            required=True, widget=forms.TextInput(attrs={'size': '35'}))

    division = forms.CharField(max_length=30, label="แผนก",
                              required=True, widget=forms.Select(choices=DIVISION_LIST))

    status = forms.CharField(max_length=30,label="ตำแหน่ง",
                             required=True,widget=forms.RadioSelect(choices=STATUS_LIST))

    salary = forms.FloatField(label="เงินเดือน" ,required=True,
                              widget=forms.NumberInput(attrs={'size':'13'}))


class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category','pid','name','brand','price','net')
        widgets = {
            'category' : forms.Select(attrs={'class':'form-control'}),
            'pid' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control','min':10 ,'max':10000}),
            'net' : forms.NumberInput(attrs={'class':'form-control'})
        }
        labels ={
            'category': 'ประเภท',
            'pid': 'รหัสสินค้า',
            'name': 'ชื่อสินค้า',
            'brand': 'ยี่ห้อ',
            'price': 'ราคา',
            'net': 'คงเหลือ'
        }

    def updateForm(self):
        self.fields['pid'].widget.attrs['readonly'] = True
        self.fields['pid'].label = 'รหัสสินค้า [ไม่อนุญาตให้แก้ไขได้]'

    # def deleteForm(self):

