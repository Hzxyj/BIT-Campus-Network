#!/usr/bin/env python
# -*- coding: utf-8 -*-

from byod import byod
from gd165 import visit
from login import login
import json
import sys

class auto_load:
    __config=None

    def __init__(self,json):
        self.__set_config(json)
        self.main()

    def __set_config(self,conf):
        try:
            with open(conf,'r') as js:
                self.__config=json.load(js)
        except:
            print("fail to open config")

    def __byod(self):
        if(byod(self.__config['id'],self.__config['byodpw'])):
            print("byod connection successfull")
        else:
            print("unexpected error in byod")

    def __gd165(self):
        info=visit()
        print(info)
        login(info,self.__config['id'],self.__config['gd165pw'])

    def main(self):
        self.__byod()
        self.__gd165() 


if __name__=='__main__':
    load=auto_load("loginfo.json")
