from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def homeView(request):
    return render(request,'home.html')


@login_required(login_url='loginpage')
def profileView(request):
    return render(request,'profile.html')

def loginView(request):
    obj=User.objects.all()
    if request.user.is_authenticated:
        messages.warning(request,"Mama you already logged! ")
        return redirect('homepage')
    if request.method=="POST":
        a=request.POST.get('uname')
        b=request.POST.get('passw')
        result=authenticate(request,username=a,password=b)
        if result is not None:
            login(request,result)
            messages.success(request,"Thank you for coming back ! ")
            return redirect('profilepage')
        else:
            messages.error(request,"are you trying to cheat me ! Wrong creds")
            return redirect('loginpage')
    if request.user.is_superuser:
        print(request.user.username)
        return redirect('/admin')
    else:
       return render(request,'login.html')
    
def logoutView(request):
    logout(request)
    return render(request,'logout.html')

def registerView(request):
    return render(request,'register.html')


@login_required(login_url='loginpage')
def createView(request):
    if request.method=="POST":


        return render(request,'create.html')


def singleView(request):
    return render(request,'single.html')




