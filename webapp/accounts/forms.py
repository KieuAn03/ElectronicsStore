from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.forms.widgets import FileInput
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets = {
         'profile_img': FileInput(),
         }
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','phone','address','profile_image']
        exclude = ['user']
        widgets = {
            'profile_image': FileInput(),
        }