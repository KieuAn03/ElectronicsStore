from django.urls import path
from staff.views import staff_page,staff_profile

urlpatterns = [
   path('staff-main/', staff_page , name="staff" ),
   path('profile/', staff_profile , name="staff_profile" ),
]