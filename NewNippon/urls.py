from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from Electronics.sitemaps import StaticViewSitemap, LaptopSiteMap, MobileSiteMap
from django.urls import path, include
sitemaps = {
    'static': StaticViewSitemap,
    'laptop': LaptopSiteMap,
    'mobile': MobileSiteMap
}
urlpatterns = [
    path("admin/", admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("", include("Electronics.urls")),
    ]
