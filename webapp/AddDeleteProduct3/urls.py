from django.urls import path
from AddDeleteProduct3.views import AddDeleteProduct3_page

urlpatterns = [
    path('', AddDeleteProduct3_page, name = "AddDeleteProduct3")
]