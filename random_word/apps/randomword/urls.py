from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^generate$', views.generate),
    url('^random_word/reset$', views.reset)
]