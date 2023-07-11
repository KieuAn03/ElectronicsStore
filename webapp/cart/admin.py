from django.contrib import admin
from .models import *

admin.site.register(Cart)
admin.site.register(cart_item_phone)
admin.site.register(cart_item_tablet)
admin.site.register(cart_item_laptop)
admin.site.register(cart_item_watch)

# Register your models here.

