from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
# Create your models here.
class StaffProfile(models.Model):
    id_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    joinDate = models.DateField(null = True)
    typeStaff = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.id_profile.name