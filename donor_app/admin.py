from django.contrib import admin
from .models import *

class DonorModelAdmin(admin.ModelAdmin):
    list_filter = 'gender', 'blood_group', 'county', 'is_private', 'is_closed', 'is_contact_private', 'i_donated_recently'
    search_fields = 'first_name', 'last_name', 'phone', 'height'
    list_display = 'first_name', 'last_name', 'phone', 'gender', 'blood_group', 'is_private', 'is_closed', 'is_contact_private', 'i_donated_recently'

admin.site.register(Donor, DonorModelAdmin)