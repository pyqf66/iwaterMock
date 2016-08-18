# -*- coding:utf-8 -*-
from urllib import parse
from totest.models import iwater_api
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

logger = logging.getLogger("iwaterMock.app")


@csrf_exempt
def iwater_mock(request, rest_api):
    url = None
    result = None
    request_data = None
    # 设置请求的url
    # test为测试环境
    # dev为开发环境
    # prod为生产环境
    url_data = iwater_api.objects.all()
    for i in url_data:
        url = i.url
    logger.debug("真实服务器url=" + str(url))
    full_path = request.get_full_path()
    logger.debug(type(full_path))
    logger.debug("完整请求路径full_path=" + str(parse.unquote(full_path)))
    # 不包含问号的为body风格请求，否则认为是get请求或get风格的post请求
    if "?" not in full_path:
        logger.debug("body风格数据!")
        request_data = request.body
        rest_abs_api = url + '/' + rest_api
    else:
        logger.debug("get风格数据!")
        rest_abs_api = url + full_path[11:]
    logger.debug("请求的编码为：" + str(request.encoding))
    logger.debug("rest风格链接=" + str(rest_api))
    # 判断请求头并插入正确的请求头
    content_type = request.META["CONTENT_TYPE"]
    if "application/x-www-form-urlencoded" in content_type and request_data:
        headers = {"Content-Type": content_type}
    elif "multipart/form-data;" in content_type and request_data:
        headers = {"Content-Type": content_type}
        request_data={"file":request_data}
    else:
        headers = {}
    # 将获取IwaterApi对象，需要mock返回方法对象，不需要mock返回0
    mock_object = IwaterApi()
    api_mock = mock_object.mock_dict(rest_api)
    logger.info("是否需要mock的返回值：" + str(api_mock))
    logger.info("请求方法为:" + str(request.method))
    try:
        if request.method == "POST":
            logger.debug("进入POST方法!")
            # 需要mock则mock，不需要mock则直接跳过
            if api_mock != 0:
                return HttpResponse(simplejson.dumps(api_mock(), ensure_ascii=False))
            logger.debug("真实请求路径rest_abs_api=" + str(parse.unquote(rest_abs_api)))
            if request_data:
                try:
                    logger.debug("请求的数据为：" + str(parse.unquote(request_data)))
                except:
                    logger.debug("请求的数据为：" + str(request_data))
            logger.debug("请求的请求头为：" + str(content_type))
            logger.debug("请求数据request_data数据类型为"+str(type(request_data)))
            if "multipart/form-data;" in content_type:
                http_object = requests.post(url=rest_abs_api, files=request_data, headers=headers)
            else:
                http_object = requests.post(url=rest_abs_api, data=request_data, headers=headers)
            try:
                result = simplejson.dumps(http_object.json(), ensure_ascii=False)
            except:
                result = http_object.content.decode("utf-8")
                logger.debug("最终响应结果：" + str(result))
                return render_to_response(result, context_instance=RequestContext(request))
            logger.debug("最终响应结果：" + str(result))
    except:
        logger.exception("POST请求错误如下：")

    try:
        if request.method == "GET":
            logger.debug("进入GET方法!")
            # 需要mock则mock，不需要mock则直接跳过
            if api_mock != 0:
                return HttpResponse(simplejson.dumps(api_mock(), ensure_ascii=False))
            rest_abs_api = url + full_path[11:]
            logger.debug("真实请求路径rest_abs_api=" + str(parse.unquote(rest_abs_api)))
            http_object = requests.get(url=rest_abs_api)
            try:
                result = simplejson.dumps(http_object.json(), ensure_ascii=False)
                # result = simplejson.dumps(http_object.json())
                logger.debug("最终响应结果：" + str(result))
            except:
                result = http_object.content
                logger.debug("最终响应结果：" + str(result))
                # return render_to_response(result, context_instance=RequestContext(request))
                return HttpResponse(result)
            logger.debug("最终响应结果：" + str(result))
    except:
        logger.exception("GET请求错误如下：")

    return HttpResponse(result)
