from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [    
    
    path('', views.home,name="home"),
   
    path('about/', views.about,name="about"),
    path('profile/', views.profile,name="profile"),        
#products    
    path('products/', views.products,name="products"),
#orders    
    path('order_create/', views.order_create,name="order_create"),
    path('order_updpate/<str:order_id>/', views.order_update,name="order_update"),
    path('order_delete/<str:order_id>/', views.order_delete,name="order_delete"),
    path('order_list/', views.order_list,name="order_list"),

#customers
    path('create_customer/', views.create_customer,name="create_customer"),    
    path('update_customer/<str:customer_id>', views.update_customer,name="update_customer"),
    path('delete_customer/<str:customer_id>', views.delete_customer,name="delete_customer"),
    path('list_customer/', views.list_customer,name="list_customer"),
#sales users
    path('su_list/', views.su_list,name="su_list"),
    path('su_create/', views.su_create,name="su_create"),
    path('su_update/<str:su_id>/', views.su_update,name="su_update"),
    path('su_delete/<str:su_id>/', views.su_delete,name="su_delete"),

# stock unit
    path('stu_list/', views.stu_list,name="stu_list"),
    path('stu_create/', views.stu_create,name="stu_create"),
    path('stu_update/<str:stu_id>/', views.stu_update,name="stu_update"),
    path('stu_delete/<str:stu_id>/', views.stu_delete,name="stu_delete"),

# stock 
    path('stock_list/', views.stock_list,name="stock_list"),
    path('stock_create/', views.stock_create,name="stock_create"),
    path('stock_update/<str:stock_id>/', views.stock_update,name="stock_update"),
    path('stock_delete/<str:stock_id>/', views.stock_delete,name="stock_delete"),

# brand
    
    path('brand_list/', views.brand_list,name="brand_list"),
    path('brand_create/', views.brand_create,name="brand_create"),
    path('brand_update/<str:brand_id>/', views.brand_update,name="brand_update"),
    path('brand_delete/<str:brand_id>/', views.brand_delete,name="brand_delete"),
        

# class
    path('class_list/', views.class_list,name="class_list"),
    path('class_create/', views.class_create,name="class_create"),
    path('class_update/<str:class_id>/', views.class_update,name="class_update"),
    path('class_delete/<str:class_id>/', views.class_delete,name="class_delete"),

# test pdf
    path('pdf_view/<str:id>', views.PdfView.as_view(),name="pdf_view"),
#   path('pdf_download/<str:id>', views.PdfDownload.as_view(),name="pdf_download"),

# logins
    path('login/', views.loginPage,name="login"),
    path('register/', views.register,name="register"),
    path('logout/', views.logoutUser,name="logout"),

]
