#!/usr/bin/python
# -*- coding: utf8 -*- 
#*************************************************************************
# File Name: reqpests.py
# Author: huxianyong
# Mail: hxy123@163.com 
# Created Time: Tue 20 Nov 2018 02:17:39 PM CST
#************************************************************************

import requests
url = 'http://47.98.60.53:9909/service/api/'
data = {
   "type": "user_login",
    "data": {
       "username": "while",
       "password": "123"
    },
    "token": ""
}
response = requests.post(url,data=data)
with open('1.html','wb') as f:
    f.write(response.content)
print(response)
