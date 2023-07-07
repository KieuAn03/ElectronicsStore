from django.db import models
from base.models import *
from home.models import *
from django.contrib.auth.models import User

class Checkout(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username + ':' + str(self.time_created)
class Cart(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    date_order =models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction = models.CharField(max_length=100, null=True)
    
    def __str__(self) :
        return str(self.id)
    
class cart_item_phone(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Phone, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    color = models.ForeignKey(PhoneOptionColor, on_delete=models.CASCADE, null=True)
    hard = models.ForeignKey(PhoneOptionHard, on_delete=models.CASCADE, null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return Product.name + '-sl:' + str(self.id)








