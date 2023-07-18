from django.urls import path
from home.views import index , details , checkouts
urlpatterns = [
   
    path('' , index , name="index"),
    path('details/<id>/', details , name="details"),
    path('details/<id>/<color>/', details , name="detail_color"),
    path('details/<id>/<ram>/<storage>/', details , name="details"),
    path('details/<id>/<ram>/<storage>/<color>/', details , name="details"),
    path('checkout/<id>/', checkouts , name='checkout'),

    path('checkout/', checkouts , name='checkout'),


]