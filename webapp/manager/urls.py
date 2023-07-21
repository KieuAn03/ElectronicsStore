from django.urls import path
from manager.views import *

urlpatterns = [
   path('revenue_chart/', revenue_static , name="revenue"),
   path('product_control/add_phone/', add_phone_product , name="add_productphone"),
   path('product_control/add_laptop/', add_laptop_product , name="add_productlaptop"),
   path('product_control/add_watch/', add_watch_product , name="add_productwatch"),
   path('product_control/add_tablet/', add_tablet_product , name="add_producttablet"),

]