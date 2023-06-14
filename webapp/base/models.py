from django.db import models

class ProductType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
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
