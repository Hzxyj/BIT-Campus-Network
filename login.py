#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import sys
import re

def login(info,id,pw):
    cookies = {
        'JSESSIONID': info[0],
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'http://portal.gd165.com',
        'Referer': 'http://portal.gd165.com/index.do',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    }

    data = [
        ('loginpage', 'gd/blg/login.jsp'),
        ('onlinepage', 'gd/blg/online.jsp'),
        ('logoutpage', ''),
        ('accountprefixname', ''),
        ('accountsuffixname', ''),
        ('pagetype', '0'),
        ('macauth', '0'),
        ('accountvalid', '1800'),
        ('customerId', '001'),
        ('customerName', 'campus'),
        ('basName', '120.80.200.50'),
        ('basPushUrl', 'http://portal.gd165.com/?wlanuserip=10.130.128.135&wlanacname=&basname=120.80.200.50&ssid=bitzh.edu&vlanid=ethtrunk/10:4000.0'),
        ('accountName', ''),
        ('sendSMS', ''),
        ('attrName', 'ssid'),
        ('attrValue', '[bitzh.edu]'),
        ('realmName', ''),
        ('fixedAccountPrefixName', ''),
        ('errormessage', ''),
        ('keepAliveTime', ''),
        ('wlanuserip', '10.130.128.135'),
        ('client_type', 'pz'),
        ('basname', '120.80.200.50'),
        ('errormessage', ''),
        ('setUserOnline', ''),
        ('userOpenAddress', ''),
        ('accountType', ''),
        ('token', info[1]),
        ('username', id),
        ('password', pw),
    ]

    response = requests.post('http://portal.gd165.com/login.do', cookies=cookies, headers=headers, data=data, verify=False)
    print(response.text)
    
if __name__=='__main__':
    pass
    print(re.search("<h5>恭喜您,登录成功！</h5>"),idk)
