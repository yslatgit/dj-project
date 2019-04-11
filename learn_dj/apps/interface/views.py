from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Apis
from django.core import serializers
# from .tests import post_main
import json

def get(request):
    data = {}
    name = request.GET.get('name')
    age = request.GET.get('age')
    data['firstname'] = name
    data['age-age'] = age
    print(data)
    return JsonResponse(data)

def test(request):
    res=None
    data = Apis.objects.filter(id=5).values()
    data = list(data)[0]
    url1 = data['apiurl']
    aaa1 = eval(data['apiparam'])
    print(url1,aaa1)
    url = "http://account.mofanghr.com/login.action"
    data = {'action':'login','account':'yangsonglin@mofanghr.com','password':'1234'}
    # res = post_main(url=url, data=data).text
    print(url,data)
    # res = post_main(url=url1,data=aaa1).text
    return HttpResponse(res)

def get_data(request):
    """获取测试数据"""
    # apiname = request.GET('apiname')
    data = Apis.objects.filter(apiname='login').values('apiurl','apimethod','apiparam','id')
    data_list=[]
    for i in data:
        print(i)
        data_item={}
        data_item['apiurl']=i['apiurl']
        data_item['apimethod']=i['apimethod']
        data_item['apiparam']=eval(i['apiparam'])
        data_item['id']=i['id']
        data_list.append(data_item)
    res_data = json.dumps(data_list,ensure_ascii=False)
    return JsonResponse(res_data,safe=False)


def change_casestatus(request,id):
    data = Apis.objects.get(id=id)
    data.apistatus = 1
    data.save()
    return HttpResponse("测试通过")

