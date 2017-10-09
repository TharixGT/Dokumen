"""."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.LinkListView.as_view(), name='link-list'),
    url(r'^new/$',
        views.LinkNewView.as_view(), name='link-new'),
    url(r'^(?P<id>[\w\- ]+)/edit/$',
        views.LinkUpdateView.as_view(), name='link-edit'),
    url(r'^(?P<id>[^/]+)/delete/$',
        views.LinkDeleteView.as_view(), name="link-delete"),
]
