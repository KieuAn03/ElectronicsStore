from django.urls import path
from ProductRemnant.views import ProductRemnant_page

urlpatterns = [
    path('', ProductRemnant_page, name = "ProductRemnant")
]