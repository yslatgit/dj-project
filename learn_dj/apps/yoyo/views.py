from django.shortcuts import render
from django.views.generic import View
from learn.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.core.mail import send_mail
import json
from learn_dj import settings
from utils.email_send import send_user_email
# Create your views here.

class Dj15View(View):
    def get(self,request,type):
        type = int(type)
        if type == 1:
            a = User.objects.all()
            data = {}
            data["result"] = json.loads(serializers.serialize("json",a))
            return JsonResponse(data)
        else:
            data = {}
            rows = {}
            rets = User.objects.all().values('name','pwd')
            # rets = User.objects.all()
            count = rets.count()
            # for i in rets:
            #     rows["name"] = i.name
            #     rows["pwd"] = i.pwd
            #     data
            data["data"] = list(rets)
            data["count"] = count
            return JsonResponse(data,safe=False)

class Dj16View(View):
    """接口返回中文编码"""
    def get(self,request):
            data = {}
            rets = User.objects.all().values('name','pwd').order_by('-name').distinct()
            count = rets.count()
            data["data"] = list(rets)
            data["count"] = count
            return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii':False})

class Dj27View(View):
    """重置密码"""
    def get(self,request):
        return render(request,'yoyo/change_pwd.html')

    def post(self,request):
        username = request.POST.get('username')
        pwd1 = request.POST.get('password')
        is_user_exist = User.objects.filter(name=username)
        if is_user_exist:
            pwd = User.objects.get(name=username).pwd
            is_pwd_match = check_password(pwd1,pwd)
            if is_pwd_match:
                pwd2 = request.POST.get('password2','')
                pwd3 = request.POST.get('password3','')
                if pwd2 == pwd3:
                    if pwd == pwd2:
                        return render(request,'yoyo/change_pwd.html',{'msg':'新旧密码一致！'})
                    else:
                        user = User.objects.get(name=username)
                        user.pwd = make_password(pwd3)
                        user.save()
                        return render(request,'yoyo/change_pwd.html',{'msg':'修改成功！'})
                else:
                    return  render(request,'yoyo/change_pwd.html',{'msg':'新密码不一致！'})
            else:
                return render(request,'yoyo/change_pwd.html',{'msg':'密码错误！'})
        else:
            return render(request,'yoyo/change_pwd.html',{'msg':'用户名不存在！'})

class Dj28View(View):
    """发送邮件"""
    def get(self,request):
        send_user_email()
        return HttpResponse('邮件发送成功！')
