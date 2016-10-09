# -*- coding:utf-8 -*-
import requests
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from totest.models import api_mock
from django.core.paginator import Paginator
import simplejson
import logging

logger = logging.getLogger("iwaterMock.app")


def index_text(request):
    return render_to_response("tmp.html", context=RequestContext(request))


def index(request):
    return render_to_response("index.html", context=RequestContext(request))

@csrf_exempt
def menu(request):
    menu_list = [{
        "id": 1,
        "text": "api工具",
        "children": [{
            "text": "api_mock_settings",
            "attributes": {
                "url": "/mockPlatform/apiMock/settingsPage"
            }
        }, {
            "text": "iwater_kernal_api",
            "attributes": {
                "url": "/mockPlatform/kernal/iwaterAPIPage"
            }
        }, {
            "text": "mock_shift",
            "attributes": {
                "url": "/mockPlatform/kernal/mockPage"
            }
        }, {
            "text": "mock_any_api_manual",
            "attributes": {
                "url": "/mockPlatform/apiMock/mockAnyApiManualPage"
            }
        }]
    }, {
        "id": 2,
        "text": "其他工具",
        "children": [{
            "text": "阿拉伯数字转中文大写数字",
            "attributes": {
                "url": "/mockPlatform/tool/cnumberPage"
            }}, {
            "text": "饮水量计算",
            "attributes": {
                "url": "/mockPlatform/tool/drinkCalcPage"
            }}, {
            "text": "短信验证码获取",
            "attributes": {
                "url": "/mockPlatform/tool/getSmsPage"
            }}
        ]
    }]
    return HttpResponse(simplejson.dumps(menu_list, ensure_ascii=False))
