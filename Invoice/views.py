
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from requests import request
from .forms import ClientForm,InvoiceForm
from .models import Client,Inventory
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
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

def inventory(request):
    items = Inventory.objects.filter(users=request.user)
    return render(request,'Invoice/inventory.html',{'items':items})

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
         return render(request,'Invoice/login.html',{'form':AuthenticationForm()})

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



def add_invoice(request):
   
    form = InvoiceForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        "form": form,
        "title": "New Invoice",
    }
    
    return render(request, "Invoice/invoice.html", context)


def render_pdf_view(request):
    template_path = 'Invoice/pdf.html'
    context = {'name': request.POST['name'],
    'date':request.POST['invoice_date'],
    'phone':request.POST['phone_number'],
    'line_one':request.POST['line_one'],
    'line_one_quantity':request.POST['line_one_quantity'],
    'line_one_price':request.POST['line_one_unit_price'],
    'line_one_total':request.POST['line_one_total_price'],
    
    'line_two':request.POST['line_two'],
    'line_two_quantity':request.POST['line_two_quantity'],
    'line_two_price':request.POST['line_one_unit_price'],
    'line_two_total':request.POST['line_two_total_price'],
    
    'line_three':request.POST['line_three'],
    'line_three_quantity':request.POST['line_three_quantity'],
    'line_three_price':request.POST['line_one_unit_price'],
    'line_three_total':request.POST['line_three_total_price'],
    
    'line_four':request.POST['line_four'],
    'line_four_quantity':request.POST['line_four_quantity'],
    'line_four_price':request.POST['line_one_unit_price'],
    'line_four_total':request.POST['line_four_total_price'],
    
    'line_five':request.POST['line_five'],
    'line_five_quantity':request.POST['line_five_quantity'],
    'line_five_price':request.POST['line_one_unit_price'],
    'line_five_total':request.POST['line_five_total_price'],
    
    'type':request.POST['invoice_type'],
    'total':request.POST['total']}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

    


