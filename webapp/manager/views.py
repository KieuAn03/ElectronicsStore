from django.shortcuts import render

# Create your views here.
def revenue_static(request):
    return render(request, 'manager/revenue-static.html')