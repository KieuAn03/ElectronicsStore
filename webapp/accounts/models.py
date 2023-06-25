from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name="profile")
    username = models.CharField(max_length=100,null=True)
    password = models.CharField(max_length=100,null=True)
    profile_image = models.ImageField(upload_to='profile')
    address = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=100,null=True)
    age = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.username