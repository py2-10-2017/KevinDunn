from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses_app$', views.index),
    url(r'^courses_app/create$', views.create),
    url(r'courses_app/doublecheck$', views.doublecheck, name="double_check")
]