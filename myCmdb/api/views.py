from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt  # 装饰器，用来使函数避免csrf


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

