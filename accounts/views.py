from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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

def customer(request):
    return render(request,'accounts/customer.html')

def products(request):
    products=Product.objects.all()    
    context={'products': products,}
    return render(request,'accounts/products.html',context)