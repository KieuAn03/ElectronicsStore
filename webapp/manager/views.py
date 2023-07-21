from django.shortcuts import render
from django.http import HttpResponseRedirect
from home.models import Product
from django.contrib import messages    
from django.contrib.auth.models import User
from .models import CountItems,TotalRevenue
from accounts.models import *
from staff.models import *
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