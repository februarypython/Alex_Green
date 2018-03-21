from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^user/registration$', views.validate_reg),
    url('^success$', views.success),
    url('^login$', views.login)
]