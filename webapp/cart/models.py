from django.db import models
from base.models import *
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username + ':' + str(self.time_created)

class Cart_Item(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    time_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return User.username + ':' + Product.name + '-sl:' + str(self.quantity)





