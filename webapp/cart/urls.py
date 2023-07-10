from django.urls import path
from. import views
from cart.views import *
urlpatterns = [
    path("", views.index),
    path('remove-cart/<cart_item_uid>/' , remove_cart, name="remove_cart"),
    
    
    path('add-to-cart/<id>/' , add_to_cart, name="add_to_cart"),
    path('add-to-cart/<id>/<color>/' , add_to_cart, name="add_to_cart"),
    path('add-to-cart/<id>/<ram>/<storage>/' , add_to_cart, name="add_to_cart"),
    path('add-to-cart/<id>/<ram>/<storage>/<color>/' , add_to_cart, name="add_to_cart"),
    
]
