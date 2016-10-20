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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.login),
    url(r'^mockPlatform/loginCheck', views.login_check),
    url(r'^mockPlatform/index', views.index),
    url(r'^mockPlatform/menu.json', views.menu),
    url(r'^mockPlatform/menu.json', views.menu),
    url(r'^mockPlatform/apiMock/settingsPage', views.api_mock_settings_page),
    url(r'^mockPlatform/apiMock/settingsData', views.api_data_json_response),
    url(r'^mockPlatform/apiMock/apiSet', views.api_mock_setting),
    url(r'^mockPlatform/apiMock/mockAnyApiManual$', views.mock_api_manual),
    url(r'^mockPlatform/apiMock/mockAnyApiManualPage$', views.mock_any_api_manual_page),
    url(r'^mockPlatform/apiMock/saveMockAnyApiManual$', views.save_mock_any_api_manual),
    url(r'^mockPlatform/apiMock/queryMockAnyApiManual$', views.query_mock_any_api_manual),
    url(r'^mockPlatform/tool/cnumberPage', views.cnumber_page),
    url(r'^mockPlatform/tool/cnumber', views.tool_cnumber),
    url(r'^mockPlatform/tool/drinkCalcPage', views.drink_calc_page),
    url(r'^mockPlatform/tool/getWaterSettings', views.get_water_setting),
    url(r'^mockPlatform/tool/drinkCalc', views.drink_calc),
    url(r'^mockPlatform/tool/getSmsPage$', views.get_sms_page),
    url(r'^mockPlatform/tool/getSms$', views.get_sms),
    url(r'^mockPlatform/tool/getSmsDev$', views.get_sms_dev),
    url(r'^mockPlatform/tool/getSmsTransfer$', views.get_sms_transfer),
    url(r'^mockPlatform/kernal/iwaterAPIPage$', views.iwater_api_page),
    url(r'^mockPlatform/kernal/iwaterAPIJson$', views.iwater_api_json),
    url(r'^mockPlatform/kernal/saveIwaterAPI$', views.save_iwater_api),
    url(r'^mockPlatform/kernal/queryIwaterApi$', views.query_iwater_api),
    url(r'^mockPlatform/kernal/mockPage$', views.mock_page),
    url(r'^mockPlatform/kernal/mockShiftJson$', views.mock_shift_json),
    url(r'^mockPlatform/kernal/saveMockShift$', views.save_mock_shift),
    url(r'^mockPlatform/kernal/queryMockShift$', views.query_mock_shift),
    url(r'^iwaterMock/(.+)', views.iwater_mock),
    url(r'^statics/(?P<path>.*)$', django.views.static.serve, {'document_root': settings.STATICFILES_DIRS[0]}),
]
