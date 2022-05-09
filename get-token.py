#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests,sys,re
cookies = {
    #'JSESSIONID': '209FA33D703870C07C6DB30A652D78D0',
    'JSESSIONID': '6811AE4BCC09A6068E98BD07B5A63923',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'JSESSIONID=209FA33D703870C07C6DB30A652D78D0',
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
print(response.cookies)
#print(response.text)
print(re.search("(?<=\"token\"value=\")\w*",str(response.text)).group())
