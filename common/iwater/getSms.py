# -*- coding:utf-8 -*-
import pymysql


def get_sms_num(phone_num):
    try:
        int(phone_num)
    except:
        return "请输入手机号!"
    if len(phone_num.split('.')) > 1:
        return "请输入手机号!"
    conn = pymysql.connect(host='123.57.47.236', user='iwater', passwd='p@ssw0rd', db='iwater2', charset='utf8')
    cur = conn.cursor()
    sql = "select UserCode from mb_userper where UserMobile=" + phone_num
    print(sql)
    cur.execute(sql)
    result = cur.fetchone()
    cur.close()
    conn.close()
    if result:
        return result[0]
    else:
        return "没查到对应的验证码!"


def get_sms_num_dev(phone_num):
    try:
        int(phone_num)
    except:
        return "请输入手机号!"
    if len(phone_num.split('.')) > 1:
        return "请输入手机号!"
    conn = pymysql.connect(host='123.57.47.236', user='iwater', passwd='p@ssw0rd', db='iwater_test_db', charset='utf8')
    cur = conn.cursor()
    sql = "select UserCode from mb_userper where UserMobile=" + phone_num
    cur.execute(sql)
    result = cur.fetchone()
    print(result)
    cur.close()
    conn.close()
    if result:
        return result[0]
    else:
        return "没查到对应的验证码!"

def get_sms_num_transfer(phone_num):
    try:
        int(phone_num)
    except:
        return "请输入手机号!"
    if len(phone_num.split('.')) > 1:
        return "请输入手机号!"
    conn = pymysql.connect(host='123.57.47.236', user='iwater', passwd='p@ssw0rd', db='iwater2_transfer', charset='utf8')
    cur = conn.cursor()
    sql = "select UserCode from mb_userper where UserMobile=" + phone_num
    cur.execute(sql)
    result = cur.fetchone()
    print(result)
    cur.close()
    conn.close()
    if result:
        return result[0]
    else:
        return "没查到对应的验证码!"
