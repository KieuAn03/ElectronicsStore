from django.db import models
from base.models import *
# Create your models here.
class Product (models.Model):
    id = models.AutoField(primary_key=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    price = models.IntegerField(null=True)
    stock = models.IntegerField(null=True)
    discount_product = models.IntegerField(null=True)
    def __str__ (self):
        return self.Name 
    def price_after_discount(self):
        return self.price - self.discount_product
class Phone (models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image0 = models.ImageField(upload_to='products/', null=True, blank=True)
    image1 = models.ImageField(upload_to='products/', null = True, blank=True)
    image2 = models.ImageField(upload_to='products/', null = True, blank=True)
    color = models.ForeignKey(PhoneColor, on_delete=models.CASCADE, null=True)
    ram = models.ForeignKey(PhoneRam, on_delete=models.CASCADE, null=True)
    storage = models.ForeignKey(PhoneStorage, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(PhoneBrand, on_delete=models.CASCADE, null=True)
    screen = models.ForeignKey(PhoneScreen, on_delete=models.CASCADE, null=True)
    OS = models.ForeignKey(PhoneOS, on_delete=models.CASCADE, null=True)
    BackCamera = models.ForeignKey(BackPhoneCamera, on_delete=models.CASCADE, null=True)
    FrontCamera = models.ForeignKey( FrontPhoneCamera, on_delete=models.CASCADE, null=True)
    chips = models.ForeignKey(PhoneChips, on_delete=models.CASCADE, null=True)
    Sim = models.ForeignKey(PhoneSim, on_delete=models.CASCADE, null=True)
    battery = models.ForeignKey(PhoneBattery, on_delete=models.CASCADE, null=True)
    Info = models.TextField( null=True, blank=True)
    def __str__ (self):
        return str(self.id)
    
class Laptop (models.Model):   
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image0 = models.ImageField(upload_to='products/',null= True, blank=True)
    image1 = models.ImageField(upload_to='products/',null= True, blank=True)
    image2 = models.ImageField(upload_to='products/',null= True, blank=True)
    brand = models.ForeignKey(LaptopBrand, on_delete=models.CASCADE,null= True, blank=True)
    color = models.ForeignKey(LaptopColor, on_delete=models.CASCADE,null= True, blank=True)
    CPU = models.ForeignKey(LaptopCPU, on_delete=models.CASCADE,null= True, blank=True)
    ram = models.ForeignKey(LaptopRam, on_delete=models.CASCADE,null= True, blank=True)
    storage = models.ForeignKey(LaptopStorage, on_delete=models.CASCADE,null= True, blank=True)
    screen = models.ForeignKey(LaptopScreen, on_delete=models.CASCADE,null= True, blank=True)
    VGA = models.ForeignKey(LaptopVGA, on_delete=models.CASCADE,null= True, blank=True)
    USB = models.ForeignKey(LaptopUSB, on_delete=models.CASCADE,null= True, blank=True)
    Special = models.ForeignKey(LaptopSpecial, on_delete=models.CASCADE, null= True)
    OS = models.ForeignKey(LaptopOS, on_delete=models.CASCADE,null= True, blank=True)
    design = models.ForeignKey(LaptopDesign, on_delete=models.CASCADE,null= True, blank=True)
    size = models.ForeignKey(LaptopSize, on_delete=models.CASCADE,null= True, blank=True)
    Info = models.TextField()
    def __str__ (self):
         return self.product_id.Name

class watch (models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image0 = models.ImageField(upload_to='products/',null= True, blank=True)
    image1 = models.ImageField(upload_to='products/',null= True, blank=True)
    image2 = models.ImageField(upload_to='products/',null= True, blank=True)
    DoiTuong = models.CharField(choices=[('Nam',('Nam')), ('Nữ',('Nữ')), ('UniSex',('Unisex'))], max_length=10,null= True, blank=True)
    DuongKinh= models.ForeignKey(watchDiameter, on_delete=models.CASCADE,null= True, blank=True)
    ChatLieu = models.ForeignKey(watchChatLieu, on_delete=models.CASCADE,null= True, blank=True)
    Day = models.ForeignKey(watchDay, on_delete=models.CASCADE,null= True, blank=True)
    BoMay = models.ForeignKey(watchBoMay, on_delete=models.CASCADE,null= True, blank=True)
    ChongNuoc = models.ForeignKey(watchChongNuoc, on_delete=models.CASCADE,null= True, blank=True)
    QuocGia = models.ForeignKey(watchQuocGia, on_delete=models.CASCADE,null= True, blank=True)
    Brand = models.ForeignKey(watchBrand, on_delete=models.CASCADE,null= True, blank=True)
    Info = models.TextField(null= True, blank=True)
    def __str__ (self):
         return self.product_id.Name 

class Tablet(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image0 = models.ImageField(upload_to='products/',null= True, blank=True)
    image1 = models.ImageField(upload_to='products/',null= True, blank=True)
    image2 = models.ImageField(upload_to='products/',null= True, blank=True)
    color = models.ForeignKey(TabletColor, on_delete=models.CASCADE,null= True, blank=True)
    screen = models.ForeignKey(TabletScreen, on_delete=models.CASCADE,null= True, blank=True)
    OS = models.ForeignKey(TabletOS, on_delete=models.CASCADE,null= True, blank=True)
    brand = models.ForeignKey(TabletBrand, on_delete=models.CASCADE,null= True, blank=True)
    chips = models.ForeignKey(TabletChip, on_delete=models.CASCADE,null= True, blank=True)
    ram = models.ForeignKey(TabletRam, on_delete=models.CASCADE,null= True, blank=True)
    storage = models.ForeignKey(TabletStorage, on_delete=models.CASCADE,null= True, blank=True)
    Connect = models.ForeignKey(TabletConnect, on_delete=models.CASCADE,null= True, blank=True)
    BackCamera = models.ForeignKey(TabletBackCamera, on_delete=models.CASCADE,null= True, blank=True)
    FrontCamera = models.ForeignKey( TabletFrontCamera, on_delete=models.CASCADE,null= True, blank=True)
    battery = models.ForeignKey(TabletBattery, on_delete=models.CASCADE,null= True, blank=True)
    Info = models.TextField(null= True, blank=True)
    def __str__ (self):
        return self.product_id.Name

class PhoneOptionHard(models.Model):
    Phone_id = models.ForeignKey(Phone,on_delete=models.CASCADE, null= True,blank=True, editable=False,)
    ram= models.ForeignKey(PhoneRam, on_delete=models.CASCADE, null= True)
    Storage = models.ForeignKey(PhoneStorage, on_delete=models.CASCADE, null= True)
    price_add = models.IntegerField(blank=True, null= True)
    def __str__(self):
        return str(self.ram.name +"+" + self.Storage.name)
class PhoneOptionColor(models.Model):
    Phone_id = models.ForeignKey(Phone,on_delete=models.CASCADE)
    color = models.ForeignKey(PhoneColor, on_delete=models.CASCADE)
   
   
class TabletOptionHard(models.Model):
    Tablet_id = models.ForeignKey(Tablet,on_delete=models.CASCADE,null= True,blank=True, editable=False,)
    ram = models.ForeignKey(TabletRam, on_delete=models.CASCADE, null= True, blank=True)
    Storage = models.ForeignKey(TabletStorage, on_delete=models.CASCADE)
    price_add = models.IntegerField(blank=True, null= True)
    def __str__(self):
        return str(self.ram.name +"+" + self.Storage.name)
class TabletOptionColor(models.Model):
    Tablet_id = models.ForeignKey(Tablet,on_delete=models.CASCADE)
    color = models.ForeignKey(TabletColor, on_delete=models.CASCADE)


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
    amount = models.IntegerField(default=1)
    def __str__ (self):
        return self.code