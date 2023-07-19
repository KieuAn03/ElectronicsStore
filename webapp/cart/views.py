from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.http import HttpResponseRedirect,HttpResponse

def cart(request):
    cart = Cart.objects.get(complete = False, user = request.user)
    print(cart)
    cart_item_phone = cart.cart_item_phone_set.all()
    cart_item_tablet = cart.cart_item_tablet_set.all()
    cart_item_laptop = cart.cart_item_laptop_set.all()
    cart_item_watch = cart.cart_item_watch_set.all()
    context = {
        'cart':cart,
        'cart_items_phone': cart_item_phone,
        'cart_items_tablet': cart_item_tablet,
        'cart_items_laptop': cart_item_laptop,
        'cart_items_watch': cart_item_watch,
    }
    return render(request, 'cart.html',context)

def add_to_cart(request , **kwargs):
    product = Product.objects.get(id = kwargs.get('id'))
    user = request.user
    cart ,  _= Cart.objects.get_or_create(user = user , complete = False)
   
    print(product.product_type) 
    if(str(product.product_type) == 'Phone'):
        
        
        phone = Phone.objects.get(product_id =  kwargs.get('id'))
        if(kwargs.get('ram')):
            print("THIS IS THE TYPEEE") 
            customs = PhoneOptionHard.objects.all()
            print(customs)
            custom = PhoneOptionHard.objects.get(id=1)
            for option in customs:
                if(str(option.ram) == str(kwargs.get('ram')) and str(option.Storage) == str(kwargs.get('storage'))):
                    custom = option
                    break
            if(kwargs.get('color')):  
                print("IM GONNAA SAVEEEE")   
                color = PhoneOptionColor.objects.get(color = kwargs.get('color'))    
                cart_item = cart_item_phone.objects.create(cart=cart , product = phone , quantity = 1 ,price_add= custom,color = color)
                cart_item.save()    
                print("SAVVVVVVEEEE")
            else:
                color = PhoneOptionColor.objects.get(color = phone.color)    
                cart_item = cart_item_phone.objects.create(cart=cart , product = phone , quantity = 1 ,price_add= custom,color = color)
                cart_item.save()   
        elif(kwargs.get('color')):
            custom = PhoneOptionHard.objects.get(ram = phone.ram , storage = phone.storage)
            cart_item = cart_item_phone.objects.create(cart = cart , phone = product ,quantity = 1, price_add= custom,color = kwargs.get('color'))
            cart_item.save()
        else:
            custom = PhoneOptionHard.objects.get(ram = phone.ram , storage = phone.storage)
            cart_item = cart_item_phone.objects.create(cart = cart , product = phone ,quantity = 1,price_add= custom, color = phone.color)
            cart_item.save()
    if(str(product.product_type) == 'Tablet'):
  
        phone = Tablet.objects.get(product_id =  kwargs.get('id'))
        if(kwargs.get('ram')):
            print("THIS IS THE TYPEEE") 
            customs = TabletOptionHard.objects.all()
            print(customs)
            custom = TabletOptionHard.objects.get(id=1)
            for option in customs:
                if(str(option.ram) == str(kwargs.get('ram')) and str(option.Storage) == str(kwargs.get('storage'))):
                    custom = option
                    break
            if(kwargs.get('color')):  
                print("IM GONNAA SAVEEEE")   
                color = TabletOptionColor.objects.get(color = kwargs.get('color'))    
                cart_item = cart_item_tablet.objects.create(cart=cart , product = phone , quantity = 1 ,price_add= custom,color = color)
                cart_item.save()    
                print("SAVVVVVVEEEE")
            else:
                color = TabletOptionColor.objects.get(color = phone.color)    
                cart_item = cart_item_tablet.objects.create(cart=cart , product = phone , quantity = 1 ,price_add= custom,color = color)
                cart_item.save()   
        elif(kwargs.get('color')):
            custom = TabletOptionHard.objects.get(ram = phone.ram , storage = phone.storage)
            cart_item = cart_item_tablet.objects.create(cart = cart , phone = product ,quantity = 1, price_add= custom,color = kwargs.get('color'))
            cart_item.save()
        else:
            custom = TabletOptionHard.objects.get(ram = phone.ram , storage = phone.storage)
            cart_item = cart_item_tablet.objects.create(cart = cart , product = phone ,quantity = 1,price_add= custom, color = phone.color)
            cart_item.save() 
            
            
    if(str(product.product_type) == 'Laptop'):
  
        phone = Laptop.objects.get(product_id =  kwargs.get('id'))
        cart_item = cart_item_laptop.objects.create(cart = cart , product = phone ,quantity = 1)
        cart_item.save() 
    if(str(product.product_type) == 'Watch'):
  
        phone = watch.objects.get(product_id =  kwargs.get('id'))
        cart_item = cart_item_watch.objects.create(cart = cart , product = phone ,quantity = 1)
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

