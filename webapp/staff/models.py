from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StaffProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.jpg',upload_to='profile_images')
    address = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    joinDate = models.DateField(null = True)
    typeStaff = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.user.username