#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : requests_sendServer.py
# Author: HuXianyong
# Date  : 2018/11/23

import json
import requests
from time import sleep


#先按照老师的写，先把过程走通，然后按照自己想的，把整个数据都当成一个post提交上去
class SendServerData:
    def __init__(self,url,username,password):#直接把变量一股脑的传给类，下面的方法直接调用就好了
        self.url = url
        self.username = username
        self.password = password
        self.login_data = login_data

    def user_check(self):
        login_data = {#定义登录的账户密码信息
            "username": self.username,
            "password": self.password
        }
        data = {#定义post传入的data信息
           "type": "user_login", #发送的数据库类型为user_login
            "data": json.dumps(login_data),#把数据格式转化成json格式
            "token": ""
        }
        response = requests.post(self.url,data = data)#发送请求

        try:
            self.token = response.json()['data']['token']#获取返回的token
            sleep(1) #这里的sleep是为了等同步token，才能完成token校验，不然会无法校验成功
        except Exception as e:
            print('小伙子，你错啦！ %s'%e)

    def addServerData(self,server_data):
        data = {
            "type": "addServer",#发送的数据库类型为addServer，给服务器接受请求做判断的
            "data": json.dumps(self.server_data),#把格式有Python的字典转成html的json
            "token": self.token
        }

        data_response = requests.post(self.url, data=data) #发送请求
        b = data_response.json()
        print(b)

    def addTimes(self,times):
        self.times = times
        self.user_check()

        for time in range(times):
            ip = '192.168.1.%s'%time
            hostname = 'saltmaster%s'%time
            self.server_data = {
                "ip": "192.168.1.88",
                "mac": "00:01:6C:06:A6:29",
                "cpu": "Intel(R) Core(TM) i7 CPU L 640  @ 2.13GHz",
                "memory": "1800099",
                "hostname": "saltmaster"
            }
            self.server_data['ip'] = ip
            self.server_data['hostname'] = hostname


            self.addServerData(self.server_data)


if __name__ == '__main__':
    url = "http://127.0.0.1:8888/api/"
    username = 'hxy'
    password = '12345678'

    login_data = {
        "ip": "192.168.1.88",
        "mac": "00:01:6C:06:A6:29",
        "cpu": "Intel(R) Core(TM) i7 CPU L 640  @ 2.13GHz",
        "memory": "180004",
        "hostname": "saltmaster"
    }
    s = SendServerData(url,username,password)
    s.addTimes(10)
###############################################################
    # user_data = {  # 定义登录的账户密码信息
    #     "username": self.username,
    #     "password": self.password
    # }
    #
    # user_request = {  # 定义post传入的data信息
    #     "type": "user_login",  # 发送的数据库类型为user_login
    #     "data": json.dumps(user_data),  # 把数据格式转化成json格式
    #     "token": ""
    # }
    #
    # server_request = {
    #     "type": "addServer",  # 发送的数据库类型为addServer，给服务器接受请求做判断的
    #     "data": json.dumps(self.login_data),  # 把格式有Python的字典转成html的json
    #     "token": self.token
    # }
    # server_data = {
    #     "ip": "192.168.1.88",
    #     "mac": "00:01:6C:06:A6:29",
    #     "cpu": "Intel(R) Core(TM) i7 CPU L 640  @ 2.13GHz",
    #     "memory": "180004",
    #     "hostname": "saltmaster"
    # }