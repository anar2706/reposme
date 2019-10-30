"""blood_bank_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from auth_app.views import *
from donor_app.views import members
from donor_app.sitemaps import DonorSitemap, SearchInnerPageSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'donors': DonorSitemap,
    'search_inner_pages': SearchInnerPageSitemap
}

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('dashboard/', include('donor_app.urls')),
    path('contact/',include('contact.urls')),
    url(r'^accounts/signup/', DonorSignupView.as_view(), name='account_signup'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^messages/', include('messages_extends.urls')),
    path('questions/',include('faq.urls')),
    path('members/',members,name='members'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps})
    
]
