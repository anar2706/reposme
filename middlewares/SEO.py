from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages
from seo_app.models import SEO
from django.urls import get_resolver

class SEOMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        self.get_seo(request)
        self.set_pages_path(request)
        

        response = self.get_response(request)

        return response

    def get_seo(self, request):
        seo = SEO.objects.filter(path=request.path)

        if seo.count():
            request.seo = seo[0]


    def set_pages_path(self, request):
        for i in get_resolver().reverse_dict.values():
            try:
                SEO.objects.get_or_create(path=f"/{i[0][0][0]}")
            except:
                pass