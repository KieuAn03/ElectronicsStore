from django.urls import path
from ordermanagement.views import ordermanagement_page

urlpatterns = [
    path('', ordermanagement_page, name = "ordermanagement")
]