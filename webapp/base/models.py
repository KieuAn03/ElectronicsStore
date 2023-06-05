from django.db import models


class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
    
class PhoneOS(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100 )
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
    
class FrontPhoneCamera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
    
class BackPhoneCamera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
    
class PhoneColor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name 
    
class PhoneRam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
     
class PhoneStorage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class PhoneSim(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class PhoneBattery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class PhoneChips(models.Model):
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
    color = models.ForeignKey(PhoneColor, on_delete=models.CASCADE)
    ram = models.ForeignKey(PhoneRam, on_delete=models.CASCADE)
    storage = models.ForeignKey(PhoneStorage, on_delete=models.CASCADE)
    brand = models.ForeignKey(PhoneBrand, on_delete=models.CASCADE)
    screen = models.ForeignKey(PhoneScreen, on_delete=models.CASCADE)
    OS = models.ForeignKey(PhoneOS, on_delete=models.CASCADE)
    BackCamera = models.ForeignKey(BackPhoneCamera, on_delete=models.CASCADE)
    FrontCamera = models.ForeignKey( FrontPhoneCamera, on_delete=models.CASCADE)
    chips = models.ForeignKey(PhoneChips, on_delete=models.CASCADE)
    Sim = models.ForeignKey(PhoneSim, on_delete=models.CASCADE)
    battery = models.ForeignKey(PhoneBattery, on_delete=models.CASCADE)
    Info = models.TextField()
    def __str__ (self):
        return self.Name