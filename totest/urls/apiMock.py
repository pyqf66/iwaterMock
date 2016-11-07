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
    url(r'^settingsPage', views.api_mock_settings_page),
    url(r'^settingsData', views.api_data_json_response),
    url(r'^apiSet', views.api_mock_setting),
    url(r'^mockAnyApiManual$', views.mock_api_manual),
    url(r'^mockAnyApiManualPage$', views.mock_any_api_manual_page),
    url(r'^saveMockAnyApiManual$', views.save_mock_any_api_manual),
    url(r'^queryMockAnyApiManual$', views.query_mock_any_api_manual),
]
