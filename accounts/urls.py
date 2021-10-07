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

    path('login/', views.loginPage,name="login"),
    path('register/', views.register,name="register"),
    path('logout/', views.logoutUser,name="logout"),

]
