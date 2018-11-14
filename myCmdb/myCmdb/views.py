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

# def loginValid(func):
#     def valid(request,*args,**keywords):
#         username = request.COOKIES.get('username')
#         if username:
#             try:
#                 user = CMDBUser.objects.get(username=username)
#             except:
#                 return HttpResponseRedirect('/login/',locals())
#             else:
#                 return func(request)
#         else:
#             return HttpResponseRedirect('/login/',locals())
#     return valid
#
# @loginValid
def index(request):
    register_forms = CMDBUserForm()
        #判断三个，请求的方法，post请求的内容和，请求的文件
    #判断请求方式是否为post，request.POST的意思是判断请求是否有数据，request。files是判断上传是否有文件
    if  request.method =='POST' and request.POST and request.FILES:
        register_data = CMDBUserForm(data=request.POST,files=request.FILES)
        if register_data.is_valid():
            #检验成功
            register_post_data = register_data.cleaned_data

            username = register_post_data.get('username')
            cname = CMDBUser.objects.filter(username=username)
            if len(cname) < 1 :
                password = register_post_data.get('password')
                nickname = register_post_data.get('nickname')
                phone = register_post_data.get('phone')
                email = register_post_data.get('email')

                #当去get图片的时候的导师是一个对象，用。name是获取photo的值
                photo = register_post_data.get('photo').name

                CMDBUser.objects.create(
                    username= username,
                    password= password,
                    nickname=nickname,
                    phone=phone,
                    email=email,
                    photo=photo,

                )
                photofile = request.FILES.get('photo')
                photoSavePath=os.path.join(BASE_DIR,'static/images/%s'%photofile.name)
                with open(photoSavePath,'wb') as pf:
                    for chunk in photofile.chunks():
                        pf.write(chunk)
            else:
                info = {'info':'用户名已经存在，请换个用户名！'}
        else:
            print(register_data.errors)
    return render(request,'index.html',locals())

def form_test(request):
    data = request.POST
    phone = data['phone']

    print(phone)
    return HttpResponse(phone)


def et(request):
    # return render(request,'aa.html')
    return render(request,'echartsExample.html')

def login(request):
    if request.method =='POST' and request.POST:
        #获取校验cookie
        login_cookie = request.COOKIES.get('hello')
        if login_cookie:
            data = request.POST
            username = data.get('username')
            password = data.get('password')
            try:
                user = CMDBUser.objects.get(username=username)
            except:
                return HttpResponse('用户不存在')
            else:
                db_password = user.password
                if password == db_password:
                    response = HttpResponseRedirect('/index/',locals())
                    response.set_cookie(key='username',value=user.username)
                    return response
                else:
                    return HttpResponse('密码错误')
        else:
            return HttpResponse('404')
    else:
        #生成response实例
        response = render(request,'login.html')
        #设置cookie,加盐cookie
        # response.set_signed_cookie('hello','aaaaa',salt='nidaye',max_age=6666)
        response.set_cookie('hello','aaaaa',max_age=6666)
        #设置返回的cookie
        return response

def register(request):
    return render(request,'register_check.html')

import json
def register_check(request):
    username = request.GET.get('username')
    cname = CMDBUser.objects.filter(username=username)
    print(cname)
    if len(cname) < 1 :
        info = {'info':'true'}
    else:
        info = {'info':'false'}

    return JsonResponse(info)