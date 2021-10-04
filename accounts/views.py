from typing import ContextManager
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
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
