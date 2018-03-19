from django.conf.urls import url
from . import views

urlpatterns = [
    url('^users$', views.index),
    url('^users/new$', views.new_user),
    url('^users/create$', views.create),
    url('^users/(?P<id>\d+)$', views.show),
    url('^users/(?P<id>\d+)/edit$', views.edit),
    url('^users/(?P<id>\d+)/destroy$', views.destroy)
]