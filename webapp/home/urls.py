from django.urls import path
from home.views import index , details , checkouts
urlpatterns = [
   
    path('' , index , name="index"),
    path('details/', details , name="details"),
    path('checkout/', checkouts , name='checkout')
]