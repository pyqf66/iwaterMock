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
from iwaterMock import settings

urlpatterns = [
    url(r'^testInstall$', "totest.views.index_text"),
    url(r'^$', "totest.views.index"),
    url(r'^mockPlatform/menu.json', "totest.views.menu"),
    url(r'^mockPlatform/apiMock/settingsPage', "totest.views.api_mock_settings_page"),
    url(r'^mockPlatform/apiMock/settingsData', "totest.views.api_data_json_response"),
    url(r'^mockPlatform/apiMock/apiSet', "totest.views.api_mock_setting"),
    url(r'^mockPlatform/tool/cnumberPage', "totest.views.cnumber_page"),
    url(r'^mockPlatform/tool/cnumber', "totest.views.tool_cnumber"),
    url(r'^mockPlatform/tool/drinkCalcPage', "totest.views.drink_calc_page"),
    url(r'^mockPlatform/tool/getWaterSettings', "totest.views.get_water_setting"),
    url(r'^mockPlatform/tool/drinkCalc', "totest.views.drink_calc"),
    url(r'^mockPlatform/tool/getSmsPage$', "totest.views.get_sms_page"),
    url(r'^mockPlatform/tool/getSms$', "totest.views.get_sms"),
    url(r'^mockPlatform/tool/getSmsDev$', "totest.views.get_sms_dev"),
    url(r'^mockPlatform/tool/getSmsTransfer$', "totest.views.get_sms_transfer"),
    url(r'^mockPlatform/kernal/iwaterAPIPage$', "totest.views.iwater_api_page"),
    url(r'^mockPlatform/kernal/iwaterAPIJson$', "totest.views.iwater_api_json"),
    url(r'^mockPlatform/kernal/saveIwaterAPI$', "totest.views.save_iwater_api"),
    url(r'^mockPlatform/kernal/queryIwaterApi$', "totest.views.query_iwater_api"),
    url(r'^iwaterMock/(.+)', "totest.views.iwater_mock"),
    url(r'^statics/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS}),
]
