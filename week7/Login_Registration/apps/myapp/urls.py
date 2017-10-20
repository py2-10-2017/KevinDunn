from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^myapp$', views.index),
    
    url(r'^success$', views.success),
    # url(r'^users/success/(?P<id>\d+)/$', views.success),
    url(r'^myapp/register$', views.register),
    url(r'^myapp/login$', views.login),
]