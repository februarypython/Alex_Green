from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^user/registration$', views.validate),
    url('^user/login$', views.login),
]
