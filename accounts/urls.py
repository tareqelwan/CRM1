"""crm1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('profile/', views.profile,name="profile"),    
    path('customer/<str:customer_id>/', views.customer,name="customer"),
    path('products/', views.products,name="products"),
    path('create_order/', views.create_order,name="create_order"),
    path('update_order/<str:order_id>/', views.update_order,name="update_order"),
    path('delete_order/<str:order_id>/', views.delete_order,name="delete_order"),
]
