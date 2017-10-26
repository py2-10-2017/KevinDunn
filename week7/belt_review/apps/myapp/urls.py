from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^myapp$', views.index),
    url(r'^myapp/register$', views.register),
    url(r'^myapp/login$', views.login),
    url(r'^success$', views.reviews),
    url(r'^add$', views.add),
    url(r'^new$', views.create),
    url(r'^add/new$', views.create),
    url(r'^book/(?P<book_id>\d+)/create$', views.create_additional),
    url(r'^myapp/reviews$', views.reviews),
    url(r'^book/(?P<id>\d+)$', views.book),
    url(r'^user/(?P<id>\d+)$', views.user),
    url(r'^book/(?P<book_id>\d+)/delete/(?P<review_id>\d+)$', views.delete_review),
    url(r'^logout$', views.logout)
]