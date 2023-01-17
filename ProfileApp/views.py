from django.shortcuts import render,HttpResponse

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