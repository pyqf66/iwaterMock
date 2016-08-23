# -*- coding:utf-8 -*-
from django.db import models


# Create your models here.

# 功能菜单-测试接口设置表
class api_mock(models.Model):
    api_id = models.AutoField(primary_key=True)
    api_name = models.CharField(max_length=50, null=True)
    api_resp_json = models.TextField(null=True)


class drink_plan(models.Model):
    drink_plan = models.CharField(max_length=10, null=True)
    age = models.CharField(max_length=10, null=True)
    weight = models.CharField(max_length=10, null=True)
    sex = models.CharField(max_length=10, null=True)
    job = models.CharField(max_length=10, null=True)
    distance_days = models.CharField(max_length=10, null=True)
    birth_days = models.CharField(max_length=10, null=True)
    water = models.CharField(max_length=10, null=True)


class hydrating_plan(models.Model):
    hydrating_plan = models.CharField(max_length=10, null=True)
    decrement_weight = models.CharField(max_length=10, null=True)
    sports_type = models.CharField(max_length=10, null=True)
    sports_distance = models.CharField(max_length=10, null=True)
    temperature = models.CharField(max_length=10, null=True)
    water = models.CharField(max_length=10, null=True)

class iwater_api(models.Model):
    environment = models.CharField(max_length=10, null=True)
    url = models.CharField(max_length=50, null=True)

class mock_shift(models.Model):
    is_open = models.CharField(max_length=10)
