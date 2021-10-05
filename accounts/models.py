from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('In door','In door'), 
        ('Out door','Out door'),        
    )
    name=models.CharField(max_length=200,null=True)
    price=models.FloatField(null=True)
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    description=models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(
        ('Pending','Pending'), 
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    
    def __str__(self):
        return str(self.product.name)

class SalesUser(models.Model):    
    SALES_GROUP=( ('CA','Cashier'),  ('AC','Account'),  ('WH','Whouse'), ('MA','Manager'), ('SA','Sales'), ('AD','Admin'), ('GU','Guest'), ('CO','Control'),)
    USER_LEVEL=( ('L1','Level1'),  ('L2','Level2'), ('L3','Level3'), )
    USER_BR = ( ('HO','HO'), ('DR','DR'), ('RR','RR'), ('JR','JR'), ('KR','KR'), ('S!','S1'), ('MW','MW'), )    
    USER_PRICING=(  ('Any','Any'),  ('Retail','Retail'), ('Dealer','Dealer'),  )        
    su_name = models.CharField(max_length=200,null=True)
    su_group = models.CharField(max_length=2,null=True,choices=SALES_GROUP)
    su_level = models.CharField(max_length=2,null=True,choices=USER_LEVEL)
    su_br = models.CharField(max_length=2,null=True,choices=USER_BR)
    su_pricing = models.CharField(max_length=6,null=True,choices=USER_PRICING)    
    def __str__(self):
        return str(self.su_name)
