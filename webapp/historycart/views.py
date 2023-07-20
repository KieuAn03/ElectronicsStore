from django.shortcuts import render
from cart.models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.http import HttpResponseRedirect,HttpResponse
from accounts.models import *
# Create your views here.
def historycart_page(request):
    if(request.user.is_authenticated):
        user = request.user
        cart = Cart.objects.get(complete = False, user = user)
        userprofile = Profile.objects.get(user = user)
        history = Cart.objects.filter(complete = True, user = user)
        context ={
            'history':history,
            'user': userprofile,
            'cart':cart,
        }
        return render(request, 'historycart.html',context)
    else:
        return render(request, 'historycart.html')
# Create your views here.
