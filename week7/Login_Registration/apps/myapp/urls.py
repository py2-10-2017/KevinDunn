from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^myapp/success$', views.success),
    url(r'^myapp/create$', views.create),
    url(r'^myapp/login$', views.login),
]