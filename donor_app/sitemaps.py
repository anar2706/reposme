from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from django.conf import settings
from .models import Donor

class DonorSitemap(Sitemap):
    changefreq = 'daily'

    def items(self):
        return 'homepage', 'search', 'donated_already', 'contact_f', 'account_signup', 'members'

    def location(self, item):
        return reverse(item)


class SearchInnerPageSitemap(Sitemap):
    changefreq = 'hourly'

    def items(self):
        cnt = Donor.objects.count()
        cnt = cnt // settings.DONORS_PER_PAGE
        pages = []
        for i in range(1, cnt+1):
            pages.append(str(i))
        
        return pages


    def location(self, item):
        return reverse('search_inner_page', args=(item,))

