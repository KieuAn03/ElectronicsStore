from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'home/index.html')

def details(request):
    return render(request , 'detail.html')
def checkouts(request):
    return render(request, 'checkout.html')
