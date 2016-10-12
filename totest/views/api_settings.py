# -*- coding:utf-8 -*-
import requests
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from totest.models import api_mock
from django.core.paginator import Paginator
import simplejson
import logging

logger = logging.getLogger("iwaterMock.app")


@csrf_exempt
def api_mock_settings_page(request):
    return render_to_response("apiSettingsTreegrid.html", context=RequestContext(request))


@csrf_exempt
def api_data_json_response(request):
    try:
        paging_data = request.GET
        logger.info("请求的分页要求数据信息paging_data=" + str(paging_data))
        page = paging_data.get("page")
        logger.info("当前页page=" + str(page))
        rows = paging_data.get("rows")
        logger.info("每页显示行数rows=" + str(rows))
        interface_settings_json_data = api_mock.objects.all()
        interface_settings_json_list = []
        indexNum = 0
        # 数据库读取数据并插入字典
        for i in interface_settings_json_data.order_by("-api_id"):
            interface_settings_json_list.append({})
            interface_settings_json_list[indexNum]["api_id"] = i.api_id
            interface_settings_json_list[indexNum]["api_no"] = i.api_no
            interface_settings_json_list[indexNum]["api_name"] = i.api_name
            interface_settings_json_list[indexNum]["api_resp_json"] = i.api_resp_json
            interface_settings_json_list[indexNum]["is_open"] = i.is_open
            indexNum = indexNum + 1
        paging_object = Paginator(interface_settings_json_list, rows)
        results = paging_object.page(page).object_list
        logger.info("分页结果数据类型为:" + str(type(results)))
        logger.info("分页结束results=" + str(results))
        total_Records = paging_object.count
        interface_settings_json_str = simplejson.dumps({"totalRecord": total_Records, "results": results})
        return HttpResponse(interface_settings_json_str, content_type="application/json")
    except Exception as e:
        logger.error(e)
        logger.exception(u"测试接口设置页面分页错误如下:")


@csrf_exempt
def api_mock_setting(request):
    try:
        result = "success!!!"
        # 接收json数据
        if request.method == 'POST':
            received_json_data = request.POST.get("effectRow")
            datalist = simplejson.loads(received_json_data)
            logger.info(datalist)
            if "inserted" in datalist:
                for i in list(simplejson.loads(datalist["inserted"])):
                    # 增加数据
                    logger.info(received_json_data)
                    logger.info(i)
                    http_interface_info_db = api_mock(api_name=i["api_name"],
                                                      api_resp_json=i["api_resp_json"],
                                                      is_open=i["is_open"],
                                                      api_no=i["api_no"])
                    http_interface_info_db.save()
            if "deleted" in datalist:
                for i in list(simplejson.loads(datalist["deleted"])):
                    # 删除数据
                    api_mock.objects.get(api_id=i["api_id"]).delete()
            if "updated" in datalist:
                for i in list(simplejson.loads(datalist["updated"])):
                    # 更新数据
                    api_mock.objects.filter(api_id=i["api_id"]).update(
                        api_id=i["api_id"], api_name=i["api_name"],api_no=i["api_no"],
                        api_resp_json=i["api_resp_json"], is_open=i["is_open"],)
            result = simplejson.dumps(result)
            return HttpResponse(result)
        else:
            result = "error!!!"
            result = simplejson.dumps(result)
            return HttpResponse(result)
    except Exception as e:
        logger.error(e)
        logger.exception(u"捕获到错误如下:")
