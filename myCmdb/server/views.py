from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class API(View):
    def post(self,request):
        '''
        处理post请求
        :param request:
        :return:
        '''

        pass

    def __get__(self, request):
        '''
        处理get请求
        :param request:
        :return:
        '''
        pass