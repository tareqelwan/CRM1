from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .models import Order,Customer, SalesUser

class OrderForm(ModelForm):
    class Meta:
        model=Order
        #fields=['customer','product']
        fields='__all__'

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        #fields=['customer','product']
        fields='__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class SalesUserForm(ModelForm):
    class Meta:
        model=SalesUser
        #fields=['customer','product']
        fields='__all__'
