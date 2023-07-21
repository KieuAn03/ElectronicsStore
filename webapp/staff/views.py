from django.shortcuts import render
from staff.models import *
# Create your views here.
def staff_page(request):
    
    return render(request, 'staff/staff_page.html')


def staff_profile(request,id_profile):
    #user = request.user
    staff_profile = StaffProfile.objects.get(id_profile= id_profile)
    context = {
        'staff_profile':staff_profile
    }
    return render(request, 'staff/staff_profile.html',context)
