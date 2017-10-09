"""."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.FileListView.as_view(), name='file-list'),
    url(r'^new/$',
        views.FileNewView.as_view(), name='file-new'),
    url(r'^(?P<id>[\w\- ]+)/edit/$',
        views.FileUpdateView.as_view(), name='file-edit'),
    url(r'^(?P<id>[^/]+)/delete/$',
        views.FileDeleteView.as_view(), name="file-delete"),
    url(r'^search/$',
        views.FileSearchView.as_view(), name="file-search"),
]
