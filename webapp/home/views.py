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
def details(request):
    id = request.GET.get('id') 
    products = Product.objects.filter(id=id) 
    type = products[0].product_type.name
    print("this is the type: " +type)
    if(type == 'Laptop'):
        laptop = Laptop.objects.filter(product_id = id)
        context = {
            'product' : products[0],
            'laptop' : laptop[0],
            'type': type,
        }
    if(type == 'Phone'):
        phone = Phone.objects.filter(product_id = id)
      
        context = {
            'product' : products[0],
            'phone': phone[0],
            'type': type,
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
