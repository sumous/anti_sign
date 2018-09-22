# -*- coding:utf-8 -*- 
"""Description:"""
# Created_at: Sat Sep 22 17:34:58 2018 (+0800)
# 
# --------------------------------------------------------------------
# File Name          : api.py
# Author             : sumous
# --------------------------------------------------------------------

import time
import hashlib
import requests


def get_signature(params):
    params_int =  '93005302'

    s = ''
    for k in sorted(params.keys(), reverse=False):
        s += k+params[k]

    key = '1fd6e28fd158406995f77727b35bf20a'
    s = s + key + params_int + '7895e5723ccdc2fd094e50a898561321'
    return hashlib.md5(s.encode('utf8')).hexdigest().upper()


def get_signature_v2(params):
    params_int =  '93005302'

    s = ''
    for k in sorted(params.keys(), reverse=False):
        s += k+params[k]

    key = '9CCFDE35C19775C9A15D91E7C19BD4A9'
    s = s + key + params_int + '7895e5723ccdc2fd094e50a898561321'
    return hashlib.md5(s.encode('utf8')).hexdigest().upper()

def get_event_list(crewid):
    """获取活动列表
    :params crewid: 跑团id
    """
    d = {
        "timestamp":    str(int(time.time())),
        "limit_cnt":    "10",
        "crew_node_id": "0",
        "crewid":       str(crewid)
    }
    headers = {
        "Cookie":           "***YOUR COOKIE***",
        "ypcookie":         "***YOUR COOKIE***",
        "MODELTYPE":        "Hisense M20-T",
        "SYSVERSION":       "4.4.4",
        "APPVERSION":       "4.1.0",
        "MODELIMEI":        "A100004221E3BB",
        "Accept-Language":  "zh_CN",
        "APP_DEV_INFO":     "Android#4.1.0#Hisense M20-T#4.4.4#A100004221E3BB#93005302#360",
        "Content-Type":     "application/x-www-form-urlencoded",
        "Host":             "crewapp.api.thejoyrun.com",
        "Accept-Encoding":  "gzip",
        "User-Agent":       "okhttp/3.10.0"
    }
    headers["_sign"] = get_signature_v2(d)
    d["signature"] = get_signature(d)
    
    url = "https://crewapp.api.thejoyrun.com/crew-app-event-list-top"

    r = requests.post(url, headers=headers, data = d)
    return r.text

def get_crew_info(crewid):
    """获取跑团详情
    :params crewid: 跑团id
    """
    d = {
        "timestamp":    str(int(time.time())),
        "nodeId": "0",
        "crewId":       str(crewid)
    }
    headers = {
        "Cookie":           "***YOUR COOKIE***",
        "ypcookie":         "***YOUR COOKIE***",
        "MODELTYPE":        "Hisense M20-T",
        "SYSVERSION":       "4.4.4",
        "APPVERSION":       "4.1.0",
        "MODELIMEI":        "A100004221E3BB",
        "Accept-Language":  "zh_CN",
        "APP_DEV_INFO":     "Android#4.1.0#Hisense M20-T#4.4.4#A100004221E3BB#93005302#360",
        "Content-Type":     "application/x-www-form-urlencoded",
        "Host":             "crew-muilt.api.thejoyrun.com",
        "Accept-Encoding":  "gzip",
        "User-Agent":       "okhttp/3.10.0"
    }
    headers["_sign"] = get_signature_v2(d)
    d["signature"] = get_signature(d)

    url = "https://crew-muilt.api.thejoyrun.com/structure/getCrewInfo"

    r = requests.post(url, headers=headers, data = d)
    return r.text
