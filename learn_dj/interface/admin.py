#coding:utf-8
from django.contrib import admin
from .models import *

@admin.register(Apis)
class ControlApis(admin.ModelAdmin):
    #设置要显示在列表中的字段
    list_display = ["apiname","apiurl","apimethod","apiresult","apistatus","create_time"]
    #设置每页显示的条数，默认显示100条
    list_per_page = 2
    #操作项功能显示的位置
    actions_on_top = True
    # actions_on_bottom = True
    #字段为空的项显示的内容
    empty_value_display="-空白-"

    admin.site.site_header = '杨松林后台管理'
    admin.site.site_title = '杨松林'

@admin.register(Types)
class ConrrolTypes(admin.ModelAdmin):
    empty_value_display = "-空白-"
    list_display = ["name","types","email","email2","ip","create_time","update_time"]
# admin.site.register(Apis,ControlApis)
