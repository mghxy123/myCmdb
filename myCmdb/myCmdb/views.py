#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : views.py
# Author: HuXianyong
# Date  : 18/11/8

from django.shortcuts import render
from user.forms import CMDBUserForm
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
import os
from server.models import CMDBUser
from myCmdb.settings import BASE_DIR
def blank(request):
     return render(request,'blank.html')



def form_test(request):
    data = request.POST
    phone = data['phone']

    print(phone)
    return HttpResponse(phone)





