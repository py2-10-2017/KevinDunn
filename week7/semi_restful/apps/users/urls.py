from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.index),
    url(r'^users/new/$', views.new),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<id>\d+)$', views.show),
    url(r'^users/(?P<id>\d+)/edit/$', views.edit),
    url(r'^users/(?P<id>\d+)/update$', views.update),
    url(r'^users/(?P<id>\d+)/delete/$', views.destroy)
]