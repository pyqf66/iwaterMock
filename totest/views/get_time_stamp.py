# -*- coding:utf-8 -*-
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from totest.models import api_mock
from django.core.paginator import Paginator
import simplejson
from django.contrib.auth.decorators import login_required
import logging
from django.shortcuts import render_to_response
from django.template import RequestContext
import time

logger = logging.getLogger("iwaterMock.app")


@login_required(login_url="/")
@csrf_exempt
def get_time_stamp_page(request):
    return render_to_response("getTimeStamp.html", context=RequestContext(request))


@login_required(login_url="/")
@csrf_exempt
def get_time_stamp_current_time(request):
    try:
        time_stamp = int(time.time() * 1000)
        result = {"timeStamp": str(time_stamp)}
        return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.exception(u"获取当前时间戳错误如下:")


@login_required(login_url="/")
@csrf_exempt
def get_time_stamp_by_date(request):
    try:
        status = '0'
        date_time = request.POST.get("dateTime")
        try:
            time_array = time.strptime(date_time, "%Y-%m-%d %H:%M:%S")
            time_stamp = int(time.mktime(time_array) * 1000)
        except ValueError:
            status = '1'
            time_stamp = ''
        # return int(time_stamp*1000)
        result = {'status': status, 'timeStamp': str(time_stamp)}
        return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.exception(u"获取当前时间戳错误如下:")
