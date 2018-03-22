from django.conf.urls import url
from . import views

urlpatterns = [
    url('^success$', views.success),
    url('^(?P<id>\d+)$', views.view_book),
    url('^add$', views.add_book_review),
    url('^process_new_review', views.process_new_review),
    url('^(?P<id>\d+)/delete$', views.delete_review),
    url('^(?P<id>\d+)/add_review_only$', views.add_review_only),
    url('^users/(?P<id>\d+)$', views.user_info)

]