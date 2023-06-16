from django.shortcuts import render
from home.models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products' : products}

    return render(request , 'home/index.html',context)

def details(request):
    return render(request , 'detail.html')
def checkouts(request):
    return render(request, 'checkout.html')
