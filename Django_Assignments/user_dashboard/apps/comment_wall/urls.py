from django.conf.urls import url
from . import views

urlpatterns = [
    url('^users/(?P<id>\d+)$', views.index),
    url('^process_message/(?P<id>\d+)$', views.process_message),
    url('^(?P<id>\d+)/process_comment/(?P<messageid>\d+)$', views.process_comment)
]