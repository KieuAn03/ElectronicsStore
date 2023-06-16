from django.shortcuts import redirect, render
from django.contrib import messages      
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse

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
            user = User.objects.create_user(first_name = firstName , last_name= lastName , email = email , username = user_name)
            user.set_password(password)
            user.save()
            return redirect('index')
    return render(request ,'accounts/register.html')
