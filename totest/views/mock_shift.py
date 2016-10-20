# -*- coding:utf-8 -*-
from urllib import parse
import requests
from django.contrib.auth.decorators import login_required
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
from totest.models import mock_shift

logger = logging.getLogger("iwaterMock.app")

@login_required(login_url="/")
@csrf_exempt
def mock_page(request):
    return render_to_response("mockShift.html", context=RequestContext(request))


@login_required(login_url="/")
@csrf_exempt
def mock_shift_json(request):
    api_list = [{
        "isOpen": '1',
        "status": "开"
    }, {
        "isOpen": '0',
        "status": "关"
    }]
    return HttpResponse(simplejson.dumps(api_list, ensure_ascii=False))


@login_required(login_url="/")
@csrf_exempt
def save_mock_shift(request):
    received_json_data = request.POST.get("settings")
    data_list = simplejson.loads(received_json_data)
    logger.info(data_list)
    # 更新数据
    mock_shift.objects.filter(id=1).update(is_open=data_list["isOpen"])
    return HttpResponse(1)


@login_required(login_url="/")
@csrf_exempt
def query_mock_shift(request):
    mock_shift_data = mock_shift.objects.all()
    mock_shift_dict = dict()
    indexNum = 0
    # 数据库读取数据并插入字典
    for i in mock_shift_data:
        mock_shift_dict["id"] = i.id
        mock_shift_dict["is_open"] = i.is_open
        indexNum = indexNum + 1
    logger.debug(mock_shift_dict)
    return HttpResponse(simplejson.dumps(mock_shift_dict, ensure_ascii=False), content_type="application/json")
