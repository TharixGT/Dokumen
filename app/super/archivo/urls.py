"""."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.ArchivoListView.as_view(), name='archivo-list'),
    url(r'^new/$',
        views.ArchivoNewView.as_view(), name='archivo-new'),
    url(r'^(?P<id>[\w\- ]+)/edit/$',
        views.ArchivoUpdateView.as_view(), name='archivo-edit'),
    url(r'^(?P<id>[^/]+)/delete/$',
        views.ArchivoDeleteView.as_view(), name="archivo-delete"),
]
