from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from Electronics.models import Laptop, Mobile
class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home']
    def location(self, item):
        return reverse(item)

class LaptopSiteMap(Sitemap):
    def items(self):
        return Laptop.objects.all()
    def location(self, item):
        return reverse('detail', args=['laptop', item.slug])

class MobileSiteMap(Sitemap):
    def items(self):
        return Mobile.objects.all()
    def location(self, item):
        return reverse('detail', args=['mobile', item.slug])