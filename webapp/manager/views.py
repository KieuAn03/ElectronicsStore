from django.shortcuts import render,redirect
from django.contrib import messages      

from home.models import *
from .models import CountItems,TotalRevenue
from base.models import *
from django.core.files.storage import FileSystemStorage
from .form import add_Product,add_Phone
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


def add_phone_product(request):

    if request.method == 'POST' :
        type = ProductType.objects.get(name='Phone')
        pro = Product.objects.create(product_type=type)
        pro.save()
        phone = Phone.objects.create(product_id=pro)
        phone.save()
        u_form = add_Product(request.POST , request.FILES, instance= pro)
        p_form = add_Phone(request.POST, request.FILES, instance= phone)
        if u_form.is_valid():
            pro.save()  
            u_form.save()
            p_form.save()
            messages.success(request, f'Thông tin đã được cập nhật thành công!')
            return redirect('add_product') 
    else:
        u_form = add_Product(request.FILES)
        p_form = add_Phone(request.FILES)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'manager/add_change_phone.html',context) 
