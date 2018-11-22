# -*- coding: utf-8 -*-
# File  : urls.py
# Author: HuXianyong
# Date  : 2018-11-15 21:36

from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^et/', et),
    url(r'^$', et),

]