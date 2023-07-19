from django.db import models

# Create your models here.
class TotalRevenue(models.Model):
    order_number = models.IntegerField(null=True,default=0)
    total = models.IntegerField(null=True, default=0)
    def add(self):
        self.order_number += 1
    

class CountItems(models.Model):
    laptop = models.IntegerField(null=True,default=0)
    tablet = models.IntegerField(null=True,default=0)
    phone = models.IntegerField(null=True,default=0)
    watch = models.IntegerField(null=True,default=0)