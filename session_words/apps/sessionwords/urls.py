from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^submit$', views.submit),
    url('^clear$', views.clear)
]