from django.urls import path
from .views import *

urlpatterns = [
    path('', DonorDashboard.as_view(), name='donor_dashboard'),
    path('edit/', DonorProfileEdit.as_view(), name='donor_profile_edit'),
    path('give_me_your_contact/<pk>/', give_me_your_contact, name='give_me_your_contact'),
]
