from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import FileInput
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from home.models import *
from base.models import *

class add_Product(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['id','image','product_type']
        fields = "__all__"
        
class add_Phone(forms.ModelForm):
    class Meta:
        model = Phone
        exclude = ['id','product_id']
        fields="__all__"

