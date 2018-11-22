from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt  # 装饰器，用来使函数避免csrf
import json

##这个是第一个脚本的api(就只是一个简单的get请求)
# class api(View):
#     def get(self, request):
#         '''
#         处理get请求
#         :param request:
#         :return:
#         '''
#         if request.GET:
#             getData = request.GET['key']
#             return HttpResponse(getData)
#
#     def post(self,request):
#         '''
#         处理post请求
#         :param request:
#         :return:
#         '''
#
#         if request.POST:
#             postData = request.POST
#             return HttpResponse(postData)

##这个是第二个脚本的api(简单的自定义了一个token，返回返回给客户端)
#
# class api(View):
#     def __init__(self,**kwargs):
#         View.__init__(self,**kwargs)
#         self.result = {
#             'status':'',
#             'data':{}
#         }
#
#     def get(self,request):
#         if request.GET:
#             getdata = request.GET['key']
#             return HttpResponse(getdata)
#
#     def post(self,request):
#         if request.POST:
#             postdata = request.POST.get('type')
#             if postdata == 'user_login':
#                 self.result['status'] = 'success'
#                 self.result['data']['token'] = 'I Love You baby'
#             else:
#                 self.result['status'] = 'error'
#                 self.result['data']['token'] = 'you method is error %'%postdata
#
#             return JsonResponse(self.result)

##这个是第三个脚本的api
import json
import time
import datetime
import hashlib

from server.models import CMDBUser,APITonken,Service

class api(View):
    """
    #........
    """
    def __init__(self,**kwargs):
        View.__init__(self,**kwargs)
        self.result = {
            "status": "",
            "data": {}
        }

    def makeToken(self,username):
        """
            md5算法生成token
        """
        time_stamp = str(time.time()) # 获取当前时间的时间的时间戳，然后转换为字符串
        value = username + time_stamp  # 将值和时间戳字符进行拼接

        md5 =hashlib.md5()
        md5.update(value.encode())
        token = md5.hexdigest()
        return token

    def tokenValid(self,token):
        #校验存在
        try:
            db_token = APITonken.objects.get(value = token)
        except:
            return "token error"
        else:
            #校验过期
            db_time_tuple = db_token.time.timetuple()
            db_time_stamp = time.mktime(db_time_tuple)  # 数据库时间的时间戳

            now_time_tupe = datetime.datetime.now().timetuple()
            now_time_stamp = time.mktime(now_time_tupe)  # 当前时间的时间戳
            if 0 < now_time_stamp - db_time_stamp < 3600:
                return "ok"
            else:
                db_token.delete()
                return "time out"

    def get(self,request):
        if request.GET:
            getdata = request.GET['key']
            return HttpResponse(getdata)

    def post(self,request):
        if request.POST:
            postdata = json.loads(request.POST.get('data'))
            postype = request.POST.get('type')
            if postype == 'user_login':
                if postdata:
                    username = postdata.get('username')
                    password = postdata.get('password')
                    try:
                        loginUser = CMDBUser.objects.get(username=username)
                    except Exception as e:
                        self.result['status'] = 'error'
                        self.result['data']['error'] = 'no has mamed %s' %username
                    else:
                        db_password = loginUser.password
                        if db_password == CMDBUser.password:
                            try:
                                db_token = APITonken.objects.get(user_id=loginUser.id)
                            except:
                                new_token = self.maketoken(username)

                                APITonken.objects.create(
                                    value=new_token,
                                    time=datetime.datetime.now(),
                                    user_id=loginUser.id
                                )

                                self.result['status'] = 'success',
                                self.result['data']['token'] = new_token
                            else:
                                db_time_tuple = db_token.time.timetuple()
                                db_time_stamp = time.mktime(db_time_tuple)
                                now_time_tuple = datetime.datetime.now().timetuple()
                                now_time_stamp = time.mktime(now_time_tuple)

                                if 0 < now_time_stamp - db_time_stamp < 3600:
                                    self.result['status'] = 'error'
                                    self.result['data']['error'] = 'you aready has a token %s'%db_token.value

                                else:
                                    new_token = self.maketoken(username)

                                    APITonken.objects.create(
                                        value=new_token,
                                        time=datetime.datetime.now(),
                                        user_id=loginUser.id
                                    )
                                    self.result['status'] = 'success',
                                    self.result['data']['token'] = new_token
                        else:#密码错误
                            self.result['status'] = 'error'
                            self.result['data']['error'] = '%s: you password wrong'%username
                else:#post没有带值
                    self.result['status'] = 'error'
                    self.result['data'] = 'you post value is null'

            else:#请求的，类型不是user_login
                self.result['status'] = 'error'
                self.result['data'] = 'you request type not user_login %s'%postdata


def login(username, passwrod):
    result = {
        "token": "",
        "error": ""
    }
    return result

@csrf_exempt
def CMDBApi(requst):
    # 定义响应的结构
    result = {
        "status": "error",
        "data": {},
        "error": ""
    }
    # 判断如果请求的方式是post并且post有值
    if requst.method == "POST" and  requst.POST:
        data = requst.POST #获取post的值
        ty = data.get("type") #获取具体的参数 #getServer
        dt = data.get("data") #{ "by": "ip" ,"data": "192.168.2.*"}
        tk = data.get("token") #123zasdq23

        if tk and dt and ty: #如果请求的类型(type)不对 ty = "getserver"
            result["error"] = "we have no method named %s"%ty #返回无此类型


        elif tk == '' and ty == "login" and dt: #如果请求是登录
            #dt 是一个字符串
            try:
                dt = json.loads(dt.replace("\'","\""))
            except Exception as e:
                print(e)
            username = dt.get("username") #获取用户名
            password = dt.get("password") #获取密码
            token = login(username,password)["token"] #进行登录校验，获取校验的结果
            if token: #如果token有值
                result["status"] = "success" #返回成功
                result["data"] = {"token": token} #返回token
            else: #否则,也就是没值
                result["error"] = login(username,password)["error"] #返回没有token的错误
                #大致有
                    #用户名不存在
                    #密码错误
        else: #传参不完整
            print(tk == '')
            print(ty == "login")
            print(dt)
            result["error"] = "data is not true"
    else: #请求方式不是post或者post没有值
        result["error"] = "request must be post and post data not be null"
    return JsonResponse(result)

