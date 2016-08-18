# -*- coding:utf-8 -*-
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from common.iwater.getSms import get_sms_num
from common.iwater.getSms import get_sms_num_dev
from common.iwater.getSms import get_sms_num_transfer
import simplejson
import logging

logger = logging.getLogger("iwaterMock.app")


def get_sms_page(request):
    return render_to_response("getSms.html", context_instance=RequestContext(request))

@csrf_exempt
def get_sms(request):
    phone_num = request.GET.get("phoneNumber")
    logger.info(phone_num)
    logger.info(type(phone_num))
    sms = get_sms_num(phone_num)
    logger.info(sms)
    return HttpResponse(sms)

@csrf_exempt
def get_sms_dev(request):
    phone_num = request.GET.get("phoneNumber")
    logger.info(phone_num)
    logger.info(type(phone_num))
    sms = get_sms_num_dev(phone_num)
    logger.info(sms)
    return HttpResponse(sms)

@csrf_exempt
def get_sms_transfer(request):
    phone_num = request.GET.get("phoneNumber")
    logger.info(phone_num)
    logger.info(type(phone_num))
    sms = get_sms_num_transfer(phone_num)
    logger.info(sms)
    return HttpResponse(sms)

