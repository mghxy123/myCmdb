from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from user.forms import *
from server.models import *
from myCmdb.settings import BASE_DIR
import os

# Create your views here.


def register(request):
    # if request.method == 'POST':
    #     return JsonResponse({"method":'POST'})
    #
    # else:
    #     return JsonResponse({"method":"GET"})

    result = {"submit":'success'}
    #判断三个，请求的方法，post请求的内容和，请求的文件
    #判断请求方式是否为post，request.POST的意思是判断请求是否有数据，request。files是判断上传是否有文件
    if  request.method =='POST' and request.POST and request.FILES:
        register_data = CMDBUserForm(data=request.POST,files=request.FILES)
        if register_data.is_valid():
            #检验成功
            register_post_data = register_data.cleaned_data

            username = register_post_data.get('username')
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
            return JsonResponse(result)
        else:
            result["submit"] = "failed"
            print(register_data.errors)
            return JsonResponse(result)
    else:
        return JsonResponse({"method":'GET'})