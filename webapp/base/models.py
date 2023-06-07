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
    image0 = models.ImageField()
    image1 = models.ImageField()
    image2 = models.ImageField()
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

class LaptopBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class LaptopScreen(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class LaptopRam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class LaptopStorage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class LaptopColor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class LaptopBattery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class LaptopOS(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class LaptopVGA(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class LaptopCPU(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class LaptopUSB(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class LaptopSpecial(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class LaptopDesign(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class LaptopSize(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name

class Laptop (models.Model):   
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image0 = models.ImageField()
    image1 = models.ImageField()
    image2 = models.ImageField()
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
        return self.Name
    
    
    

class watchDiameter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class watchChatLieu(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class watchDay(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class watchBoMay(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class watchChongNuoc(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class watchQuocGia(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class watchBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name

class watch (models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image0 = models.ImageField()
    image1 = models.ImageField()
    image2 = models.ImageField()
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
        return self.Name


class TabletBrand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class TabletScreen(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
class TabletRam(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class TabletStorage(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class TabletColor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class TabletBattery(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class TabletOS(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class TabletChip(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class TabletConnect(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
         return self.name
class TabletFrontCamera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
    
class TabletBackCamera(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__ (self):
        return self.name
    
class Tablet(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image0 = models.ImageField()
    image1 = models.ImageField()
    image2 = models.ImageField()
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
        return self.Name
    
