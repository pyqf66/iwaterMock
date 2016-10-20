# -*- coding:utf-8 -*-
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import simplejson
import logging
from totest.models import mock_any_api_manual

logger = logging.getLogger("iwaterMock.app")


@csrf_exempt
def mock_any_api_manual_page(request):
    return render_to_response("mockAnyApiManual.html", context=RequestContext(request))


@csrf_exempt
def save_mock_any_api_manual(request):
    received_json_data = request.POST.get("settings")
    data_list = simplejson.loads(received_json_data)
    logger.info(data_list)
    # 更新数据
    mock_any_api_manual.objects.filter(id=1).update(response_content=data_list["response_content"])
    return HttpResponse(1)


@csrf_exempt
def query_mock_any_api_manual(request):
    try:
        response_content_dict = dict()
        for i in mock_any_api_manual.objects.filter(id=1):
            response_content_dict["response_content"] = i.response_content
        return HttpResponse(simplejson.dumps(response_content_dict, ensure_ascii=False),
                            content_type="application/json")
    except:
        logger.exception("查询api失败：")


@csrf_exempt
def mock_api_manual(request):
    for i in mock_any_api_manual.objects.filter(id=1):
        resp = i.response_content
    try:
        return HttpResponse(resp, content_type="application/json;charset=utf-8")
    except:
        return HttpResponse(resp)
