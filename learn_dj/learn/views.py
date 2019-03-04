#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from learn.models import LEARN,User
# from templates import *
# Create your views here.

def index(request):
    context = {}
    context['name']='ysl'
    # return HttpResponse('HELLO WORLD!')
    return render(request,'index.html',context)

def test(request):
    return HttpResponse('TEST!')

def page(request):
    context={"name":"ysl","dj":"Django"}
    return render(request,'page.html',context)

def child(request):
    context={"abs_data":["selenium","appium","django"]}
    return render(request,'child.html',context)

def db_add(request):
    test1 = LEARN(name='ysl')
    test1.save()
    return HttpResponse('数据库添加数据成功！')

def default(request):
    return render(request,'form.html')

def add_user(request):

    try:
        name = User.objects.get(name=request.POST['user'])
        if name:
            return HttpResponse('该用户已存在！')
    except:
        test = User(name=request.POST['user'],pwd=request.POST['pwd'])
        test.save()
        return HttpResponse('添加用户信息成功！')

def delete_user(request,id):
    '''根据ID删除数据1.根据位置参数传递2.根据名称传递(?P<v1>\d+)'''

    test = User.objects.filter(id=id)
    test.delete()
    return HttpResponse('数据删除成功！')

def select_all(request):
    ret = User.objects.all()
    count = User.objects.count()

    ret1 = User.objects.values()
    context1 = {}

    print(count)
    # name_list = {"name":"['杨松林','杨松','大辅']"}
    context = {}
    name_list = []
    for i in ret:
        name_list.append(i.name)
    context['name']=name_list

    context1['data'] = list(ret1)
    context1['msg'] = '数据正常返回'
    context1['code'] = 200
    # return render(request,'all.html',context)
    # 返回字典类型的数据
    return JsonResponse(context1,safe=False)

def ajax(request):
    '''渲染ajax入口页面'''
    return render(request,'ajax2.html')

def ajax_action1(request):
    '''点击ajax修改内容按钮'''
    data = {}
    ret = User.objects.values()
    data['code'] = 200
    data['msg'] = '正常调用'
    data['data'] = list(ret)
    return JsonResponse(data,safe=False)

def ajax_action2(request,id):
    """输入字母出现联想词"""
    ret = User.objects.filter(id=id)
    code = ret[0].code
    ret1 = User.objects.filter(code=code)
    name_list = []
    for i in ret1:
        name_list.append(i.name)
        name_list.append(" ")
    return HttpResponse(name_list)