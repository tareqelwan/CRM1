from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home,name="home"),
    
    path('about/', views.about,name="about"),
    path('profile/', views.profile,name="profile"),        
    
    path('products/', views.products,name="products"),
    
    path('create_order/', views.create_order,name="create_order"),
    path('update_order/<str:order_id>/', views.update_order,name="update_order"),
    path('delete_order/<str:order_id>/', views.delete_order,name="delete_order"),

    path('create_customer/', views.create_customer,name="create_customer"),    
    path('update_customer/<str:customer_id>', views.update_customer,name="update_customer"),
    path('delete_customer/<str:customer_id>', views.delete_customer,name="delete_customer"),
    path('list_customer/', views.list_customer,name="list_customer"),

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

    path('login/', views.loginPage,name="login"),
    path('register/', views.register,name="register"),
    path('logout/', views.logoutUser,name="logout"),

]
