from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.profileOther, name='profileOther'),
    url(r'^create/$', views.createProfile, name='createProfile'),
]


# New user
# Search user maybe