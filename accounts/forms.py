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
        fields = ('su_name', 'su_group', 'su_level','su_br','su_pricing')
        labels = {
            'su_name': ('USER NAME:'),
            'su_group': ('GROUP:'),
            'su_level': ('LEVEL:'),
            'su_br': ('BRANCH:'),
            'su_pricing': ('PRICING:'),            
            }
        help_texts = {
            'su_name': ('enter user name.'),
            'su_group': ('select user profile'),
            'su_br': ('select branch'),
            'su_pricing': ('select pricing profile'),
            'su_level': ('select level of security'),
        }
        error_messages = {
            'su_name': {
                'max_length': ("This name is too long."),
            },
        }

