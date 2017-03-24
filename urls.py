from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^searchResults/$', views.searchResults, name='searchResults'),
    url(r'^(?P<venue_id>[0-9]+)/$', views.detail, name='detail'),
]
