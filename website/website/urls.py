
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps.views import sitemap
# Comes from Sitemap.py
from sweden.sitemaps import StaticViewSitemap, ArticleSitemap

sitemaps = {
    'static':StaticViewSitemap,
    'article':ArticleSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('sweden.urls')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
    path('api/', include('djangoApi.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
