from django.urls import path
from AddDeleteProduct.views import AddDeleteProduct_page

urlpatterns = [
    path('', AddDeleteProduct_page, name = "AddDeleteProduct")
]