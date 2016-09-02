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
            mock_value_list = [simplejson.loads(weather.api_resp_json), int(weather.is_open)]
        logger.info(self.api_name + "接口:mock天气为:" + str(mock_value_list))
        return mock_value_list

    def iwater_today(self):
        today_object = api_mock.objects.filter(api_name="today")
        for today in list(today_object):
            mock_value_list = [simplejson.loads(today.api_resp_json), int(today.is_open)]
        logger.info(self.api_name + "接口:mock today为:" + str(mock_value_list))
        return mock_value_list

    # 同意的接口存储词典
    def mock_dict(self, api_name):
        self.api_name = api_name
        api_dict = dict()
        # 所有可以mock的接口存入词典
        api_dict["getWeatherCond"] = self.iwater_weather
        api_dict["today"] = self.iwater_today
        logger.info(self.api_name + "接口:请求的api为" + str(self.api_name))
        # 接口存在于词典返回对应方法，不存在返回0
        if api_name in api_dict:
            logger.info(self.api_name + "接口:获取mock方法！")
            return api_dict[self.api_name]
        else:
            return 0

    @staticmethod
    def get_api_name(rest_api):
        # 接口通过斜线拆分到list中，倒数第个数据为接口名称
        rest_api_list = rest_api.split("/")
        api = rest_api_list[-2]
        return api
