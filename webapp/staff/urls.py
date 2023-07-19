from django.urls import path
from staff.views import staff_page

urlpatterns = [
   path('staff-main/', staff_page , name="staff" ),
]