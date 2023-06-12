from django.urls import path
from Profile.views import profile_page

urlpatterns = [
    path('Profile/', profile_page, name = "Profile")
]
