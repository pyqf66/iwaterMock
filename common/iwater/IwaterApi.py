# -*- coding:utf-8 -*-
from totest.models import api_mock
import simplejson
from django.http.response import HttpResponse
import logging

logger = logging.getLogger("iwaterMock.app")


class IwaterApi(object):
    def __init__(self):
        pass

    def get_mock_value_list(self, api_name):
        api_object = api_mock.objects.filter(api_name=api_name)
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
