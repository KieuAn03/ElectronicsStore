from django.urls import path
from manager.views import revenue_static,add_staff

urlpatterns = [
   path('revenue_chart/', revenue_static , name="revenue"),
   path('add_staff/', add_staff , name="add_staff"),
]