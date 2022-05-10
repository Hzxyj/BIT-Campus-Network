#!/usr/bin/env python
# -*- coding: utf-8 -*-
#obtain 'cookie' and 'token' in http://portal.gd165.com

import requests,sys,re

def do_post(cookie):
    if(cookie!=None):
        cookies = {
            'JSESSIONID': cookie, 
        }
    else:
        cookies = {}

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'http://portal.gd165.com',
        'Referer': 'http://portal.gd165.com/?wlanuserip=10.130.128.135&wlanacname=&basname=120.80.200.50&ssid=bitzh.edu&vlanid=ethtrunk/10:4000.0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    }

    data = {
        'basPushUrl': 'http://portal.gd165.com/?wlanuserip=10.130.128.135&wlanacname=&basname=120.80.200.50&ssid=bitzh.edu&vlanid=ethtrunk/10:4000.0',
        'debugua': '',
        'testmacauth': 'false',
    }

    response = requests.post('http://portal.gd165.com/index.do', cookies=cookies, headers=headers, data=data, verify=False)
    return response

def without_cookie():
    response=do_post(None)
    cookie=re.search("(?<=JSESSIONID=)\w+",str(response.cookies)).group()
    return cookie

def with_known_cookie(cookie):
    response=do_post(cookie)
    token=re.search("(?<=\"token\"value=\")\w*",str(response.text)).group()
    return token


if __name__=='__main__':
    cookie=without_cookie()
    print(cookie)
    token=with_known_cookie(cookie)
    print(token)
