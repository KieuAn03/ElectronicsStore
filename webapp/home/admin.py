from django.contrib import admin
from .models import *
from base.models import *

admin.site.register(Product)
admin.site.register(Phone)
admin.site.register(Laptop)
admin.site.register(watch)
admin.site.register(Tablet)
admin.site.register(voucher)
admin.site.register(discount)

# Register your models here.
