from django.urls import path
from manager.views import revenue_static,add_staff,staff_list, remove_staff,edit_staff_profile,mainpage
from manager.views import *

urlpatterns = [
   path('ordermanagement/', ordermanagement , name="ordermanagement"),
   path('ordermanagement/confirm/<id>/', confirmordermanagement , name="ordermanagement"),
   path('ordermanagement/cancel/<id>/', cancelordermanagement , name="ordermanagement"),
   path('', mainpage , name="main"),
   path('revenue_chart/', revenue_static , name="revenue"),
   path('add_staff/', add_staff , name="add_staff"),
   path('staff_list/', staff_list, name="staff_list"),
   path('remove_staff/<id_profile>', remove_staff, name='remove_staff'),
   path('product_control/', product_control , name="product_control"),
   path('product_control/delete/<id>/', delete_product , name="deleteproduct"),
   path('staff_profile/<id_profile>/', staff_profile, name='staff_profile'),
   path('edit_staff_profile/<id_profile>/', edit_staff_profile, name='edit_staff_profile'),
   path('product_control/add_phone/', add_phone_product , name="add_productphone"),
   path('product_control/add_laptop/', add_laptop_product , name="add_productlaptop"),
   path('product_control/add_watch/', add_watch_product , name="add_productwatch"),
   path('product_control/add_tablet/', add_tablet_product , name="add_producttablet"),
   path('product_control/edit_phone/<id>/', edit_phone_product , name="edit_productphone"),
   path('product_control/edit_laptop/<id>/', edit_laptop_product , name="edit_productlaptop"),
   path('product_control/edit_tablet/<id>/', edit_tablet_product , name="edit_producttablet"),
   path('product_control/edit_watch/<id>/', edit_watch_product , name="edit_productwatch"),

]  