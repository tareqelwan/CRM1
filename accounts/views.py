from typing import ContextManager
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .filters import *

# Create your views here.
@login_required(login_url='login')
def home(request):
    orders=Order.objects.all()
    customers=Customer.objects.all()
    total_customers=customers.count()
    total_orders=orders.count()
    total_delivered=orders.filter(status='Delivered').count()
    total_pending=orders.filter(status='Pending').count()
    context={'orders':orders,'customers':customers,'total_customers':total_customers,'total_orders':total_orders,'total_delivered':total_delivered,'total_pending':total_pending}
    return render(request,'accounts/dashboard.html',context)

def about(request):
    return render(request,'accounts/about.html')

def profile(request):
    return render(request,'accounts/profile.html')

def customer(request,customer_id):
    customer=Customer.objects.get(id=customer_id)
    orders=customer.order_set.all()
    orders_count = orders.count()
    context={'customer':customer,'orders':orders,'orders_count':orders_count,}
    return render(request,'accounts/customer.html',context)

def products(request):
    products=Product.objects.all()    
    context={'products': products,}
    return render(request,'accounts/products.html',context)

def create_order(request):
    form=OrderForm()
    if request.method == "POST":
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')            
    context={'form':form}
    return render(request,'accounts/create_order.html',context)

def update_order(request,order_id):    
    order=Order.objects.get(id=order_id)
    form=OrderForm(instance=order)
    if request.method == "POST":
        form=OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')    
    context={'form':form}
    return render(request,'accounts/create_order.html',context)    

def delete_order(request,order_id):    
    order=Order.objects.get(id=order_id)
    if request.method=="POST":
        order.delete()
        return redirect('/')
    context={'order':order}
    return render(request,'accounts/delete_order.html',context)    

def create_customer(request):
    form=CustomerForm()
    if request.method == "POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')            
    context={'form':form}
    return render(request,'accounts/create_customer.html',context)

def update_customer(request,customer_id):    
    customer=Customer.objects.get(id=customer_id)
    form=CustomerForm(instance=customer)
    if request.method == "POST":
        form=CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')    
    context={'form':form}
    return render(request,'accounts/create_customer.html',context)    

def list_customer(request):
    customers=Customer.objects.all()
    total_customers=customers.count()   
    
    customer_filter = CustomerFilter(request.GET,queryset=customers)     
    customers = customer_filter.qs

    context={'customers':customers,'total_customers':total_customers,'customer_filter':customer_filter,}
    return render(request,'accounts/list_customer.html',context)

def loginPage(request):    
    
    if request.method=="POST":
        p_user=request.POST.get('username')
        p_pass=request.POST.get('password')
        user=authenticate(request,username=p_user,password=p_pass)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,"User name or password is not correct")    

    context={}
    return render(request,'accounts/loginpage.html',context)

def register(request):
    if request.user.is_authenticated:
        return redirect('home')

    form=CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        

    context={}
    return render(request,'accounts/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')