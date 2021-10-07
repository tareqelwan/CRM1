from django.db import models

#------------------------------ CUSTOMER ---------------------    
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    
    class Meta:
        unique_together = ["name",]
            
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

#------------------------------- USERS -----------------------------
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
    
    class Meta:
        unique_together = ["su_name",]

    def __str__(self):
        return str(self.su_name)

#------------------------------ STOCK ---------------------    
class StockBrand(models.Model):        
    name = models.CharField(max_length=20,null=True)    
    class Meta:
        unique_together = ["name",]
    def __str__(self):
        return str(self.name)

class StockClass(models.Model):        
    name = models.CharField(max_length=20,null=True)    
    class Meta:
        unique_together = ["name",]
    def __str__(self):
        return str(self.name)

class StockCat(models.Model):        
    name = models.CharField(max_length=20,null=True)    
    class Meta:
        unique_together = ["name",]
    def __str__(self):
        return str(self.name)

class StockUnit(models.Model):        
    name = models.CharField(max_length=20,null=True)    
    class Meta:
        unique_together = ["name",]
    def __str__(self):
        return str(self.name)

class Stock(models.Model):
    
    stock_no = models.CharField(max_length=8,null=True,default='0')
    stock_name = models.CharField(max_length=50,null=True)
    stock_model = models.CharField(max_length=20,null=True)
    stock_class = models.ForeignKey(StockClass,null=True,on_delete=models.CASCADE)
    stock_brand = models.ForeignKey(StockBrand,null=True,on_delete=models.CASCADE)
    stock_unit = models.ForeignKey(StockUnit,null=True,on_delete=models.CASCADE)    
    stock_qin = models.FloatField(null=True,default=0)
    stock_qout= models.FloatField(null=True,default=0)
    stock_bf = models.FloatField(null=True,default=0)    
    stock_price = models.FloatField(null=True,default=0)    
    stock_ucost = models.FloatField(null=True,default=0)    
    stock_location = models.CharField(max_length=20,null=True,default='*')    

    class Meta:
        unique_together = ["stock_no","stock_name"]

    def __str__(self):
        return str(self.stock_no)
#------------------------------ END STOCK ---------------------    

