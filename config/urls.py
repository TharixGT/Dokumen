"""ManejadorDocumentos URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from app.accounts import views

urlpatterns = [
    url(r'accounts/login/$', views.custom_login),
    url(r'accounts/logout/$', views.custom_logout),
    url(r'accounts/password/change/$', views.custom_password_change),
    url(r'accounts/inactive', views.custom_inactive),

    # reset password
    url(r'^accounts/password/reset/$', views.custom_password_reset),
    url(r'^accounts/password/reset/done/$', views.custom_password_reset_done),
    url(r'^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$',
        views.custom_password_reset_from_key),
    url(r'^accounts/password/reset/key/done/$',
        views.custom_password_reset_from_key_done),

    # email
    url(r'^accounts/email/$', views.custom_email),
    url(r'^accounts/confirm-email/$', views.custom_email_verification_sent),
    url(r'^accounts/confirm-email/(?P<key>\w+)/$', views.custom_confirm_email),

    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('app.super.urls', namespace='super')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
