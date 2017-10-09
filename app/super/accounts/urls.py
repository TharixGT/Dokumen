"""."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',
        views.UserListView.as_view(), name='user-list'),
    url(r'^new/$',
        views.UserNewView.as_view(), name='user-new'),
    url(r'^(?P<id>[\w\- ]+)/edit/$',
        views.UserUpdateView.as_view(), name='user-edit'),
    url(r'^(?P<id>[^/]+)/delete/$',
        views.UserDeleteView.as_view(), name="user-delete"),
    url(r'^search/$',
        views.SearchView.as_view(), name="user-search"),
    url(r'^(?P<id>[\w\- ]+)/change-password/$',
        views.ChangePasswordView.as_view(), name='change-password'),
]
