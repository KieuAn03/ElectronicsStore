from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE,null=True)
    profile_image = models.ImageField(default='default.jpg',upload_to='profile_images')
    address = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        try:
            return self.user.username
        except:
            return "None"