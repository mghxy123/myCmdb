from django.shortcuts import render
from django.views.generic import View
from server.models import *
from django.http import JsonResponse,HttpResponse

# Create your views here.

def et(request):
    return render(request,'server/echartsExample.html')

def serverList(request):
    return render(request,'server/getpage.html')

def setPage(page,one_times_num,one_page_num,db):
    '''
        就是进行分页，分页的公共用法
    :param request:
    :return:
    '''
    db_count = db.objects.all() #查询指定数据库的所有数据
    #设定findIndex为索引
    if page/one_times_num > page//one_times_num:#如果输入的页数大于一次请求的页数，那么索引就需要向前加一
        findIndex = page//one_times_num +1
    else:
        findIndex = page // one_times_num
    # print(findIndex)
    select_num = one_times_num*one_page_num #一次请求的数据个数
    select_start = (findIndex-1)* select_num
    select_end = (findIndex+0)* select_num
    select_data = db_count[select_start:select_end]

    #这里利用余数来对数据列表进行当前页的取值，
    # if page%one_times_num !=0:#如果当前页不是请求页数的倍数的话，起始位置就是余数减一乘以每页的数据条数，结束位置就是余数乘以每页的数据条数
    #     now_index = page%one_times_num
    #     now_page_start = (now_index -1)*one_page_num
    #     now_page_end = (now_index -0)*one_page_num
    #     now_page_data = select_data[now_page_start:now_page_end]
    # else:
    #     now_page_data = select_data[-one_page_num:]

    now_index = page - (findIndex-1)*one_times_num

    now_page_start = (now_index -1)*one_page_num
    now_page_end = (now_index -0)*one_page_num
    now_page_data = select_data[now_page_start:now_page_end]

    result = {
        'page':page,
        'pageData':now_page_data,

    }

    #定义页面的数量，防止请求超出页面的范围导致取不到值
    count = db.objects.count() #总条数
    final_page = count/one_page_num #总页数
    if final_page != int(final_page): #如果不是整数倍就需要多加一页
        final_page +=1
    final_page = int(final_page)#转化为整形

    #定义判断页面的范围
    islast = 0
    if page >= final_page:
        page = final_page
        islast = 1

    #获取页码
    if page in [1,2,3]:
        prange_start = 1
        prange_end = 6
    else:
        prange_start = page-2
        prange_end= page + 3
    if prange_end >= final_page:
        prange_end = final_page

    prange = list(range(prange_start,prange_end))
    result['count'] = count#总条数
    result['prange'] = prange#当前页码
    result['islast'] = islast#是否为最后一条
    return result

def serverData(request):

    if request.method == 'GET' and request.GET:
        page = int(request.GET.get('page'))

        one_page_num = 10 #每页10条
        one_times_num = 3 #每次3页

        result_list = []

        page_data = setPage(page,one_times_num,one_page_num,Service)
        datas = page_data.get('pageData')
        for data in datas:
            result_list.append(
                {
                    'id':data.id,
                    'ip':data.ip,
                    'mac':data.mac,
                    'cpu':data.cpu,
                    'memeory':data.memory,
                    'hostname':data.hostname,
                    'isalive':data.isalive,
                }
            )
        page_data['pageData'] = result_list
        # print(page_data)
        return JsonResponse(page_data)
    else:
        return JsonResponse({'error':'no data'})


def serverList1(request):
    return render(request,'server/getpage1.html')

def gateone(request):
    return render(request,'server/gateoneConnect.html')

def gateonev2(request):
    if request.method == 'GET' and request.GET:
        rget = request.GET
        ip = rget.get('ip','172.16.188.128')
        port = rget.get('port',22)
        user = rget.get('user','root')
        return render(request,'server/gateOneConnect_v2.html',locals())
    else:
        return HttpResponse('404 not found!!!')

import time,hmac,json
import hashlib
def gateValid(request):
    gateone_server = 'https://172.16.188.128:443'

    key = 'MzY0OGVkZmFjYzA4NDg0N2JhMDhkZjYzYWViMjE5YzY1N'
    value = 'ZjBlMWVlODkwYzQzNGViMThhN2NjNGQxNWNiMzNjZWJjM'.encode()

    # authobj_dict = {
    #     'api_key':key,
    #     'upn':'gateone',
    #     'timestamp':str(int(time.time()*1000)),
    #     'signature_method': 'HMAC-SHA1',
    #     'api_version':'1.0'
    #
    # }
    # my_hash = hmac.new(value,digestmod=hashlib.sha1)
    # update_data = authobj_dict['api_key']+authobj_dict['upn']+authobj_dict['timestamp']
    # my_hash.update(update_data.encode())
    #
    # authobj_dict['signatrue'] = my_hash.hexdigest()
    # auth_info_and_server = {'url':gateone_server,'auth':authobj_dict}
    # valid_json_auth_info = json.dumps(auth_info_and_server)
    # return JsonResponse(valid_json_auth_info)
    authodj_dict = {
        'api_key': key,
        'upn': 'gateone',
        'timestamp': str(int(time.time() * 1000)),
        'signature_method': 'HMAC-SHA1',
        'api_version': '1.0'
    }
    my_hash = hmac.new(value,digestmod = hashlib.sha1)
    update_data = authodj_dict['api_key'] + authodj_dict['upn'] + authodj_dict['timestamp']
    my_hash.update(update_data.encode())

    authodj_dict['signature'] = my_hash.hexdigest()
    auth_info_and_server = {"url": gateone_server, "auth": authodj_dict}
    valid_json_auth_info = json.dumps(auth_info_and_server)
    return HttpResponse(valid_json_auth_info)