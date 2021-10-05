import django_filters

from .models import *

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model=Customer
        fields=['name','phone']

class SalesUserFilter(django_filters.FilterSet):
    class Meta:
        model=SalesUser
        fields=['su_name']