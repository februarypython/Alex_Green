from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^process_note$', views.process_note),
    url('^(?P<id>\d+)/delete_note$', views.delete_note)
]