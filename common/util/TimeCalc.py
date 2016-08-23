# -*- coding:utf-8 -*-
import time
import logging

logger = logging.getLogger('timeCale')


class TimeCalc(object):
    def __init__(self):
        pass

    @staticmethod
    def time_clac(instance_objects, interface):
        api = interface.split('/')[-2]
        start = time.time()
        result = instance_objects
        end = time.time()
        logger.debug(api + "接口总响应时间:%.15f秒" % (end - start))
        return result
