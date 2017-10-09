"""Url Super.

Attributes:
    urlpatterns (TYPE): Description
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',
        views.HomeView.as_view(), name="home"),
    url(r'^folder/',
        include('app.super.folder.urls')),
    url(r'^file/',
        include('app.super.file.urls')),
    url(r'^role/',
        include('app.super.role.urls')),
    url(r'^link/',
        include('app.super.link.urls')),
    url(r'^setting/',
        include('app.super.settings.urls')),
    url(r'^users/',
        include('app.super.accounts.urls')),
    url(r'^(?P<carpeta>[^/]+)/view/$',
        views.CarpetaArchivoListView.as_view(), name="folder-view"),
    url(r'^(?P<carpeta>[^/]+)/search/$',
        views.CarpetaSearchListView.as_view(), name="folder-search"),
    url(r'^search/$',
        views.SearchView.as_view(), name='search'),
    url(r'^(?P<id>[^/]+)/view-file/$',
        views.ViewFileView.as_view(), name="file-view"),
]
