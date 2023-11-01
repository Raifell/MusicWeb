from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    re_path(r'^bands/(?P<genre>\D+)/(?P<slug>\D+)/$', views.band_info_page, name='info_page'),
    re_path(r'^bands/(?P<genre>\D+)/$', views.bands_page, name='bands_page'),
    re_path(r'^$', views.main_page, name='main_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
