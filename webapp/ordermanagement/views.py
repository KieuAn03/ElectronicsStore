from django.shortcuts import render

# Create your views here.
def ordermanagement_page(request):
    
    return render(request, 'ordermanagement.html')
