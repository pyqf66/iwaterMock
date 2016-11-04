# -*- coding:utf-8 -*-
from urllib import parse
from django.contrib.auth.decorators import login_required
from totest.models import iwater_api
import requests
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from totest.models import api_mock
from django.core.paginator import Paginator
from common.iwater.IwaterApi import IwaterApi
import simplejson
import logging
from totest.models import mock_shift
from common.iwater.get_mock_shift import get_mock_shift
from common.util.TimeCalc import TimeCalc
import subprocess
from common.iwater.api_config import *

logger = logging.getLogger("iwaterMock.app")


def execcommand(command_list):
    # ['sh',scriptname,host.hostname,project.servicename]
    output = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data_stdout = list(output.stdout)
    data_stderr = list(output.stderr)
    data_return_code = output.returncode
    return [data_stdout, data_stderr, data_return_code]


@login_required(login_url="/")
@csrf_exempt
def ajax_get_log(request):
    return render_to_response("logs.html", context=RequestContext(request))


@login_required(login_url="/")
@csrf_exempt
# def ajax_get_log(request, pid, hid):
def ajax_get_log_line(request):
    line = 1
    # project = Project.objects.get(pk=pid)
    # host = Host.objects.get(pk=hid)
    # scriptname = '/root/get_log.sh'
    # scriptname = '%s%s'%(base_path,'get_log.sh')
    # res = execcommand(['sh',scriptname,host.hostname,project.servicename])
    res = execcommand(['sh', scriptname])
    # 如果错误输出不为空，直接返回错误输出
    if not res[1]:
        try:
            # res[0]为行号，如果大于20行，从当前行的上面20行开始输出，为了用户体验，你懂得
            if int(res[0][0].decode("utf-8")) > 20:
                line = int(res[0][0].decode("utf-8")) - 20
            if int(res[0][0].decode("utf-8")) == 0:
                line = 1
            line_dict = {'line': line}
            return HttpResponse(simplejson.dumps(line_dict, ensure_ascii=False), content_type="application/json")
        except Exception as e:
            logger.exception("获取日志内容时出错:")
            return HttpResponse(e)
    else:
        return HttpResponse(res[1])


@login_required(login_url="/")
@csrf_exempt
def ajax_get_log_handle(request):
    line = request.GET.get("line")
    # project = Project.objects.get(pk=pid)
    # host = Host.objects.get(pk=hid)
    # scriptname = '%s%s'%(base_path,'get_log.sh')
    # scriptname = '/root/get_log.sh'
    res = execcommand(['sh', scriptname, line])
    if not res[1] and res[0]:
        return HttpResponse(res[0])
    else:
        return HttpResponse(500)
