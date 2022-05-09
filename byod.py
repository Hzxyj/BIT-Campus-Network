#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

def byod():
    try:
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Origin': 'http://10.7.0.103:30004',
            'Referer': 'http://10.7.0.103:30004/byod/view/byod/template/templatePhone.html?customId=-4',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

        json_data = {
            'userName': '',
            'userPassword': '',
            'serviceSuffixId': '-1',
            'dynamicPwdAuth': False,
            'code': '',
            'codeTime': '',
            'validateCode': '',
            'licenseCode': '',
            'userGroupId': -1,
            'validationType': 2,
            'guestManagerId': -1,
        }

        response = requests.post('http://10.7.0.103:30004/byod/byodrs/login/defaultLogin', headers=headers, json=json_data, verify=False)
        return True
    except:
        return False

if __name__=='__main__':
    byod()
