from django.db import models
from datetime import date
from django.contrib.auth.models import User

class TimeStamp(models.Model):
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True
  
# Create your models here.
class Seller(TimeStamp):
    name = models.CharField(max_length=100) 
    tel = models.CharField(max_length=10)
    address = models.CharField(max_length=150)
    post_code = models.CharField(max_length=6)
    email = models.EmailField()
    def __str__(self):
        return self.name


class ProductCategory(TimeStamp):
    # product_category_id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class ProductSubCategory(TimeStamp):
    # product_sub_category_id = models.CharField(max_length=6, primary_key=True)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    subname = models.CharField(max_length=150)
    def __str__(self):
        return self.subname

   
class Product(TimeStamp):
    product_sub_category = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150,null=True, blank=True)
    active = models.BooleanField(default=True)
    unit = models.CharField(max_length=20)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name


class Location(models.Model):
    location = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.location

class Move(TimeStamp):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=10, decimal_places=3)
    src_location = models.ForeignKey(Location, related_name='src_zones', on_delete=models.CASCADE)
    des_location = models.ForeignKey(Location, related_name='des_zones', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Inbound(TimeStamp):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    qty = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id) 

class Profile(TimeStamp):
    SEX_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    post_code = models.CharField(max_length=5)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    birth_date = models.DateField()
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

class PickRequest(TimeStamp):
    
    def __str__(self):
        return str(self.id)
    
class SaleOrder(TimeStamp):
    TYPE_ORDER = (
        ('Website','Website'),
        ('Shopee','Shopee'),
        ('Lazada','Lazada'),
    )
    cust_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    picking_request = models.ForeignKey(PickRequest, on_delete = models.CASCADE, blank=True ,null=True)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    type_order = models.CharField(max_length=10, choices=TYPE_ORDER)

    def __str__(self):
        return str(self.id)

class OrderItem(TimeStamp):
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE,blank=True ,null=True)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField()
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __ini__(self):
        return self.id

class Payment(TimeStamp):
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE)
    total_payment = models.DecimalField(max_digits=10, decimal_places=2)
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class PackRequest(TimeStamp):
    sale_order = models.ForeignKey(SaleOrder,on_delete=models.CASCADE, blank=True ,null=True)
    customer_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.sale_order)
    
class PackItem(TimeStamp):
    
    pack_request = models.ForeignKey(PackRequest,on_delete=models.CASCADE, blank=True ,null=True)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return str(self.id)

class PickItem(TimeStamp):
    
    pick_request = models.ForeignKey(PickRequest,on_delete=models.CASCADE, blank=True ,null=True)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField()
    
    
    def __str__(self):
        return str(self.pick_request.id)

class DeliveryStatusTracking(TimeStamp):
    
    def __str__(self):
        return self.id
