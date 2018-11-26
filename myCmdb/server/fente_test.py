#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : fente_test.py
# Author: HuXianyong
# Date  : 2018/11/23

count_num=100
db_list = list(range(1,count_num+1))#range循环的个数要比总个数少一个，所以要加一

one_page_num = 4 #每页四条数据
one_times_num = 3 #每次请求三页

while True:
    page = int(input('page >>>')) #请输入你当前的页码

    #设定findIndex为索引
    if page/one_times_num > page//one_times_num:#如果输入的页数大于一次请求的页数，那么索引就需要向前加一
        findIndex = page//one_times_num +1
    else:
        findIndex = page // one_times_num
    # print(findIndex)
    select_num = one_times_num*one_page_num #一次请求的数据个数
    select_start = (findIndex-1)* select_num
    select_end = (findIndex+0)* select_num
    select_data = db_list[select_start:select_end]

    #这里利用余数来对数据列表进行当前页的取值，
    if page%one_times_num !=0:#如果当前页不是请求页数的倍数的话，起始位置就是余数减一乘以每页的数据条数，结束位置就是余数乘以每页的数据条数
        now_index = page%one_times_num
        now_page_start = (now_index -1)*one_page_num
        now_page_end = (now_index -0)*one_page_num
        now_page_data = select_data[now_page_start:now_page_end]
    else:
        now_page_data = select_data[-one_page_num:]


    # now_index = page - (findIndex-1)*one_times_num
    #
    # now_page_start = (now_index -1)*one_page_num
    # now_page_end = (now_index -0)*one_page_num
    # now_page_data = select_data[now_page_start:now_page_end]

    print('+'*30)
    print('page %s'%page)
    print('page start %s'%select_start)
    print('page end %s'%select_end)
    print('now page data \n%s'%now_page_data)
    print('page data \n%s'%select_data)
    print('+'*30)