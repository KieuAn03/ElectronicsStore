from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages      
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm, ProfileForm

# Create your views here.
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form':form}
    return render(request, 'profileapp/profile.html', context)


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('userName')
        password = request.POST.get('password')

        user_obj = authenticate(username = username , password= password)

        if user_obj is not None:
            login(request , user_obj)
            return redirect('/')
        
    return render(request, 'accounts/login.html')

def register_page(request):
    form = UserRegisterForm()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('login')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'accounts/register.html', context)

    context = {'form': form}
    return render(request, 'accounts/register.html', context)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('login')

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

def logout_page(request):
    logout(request)
    return render(request, 'accounts/logout.html')
def remove_coupon(request, cart_id):
    cart = Cart.objects.get(uid = cart_id)
    cart.coupon = None
    cart.save()
    messages.warning(request, 'Coupon removed.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))