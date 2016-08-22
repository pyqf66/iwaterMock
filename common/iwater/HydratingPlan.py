# -*- coding:utf-8 -*-
################################################################
#
#   作者:张羽锋
#   工具名称:喝水计划饮水量计算工具
#   版本:1.0
#   创建日期:2016/7/12
#
################################################################
import sys
import math


class HydratingPlan(object):
    def __init__(self):
        pass

    # 感冒发烧。
    def clac_water1(self, weight, *args, **kwargs):
        return weight * 15

    # 急性腹泻
    def clac_water2(self, weight, decrement_weight, *args, **kwargs):
        if weight < 50:
            if decrement_weight <= 1:
                return decrement_weight * 50
            else:
                return decrement_weight * 100
        elif 50 <= weight <= 80:
            if decrement_weight <= 3:
                return decrement_weight * 50
            else:
                return decrement_weight * 100
        elif weight > 80:
            if decrement_weight <= 5:
                return decrement_weight * 50
            else:
                return decrement_weight * 100
        else:
            return 0

    # 运动补水
    def clac_water3(self, sports_type, sports_distance, weight, *args, **kwargs):
        if sports_type == 1:
            return weight * 1.46 * sports_distance
        elif sports_type == 2:
            return weight * 1.55 * sports_distance
        elif sports_type == 3:
            return weight * 1.72 * sports_distance
        else:
            return 0

    # 自定义补水
    def clac_water4(self, water_hydrating, *args, **kwargs):
        return water_hydrating

    # 极端天气补水
    def clac_water5(self, temperature, weight, *args, **kwargs):
        if temperature > 30:
            return weight * 10
        else:
            return 0

    # 计算
    def calculate(self, hydrating_plan=None, weight=None, decrement_weight=None, sports_type=None, sports_distance=None,
                  temperature=None, water_hydrating=None):
        calc_dict = dict()
        calc_dict[1] = self.clac_water1
        calc_dict[2] = self.clac_water2
        calc_dict[3] = self.clac_water3
        calc_dict[4] = self.clac_water4
        calc_dict[5] = self.clac_water5
        if hydrating_plan in calc_dict:
            result = calc_dict[hydrating_plan](hydrating_plan=hydrating_plan, weight=weight,
                                               decrement_weight=decrement_weight, sports_type=sports_type,
                                               sports_distance=sports_distance, temperature=temperature, water_hydrating=water_hydrating)
        else:
            result = 0
        return result
