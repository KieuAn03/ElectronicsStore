from django.shortcuts import redirect, render
from django.contrib import messages      
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile

# Create your views here.
def login_page(request):
    
    if request.method == 'POST':
        username = request.POST.get('userName')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)



        user_obj = authenticate(username = username , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)

    return render(request ,'accounts/login.html')

def register_page(request):
    if request.method=='POST':
        user_name = request.POST.get('userName')
        email = request.POST.get('email')
        firstName = request.POST.get('first_name')
        lastName = request.POST.get('last_name')
        password = request.POST.get('password')
        re_pass = request.POST.get('rePassword')

        if password != re_pass:
            messages.warning(request, 'Coupon already exists.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            user = User.objects.create_user(username = user_name , email = email)
            user.set_password(password)
            user.save()
            return redirect('index')
    return render(request ,'accounts/register.html')

def profile_page(request):
    form = ProfileUpdateForm()
    context = {'form':form}
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

    return render(request, 'accounts/profile.html',context)


@login_required(login_url='login.html')
def update_profile_page(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST , instance=request.user)
        p_form = ProfileUpdateForm(request.POST , request.FILES ,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Thông tin đã được cập nhật thành công!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/update_profile.html', context)
