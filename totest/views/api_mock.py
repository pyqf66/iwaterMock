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
from totest.models import mock_shift
from common.iwater.get_mock_shift import get_mock_shift
from common.util.TimeCalc import TimeCalc

logger = logging.getLogger("iwaterMock.app")


@csrf_exempt
def iwater_mock(request, rest_api):
    try:
        url = None
        result = None
        request_data = None
        # 总开关
        api_mock = 0
        # mock api的开关,对每个mock api单独操作
        api_is_open = 0
        api_name = IwaterApi.get_api_name(rest_api)
        # 设置请求的url
        # test为测试环境
        # dev为开发环境
        # prod为生产环境
        url_data = iwater_api.objects.all()

        for i in url_data:
            url = i.url
        logger.debug(api_name + "接口:真实服务器url=" + str(url))
        full_path = request.get_full_path()
        logger.debug(api_name + "接口:全路径的数据类型为" + str(type(full_path)))
        logger.debug(api_name + "接口:完整请求路径full_path=" + str(parse.unquote(full_path)))

        # 不包含问号的为body风格请求，否则认为是get请求或get风格的post请求
        if "?" not in full_path:
            logger.debug(api_name + "接口:body风格数据!")
            request_data = request.body
            rest_abs_api = url + '/' + rest_api
        else:
            logger.debug(api_name + "接口:get风格数据!")
            rest_abs_api = url + full_path[11:]
        logger.debug(api_name + "接口:请求的编码为：" + str(request.encoding))
        logger.debug(api_name + "接口:rest风格链接=" + str(rest_api))

        # 判断请求头并插入正确的请求头
        content_type = request.META["CONTENT_TYPE"]
        if "application/x-www-form-urlencoded" in content_type and request_data:
            headers = {"Content-Type": content_type}
        elif "multipart/form-data;" in content_type and request_data:
            headers = {"Content-Type": content_type}
            request_data = {"file": request_data}
        else:
            headers = {}

        if request_data is None:
            request_data_for_get_api_no = full_path.split("?")[-1]
            api_no = IwaterApi.get_api_no(request_data_for_get_api_no)
        else:
            api_no = IwaterApi.get_api_no(request_data)
        logger.info(api_name + "接口:api_no为" + str(api_no))

        # 将获取IwaterApi对象，需要mock返回方法对象，不需要mock返回0
        mock_object = IwaterApi()
        if get_mock_shift() == '1':
            result_list = mock_object.get_mock_value_list(api_name, api_no)
        logger.info(api_name + "接口:是否需要mock的返回值：" + str(result_list))
        logger.info(api_name + "接口:请求方法为:" + str(request.method))
    except:
        logger.exception(api_name + "接口:准备数据错误：")

    try:
        if request.method == "POST":
            logger.debug(api_name + "接口:进入POST方法!")
            # 需要mock则mock，不需要mock则直接跳过
            if request_data:
                try:
                    if type(request_data) == bytes:
                        logger.debug(api_name + "接口:请求的数据为：" + str(parse.unquote(request_data.decode('utf-8'))))
                    else:
                        logger.debug(api_name + "接口:请求的数据为：" + str(parse.unquote(request_data)))
                except:
                    logger.debug(api_name + "接口:请求的数据为：" + str(request_data))
            if result_list != 0:
                logger.debug(api_name + "接口:使用mock!")
                api_is_open = result_list[1]
                logger.debug(api_name + "接口:子开关为" + str(api_is_open))
                if api_is_open == 1:
                    logger.debug(api_name + "接口:最终mock的数据为" + str(
                        simplejson.dumps(result_list[0], ensure_ascii=False)))
                    return HttpResponse(simplejson.dumps(result_list[0], ensure_ascii=False))
            logger.debug(api_name + "接口:真实请求路径rest_abs_api=" + str(parse.unquote(rest_abs_api)))
            logger.debug(api_name + "接口:请求的请求头为：" + str(content_type))
            logger.debug(api_name + "接口:请求数据request_data数据类型为" + str(type(request_data)))
            if "multipart/form-data;" in content_type:
                http_object = TimeCalc.time_clac(requests.post(url=rest_abs_api, files=request_data, headers=headers),
                                                 rest_api)
            else:
                http_object = TimeCalc.time_clac(requests.post(url=rest_abs_api, data=request_data, headers=headers),
                                                 rest_api)
            try:
                result = simplejson.dumps(http_object.json(), ensure_ascii=False)
            except:
                result = http_object.content.decode("utf-8")
                logger.debug(api_name + "接口:最终响应结果：" + str(result))
                return render_to_response(result, context=RequestContext(request))
            logger.debug(api_name + "接口:最终响应结果：" + str(result))
    except:
        logger.exception(api_name + "接口:POST请求错误如下：")

    try:
        if request.method == "GET":
            logger.debug(api_name + "接口:进入GET方法!")
            # 需要mock则mock，不需要mock则直接跳过
            if result_list != 0:
                logger.debug(api_name + "接口:使用mock!")
                api_is_open = result_list[1]
                logger.debug(api_name + "接口:子开关为" + str(api_is_open))
                if api_is_open == 1:
                    logger.debug(api_name + "接口:最终mock的数据为" + str(
                        simplejson.dumps(result_list[0], ensure_ascii=False)))
                    return HttpResponse(simplejson.dumps(result_list[0], ensure_ascii=False))
            rest_abs_api = url + full_path[11:]
            logger.debug(api_name + "接口:真实请求路径rest_abs_api=" + str(parse.unquote(rest_abs_api)))
            http_object = TimeCalc.time_clac(requests.get(url=rest_abs_api), rest_api)
            mock_content_type = http_object.headers["Content-Type"]
            try:
                result = simplejson.dumps(http_object.json(), ensure_ascii=False)
                logger.debug(api_name + "接口:最终响应结果：" + str(result))
            except:
                result = http_object.content
                logger.debug(api_name + "接口:最终响应结果：" + str(result))
                logger.debug(api_name + "接口:content_type=" + str(http_object.headers))
                return HttpResponse(result, content_type=mock_content_type)
            logger.debug(api_name + "接口:最终响应结果：" + str(result))
    except:
        logger.exception(api_name + "接口:GET请求错误如下：")

    return HttpResponse(result)
