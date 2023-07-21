from django.urls import path
from manager.views import revenue_static,add_staff,staff_list

urlpatterns = [
   path('revenue_chart/', revenue_static , name="revenue"),
   path('add_staff/', add_staff , name="add_staff"),
   path('staff_list/', staff_list, name="staff_list"),
]