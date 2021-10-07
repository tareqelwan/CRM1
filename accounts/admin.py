from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

admin.site.register(StockUnit)
admin.site.register(StockBrand)
admin.site.register(StockCat)
admin.site.register(StockClass)
admin.site.register(Stock)



