from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *
    

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
class StockUnitForm(ModelForm):
    class Meta:
        model=StockUnit
        fields = ('name',)
        labels = {'name': ('Name:'),                        }
        help_texts = {'name': ('enter unit name'),                    }
        error_messages = {
            'name': {
                'max_length': ("This name is too long."),
            },
        }
class StockBrandForm(ModelForm):
    class Meta:
        model=StockBrand
        fields = ('name',)
        labels = {'name': ('Name:'),                        }
        help_texts = {'name': ('enter brand name'),                    }
        error_messages = {
            'name': {
                'max_length': ("This name is too long."),
            },
        }

class StockClassForm(ModelForm):
    class Meta:
        model=StockClass
        fields = ('name',)
        labels = {'name': ('Name:'),                        }
        help_texts = {'name': ('enter class name'),                    }
        error_messages = {
            'name': {
                'max_length': ("This name is too long."),
            },
        }

class StockForm(ModelForm):
    class Meta:
        model=Stock
        fields = (
            'stock_no',
            'stock_name',
            'stock_model',
            'stock_class',
            'stock_brand',
            'stock_unit',
            'stock_price',
            'stock_ucost',
            'stock_location',)
        labels = {
            'stock_no': ('No:'),                        
            'stock_name': ('Name:'),                        
            'stock_model': ('Model:'),                        
            'stock_class': ('Class:'),                        
            'stock_brand': ('Brand:'),                        
            'stock_unit': ('Unit:'),                                    
            'stock_price': ('Price:'),                        
            'stock_ucost': ('Cost:'),                        
            'stock_location': ('Location:'),                        
            }
        
        help_texts = {
            'stock_no': ('stock no'),                    
            'stock_name': ('stock name'),                    
            'stock_model': ('stock model'),                    
            'stock_class': ('select class'),                    
            'stock_brand': ('select brand'),                    

            }

        error_messages = {
            'stock_name': {
                'max_length': ("This name is too long."),
            },
        }
