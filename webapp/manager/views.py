from django.http import HttpResponseRedirect
from home.models import Product
from django.contrib import messages    
from django.contrib.auth.models import User
from .models import CountItems,TotalRevenue
from accounts.models import *
from staff.models import *
from django.shortcuts import render,redirect    
from home.models import *
from base.models import *
from django.core.files.storage import FileSystemStorage
from .form import *
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

def add_staff(request):
    if request.method == 'POST':
        user_name = request.POST.get('userName')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        user_type = request.POST.get('user_type')

        user = User.objects.create_user(email = email , username = user_name)
        user.set_password(password)
        user.save()
        
        profile = Profile.objects.get( user =user  )
        profile.name= name
        profile.phone =phone
        profile.is_staff= True
        profile.is_customer= False
        profile.save()
        try:
            staff  = StaffProfile.objects.create(id_profile =profile)
            staff.typeStaff = user_type
            staff.save()
        except:
            print(profile)

    return render(request, 'manager/add_staff.html')

def staff_list(request):
    user_profile = Profile.objects.filter(is_staff = True)
    staff_profile = StaffProfile.objects.all()
    context = {
        'profile':user_profile,
        'staff_profile':staff_profile
    }
    return render(request, 'manager/staff_list.html',context)

def remove_staff(request, id_profile):
    try:
        u = User.objects.get(username = id_profile)
        u.delete()
        
        messages.success(request, "The user is deleted")  
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))       

    except User.DoesNotExist:
        messages.error(request, "User does not exist")    
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    except Exception as e: 
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def add_phone_product(request):
    if request.method == 'POST':
        type = ProductType.objects.get(name='Phone')
        pro = Product.objects.create(product_type=type)
        pro.save()
        phone = Phone.objects.create(product_id=pro)
        phone.save()
        u_form = add_Product(request.POST , request.FILES, instance= pro)
        p_form = add_Phone(request.POST, request.FILES, instance= phone)
        if u_form.is_valid():
            if p_form.data.get('coloroption'):
                color_id = p_form.data.get('coloroption')
                color = PhoneColor(id = color_id)
                cl = PhoneOptionColor.objects.create(color=color,Phone_id=phone)
                cl.save()
            if p_form.data.get('coloroption1'):
                color_id = p_form.data.get('coloroption1')
                color = PhoneColor(id = color_id)
                cl = PhoneOptionColor.objects.create(color=color,Phone_id=phone)
                cl.save()
            if p_form.data.get('coloroption2'):
                color_id = p_form.data.get('coloroption2')
                color = PhoneColor(id = color_id)
                cl = PhoneOptionColor.objects.create(color=color,Phone_id=phone)
                cl.save()
            if p_form.data.get('ram_storage_option'):
                color_id = p_form.data.get('ram_storage_option')
                hard = PhoneOptionHard.objects.get(id = color_id)
                hard.Phone_id = phone
                hard.save()
            if p_form.data.get('ram_storage_option1'):
                color_id = p_form.data.get('ram_storage_option1')
                hard = PhoneOptionHard.objects.get(id = color_id)
                hard.Phone_id = phone
                hard.save()
            if p_form.data.get('ram_storage_option2'):
                color_id = p_form.data.get('ram_storage_option2')
                hard = PhoneOptionHard.objects.get(id = color_id)
                hard.Phone_id = phone
                hard.save()
            pro.save()  
            u_form.save()
            p_form.save()
            messages.success(request, f'Thông tin đã được cập nhật thành công!')
            return redirect('add_productphone') 
    else:
        u_form = add_Product(request.FILES)
        p_form = add_Phone(request.FILES)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'manager/add_change_phone.html',context) 

def add_laptop_product(request):
    if request.method == 'POST':
        type = ProductType.objects.get(name='Laptop')
        pro = Product.objects.create(product_type=type)
        pro.save()
        phone = Laptop.objects.create(product_id=pro)
        phone.save()
        u_form = add_Product(request.POST , request.FILES, instance= pro)
        p_form = add_Laptop(request.POST, request.FILES, instance= phone)
        if u_form.is_valid():
            
            pro.save()  
            u_form.save()
            p_form.save()
            messages.success(request, f'Thông tin đã được cập nhật thành công!')
            return redirect('add_productlaptop') 
    else:
        u_form = add_Product(request.FILES)
        p_form = add_Laptop(request.FILES)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'manager/add_change_phone.html',context)

def add_watch_product(request):
    if request.method == 'POST':
        type = ProductType.objects.get(name='Watch')
        pro = Product.objects.create(product_type=type)
        pro.save()
        phone = watch.objects.create(product_id=pro)
        phone.save()
        u_form = add_Product(request.POST , request.FILES, instance= pro)
        p_form = add_Watch(request.POST, request.FILES, instance= phone)
        if u_form.is_valid():
            pro.save()  
            u_form.save()
            p_form.save()
            messages.success(request, f'Thông tin đã được cập nhật thành công!')
            return redirect('add_productwatch') 
    else:
        u_form = add_Product(request.FILES)
        p_form = add_Watch(request.FILES)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'manager/add_change_phone.html',context)

def add_tablet_product(request):
    if request.method == 'POST':
        type = ProductType.objects.get(name='Tablet')
        pro = Product.objects.create(product_type=type)
        pro.save()
        phone = Tablet.objects.create(product_id=pro)
        phone.save()
        u_form = add_Product(request.POST , request.FILES, instance= pro)
        p_form = add_Tablet(request.POST, request.FILES, instance= phone)
        if u_form.is_valid():
            if p_form.data.get('coloroption'):
                color_id = p_form.data.get('coloroption')
                color = TabletColor(id = color_id)
                cl = TabletOptionColor.objects.create(color=color,Tablet_id=phone)
                cl.save()
            if p_form.data.get('coloroption1'):
                color_id = p_form.data.get('coloroption1')
                color = TabletColor(id = color_id)
                cl = TabletOptionColor.objects.create(color=color,Tablet_id=phone)
                cl.save()
            if p_form.data.get('coloroption2'):
                color_id = p_form.data.get('coloroption2')
                color = TabletColor(id = color_id)
                cl = TabletOptionColor.objects.create(color=color,Tablet_id=phone)
                cl.save()
            if p_form.data.get('ram_storage_option'):
                color_id = p_form.data.get('ram_storage_option')
                hard = TabletOptionHard.objects.get(id = color_id)
                hard.Phone_id = phone
                hard.save()
            if p_form.data.get('ram_storage_option1'):
                color_id = p_form.data.get('ram_storage_option1')
                hard = TabletOptionHard.objects.get(id = color_id)
                hard.Phone_id = phone
                hard.save()
            if p_form.data.get('ram_storage_option2'):
                color_id = p_form.data.get('ram_storage_option2')
                hard = TabletOptionHard.objects.get(id = color_id)
                hard.Phone_id = phone
                hard.save()
            pro.save()  
            u_form.save()
            p_form.save()
            messages.success(request, f'Thông tin đã được cập nhật thành công!')
            return redirect('add_producttablet') 
    else:
        u_form = add_Product(request.FILES)
        p_form = add_Tablet(request.FILES)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'manager/add_change_phone.html',context) 
