# -*- coding:utf-8 -*-
################################################################
#
#   作者:张羽锋
#   工具名称:喝水计划饮水量计算工具
#   版本:1.0
#   创建日期:2016/7/12
#
################################################################
import math


class DrinkPlan(object):
    def __init__(self):
        pass

    # 参数最多为年龄，体重，性别，职业
    # calc_water1(age, weight, sex, job)
    # calc_water2(age, weight, sex, job)
    # calc_water3(sex, job)
    # 健康计划。性别为0、1,女性为0。职业为1时返回3/2
    def clac_water1(self, age, weight, sex, job, *args, **kwargs):
        if job == 1:
            job_last = 3 / 2
        else:
            job_last = job
        if age <= 2:
            return weight * 90
        elif 3 <= age <= 10:
            return 975 + 75 * (age - 3) + (sex * 1) * 75
        elif 11 <= age <= 13:
            return 1650 + (sex * 1) * 150
        elif 14 <= age <= 17:
            return 1800 + (sex * 1) * 375
        elif age > 17:
            return 1575 + (2 * job_last - 3) * 150 + (sex * job_last) * 150
        else:
            return 0

    # 塑身计划，饮水量(ml)	<45KG为体重段1，>=96KG为体重段2，余下为体重段3。性别=0，1。女性为0。职业=1时，返回3/2
    def clac_water2(self, age, weight, sex, job, *args, **kwargs):
        if job == 1:
            job_last = 3 / 2
        else:
            job_last = job

        if weight < 45:
            weight_section = 1
        elif weight >= 96:
            weight_section = 2
        else:
            weight_section = 3

        if age <= 1:
            return 988
        elif age == 2:
            return 1062
        elif 3 <= age <= 10:
            return 1175 + 75 * (age - 3) + (sex * 1) * 75
        elif age > 10:
            return 1775 + (weight_section - 1) * 1225 - (math.floor(weight_section / 3)) * (3530 - 24 * weight)

    # 康复计划
    def clac_water3(self, *args, **kwargs):
        return 2500

    # 备孕计划，性别=0，1女性为0	职业=1时，返回3/2
    def clac_water4(self, sex, job, *args, **kwargs):
        if job == 1:
            job_last = 3 / 2
        else:
            job_last = job
        result = 1775 + 150 * (2 * job_last - 3) + sex * job_last * 150
        return result

    # 孕期计划
    def clac_water5(self, days, *args, **kwargs):
        if 200 < days < 280:
            return 1575
        elif 100 < days <= 200:
            return 2000
        elif days <= 100:
            return 1575
        else:
            return 0

    # 哺乳计划
    def clac_water6(self, birth_days, *args, **kwargs):
        if birth_days <= 90:
            return 2400
        elif 90 < birth_days <= 180:
            return 2800
        elif 180 < birth_days <= 360:
            return 2500
        elif birth_days > 360:
            return 2000
        else:
            return 0

    # 结石计划
    def clac_water7(self, *args, **kwargs):
        return 3000

    # 自定义喝水计划
    def clac_water8(self,water_plan, *args, **kwargs):
        return water_plan

    # 计算
    def calculate(self, drink_plan=None, age=None, weight=None, sex=None, job=None, days=None, birth_days=None,water_plan=None):
        calc_dict = dict()
        calc_dict[1] = self.clac_water1
        calc_dict[2] = self.clac_water2
        calc_dict[3] = self.clac_water3
        calc_dict[4] = self.clac_water4
        calc_dict[5] = self.clac_water5
        calc_dict[6] = self.clac_water6
        calc_dict[7] = self.clac_water7
        calc_dict[8] = self.clac_water8
        return calc_dict[drink_plan](age=age, weight=weight, sex=sex, job=job, days=days, birth_days=birth_days,water_plan=water_plan)
