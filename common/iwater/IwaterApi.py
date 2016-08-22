# -*- coding:utf-8 -*-
from totest.models import api_mock
import simplejson
from django.http.response import HttpResponse
import logging

logger = logging.getLogger("iwaterMock.app")


class IwaterApi(object):
    def __init__(self):
        pass
    
    # 可以mock的接口
    def iwater_weather(self):
        weather_object = api_mock.objects.filter(api_name="getWeatherCond")
        for weather in list(weather_object):
            resp = simplejson.loads(weather.api_resp_json)
        logger.info("mock天气为:" + str(resp))
        return resp
    
    # 同意的接口存储词典
    def mock_dict(self, rest_api):
        api_dict = dict()
        # 所有可以mock的接口存入词典
        api_dict["getWeatherCond"] = self.iwater_weather
        # 接口通过斜线拆分到list中，倒数第个数据为接口名称
        rest_api_list = rest_api.split("/")
        api = rest_api_list[-2]
        logger.info("请求的api为" + str(api))
        # 接口存在于词典返回对应方法，不存在返回0
        if api in api_dict:
            logger.info("获取mock方法！")
            return api_dict[api]
        else:
            return 0
