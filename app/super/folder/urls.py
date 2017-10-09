"""."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.FolderListView.as_view(), name='folder-list'),
    url(r'^new/$',
        views.FolderNewView.as_view(), name='folder-new'),
    url(r'^(?P<id>[\w\- ]+)/edit/$',
        views.FolderUpdateView.as_view(), name='folder-edit'),
    url(r'^(?P<id>[^/]+)/delete/$',
        views.FolderDeleteView.as_view(), name="folder-delete"),
    url(r'^(?P<id>[\w\- ]+)/edit-file/$',
        views.FolderFileUpdateView.as_view(), name='folder-edit-file'),
]
