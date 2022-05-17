
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .forms import ClientForm
from .models import Client
# Create your views here.


def home(request):
    return render(request,'Invoice/home.html')


def add_client(request):
    if request.method=='GET':
        return render(request,'Invoice/form.html',{'form':ClientForm()})
    else:
        form = ClientForm(request.POST)
        new_client = form.save(commit=False)
        new_client.user = request.user
        new_client.save()
        return redirect('clients')

def clients(request):
    clients = Client.objects.filter(user=request.user)
    return render(request,'Invoice/clients.html',{'clients':clients})



def signupuser(request):
    if request.method =='GET':
         return render(request,'Invoice/signup.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('clients')
            except IntegrityError:
                return render(request,'Invoice/signup.html',{'form':UserCreationForm(),'error':'That username has already been taken'})
        else:
            return render(request,'Invoice/signup.html',{'form':UserCreationForm(),'error':'The passwords did not match'})



def loginuser(request):
    if request.method =='GET':
         return render(request,'Invoice/signup.html',{'form':AuthenticationForm()})

    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'Invoice/login.html',{'form':AuthenticationForm(),'error':'Wrong credentials'})
        else:
            login(request,user)
            return redirect('clients')


def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')




