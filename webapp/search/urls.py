from django.urls import path
from search.views import search_page

urlpatterns = [
    path('', search_page, name = "search")
]
