import datetime
from django.template.loader import get_template
#from typing import ContextManager
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, Paginator,EmptyPage
from django.views.generic import View
from crm1.utils import render_to_pdf #created in step 4


from .models import *
from .forms import *
from .filters import *

@login_required(login_url='login')
def home(request):
    orders=Order.objects.all()
    
    customers=Customer.objects.all()
    stocks=Stock.objects.all()
    susers=SalesUser.objects.all()    
    
    total_susers='Users ( '
    total_susers+=str(susers.count())
    total_susers+=' )'    

    total_stocks='Stocks ( '
    total_stocks+=str(stocks.count())
    total_stocks+=' )'    
    
    total_customers = 'Customers ( '    
    total_customers+=str(customers.count())
    total_customers+=' )'    

    total_orders=orders.count()
    total_delivered=orders.filter(status='Delivered').count()
    total_pending=orders.filter(status='Pending').count()

    context={'total_susers':total_susers,'total_stocks':total_stocks,'customers':customers,'total_customers':total_customers,'total_orders':total_orders,'total_delivered':total_delivered,'total_pending':total_pending,'orders':orders,}
    return render(request,'accounts/dashboard.html',context)

def about(request):
    return render(request,'accounts/about.html')

def profile(request):
    return render(request,'accounts/profile.html')

#---------------------------------------------------- PRODUCT ------------------------------------------------ 
@login_required(login_url='login')
def products(request):
    products=Product.objects.all()    
    context={'products': products,}
    return render(request,'accounts/products.html',context)

#---------------------------------------------------- ORDER ------------------------------------------------ 

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

#---------------------------------------------------- CUSTOMER ------------------------------------------------ 
@login_required(login_url='login')

def create_customer(request):
    form=CustomerForm()
    if request.method == "POST":
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_customer')            
    context={'form':form}
    return render(request,'accounts/create_customer.html',context)

def update_customer(request,customer_id):    
    customer=Customer.objects.get(id=customer_id)
    form=CustomerForm(instance=customer)
    if request.method == "POST":
        form=CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('list_customer')    
    context={'form':form}
    return render(request,'accounts/create_customer.html',context)    

def delete_customer(request,customer_id):    
    customer=Customer.objects.get(id=customer_id)
    if request.method=="POST":
        customer.delete()
        return redirect('list_customer')
    context={'customer':customer}
    return render(request,'accounts/delete_customer.html',context)    

@login_required(login_url='login')
def list_customer(request):
    customers=Customer.objects.all()
    total_customers=customers.count()       
    customer_filter = CustomerFilter(request.GET,queryset=customers )     
    customers = customer_filter.qs
    context={'customers':customers,'total_customers':total_customers,'customer_filter':customer_filter,}
    return render(request,'accounts/list_customer.html',context)

#---------------------------------------------------- AUTHENTICATION ------------------------------------------------ 

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

    context={'form':form}
    return render(request,'accounts/register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

#---------------------------------------------------- SALES USERS ------------------------------------------------ 
@login_required(login_url='login')
def su_list(request):
    salesusers=SalesUser.objects.all()
    total_salesusers=salesusers.count()       
    salesusers_filter = SalesUserFilter(request.GET,queryset=salesusers)     
    salesusers=salesusers_filter.qs
    context={'salesusers':salesusers,'total_salesusers':total_salesusers,'salesusers_filter':salesusers_filter,}
    return render(request,'accounts/su_list.html',context)

def su_create(request):
    form=SalesUserForm()
    if request.method == "POST":
        form=SalesUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('su_list')            
    context={'form':form}
    return render(request,'accounts/su_create.html',context)

def su_update(request,su_id):    
    salesuser=SalesUser.objects.get(id=su_id)
    form=SalesUserForm(instance=salesuser)
    if request.method == "POST":
        form=SalesUserForm(request.POST,instance=salesuser)
        if form.is_valid():
            form.save()
            return redirect('su_list')    
    context={'form':form}
    return render(request,'accounts/su_update.html',context)    

def su_delete(request,su_id):    
    salesuser=SalesUser.objects.get(id=su_id)
    if request.method=="POST":
        salesuser.delete()
        return redirect('su_list')    
    context={'salesuser':salesuser}
    return render(request,'accounts/su_delete.html',context)    
#---------------------------------------------------- END OF SALES USERS ------------------------------------------------ 

#---------------------------------------------------- Stock Unit ------------------------------------------------ 
@login_required(login_url='login')

def stu_list(request):
    stockunits=StockUnit.objects.all()
    total_stockunits=stockunits.count()       
    stockunits_filter = StockUnitFilter(request.GET,queryset=stockunits)     
    stockunits=stockunits_filter.qs
    context={'stockunits':stockunits,'total_stockunits':total_stockunits,'stockunits_filter':stockunits_filter,}
    return render(request,'accounts/stu_list.html',context)

def stu_create(request):
    form=StockUnitForm()
    if request.method == "POST":
        form=StockUnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stu_list')            
    context={'form':form}
    return render(request,'accounts/stu_create.html',context)    

def stu_update(request,stu_id):    
    stockunit=StockUnit.objects.get(id=stu_id)
    form=StockUnitForm(instance=stockunit)
    if request.method == "POST":
        form=StockUnitForm(request.POST,instance=stockunit)
        if form.is_valid():
            form.save()
            return redirect('stu_list')    
    context={'form':form}
    return render(request,'accounts/stu_update.html',context)        

def stu_delete(request,stu_id):    
    stockunit=StockUnit.objects.get(id=stu_id)
    print(stockunit)
    if request.method=="POST":
        stockunit.delete()
        return redirect('stu_list')    
    context={'stockunit':stockunit}
    return render(request,'accounts/stu_delete.html',context)    



#---------------------------------------------------- Stock  ------------------------------------------------ 
@login_required(login_url='login')

def stock_list(request):
    stock=Stock.objects.all()
    total_stock=stock.count()       
    stock_filter = StockFilter(request.GET,queryset=stock)     
    stock=stock_filter.qs
    context={'stock':stock,'total_stock':total_stock,'stock_filter':stock_filter,}
    return render(request,'accounts/stock_list.html',context)

def stock_create(request):
    form=StockForm()
    if request.method == "POST":
        form=StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')            
    context={'form':form}
    return render(request,'accounts/stock_create.html',context)    

def stock_update(request,stock_id):    
    stock=Stock.objects.get(id=stock_id)
    form=StockForm(instance=stock)
    if request.method == "POST":
        form=StockForm(request.POST,instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_list')    
    context={'form':form}
    return render(request,'accounts/stock_update.html',context)        

def stock_delete(request,stock_id):    
    stock=Stock.objects.get(id=stock_id)    
    if request.method=="POST":
        stock.delete()
        return redirect('stock_list')    
    context={'stock':stock}
    return render(request,'accounts/stock_delete.html',context)    


#---------------------------------------------------- Brand  ------------------------------------------------ 
@login_required(login_url='login')
def brand_list(request):        
    brand=StockBrand.objects.all()    
    brand_filter = StockBrandFilter(request.GET,queryset=brand)         
    brand=brand_filter.qs
    page_num = request.GET.get('page')    
    paginator=Paginator(brand,5)    
    try:
        brands = paginator.page(page_num)        
    except PageNotAnInteger:
        brands = paginator.page(1)        
    except EmptyPage:
        brands = paginator.page(paginator.num_pages)        
    context={'brand':brand,'brand_filter':brand_filter,'brands':brands,}
    return render(request,'accounts/brand_list.html',context)

def brand_create(request):
    form=StockBrandForm()
    if request.method == "POST":
        form=StockBrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brand_list')            
    context={'form':form}
    return render(request,'accounts/brand_create.html',context)    

def brand_update(request,brand_id):    
    brand=StockBrand.objects.get(id=brand_id)
    form=StockBrandForm(instance=brand)
    if request.method == "POST":
        form=StockBrandForm(request.POST,instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brand_list')    
    context={'form':form}
    return render(request,'accounts/brand_update.html',context)        

def brand_delete(request,brand_id):    
    brand=StockBrand.objects.get(id=brand_id)    
    if request.method=="POST":
        brand.delete()
        return redirect('brand_list')    
    context={'brand':brand}
    return render(request,'accounts/brand_delete.html',context)    

#---------------------------------------------------- Class  ------------------------------------------------ 
@login_required(login_url='login')

def class_list(request):
    stock_class=StockClass.objects.all()
    total_class=stock_class.count()       
    class_filter = StockClassFilter(request.GET,queryset=stock_class)     
    stock_class=class_filter.qs
    context={'stock_class':stock_class,'total_class':total_class,'class_filter':class_filter,}
    return render(request,'accounts/class_list.html',context)

def class_create(request):
    form=StockClassForm()
    if request.method == "POST":
        form=StockClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')            
    context={'form':form}
    return render(request,'accounts/class_create.html',context)    

def class_update(request,class_id):    
    stock_class=StockClass.objects.get(id=class_id)
    form=StockClassForm(instance=stock_class)
    if request.method == "POST":
        form=StockClassForm(request.POST,instance=stock_class)
        if form.is_valid():
            form.save()
            return redirect('class_list')    
    context={'form':form,}
    return render(request,'accounts/class_update.html',context)        

def class_delete(request,class_id):    
    stock_class=StockClass.objects.get(id=class_id)    
    if request.method=="POST":
        stock_class.delete()
        return redirect('class_list')    
    context={'stock_class':stock_class}
    return render(request,'accounts/class_delete.html',context)    


# -------------- PDF : Invoice ----------
# class based views

import os

class PdfView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': datetime.date.today(), 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        print(os.path)
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

#class PdfDownload(View):   
#    def get(self, request, *args, **kwargs):        
#        template = get_template('invoice.html')
#        context = {
#            "invoice_id": 123,
#            "customer_name": "John Cooper",
#            "amount": 1399.99,
#            "today": "Today",
#        }
#        html = template.render(context)
#        pdf = render_to_pdf('invoice.html', context)
#        if pdf:
#            response = HttpResponse(pdf, content_type='application/pdf')
#            filename = "Invoice_%s.pdf" %("12341231")
#            content = "inline; filename='%s'" %(filename)
#            download = request.GET.get("download")
#            if download:
#                content = "attachment; filename='%s'" %(filename)
#            response['Content-Disposition'] = content
#            return response
#        return HttpResponse("Not found")
