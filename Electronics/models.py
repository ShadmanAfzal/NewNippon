from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class Laptop(models.Model):
    name = models.CharField(max_length=100)
    details = RichTextField(blank=True,null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="Laptops")
    reviews = models.IntegerField(default=3)
    small_desc = models.TextField(blank=True, default="none", max_length=500)
    def __str__(self):
        return self.name
    
class Mobile(models.Model):
    name = models.CharField(max_length=100)
    details = RichTextField(blank=True,null=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to="Mobiles")
    reviews = models.IntegerField(default=3)
    small_desc = models.TextField(blank=True, default="none", max_length=500)    
    def __str__(self):
        return self.name

class About(models.Model):
    details = RichTextField(blank=True, null=True)
    address = RichTextField(blank=True, null=True)
        
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"
        
class Cart(models.Model):
    product_name = models.CharField(blank=False, max_length=50)
    product_type = models.CharField(blank=False, max_length=50, default="")
    user_email = models.CharField(blank=False, max_length=50)
    price = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    Laptop_details = models.ForeignKey(Laptop, on_delete = models.CASCADE,blank=True, null=True)
    Mobile_details = models.ForeignKey(Mobile, on_delete = models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.product_name

class Order(models.Model):
    product_name = models.CharField(blank=False, max_length=50)
    order_id = models.AutoField(primary_key=True)
    total_amount = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    order_receive = models.CharField(default="", blank=False, max_length=50)
    receiver_phone = models.IntegerField(default=0)
    address = models.TextField(blank=True,default="")
    address1 = models.TextField(blank=False,default="")
    landmark = models.CharField(max_length=100,default="",blank=False)
    city = models.CharField(max_length=50,default="",blank=False)
    State = models.CharField(max_length=50,default="",blank=False)
    zip = models.IntegerField(default=0)
    
    def __str__(self):
        return "Order Id "+str(self.order_id)

class Order_Recieve(models.Model):
    order_id = models.AutoField(primary_key=True)
    product_name = models.CharField(blank=False, max_length=50)
    Currency = models.CharField(max_length=10,blank=False)
    GatewayName = models.CharField(max_length=10,blank=False)
    Respmsg = models.CharField(max_length=10,blank=False)
    Bankname = models.CharField(max_length=50,blank=False)
    PAYMENTMODE = models.CharField(max_length=50,blank=False)
    respcode = models.CharField(max_length=10,blank=False)
    Txnid = models.CharField(max_length=1000,blank=False)
    txnamount = models.CharField(max_length=100,blank=False,default="")
    Status = models.CharField(max_length=10,blank=False)
    BANKTXNID = models.CharField(max_length=10,blank=False)
    TXNDATE = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return str(self.order_id) +"|"+ self.product_name
    