from django.shortcuts import render
from home.models import *
# Create your views here.
def index(request):
    if 'que' in request.GET:
        que = request.GET['que']
        products = Product.objects.filter(Name__icontains=que)
    else:
        products = Product.objects.all()
    context = {'products' : products}

    return render(request , 'home/index.html',context)

def checkouts(request):
    return render(request, 'checkout.html')
def details(request, id, **kwargs):
    products = Product.objects.get(id=id) 
    type = products.product_type.name
    print("HAHAHAAHA")
    
       
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
            select_ram = kwargs['ram']
            select_storage = kwargs['storage']
            option = PhoneOptionHard.objects.filter(Phone_id = phone_id, ram = select_ram, Storage = select_storage)
            context = {
                'product' : products,
                'phone': phone,
                'type': type,
                'hards': Hardoptions,
                'Colors':Colors,
                'rsl': select_ram,
                'ssl': select_storage,
                'option': option[0],
            }  
            
               
    if(type == 'watch'):
        watch = watch.objects.filter(product_id = id)
        context = {
            'products' : products,
            'watch' : watch,
            'type': type,
        }
    if(type == 'tablet'):
        tb = Tablet.objects.filter(product_id = id)
        context = {
            'products' : products,
            'tablet' : tb,
            'type': type,
        }
    return render(request, 'detail.html',context)
