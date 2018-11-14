#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : form.py
# Author: HuXianyong
# Date  : 18/11/8

from django import forms

class CMDBUserForm(forms.Form):
    username=forms.CharField(max_length=32, label='用户账号', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(max_length=32, label='用户密码', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    nickname=forms.CharField(max_length=32, label='用户姓名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone=forms.CharField(max_length=32, label='用户手机', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(label='用户邮箱', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    photo=forms.ImageField(label='用户头像')

    def clean_phone(self):
        #获取数据
        data = self.cleaned_data['phone']
        if len(data) < 11:
            raise forms.ValidationError('手机号码必须是11位')#如果不满足条件报出异常
        else:
            return data#满足条件返回数据
