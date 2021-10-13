from django.db import models

#------------------------------ CUSTOMER ---------------------    
# Create your models here.
class Branch(models.Model):
    br_code= models.CharField(max_length=2,null=True)    
    br_name= models.CharField(max_length=50,null=True)    
    class Meta:
        unique_together = ["br_code","br_name",]
    def __str__(self):
        return str(self.br_code)

class SalesUser(models.Model):    
    SALES_GROUP=( ('CA','Cashier'),  ('AC','Account'),  ('WH','Whouse'), ('MA','Manager'), ('SA','Sales'), ('AD','Admin'), ('GU','Guest'), ('CO','Control'),)
    USER_LEVEL=( ('L1','Level1'),  ('L2','Level2'), ('L3','Level3'), )    
    USER_PRICING=(  ('Any','Any'),  ('Retail','Retail'), ('Dealer','Dealer'),  )        
    
    su_name = models.CharField(max_length=200,null=True)
    su_group = models.CharField(max_length=2,null=True,choices=SALES_GROUP)
    su_level = models.CharField(max_length=2,null=True,choices=USER_LEVEL)
    su_br = models.ForeignKey(Branch, null=True,on_delete=models.SET_NULL)
    su_pricing = models.CharField(max_length=6,null=True,choices=USER_PRICING)    
    
    class Meta:
        unique_together = ["su_name",]

    def __str__(self):
        return str(self.su_name)

class Salesman(models.Model):
    salesm_name = models.CharField(max_length=50,null=True)
    salesm_br = models.ForeignKey( Branch,null=True,on_delete=models.SET_NULL)
    class Meta:
        unique_together = ["salesm_name",]
    def __str__(self):
        return str(self.salesm_name)

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


#------------------------------- Sales USERS, also known as operators -----------

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

#--------------------------------- ORDERS ---------------------    
class Order(models.Model):    
    STATUS=(
        ('Pending','Pending'), 
        ('Confirmed','Confirmed'),        
    )
    ORDER_TYPE=(
        ('CASH','CASH'),
        ('CASH RET','CASH RET'),
        ('CREDIT','CREDIT'),
        ('CREDIT RET','CREDIT RET'),
    )    
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)    
    salesman = models.ForeignKey(Salesman,null=True,on_delete=models.SET_NULL)
    salesuser = models.ForeignKey(SalesUser,null=True,on_delete=models.SET_NULL)
    branch= models.ForeignKey(Branch,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    order_type = models.CharField(max_length=10,null=True,choices=ORDER_TYPE)    
    order_total = models.FloatField(null=True,default=0)
    order_less = models.FloatField(null=True,default=0)
    order_vat = models.FloatField(null=True,default=0)
    order_tax = models.FloatField(null=True,default=0)
    order_amt = models.FloatField(null=True,default=0)

    def __str__(self):
        return str(self.id)

class OrderItems(models.Model):    
    order = models.ForeignKey(Order,null=True,on_delete=models.SET_NULL)    
    product= models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)    
    qty=models.IntegerField(default=0,null=True)
    price=models.FloatField(default=0,null=True)
    
    def __str__(self):
        return str(self.order)
