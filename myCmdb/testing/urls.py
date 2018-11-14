#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 18/11/7

from django.conf.urls import url
from testing.views import *

urlpatterns=[
    url(r'^$',index),
    url(r'^index/$',index),
]