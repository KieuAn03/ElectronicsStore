from django.urls import path
from historycart.views import historycart_page

urlpatterns = [
    path('', historycart_page, name = "Historycart")
]
