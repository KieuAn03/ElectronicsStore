from django.shortcuts import render
from home.models import Product
# Create your views here.
def revenue_static(request):
    return render(request, 'manager/revenue-static.html')