import django_filters

from .models import *

class CustomerFilter(django_filters.FilterSet):
    class Meta:
        model=Customer
        fields=['name']
        
class SalesUserFilter(django_filters.FilterSet):
    class Meta:
        model=SalesUser
        fields=['su_name']
        
class StockUnitFilter(django_filters.FilterSet):
    class Meta:
        model=StockUnit
        fields=['name']        

class StockFilter(django_filters.FilterSet):
    class Meta:
        model=Stock
        fields=['stock_name']        

class StockBrandFilter(django_filters.FilterSet):
    class Meta:
        model=StockBrand
        fields=['name']        
        
class StockClassFilter(django_filters.FilterSet):
    class Meta:
        model=StockClass
        fields=['name']        