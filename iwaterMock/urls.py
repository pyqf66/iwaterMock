"""iwaterMock URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
import django.views.static
from iwaterMock import settings
from totest import views
from totest.urls import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.iwater_login),
    url(r'^mockPlatform/index/', include(index)),
    url(r'^mockPlatform/apiMock/', include(apiMock)),
    url(r'^mockPlatform/tools/', include(tools)),
    url(r'^mockPlatform/kernal/', include(kernal)),
    url(r'^iwaterMock/(.+)', views.iwater_mock),
    url(r'^statics/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATICFILES_DIRS[0]}),
]
