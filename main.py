#!/usr/bin/env python
# -*- coding: utf-8 -*-

from byod import byod
import json
import sys

class auto_load:
    __config=None

    def __init__(self,json):
        self.__set_config(json)

    def __set_config(self,conf):
        try:
            with open(conf,'r') as js:
                self.__config=json.load(js)
            print("aaaa")
        except:

    def main(self):
        if(byod(self.__config['id'],self.__config['byodpw'])):
            print("byod connection successfull")
        else:
            print("unexpected error in byod")

if __name__=='__main__':
    load=auto_load("loginf.json")
    load.main()
