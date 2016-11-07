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
from django.conf.urls import url
from totest import views

urlpatterns = [
    url(r'^iwaterAPIPage$', views.iwater_api_page),
    url(r'^iwaterAPIJson$', views.iwater_api_json),
    url(r'^saveIwaterAPI$', views.save_iwater_api),
    url(r'^queryIwaterApi$', views.query_iwater_api),
    url(r'^mockPage$', views.mock_page),
    url(r'^mockShiftJson$', views.mock_shift_json),
    url(r'^saveMockShift$', views.save_mock_shift),
    url(r'^queryMockShift$', views.query_mock_shift),
]
