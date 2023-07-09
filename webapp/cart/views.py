from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.http import HttpResponseRedirect,HttpResponse

def index(request):
    cart = Cart.objects.get(complete = False, user = request.user)
    print(cart)
    cart_item_phone = cart.cart_item_phone_set.all()
    context = {
        'cart_items_phone': cart_item_phone,
    }
    return render(request, 'cart.html',context)

def add_to_cart(request , uid):
    variant = request.GET.get('variant')
    product = Product.objects.get(uid = uid)
    user = request.user
    cart ,  _ = Cart.objects.get_or_create(user = user , is_paid = False)

    cart_item = CartItems.objects.create(cart = cart , product = product , )

    if variant:
        variant = request.GET.get('variant')
        size_variant = SizeVariant.objects.get(size_name = variant)
        cart_item.size_variant = size_variant
        cart_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_cart(request , cart_item_uid):
    try:
        cart = Cart.objects.get(complete = False, user = request.user)

        cart_item = cart.cart_item_phone_set.get(id = cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))