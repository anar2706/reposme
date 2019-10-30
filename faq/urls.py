from django.urls import path
from .views import faq_view,SearchResultsView

urlpatterns = [
    path('',faq_view,name='FAQ'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
