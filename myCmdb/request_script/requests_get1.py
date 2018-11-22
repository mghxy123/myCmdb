#!/usr/bin/python
# -*- coding: utf8 -*- 
#*************************************************************************
# File Name: reqpests.py
# Author: huxianyong
# Mail: hxy123@163.com 
# Created Time: Tue 20 Nov 2018 02:17:39 PM CST
#************************************************************************

import requests
#url = 'http://47.98.60.53:9909/service/api/?key=name'
url = 'http://127.0.0.1:8888/api/?key=name'
response = requests.get(url)
print(response)
