from django.forms import ModelForm
from .models import Order,Customer

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
