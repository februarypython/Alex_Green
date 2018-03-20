from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^add_course$', views.add_course),
    url('^destroy/(?P<id>\d+)$', views.destroy),
    url('^erase/(?P<id>\d+)$', views.erase)
]