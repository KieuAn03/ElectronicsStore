from django.urls import path
from accounts.views import login_page, register_page, profile_page, update_profile_page, logout_page

urlpatterns = [
   path('login/', login_page , name="login" ),
   path('logout/', logout_page , name="logout" ),
   path('register/' , register_page , name="register"),
   path('profile/' , profile_page , name="profile"),
   path('update-profile/' , update_profile_page, name="update_profile"),
]
