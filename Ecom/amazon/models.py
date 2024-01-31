from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=100,default='',null=True)
    last_name = models.CharField(max_length=100,default='',null=True)
    email = models.CharField(max_length=100,default='',null=True)
    password = models.CharField(max_length=255,default='',null=True)
    mobile = models.BigIntegerField(default=0,)
    gender = models.CharField(max_length=100,default='',null=True)

    def __str__(self):
        return self.first_name
    
class Category(models.Model):
    category_image = models.ImageField(upload_to="uploads/category/")
    category_name = models.CharField(max_length=100,default='',null=True)

    def __str__(self):
        return self.category_name
    

class Product(models.Model):
    product_image = models.ImageField(upload_to="uploads/product")
    Product_name = models.CharField(max_length=100,default='',null=True)
    Product_price = models.IntegerField(default=1)
    Product_desc = models.CharField(max_length=100,default='',null=True)
    Product_category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.Product_name
    


class Order(models.Model):
    address = models.CharField(max_length=100,default='',null=True)
    mobile = models.BigIntegerField(default=1)
    custamer = models.ForeignKey(Registration, on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(default=1)
    quanity = models.IntegerField(default=1)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.Product.Product_name
