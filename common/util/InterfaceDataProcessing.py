# coding=utf-8
###########################################
# File: InterfaceDataProcessing.py
# Desc: http接口处理工具类
# Author: zhangyufeng
# History: 2015/11/20 zhangyufeng 新建
###########################################
from common.util.TimeStamp import TimeStamp
from common.util.Md5 import Md5
import simplejson
import logging


class InterfaceDataProcessing(object):
    global logger
    logger = logging.getLogger("DreamStar.app")

    def __init__(self, interface_code, data_dict, secretkey_value):
        try:
            # 生成时间戳
            self.__time_stamp = TimeStamp.time_stamp()
            self.__data_dict = data_dict
            self.__secretkey_value = secretkey_value
            self.__interface_code = interface_code
        except Exception as e:
            logger.error(e)
            logger.exception(u"数据处理初始化错误如下:")

    # 接口数据处理方法，key为interface_code
    def processing(self):
        try:
            pass
        except Exception as e:
            logger.error(e)
            logger.exception(u"最终数据处理错误如下:")

    # 处理application/x-www-form-urlencoded数据（a=1&b=1）为字典
    @classmethod
    def urldecoded(self, data):
        try:
            data_list_first = data.split("&")
            data_list_second = list()
            for tmp in data_list_first:
                data_list_second.append(tmp.split("="))
            result = dict()
            for i in data_list_second:
                result[i[0]] = i[1]
            return result
        except Exception as e:
            logger.error(e)
            logger.exception(u"URL格式解码错误如下:")
