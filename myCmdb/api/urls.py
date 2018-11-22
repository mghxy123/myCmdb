#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 18/11/15

from django.conf.urls import url
from api.views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', csrf_exempt(api.as_view())),

]