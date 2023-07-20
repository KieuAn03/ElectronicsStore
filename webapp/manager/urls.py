from django.urls import path
from manager.views import *

urlpatterns = [
   path('revenue_chart/', revenue_static , name="revenue"),
   path('product_control/add_phone/', add_phone_product , name="add_product"),
]