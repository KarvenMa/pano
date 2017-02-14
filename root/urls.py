from django.conf.urls import include, url

from django.contrib import admin
from panorama import views as panorama_views

admin.autodiscover()

urlpatterns = [
    url(r'^$', panorama_views.index, name='index'),
    url(r'^panorama/', include('panorama.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
