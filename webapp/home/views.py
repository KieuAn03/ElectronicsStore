from django.shortcuts import render
from home.models import *
from cart.models import *
from manager.models import *
# Create your views here.
def index(request):
    if 'que' in request.GET:
        que = request.GET['que']
        products = Product.objects.filter(Name__icontains=que)
    else:
        products = Product.objects.all()
    context = {'products' : products}

    return render(request , 'home/index.html',context)

def checkouts(request, **kwargs):

    user = request.user
    cart= Cart.objects.get(user = user , complete = False)

    print(kwargs)
    if(kwargs.get('id')):
        cart.complete= True
        cart.save()

        phone = cart.cart_item_phone_set.all()
        for item in phone:
            CountItems.phone += item.quantity

        laptop = cart.cart_item_laptop_set.all()
        for item in laptop:
            CountItems.laptop += item.quantity

        tablet = cart.cart_item_tablet_set.all()
        for item in tablet:
            CountItems.tablet = item.quantity

        watch = cart.cart_item_watch_set.all()
        for item in watch:
            CountItems.watch = item.quantity

        TotalRevenue.total += cart.total
        TotalRevenue.order_number += 1
         
    context = {
                'cart':cart,
            }
   
    return render(request,'checkout.html', context)
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
    return render(request, 'detail.html',context)
