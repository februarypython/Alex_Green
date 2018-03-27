from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('process_post', views.process_post)
]