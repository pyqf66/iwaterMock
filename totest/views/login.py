# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import logging
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
import simplejson
from urllib import parse

logger = logging.getLogger("iwaterMock.app")


def iwater_login(request):
    return render_to_response("login.html", context=RequestContext(request))


@csrf_exempt
def iwater_login_check(request):
    request_data=dict(parse.parse_qsl(request.body.decode("utf-8")))
    user = authenticate(username=request_data["username"], password=request_data["password"])
    if user is not None:
        # the password verified for the user
        if user.is_active:
            logger.info("User is valid, active and authenticated")
            login(request,user)
            result = {"status": 1}
        else:
            logger.info("The password is valid, but the account has been disabled!")
            result = {"status": 0}
    else:
        # the authentication system was unable to verify the username and password
        logger.info("The username and password were incorrect.")
        result = {"status": 0}
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json")

def iwater_logout(request):
    logout(request)
    result = {"status":1}
    return HttpResponse(simplejson.dumps(result, ensure_ascii=False), content_type="application/json")


