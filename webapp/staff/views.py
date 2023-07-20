from django.shortcuts import render

# Create your views here.
def staff_page(request):
    
    return render(request, 'staff/staff_page.html')

def staff_profile(request):
    
    return render(request, 'staff/staff_profile.html')
