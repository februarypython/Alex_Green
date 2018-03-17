from django.conf.urls import urls #gives access to url function
from . import views #imports the views.py file from same directory
urlpatterns = [ #uses the url method to look for a route using the regex, which is searching for any characters. Or an empty string
    url(r'^$', views.index) #if the regex pattern matches, run the views.index method
]