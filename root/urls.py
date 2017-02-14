from django.conf.urls import include, url

from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^init_database$', views.init_database, name='init_database'),

    url(r'^panorama/', include('panorama.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
