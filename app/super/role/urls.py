"""."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.RoleListView.as_view(), name='role-list'),
    url(r'^new/$',
        views.RoleNewView.as_view(), name='role-new'),
    url(r'^(?P<id>[\w\- ]+)/edit/$',
        views.RoleUpdateView.as_view(), name='role-edit'),
    url(r'^(?P<id>[^/]+)/delete/$',
        views.RoleDeleteView.as_view(), name="role-delete"),
]
