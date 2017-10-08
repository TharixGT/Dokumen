"""Url Super.

Attributes:
    urlpatterns (TYPE): Description
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^carpetas/', include('app.super.carpetas.urls')),
    url(r'^archivos/', include('app.super.archivo.urls')),


]
