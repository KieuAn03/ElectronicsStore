from django.db import models


class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class PhoneOS(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name

class PhoneBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name

class PhoneScreen(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
    
class Product (models.Model):
    id = models.AutoField(primary_key=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    image = models.ImageField()
    Name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    def __str__ (self):
        return self.Name 


class Phone (models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    screen = models.ForeignKey(PhoneScreen, on_delete=models.CASCADE)
    OS = models.ForeignKey(PhoneOS, on_delete=models.CASCADE)
    brand = models.ForeignKey(PhoneBrand, on_delete=models.CASCADE)
    def __str__ (self):
        return self.Name