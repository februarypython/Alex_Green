from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^surveys$', views.surveys),
    url(r'^surveys/new$', views.surveys_new)
]