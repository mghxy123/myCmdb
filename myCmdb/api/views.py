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
#             postData = request.POST.get('type')
#             if postData == 'user_login':
#                 self.result['status'] = 'success'
#                 self.result['data']['token'] = 'I Love You baby'
#             else:
#                 self.result['status'] = 'error'
#                 self.result['data']['token'] = 'you method is error %'%postData
#
#             return JsonResponse(self.result)

##第三个脚本的就不写了

##这个是第4567脚本的api,第五个脚本需要手动获取token然后放到文件里面去才能运行，不然会报错
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
    def get(self,request): #这里定义了get的数据类型是ip/api/?key=value,这样返回的会是value，切只能是key=
        if request.GET:
            getdata = request.GET['key']#获取get中的key的值
            return HttpResponse(getdata)

    def post(self,request):
        if request.POST:
            postype = request.POST.get('type')#获取type中的type的值
            postData = json.loads(request.POST.get("data"))#获取post里面data的值
            if postype == 'user_login': #判断用户是用户校验还是，上传数据，这里是用户校验
                if postData:
                    postUsername = postData.get('username')#获取提交的用户名
                    postPasswd = postData.get('password')#获取提交的密码
                    try:
                        loginUser = CMDBUser.objects.get(username=postUsername)#尝试去数据库获取这个用户的信息
                    except :#获取不到就说明这个用户不在我们的有权范围内，给这个用户返回没有这个用户
                        self.result['status'] = 'error'
                        self.result['data']['error'] = 'no has mamed %s' %postUsername
                    else:#如果有这个用户就来对密码进行校验
                        db_password = loginUser.password
                        if postPasswd == db_password:
                            try:#密码校验通过了就开始校验token了，通过用户的id到数据库里面去获取token的id，用户的id和token的id是关联了，我觉得这个不好，后面我要改成用户名关联
                                db_token = APITonken.objects.get(user_id=loginUser.id)
                            except:#如果没有获取到token就说明这个用户是刚刚登陆的，给这个用户新建一个token返回给用户，并把token入库
                                new_token = self.maketoken(postUsername)#通过调用函数生成token
                                APITonken.objects.create(#token入库，token表只就有这三个值
                                    value=new_token,
                                    time=datetime.datetime.now(),
                                    user_id=loginUser.id
                                )

                                self.result['status'] = 'success',
                                self.result['data']['token'] = new_token #入库成功之后就把token和状态存入返回字典里面
                            else:#如果是获取到了token，就对token的时间进行校验
                                db_time_tuple = db_token.time.timetuple()#他是这个样子的(tm_year=2018, tm_mon=11, tm_mday=23, tm_hour=15, tm_min=9, tm_sec=10, tm_wday=4, tm_yday=327, tm_isdst=-1)
                                db_time_stamp = time.mktime(db_time_tuple)#时间戳
                                now_time_tuple = datetime.datetime.now().timetuple()
                                now_time_stamp = time.mktime(now_time_tuple)#时间戳

                                if 0 < now_time_stamp - db_time_stamp < 1:#如果时间戳还在这个范围内就给用户返回，你已经获取过时间戳了
                                    self.result['status'] = 'error'
                                    self.result['data']['error'] = 'you aready has a token %s'%db_token.value

                                else:#如果时间戳过期了，就给用户生成一个新的时间戳
                                    new_token = self.maketoken(postUsername)
                                    APITonken.objects.create(
                                        value=new_token,
                                        time=datetime.datetime.now(),
                                        user_id=loginUser.id
                                    )
                                    self.result['status'] = 'success',
                                    self.result['data']['token'] = new_token
                        else:#密码错误
                            self.result['status'] = 'error'
                            self.result['data']['error'] = '%s: you password wrong'%postUsername
                else:#post没有带值
                    self.result['status'] = 'error'
                    self.result['data'] = 'you post value is null'
            elif postype == "addServer":
                if postData:
                    postToken = request.POST.get("token")  # 获取接口请求的数据
                    if postToken and self.tokenValid(postToken) == "ok":
                        #获取数据
                        ip = postData.get("ip")
                        mac = postData.get("mac")
                        cpu = postData.get("cpu")
                        memory = postData.get("memory")
                        hostname = postData.get("hostname")
                        #保存数据
                        server = Service()
                        server.ip = ip
                        server.mac = mac
                        server.cpu = cpu
                        server.memory = memory
                        server.hostname = hostname
                        server.isalive = "false"
                        server.save()
                        #发送返回
                        self.result["status"] = "success"
                        self.result["data"]["result"] = "save success"
                    else:
                        self.result["status"] = "error"
                        self.result["data"]["result"] = self.tokenValid(postToken)

            else: #请求类型
                self.result["status"] = "error"
                self.result["data"]["error"] = "no method named %s"%postype
            return JsonResponse(self.result)

    def maketoken(self,username):
        """
            md5算法生成token
        """
        time_stamp = str(time.time()) # 获取当前时间的时间的时间戳，然后转换为字符串
        value = username + time_stamp  # 将值和时间戳字符进行拼接

        MD5 =hashlib.md5()#实例化一个MD5算法
        MD5.update(value.encode())#先把value编码成Unicode，然后加入MD5码生成的表中
        token = MD5.hexdigest()#生成MD5值
        return token

    def tokenValid(self,token):
        #校验存在
        try:
            db_token = APITonken.objects.get(value = token)#从数据库中获取token，在数据库的表中键就是value，等到自己再写一次的时候改成token，就不会看起来会误解了
        except:
            return "token error" #如果获取不到token就说明，这个数据的post没有进行用户校验，返回token error
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