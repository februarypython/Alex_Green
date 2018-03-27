from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^sign_in$', views.sign_in),
    url('^register$', views.register),
    url('^process_registration$', views.process_registration)
]