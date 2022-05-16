import re
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
# Create your views here.


def home(request):
    return render(request,'invoice/home.html')


def signupuser(request):
    if request.method =='GET':
         return render(request,'invoice/signup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('dashboard')
            except IntegrityError:
                return render(request,'invoice/signup.html',{'form':UserCreationForm(),'error':'That username has already been taken'})
        else:
            return render(request,'invoice/signup.html',{'form':UserCreationForm(),'error':'The passwords did not match'})



def loginuser(request):
    if request.method =='GET':
         return render(request,'invoice/signup.html',{'form':AuthenticationForm()})

    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'invoice/signup.html',{'form':AuthenticationForm(),'error':'Wrong credentials'})
        else:
            login(request,user)
            return redirect('dashboard')


def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')

def dashboard(request):
    return render(request,'invoice/dashboard.html')