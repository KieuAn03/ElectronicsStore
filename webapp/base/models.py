from django.db import models

# Create your models here.
class Product (models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    def __str__ (self):
        return self.Name