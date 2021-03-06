# -*- coding:utf-8 -*-
# 本工程所有post请求参数格式均类似为requestPara={"platform":"baidu","device":"MX5"}
from totest.models import api_mock
import simplejson
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import logging
from urllib import parse
import demjson

logger = logging.getLogger("iwaterMock.app")


class IwaterApi(object):
    def __init__(self):
        pass

    def get_mock_value_list(self, api_name, api_no):
        api_object = api_mock.objects.filter(api_name=api_name).filter(api_no=api_no)
        # 判断数据库里是否查询到了对应api_name的数据
        if api_object.count() != 0:
            for i in list(api_object):
                mock_value_list = [simplejson.loads(i.api_resp_json), int(i.is_open)]
            logger.info(api_name + "接口:mock " + api_name + "为:" + str(mock_value_list))
            return mock_value_list
        else:
            return 0

    @staticmethod
    def get_api_name(rest_api):
        # 接口通过斜线拆分到list中，倒数第个数据为接口名称
        rest_api_list = rest_api.split("/")
        try:
            api = rest_api_list[-2]
        except:
            api = rest_api_list[-1]
        return api

    @staticmethod
    def get_api_no(request_data):
        if type(request_data) == bytes:
            data = request_data.decode("utf-8")
        else:
            data = request_data
        api_no = None
        try:
            api_no = simplejson.loads(data)["command"]
        except:
            try:
                api_no_list = parse.parse_qsl(data)
                api_no_dict = dict(api_no_list)
                try:
                    api_no = str(simplejson.loads(api_no_dict["requestPara"])["command"])
                except:
                    api_no = str(demjson.decode(api_no_dict["requestPara"])["command"])
            except:
                api_no = ""
        return api_no

    @staticmethod
    def response_iwater(result="", content_type="", context=""):
        if context:
            response = render_to_response(result, context=context)
        else:
            response = HttpResponse(result, content_type=content_type)
        response["Access-Control-Allow-Origin"] = '*'
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response
