from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
def index(request):
    cart = Cart.objects.get(complete = False, user = request.user)
    print(cart)
    cart_item_phone = cart.cart_item_phone_set.all()
    context = {
        'cart_items_phone': cart_item_phone,
    }
    return render(request, 'cart.html',context)
