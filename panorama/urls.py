from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^view$', views.view, name='view'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^init_scene$', views.init_scene, name='init_scene'),
    url(r'^list_spaces$', views.list_spaces, name='list_spaces'),
    url(r'^update_scene$', views.update_scene, name='update_scene'),
    url(r'^add_hot$', views.add_hot, name='add_hot'),
    url(r'^update_hot$', views.update_hot, name='update_hot'),
    url(r'^delete_hot$', views.delete_hot, name='delete_hot'),
    url(r'^update_seller$', views.update_seller, name='update_seller'),
    url(r'^init_database$', views.init_database, name='init_database'),
    url(r'^init_database2$', views.init_database2, name='init_database2'),
]