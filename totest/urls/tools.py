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
    url(r'^cnumberPage', views.cnumber_page),
    url(r'^cnumber', views.tool_cnumber),
    url(r'^drinkCalcPage', views.drink_calc_page),
    url(r'^getWaterSettings', views.get_water_setting),
    url(r'^drinkCalc', views.drink_calc),
    url(r'^getSmsPage$', views.get_sms_page),
    url(r'^getSms$', views.get_sms),
    url(r'^getSmsDev$', views.get_sms_dev),
    url(r'^getSmsTransfer$', views.get_sms_transfer),
    url(r'^logs$', views.ajax_get_log),
    url(r'^logsLine$', views.ajax_get_log_line),
    url(r'^logsHandle$', views.ajax_get_log_handle, name="ajax_handle_log"),
    url(r'^getTimeStampPage$', views.get_time_stamp_page),
    url(r'^getTimeStampCurrentTime$', views.get_time_stamp_current_time),
    url(r'^getTimeStampByDate$', views.get_time_stamp_by_date),
]
