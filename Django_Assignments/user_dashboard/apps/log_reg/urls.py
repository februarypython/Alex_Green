from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^sign_in$', views.sign_in),
    url('^register$', views.register),
    url('^process_registration$', views.process_registration),
    url('^process_sign_in$', views.process_sign_in),
    url('^dashboard/admin$', views.dashboard_admin),
    url('^logout$', views.logout),
    url('^dashboard$', views.dashboard),
    url('^add_user$', views.add_user),
    url('^users/(?P<id>\d+)/edit', views.edit_self),
    url('^users/(?P<id>\d+)/update', views.update_user),
    url('^users/(?P<id>\d+)/destroy$', views.delete_user),
    url('^admin/users/(?P<id>\d+)/edit$', views.admin_edit_user),
    url('^process/(?P<id>\d+)/edit$', views.process_admin_edit)
]