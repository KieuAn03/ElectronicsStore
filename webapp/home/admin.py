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
admin.site.register(PhoneOptionRam)
admin.site.register(PhoneOptionStorage)
admin.site.register(PhoneOptionColor)
admin.site.register(TabletOptionRam)
admin.site.register(TabletOptionStorage)
admin.site.register(TabletOptionColor)

# Register your models here.
