from django import forms
from allauth.account.forms import SignupForm
from django.utils.translation import gettext_lazy as _
from .models import *

class DonorRegisterForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = 'first_name', 'last_name', 'phone', 'gender', 'blood_group', 'height', 'county'


class DonorEditForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = 'first_name', 'last_name', 'phone', 'is_contact_private', 'gender', 'blood_group', 'height', 'county',  'is_private', 'is_closed'