from django.shortcuts import render
from home.models import Product
from .models import CountItems,TotalRevenue
# Create your views here.
def revenue_static(request):
    count_i = CountItems.objects.all()
    total = TotalRevenue.objects.all()
    money = count_i[0].laptop + count_i[0].phone + count_i[0].tablet + count_i[0].watch
    context = {
                'countItems': count_i[0],
                'total': total[0],
                'products':money,
            }
    
    return render(request, 'manager/revenue-static.html', context)