from django.urls import path
from manager.views import revenue_static

urlpatterns = [
   path('revenue_chart/', revenue_static , name="revenue"),
]