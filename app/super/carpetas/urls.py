"""."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.CarpetaListView.as_view(), name='carpeta-list'),
    url(r'^new/$',
        views.CarpetaNewView.as_view(), name='carpeta-new'),
    url(r'^(?P<id>[\w\- ]+)/edit/$',
        views.CarpetaUpdateView.as_view(), name='carpeta-edit'),
    url(r'^(?P<id>[^/]+)/delete/$',
        views.CarpetaDeleteView.as_view(), name="carpeta-delete"),
]
