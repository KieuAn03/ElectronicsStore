from django.db import models
from base.models import *
# Create your models here.
class Product (models.Model):
    id = models.AutoField(primary_key=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    Name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    def __str__ (self):
        return self.Name 
    
class Phone (models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image0 = models.ImageField(upload_to='products/')
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
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
        return self.product_id.Name
    
class Laptop (models.Model):   
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image0 = models.ImageField(upload_to='products/')
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    brand = models.ForeignKey(LaptopBrand, on_delete=models.CASCADE)
    color = models.ForeignKey(LaptopColor, on_delete=models.CASCADE)
    CPU = models.ForeignKey(LaptopCPU, on_delete=models.CASCADE)
    ram = models.ForeignKey(LaptopRam, on_delete=models.CASCADE)
    storage = models.ForeignKey(LaptopStorage, on_delete=models.CASCADE)
    screen = models.ForeignKey(LaptopScreen, on_delete=models.CASCADE)
    VGA = models.ForeignKey(LaptopVGA, on_delete=models.CASCADE)
    USB = models.ForeignKey(LaptopUSB, on_delete=models.CASCADE)
    Special = models.ForeignKey(LaptopSpecial, on_delete=models.CASCADE, null= True)
    OS = models.ForeignKey(LaptopOS, on_delete=models.CASCADE)
    design = models.ForeignKey(LaptopDesign, on_delete=models.CASCADE)
    size = models.ForeignKey(LaptopSize, on_delete=models.CASCADE)
    release_date = models.DateField()
    Info = models.TextField()
    def __str__ (self):
         return self.product_id.Name

class watch (models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image0 = models.ImageField(upload_to='products/')
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    DoiTuong = models.CharField(choices=[('Nam',('Nam')), ('Nữ',('Nữ')), ('UniSex',('Unisex'))], max_length=10)
    DuongKinh= models.ForeignKey(watchDiameter, on_delete=models.CASCADE)
    ChatLieu = models.ForeignKey(watchChatLieu, on_delete=models.CASCADE)
    Day = models.ForeignKey(watchDay, on_delete=models.CASCADE)
    BoMay = models.ForeignKey(watchBoMay, on_delete=models.CASCADE)
    ChongNuoc = models.ForeignKey(watchChongNuoc, on_delete=models.CASCADE)
    QuocGia = models.ForeignKey(watchQuocGia, on_delete=models.CASCADE)
    Brand = models.ForeignKey(watchBrand, on_delete=models.CASCADE)
    Info = models.TextField()
    def __str__ (self):
         return self.product_id.Name 

class Tablet(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image0 = models.ImageField(upload_to='products/')
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    color = models.ForeignKey(TabletColor, on_delete=models.CASCADE)
    screen = models.ForeignKey(TabletScreen, on_delete=models.CASCADE)
    OS = models.ForeignKey(TabletOS, on_delete=models.CASCADE)
    brand = models.ForeignKey(TabletBrand, on_delete=models.CASCADE)
    chips = models.ForeignKey(TabletChip, on_delete=models.CASCADE)
    ram = models.ForeignKey(TabletRam, on_delete=models.CASCADE)
    storage = models.ForeignKey(TabletStorage, on_delete=models.CASCADE)
    Connect = models.ForeignKey(TabletConnect, on_delete=models.CASCADE)
    BackCamera = models.ForeignKey(TabletBackCamera, on_delete=models.CASCADE)
    FrontCamera = models.ForeignKey( TabletFrontCamera, on_delete=models.CASCADE)
    battery = models.ForeignKey(TabletBattery, on_delete=models.CASCADE)
    Info = models.TextField()
    def __str__ (self):
        return self.product_id.Name

class PhoneOptionRam(models.Model):
    Phone_id = models.ForeignKey(Phone,on_delete=models.CASCADE)
    ram = models.ForeignKey(PhoneRam, on_delete=models.CASCADE, null= True, blank=True)
    price_add = models.IntegerField(blank=True, null= True)
    
class PhoneOptionStorage(models.Model):
    Phone_id = models.ForeignKey(Phone,on_delete=models.CASCADE)
    storage = models.ForeignKey(PhoneStorage, on_delete=models.CASCADE, null= True, blank=True)
    price_add = models.IntegerField(blank=True, null= True)

class PhoneOptionColor(models.Model):
    Phone_id = models.ForeignKey(Phone,on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=True)
   
   
class TabletOptionRam(models.Model):
    Tablet_id = models.ForeignKey(Tablet,on_delete=models.CASCADE)
    ram = models.ForeignKey(TabletRam, on_delete=models.CASCADE, null= True, blank=True)
    price_add = models.IntegerField(blank=True, null= True)
    
class TabletOptionStorage(models.Model):
    Tablet_id = models.ForeignKey(Tablet,on_delete=models.CASCADE)
    storage = models.ForeignKey(TabletStorage, on_delete=models.CASCADE, null= True, blank=True)
    price_add = models.IntegerField(blank=True, null= True)

class TabletOptionColor(models.Model):
    Tablet_id = models.ForeignKey(Tablet,on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=True) 


class discount (models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    discount = models.IntegerField()
    def __str__ (self):
        return self.Name
    
class voucher(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=100)
    discount = models.IntegerField()
    def __str__ (self):
        return self.code