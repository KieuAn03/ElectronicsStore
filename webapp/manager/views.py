from home.models import Product
from django.contrib import messages    
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib import messages      
from django.http import HttpResponseRedirect,HttpResponse
from cart.models import *
from home.models import *
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
def product_control(request):
    product = Product.objects.all()
    context = {
                'products': product,
    }
    return render(request, 'manager/ProductRemnant.html',context)

def delete_product(request, id):
    product = Product.objects.get(id = id)
    product.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def staff_profile(request,id_profile):
    u = User.objects.get(username = id_profile)
    p = Profile.objects.get(user=u )
    s_p = StaffProfile.objects.get(id_profile = p)
    context = {
        'staff_profile':s_p
    }

    return render(request, 'staff/staff_profile.html',context)

def edit_staff_profile(request, id_profile):
    if request.method == 'POST':
            u = User.objects.get(username = id_profile)
            p = Profile.objects.get(user=u )
            s_p = StaffProfile.objects.get(id_profile = p)

            u_form = UserUpdateForm(request.POST , instance=u)
            p_form = ProfileUpdateForm(request.POST , request.FILES ,instance=p)
            s_form = StaffUpdateForm(request.POST, instance=s_p)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                s_form.save()
                messages.success(request, f'Thông tin đã được cập nhật thành công!')
                return redirect('staff_list')
    else:
        u = User.objects.get(username = id_profile)
        p = Profile.objects.get(user=u )
        s_p = StaffProfile.objects.get(id_profile = p)
        u_form = UserUpdateForm( instance=u)
        p_form = ProfileUpdateForm(instance=p)
        s_form = StaffUpdateForm( instance=s_p)
        context = {
            'u_form': u_form,
            'p_form': p_form,
            's_form': s_form,
        }
        return render(request, 'manager/edit_staff_profile.html', context)
    return render(request, 'staff/staff_profile.html', context)

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



def edit_phone_product(request,id):
    if request.method == 'POST':
        pro = Product.objects.get(id = id)
        phone = Phone.objects.get(product_id=pro)
        u_form = add_Product(request.POST , request.FILES, instance= pro)
        p_form = edit_Phone(request.POST, request.FILES, instance= phone)
        if u_form.is_valid():
            pro.save()  
            u_form.save()
            p_form.save()
            messages.success(request, f'Thông tin đã được cập nhật thành công!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        profrom = Product.objects.get(id=id)
        detail = Phone.objects.get(product_id=profrom)
        u_form = add_Product(instance=profrom)
        p_form = edit_Phone(instance = detail)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'manager/add_change_phone.html',context) 

def edit_laptop_product(request,id):
    if request.method == 'POST':
        pro = Product.objects.get(id = id)
        phone = Laptop.objects.get(product_id=pro)
        u_form = add_Product(request.POST , request.FILES, instance= pro)
        p_form = edit_Laptop(request.POST, request.FILES, instance= phone)
        if u_form.is_valid():
            pro.save()  
            u_form.save()
            p_form.save()
            messages.success(request, f'Thông tin đã được cập nhật thành công!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        profrom = Product.objects.get(id=id)
        detail = Laptop.objects.get(product_id=profrom)
        u_form = add_Product(instance=profrom)
        p_form = edit_Laptop(instance = detail)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'manager/add_change_phone.html',context) 

def edit_tablet_product(request,id):
    if request.method == 'POST':
        pro = Product.objects.get(id = id)
        phone = Tablet.objects.get(product_id=pro)
        u_form = add_Product(request.POST , request.FILES, instance= pro)
        p_form = edit_Tablet(request.POST, request.FILES, instance= phone)
        if u_form.is_valid():
            pro.save()  
            u_form.save()
            p_form.save()
            messages.success(request, f'Thông tin đã được cập nhật thành công!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        profrom = Product.objects.get(id=id)
        detail = Tablet.objects.get(product_id=profrom)
        u_form = add_Product(instance=profrom)
        p_form = edit_Tablet(instance = detail)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'manager/add_change_phone.html',context) 

def edit_watch_product(request,id):
    if request.method == 'POST':
        pro = Product.objects.get(id = id)
        phone = watch.objects.get(product_id=pro)
        u_form = add_Product(request.POST , request.FILES, instance= pro)
        p_form = edit_Watch(request.POST, request.FILES, instance= phone)
        if u_form.is_valid():
            pro.save()  
            u_form.save()
            p_form.save()
            messages.success(request, f'Thông tin đã được cập nhật thành công!')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        profrom = Product.objects.get(id=id)
        detail = watch.objects.get(product_id = profrom)
        u_form = add_Product(instance=profrom)
        p_form = edit_Watch(instance = detail)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'manager/add_change_phone.html',context) 



def ordermanagement(request):
    cart = Cart.objects.filter(complete = True, paid = False)
    context = {
        'orders':cart,
        
        
    }
    return render(request, 'manager/ordermanagement.html',context)
def confirmordermanagement(request, id):
    cart = Cart.objects.get(id = id)
    cart.paid = True
   
    phone = cart.cart_item_phone_set.all()
    category = CountItems.objects.first()
    total = TotalRevenue.objects.first()
    for item in phone:
        category.phone += item.quantity
        category.save()

    laptop = cart.cart_item_laptop_set.all()
    for item in laptop:
        category.laptop += item.quantity
        category.save()

    tablet = cart.cart_item_tablet_set.all()
    for item in tablet:
        category.tablet += item.quantity
        category.save()

    watch = cart.cart_item_watch_set.all()
    for item in watch:
        category.watch += item.quantity
        category.save()

    for item in phone:
        category.phone += item.quantity
        category.save()
    total.total += cart.total()
                
                
    total.add()
    total.save()
    cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def cancelordermanagement(request, id):
    cart = Cart.objects.get(id = id)
    
    cart.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    