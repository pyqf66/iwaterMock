# -*- coding:utf-8 -*-
import requests
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from totest.models import drink_plan
from totest.models import hydrating_plan
from common.iwater.DrinkPlan import DrinkPlan
from common.iwater.HydratingPlan import HydratingPlan
import simplejson
import logging

logger = logging.getLogger("iwaterMock.app")


def drink_calc_page(request):
    return render_to_response("drinkCalc.html", context_instance=RequestContext(request))


@csrf_exempt
def get_water_setting(request):
    drink_plan_settings = drink_plan.objects.all()
    hydrating_plan_settings = hydrating_plan.objects.all()
    settings_dict = dict()
    indexNum = 0
    # 数据库读取数据并插入字典
    for i in drink_plan_settings.order_by("-id"):
        settings_dict["drinkPlan"] = i.drink_plan
        settings_dict["age"] = i.age
        settings_dict["weight"] = i.weight
        settings_dict["sex"] = i.sex
        settings_dict["job"] = i.job
        settings_dict["distanceDays"] = i.distance_days
        settings_dict["birthDays"] = i.birth_days
        settings_dict["waterPlan"] = i.water
    for j in hydrating_plan_settings.order_by("-id"):
        settings_dict["hydratingPlan"] = j.hydrating_plan
        settings_dict["decrementWeight"] = j.decrement_weight
        settings_dict["sportsType"] = j.sports_type
        settings_dict["sportsDistance"] = j.sports_distance
        settings_dict["temperature"] = j.temperature
        settings_dict["waterHydrating"] = j.water
    result = simplejson.dumps(settings_dict, ensure_ascii=False)
    logger.info("获取的饮水设置数据为：" + str(result))
    return HttpResponse(result, content_type="application/json")


@csrf_exempt
def drink_calc(request):
    try:
        logger.info("请求的数据为：" + str(request.body))
        drinkPlan = request.POST.get("drinkPlan")
        age = request.POST.get("age")
        weight = request.POST.get("weight")
        sex = request.POST.get("sex")
        job = request.POST.get("job")
        distanceDays = request.POST.get("distanceDays")
        birthDays = request.POST.get("birthDays")
        waterPlan = request.POST.get("waterPlan")
        hydratingPlan = request.POST.get("hydratingPlan")
        decrementWeight = request.POST.get("decrementWeight")
        logger.info("减少的体重为：" + str(decrementWeight))
        sportsType = request.POST.get("sportsType")
        sportsDistance = request.POST.get("sportsDistance")
        temperature = request.POST.get("temperature")
        waterHydrating = request.POST.get("waterHydrating")
        logger.info("获取的自定义补水量为：" + str(waterHydrating))
        drink_plan.objects.filter(id=1).update(drink_plan=drinkPlan, age=age, weight=weight, sex=sex, job=job,
                                               distance_days=distanceDays, birth_days=birthDays, water=waterPlan)
        hydrating_plan.objects.filter(id=1).update(hydrating_plan=hydratingPlan, decrement_weight=decrementWeight,
                                                   sports_type=sportsType, sports_distance=sportsDistance,
                                                   temperature=temperature, water=waterHydrating)

        drink_object = DrinkPlan()
        drink_result = drink_object.calculate(drink_plan=int(drinkPlan), age=int(age), weight=int(weight), sex=int(sex),
                                              job=int(job), days=int(distanceDays), birth_days=int(birthDays),
                                              water_plan=int(waterPlan))

        hydrating_object = HydratingPlan()
        if int(hydratingPlan) == 5:
            hydrating_result = hydrating_object.calculate(hydrating_plan=0,
                                                          weight=int(weight),
                                                          decrement_weight=int(decrementWeight),
                                                          sports_type=int(sportsType),
                                                          sports_distance=int(sportsDistance),
                                                          temperature=int(temperature), water_hydrating=int(waterHydrating))
        else:
            hydrating_result = hydrating_object.calculate(hydrating_plan=int(hydratingPlan),
                                                          weight=int(weight),
                                                          decrement_weight=int(decrementWeight),
                                                          sports_type=int(sportsType),
                                                          sports_distance=int(sportsDistance),
                                                          temperature=int(temperature), water_hydrating=int(waterHydrating))

        const_object = HydratingPlan()
        const_result = const_object.calculate(hydrating_plan=5, weight=int(weight),
                                              temperature=int(temperature))
        weather_water = const_result
        drink_water = drink_result
        filling_water = hydrating_result
        total_water = drink_water + filling_water + weather_water
        result = {"weatherWater": weather_water, "drinkWater": drink_water, "fillingWater": filling_water,
                  "totalWater": total_water}
        result = simplejson.dumps(result)
        logger.info("最终饮水计算结果：" + str(result))
        return HttpResponse(result, content_type="application/json")
    except:
        logger.exception("饮水计算错误：")
