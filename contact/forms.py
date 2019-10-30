from django import forms
from .models import Contact
from snowpenguin.django.recaptcha2.fields import ReCaptchaField
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget())
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content']
