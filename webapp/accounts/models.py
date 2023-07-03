from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile')
    address = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
