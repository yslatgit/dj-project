#coding:utf-8
from django import forms

class UserForm(forms.Form):
    username = forms.CharField(required=True,min_length=2,max_length=4,
                           error_messages={'required':'参数必填','min_length':'字数小与2','max_length':'字数大于4'})
    password = forms.CharField(required=True,max_length=6,
                          error_messages={'required':'参数必填','max_length':'密码长度过长'})