from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

def home(request):
    return render(request,'Home.html')

def final(request):
    return render(request,'final.html')

def newfunc(request):
    data=funclist.objects.all()
    d={
        "dta":data
    }
    return render(request,'newfunc.html',d)

def allfunc(request):
    data=funclist.objects.all()
    d={
        "dta":data
    }
    return render(request,'Allfunc.html',d)

def newdetails(request,num):
    data=funclist.objects.filter(id=num).first()
    d={"key":data}
    return render(request,'newdetails.html',d)

def sdetails(request,num):
    data=s_register.objects.filter(id=num).first()
    if data:
        d={"student":data}
        return render(request,'sdetails.html',d)
    else:
        return HttpResponse("student not found")


def fdetails(request,num):
    data=funclist.objects.filter(id=num).first()
    d={"key":data}
    return render(request,'details.html',d)
def Admins(request):
    if request.method == "POST":
        dic = request.POST
        Na = dic["pwd"]
        value="shantanu@123"
        if Na==value:
            return redirect("newfunc")
    return render(request,'Admins.html')

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def sregister(request,num):
    data=funclist.objects.get(id=num)
    if request.method == "POST":
        dic=request.POST
        Na=dic["name"]
        Ro=dic["roll"]
        Ph=dic["phone"]
        Em=dic["email"]
        s_register.objects.create(name=Na,roll=Ro,phone=Ph,email=Em)
        return redirect("fdetails",num)
    return render(request,'Sregister.html',{"crs":data})

def addfunc(request):
    if request.method == "POST":
        dic=request.POST
        na=dic["yogi"]
        Ro=dic["nme"]
        Ph=dic["brr"]
        Em=dic["Vn"]
        Ems = dic["vno"]
        Emv = dic["venue"]
        funclist.objects.create(photo=na,fname=Ro,branch=Ph,vname=Em,vnum=Ems,venue=Emv)
        return render("Admins")
    return render(request,'addfunc.html')


