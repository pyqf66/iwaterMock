# -*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required

from common.util.Cnumber import Cnumber
from django.http.response import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
import simplejson
import logging

logger = logging.getLogger("iwaterMock.app")

@login_required(login_url="/")
@csrf_exempt
def cnumber_page(request):
    return render_to_response("cnumber.html", context=RequestContext(request))


@login_required(login_url="/")
@csrf_exempt
def tool_cnumber(request):
    try:
        arabic_num = request.POST.get("arabicNum")
        logger.info("阿拉伯数字为：" + arabic_num)
        cnumber_object = Cnumber()
        chs_upper_num = cnumber_object.cwchange(arabic_num)
        logger.info("中文大写数字为：" + chs_upper_num)
        result = {"chsUpperNum": chs_upper_num}
        logger.info("result数据格式：" + str(type(result)))
        logger.info("result数据为：" + str(result))
        return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json")
    except:
        logger.exception("阿拉伯数字转中文大写数字错误：")
