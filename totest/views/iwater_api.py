# -*- coding:utf-8 -*-
from urllib import parse

from django.contrib.auth.decorators import login_required

import requests
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from totest.models import api_mock
from django.core.paginator import Paginator
from common.iwater.IwaterApi import IwaterApi
import simplejson
import logging
from common.iwater.api_config import *
from totest.models import iwater_api

logger = logging.getLogger("iwaterMock.app")


@login_required(login_url="/")
@csrf_exempt
def iwater_api_page(request):
    return render_to_response("iwaterApi.html", context=RequestContext(request))


@login_required(login_url="/")
@csrf_exempt
def iwater_api_json(request):
    api_list = [{
        "url": url_test_ip,
        "environment": "test_ip"
    }, {
        "url": url_test_domain,
        "environment": "test_domain"
    },{
        "url": url_dev,
        "environment": "dev"
    }, {
        "url": url_prod,
        "environment": "prod"
    }]
    return HttpResponse(simplejson.dumps(api_list, ensure_ascii=False))


@login_required(login_url="/")
@csrf_exempt
def save_iwater_api(request):
    received_json_data = request.POST.get("settings")
    data_list = simplejson.loads(received_json_data)
    logger.info(data_list)
    # 更新数据
    iwater_api.objects.filter(id=1).update(url=data_list["url"], environment=data_list["environment"])
    return HttpResponse(1)


@login_required(login_url="/")
@csrf_exempt
def query_iwater_api(request):
    iwater_api_json_data = iwater_api.objects.all()
    iwater_api_json_dict = dict()
    indexNum = 0
    # 数据库读取数据并插入字典
    for i in iwater_api_json_data:
        iwater_api_json_dict["id"] = i.id
        iwater_api_json_dict["url"] = i.url
        iwater_api_json_dict["environment"] = i.environment
        indexNum = indexNum + 1
    logger.debug(iwater_api_json_dict)
    return HttpResponse(simplejson.dumps(iwater_api_json_dict, ensure_ascii=False), content_type="application/json")
