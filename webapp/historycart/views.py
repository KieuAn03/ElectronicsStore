from django.shortcuts import render
from cart.models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
def historycart_page(request):
    
    user = request.user
    history = Cart.objects.filter(complete = True, user = user)
    context ={
        'history':history,
    }
    return render(request, 'historycart.html',context)
# Create your views here.
