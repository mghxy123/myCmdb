#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 18/11/13


from django.conf.urls import  url
from user.views import *


urlpatterns = [
    url(r'^$',login),
    url(r'^login/',login),
    url(r'^index/',index),
    url(r'^register/',register),

    url(r'^testing_register_page/', testing_register_page),#简单的用于用户账户的检测
    url(r'^testing_register_check/', testing_register_check),
]
