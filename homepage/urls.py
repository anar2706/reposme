from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('search/', SearchPage.as_view(), name='search'),
    path('search/page/<int:page>/', SearchPage.as_view(), name='search_inner_page'),
    path('donated-already/', DonatedAlready.as_view(), name='donated_already')
]
