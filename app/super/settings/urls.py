"""."""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<id>[\w\- ]+)/edit/$',
        views.SettingsUpdateView.as_view(), name='settings-edit'),
]
