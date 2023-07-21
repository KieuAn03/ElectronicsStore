from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import FileInput
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import ModelForm
from home.models import *
from base.models import *
from accounts.models import *
from staff.models import *
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.conf import settings

class RelatedFieldWidgetCanAdd(widgets.Select):

   def __init__(self, related_model, related_url=None, *args, **kw):

       super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

       if not related_url:
           rel_to = related_model
           info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
           related_url = 'admin:%s_%s_add' % info

       # Be careful that here "reverse" is not allowed
       self.related_url = related_url

   def render(self, name, value, *args, **kwargs):
       self.related_url = reverse(self.related_url)
       output = [super(RelatedFieldWidgetCanAdd, self).render(name, value, *args, **kwargs)]
       output.append('<a href="%s" target="_blank" rel="noopener noreferrer" class="add-another related-widget-wrapper-link add-related" id="add_id_%s" data-popup="yes" onclick="return showAddAnotherPopup(this);"> ' % \
           (self.related_url, name))
       output.append('<img src="%simage/addbtn.png" width="30" height="30" alt="%s"/></a> ' % (settings.STATIC_URL, 'Add Another'))
       return mark_safe(''.join(output))




class add_Product(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['id','product_type']
        fields = "__all__"
        
class add_Phone(forms.ModelForm):
    coloroption = forms.ModelChoiceField(required=False,queryset=PhoneColor.objects.all(),widget=RelatedFieldWidgetCanAdd(PhoneColor, ))
    coloroption1 = forms.ModelChoiceField(required=False,queryset=PhoneColor.objects.all(),widget=RelatedFieldWidgetCanAdd(PhoneColor, ))
    coloroption2 = forms.ModelChoiceField(required=False,queryset=PhoneColor.objects.all(),widget=RelatedFieldWidgetCanAdd(PhoneColor, ))
   
    ram_storage_option = forms.ModelChoiceField(required=False,queryset=PhoneOptionHard.objects.all(),widget=RelatedFieldWidgetCanAdd(PhoneOptionHard, ))
    ram_storage_option1 = forms.ModelChoiceField(required=False,queryset=PhoneOptionHard.objects.all(),widget=RelatedFieldWidgetCanAdd(PhoneOptionHard, ))
    ram_storage_option2 = forms.ModelChoiceField(required=False,queryset=PhoneOptionHard.objects.all(),widget=RelatedFieldWidgetCanAdd(PhoneOptionHard, ))
   
    
    color = forms.ModelChoiceField(
       required=False,
       queryset=PhoneColor.objects.all(),
       widget=RelatedFieldWidgetCanAdd(PhoneColor, ))
    ram = forms.ModelChoiceField(
        required=False,
        queryset=PhoneRam.objects.all(),
        widget=RelatedFieldWidgetCanAdd(PhoneRam, ))
    storage = forms.ModelChoiceField(
        required=False,
        queryset=PhoneStorage.objects.all(),
        widget=RelatedFieldWidgetCanAdd(PhoneStorage, ))
    brand = forms.ModelChoiceField(
        required=False,
        queryset=PhoneBrand.objects.all(),
        widget=RelatedFieldWidgetCanAdd(PhoneBrand, ))
    screen = forms.ModelChoiceField(
        required=False,
        queryset=PhoneScreen.objects.all(),
        widget=RelatedFieldWidgetCanAdd(PhoneScreen, ))
    OS = forms.ModelChoiceField(
        required=False,
        queryset=PhoneOS.objects.all(),
        widget=RelatedFieldWidgetCanAdd(PhoneOS, ))
    BackCamera = forms.ModelChoiceField(
        required=False,
        queryset=BackPhoneCamera.objects.all(),
        widget=RelatedFieldWidgetCanAdd(BackPhoneCamera, ))
    FrontCamera = forms.ModelChoiceField(
        required=False,
        queryset=FrontPhoneCamera.objects.all(),
        widget=RelatedFieldWidgetCanAdd(FrontPhoneCamera, ))
    chips = forms.ModelChoiceField(
        required=False,
        queryset=PhoneChips.objects.all(),
        widget=RelatedFieldWidgetCanAdd(PhoneChips, ))
    Sim = forms.ModelChoiceField(
        required=False,
        queryset=PhoneSim.objects.all(),
        widget=RelatedFieldWidgetCanAdd(PhoneSim, ))
    battery = forms.ModelChoiceField(
        required=False,
        queryset=PhoneBattery.objects.all(),
        widget=RelatedFieldWidgetCanAdd(PhoneBattery, ))
    class Meta:
        model = Phone
        exclude = ['id','product_id']
        fields="__all__"
                                

class add_Laptop(forms.ModelForm):
    color = forms.ModelChoiceField(
       required=False,
       queryset=LaptopColor.objects.all(),
       widget=RelatedFieldWidgetCanAdd(LaptopColor, ))
    ram = forms.ModelChoiceField(
        required=False,
        queryset=LaptopRam.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopRam, ))
    storage = forms.ModelChoiceField(
        required=False,
        queryset=LaptopStorage.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopStorage, ))
    brand = forms.ModelChoiceField(
        required=False,
        queryset=LaptopBrand.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopBrand, ))
    screen = forms.ModelChoiceField(
        required=False,
        queryset=LaptopScreen.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopScreen, ))
    CPU = forms.ModelChoiceField(
        required=False,
        queryset=LaptopCPU.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopCPU, ))
    OS = forms.ModelChoiceField(
        required=False,
        queryset=LaptopOS.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopOS, ))
    VGA = forms.ModelChoiceField(
        required=False,
        queryset=LaptopVGA.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopVGA, ))
    USB = forms.ModelChoiceField(
        required=False,
        queryset=LaptopUSB.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopUSB, ))
    Special = forms.ModelChoiceField(
        required=False,
        queryset=LaptopSpecial.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopSpecial, ))
    design = forms.ModelChoiceField(
        required=False,
        queryset=LaptopDesign.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopDesign, ))
    size = forms.ModelChoiceField(
        required=False,
        queryset=LaptopSize.objects.all(),
        widget=RelatedFieldWidgetCanAdd(LaptopSize, ))
    class Meta:
        model = Laptop
        exclude = ['id','product_id']
        fields="__all__"
       


class add_Watch(forms.ModelForm):
    DuongKinh = forms.ModelChoiceField(
        required=False,
        queryset=watchDiameter.objects.all(),
        widget=RelatedFieldWidgetCanAdd(watchDiameter, ))
    ChatLieu = forms.ModelChoiceField(
        required=False,
        queryset=watchChatLieu.objects.all(),
        widget=RelatedFieldWidgetCanAdd(watchChatLieu, ))
    Day = forms.ModelChoiceField(
        required=False,
        queryset=watchDay.objects.all(),
        widget=RelatedFieldWidgetCanAdd(watchDay, ))
    BoMay = forms.ModelChoiceField(
        required=False,
        queryset=watchBoMay.objects.all(),
        widget=RelatedFieldWidgetCanAdd(watchBoMay, ))
    ChongNuoc = forms.ModelChoiceField(
        required=False,
        queryset=watchChongNuoc.objects.all(),
        widget=RelatedFieldWidgetCanAdd(watchChongNuoc, ))
    QuocGia = forms.ModelChoiceField(
        required=False,
        queryset=watchQuocGia.objects.all(),
        widget=RelatedFieldWidgetCanAdd(watchQuocGia, ))
    Brand = forms.ModelChoiceField(
        required=False,
        queryset=watchBrand.objects.all(),
        widget=RelatedFieldWidgetCanAdd(watchBrand, ))
    
    
    class Meta:
        model = watch
        exclude = ['id','product_id']
        fields="__all__"
       


class add_Tablet(forms.ModelForm):
    coloroption = forms.ModelChoiceField(required=False,queryset=TabletColor.objects.all(),widget=RelatedFieldWidgetCanAdd(TabletColor, ))
    coloroption1 = forms.ModelChoiceField(required=False,queryset=TabletColor.objects.all(),widget=RelatedFieldWidgetCanAdd(TabletColor, ))
    coloroption2 = forms.ModelChoiceField(required=False,queryset=TabletColor.objects.all(),widget=RelatedFieldWidgetCanAdd(TabletColor, ))
    ram_storage_option = forms.ModelChoiceField(required=False,queryset=TabletOptionHard.objects.all(),widget=RelatedFieldWidgetCanAdd(TabletOptionHard, ))
    ram_storage_option1 = forms.ModelChoiceField(required=False,queryset=TabletOptionHard.objects.all(),widget=RelatedFieldWidgetCanAdd(TabletOptionHard, ))
    ram_storage_option2 = forms.ModelChoiceField(required=False,queryset=TabletOptionHard.objects.all(),widget=RelatedFieldWidgetCanAdd(TabletOptionHard, ))
   
    
    color = forms.ModelChoiceField(
       required=False,
       queryset=TabletColor.objects.all(),
       widget=RelatedFieldWidgetCanAdd(TabletColor, ))
    ram = forms.ModelChoiceField(
        required=False,
        queryset=TabletRam.objects.all(),
        widget=RelatedFieldWidgetCanAdd(TabletRam, ))
    storage = forms.ModelChoiceField(
        required=False,
        queryset=TabletStorage.objects.all(),
        widget=RelatedFieldWidgetCanAdd(TabletStorage, ))
    brand = forms.ModelChoiceField(
        required=False,
        queryset=TabletBrand.objects.all(),
        widget=RelatedFieldWidgetCanAdd(TabletBrand, ))
    Connect = forms.ModelChoiceField(
        required=False,
        queryset=TabletConnect.objects.all(),
        widget=RelatedFieldWidgetCanAdd(TabletConnect, ))
    screen = forms.ModelChoiceField(
        required=False,
        queryset=TabletScreen.objects.all(),
        widget=RelatedFieldWidgetCanAdd(TabletScreen, ))
    OS = forms.ModelChoiceField(
        required=False,
        queryset=TabletOS.objects.all(),
        widget=RelatedFieldWidgetCanAdd(TabletOS, ))
    BackCamera = forms.ModelChoiceField(
        required=False,
        queryset=TabletBackCamera.objects.all(),
        widget=RelatedFieldWidgetCanAdd(TabletBackCamera, ))
    FrontCamera = forms.ModelChoiceField(
        required=False,
        queryset=TabletFrontCamera.objects.all(),
        widget=RelatedFieldWidgetCanAdd(TabletFrontCamera, ))
    chips = forms.ModelChoiceField(
        required=False,
        queryset=TabletChip.objects.all(),
        widget=RelatedFieldWidgetCanAdd(TabletChip, ))
    battery = forms.ModelChoiceField(
        required=False,
        queryset=TabletBattery.objects.all(),
        widget=RelatedFieldWidgetCanAdd(TabletBattery, ))
    class Meta:
        model = Tablet
        exclude = ['id','product_id']
        fields="__all__"

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name','phone','address','profile_image']
        exclude = ['user']
        widgets = {
            'profile_image': FileInput(),
        }    
class StaffUpdateForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['typeStaff','shift']
        exclude = ['id_profile']