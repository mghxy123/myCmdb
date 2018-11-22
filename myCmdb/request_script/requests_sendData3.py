#!/usr/bin/python3
# -*- coding: utf8 -*- 
#*************************************************************************
# File Name: reqpests_post2.py
# Author: huxianyong
# Mail: hxy123@163.com 
# Created Time: Tue 20 Nov 2018 05:47:46 PM CST
#************************************************************************

import json
import requests

#url = "http://47.98.60.53:9909/service/api/"
url = "http://127.0.0.1:8888/api/"
data = {
   "type": "user_login",
    "data": {
       "username": "hxy",
       "password": "12345678"
    },
    "token": ""
	}

response = requests.post(url,data = data)
data = response.json()
print(data)
