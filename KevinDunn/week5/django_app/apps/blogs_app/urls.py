from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^$', views.index),
  url(r'^new/$', views.new),
  url(r'^(?P<blog_id>[0-9]+)/$', views.show),
  url(r'^(?P<blog_id>[0-9]+)/edit/$', views.edit),
  url(r'^(?P<blog_id>[0-9]+)/delete/$', views.destroy)
]
