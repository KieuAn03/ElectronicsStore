from django.shortcuts import render
from home.models import *
from cart.models import *
from django.utils.crypto import get_random_string
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from accounts.models import *
from manager.models import CountItems, TotalRevenue
# Create your views here.
def index(request):
    try:
        cart = Cart.objects.get(complete = False, user = request.user)
    except:
        pass

    if 'que' in request.GET:
        que = request.GET['que']
        products = Product.objects.filter(Name__icontains=que)
    else:
        products = Product.objects.all()
    if (request.user.is_authenticated ):
        try: 
            context = {'products' : products,
                    'cart': cart,
                    }
        except:
            context = {'products' : products,
                    
                    }
    else:
        context = {'products' : products,
               
                }

    return render(request , 'home/index.html',context)

def checkouts(request, **kwargs):
    if(request.user.is_authenticated):
        user = request.user
        userinfo = Profile.objects.get(user = user)
        try:
            cart= Cart.objects.get(user = user , complete = False)
        except:
            return render(request,'checkout.html')
        cart_i ,  _= cart_info.objects.get_or_create(cart  = cart)
        cart_i.Name = userinfo.name
        cart_i.Phone_num= userinfo.phone
        cart_item_phone = cart.cart_item_phone_set.all()
        cart_item_tablet = cart.cart_item_tablet_set.all()
        cart_item_laptop = cart.cart_item_laptop_set.all()
        cart_item_watch = cart.cart_item_watch_set.all()
        if request.method=='POST':
            if 'voucher' in request.POST:
                if(cart.is_discounted!= True):
                    vchr = voucher.objects.all()
                    for v in vchr:
                        
                        if(request.POST.get('voucher') == str(v.code)):
                            cart.is_discounted= True
                            cart.voucher = v
                            cart.save()
                
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        if request.method=='POST':
            if 'voucher' not in request.POST:
                if(request.POST.get('customername')):
                    cart_i.Name = request.POST.get('customername')
                    cart_i.Phone_num= request.POST.get('customerphone')
                    cart_i.save()
                unique_id = get_random_string(length=8)
                user = request.user
                unique_id = str(user)+ unique_id
                print(cart.id) 
                cart.complete= True
                cart.transaction= unique_id
                cart.save()

                

               
                history_item = historycart.objects.create(cart = cart ,user = user, cart_info = cart_i)
                history_item.save()
                phone = cart.cart_item_phone_set.all()
                for item in phone :
                    product = item.product.product_id
                    product.stock = product.stock - item.quantity
                    product.save()
                tablet = cart.cart_item_tablet_set.all()
                for item in tablet :
                    product = item.product.product_id
                    product.stock = product.stock - item.quantity
                    product.save()
                laptop = cart.cart_item_laptop_set.all()
                for item in laptop :
                    product = item.product.product_id
                    product.stock = product.stock - item.quantity
                    product.save()
                watch = cart.cart_item_watch_set.all()
                for item in watch :
                    product = item.product.product_id
                    product.stock = product.stock - item.quantity
                    product.save()
                cart_i.save()
        context = {
                    'cart':cart,
                    'info':cart_i,
                    'cart_items_phone': cart_item_phone,
                    'cart_items_tablet': cart_item_tablet,
                    'cart_items_laptop': cart_item_laptop,
                    'cart_items_watch': cart_item_watch,
                }
        return render(request,'checkout.html', context)
    else:
        return render(request,'checkout.html')





def details(request, id, **kwargs):
    products = Product.objects.get(id=id) 
    type = products.product_type.name
    
       
    if(type == 'Laptop'):
        laptop = Laptop.objects.get(product_id = id)
        context = {
            'product' : products,
            'laptop' : laptop,
            'type': type,
        }
    if(type == 'Phone'):
        phone = Phone.objects.get(product_id = id)
        phone_id = phone.id
        Hardoptions = PhoneOptionHard.objects.filter(Phone_id = phone_id)
        Colors = PhoneOptionColor.objects.filter(Phone_id = phone_id)
        context = {
            'product' : products,
            'phone': phone,
            'type': type,
            'hards': Hardoptions,
            'Colors':Colors,
        }
        if kwargs.get('ram'):
            select_ram = str(kwargs.get('ram'))
            select_storage = str(kwargs.get('storage') )
            
            choose = Hardoptions[0]
            for option in Hardoptions:
                #print(option.ram , ' ' , option.Storage)
                #print(select_ram , ' ' , select_storage)

                if str(option.ram) == str(select_ram) and str(option.Storage) == str(select_storage):
                    choose = option
                    break
            if kwargs.get('color'):
                colorselect = str(kwargs.get('color'))
                context = {
                        'product' : products,
                        'phone': phone,
                        'type': type,
                        'hards': Hardoptions,
                        'Colors':Colors,
                        'rsl': select_ram,
                        'ssl': select_storage,
                        'option': choose,
                        'colorr':colorselect,
                    }
            else:
                context = {
                    'product' : products,
                    'phone': phone,
                    'type': type,
                    'hards': Hardoptions,
                    'Colors':Colors,
                    'rsl': select_ram,
                    'ssl': select_storage,
                    'option': choose,
                }  
                
        elif kwargs.get('color'):
            colorselect = str(kwargs.get('color'))
            context = {
                        'product' : products,
                        'phone': phone,
                        'type': type,
                        'hards': Hardoptions,
                        'Colors':Colors,
                        'colorr':colorselect,
                    }
               
    if(type == 'Watch'):
        laptop = watch.objects.get(product_id = id)
        context = {
            'product' : products,
            'laptop' : laptop,
            'type': type,
        }
    if(type == 'Tablet'):
        phone = Tablet.objects.get(product_id = id)
        phone_id = phone.id
        Hardoptions = TabletOptionHard.objects.filter(Tablet_id = phone_id)
        Colors = TabletOptionColor.objects.filter(Tablet_id = phone_id)
        context = {
            'product' : products,
            'phone': phone,
            'type': type,
            'hards': Hardoptions,
            'Colors':Colors,
        }
        if kwargs.get('ram'):
            select_ram = str(kwargs.get('ram'))
            select_storage = str(kwargs.get('storage') )
            
            choose = Hardoptions[0]
            for option in Hardoptions:
                #print(option.ram , ' ' , option.Storage)
                #print(select_ram , ' ' , select_storage)

                if str(option.ram) == str(select_ram) and str(option.Storage) == str(select_storage):
                    choose = option
                    break
            if kwargs.get('color'):
                colorselect = str(kwargs.get('color'))
                context = {
                        'product' : products,
                        'phone': phone,
                        'type': type,
                        'hards': Hardoptions,
                        'Colors':Colors,
                        'rsl': select_ram,
                        'ssl': select_storage,
                        'option': choose,
                        'colorr':colorselect,
                    }
            else:
                context = {
                    'product' : products,
                    'phone': phone,
                    'type': type,
                    'hards': Hardoptions,
                    'Colors':Colors,
                    'rsl': select_ram,
                    'ssl': select_storage,
                    'option': choose,
                }  
        elif kwargs.get('color'):
            colorselect = str(kwargs.get('color'))
            context = {
                        'product' : products,
                        'phone': phone,
                        'type': type,
                        'hards': Hardoptions,
                        'Colors':Colors,
                        'colorr':colorselect,
                        
                    }
    if(request.user.is_authenticated):
        try:
            cart = Cart.objects.get(complete = False, user = request.user)
            context['cart'] = cart
        except:
            pass
    return render(request, 'detail.html',context)
