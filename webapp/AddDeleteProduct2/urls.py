from django.urls import path
from AddDeleteProduct2.views import AddDeleteProduct2_page

urlpatterns = [
    path('', AddDeleteProduct2_page, name = "AddDeleteProduct2")
]