#coding:utf-8
from django.contrib import admin
from .models import *


class ControlBank(admin.ModelAdmin):
    #显示的字段
    list_display = ["bank_name","point","city"]

class ControlCardInfo(admin.ModelAdmin):
    # 显示的字段
    list_display = ["card_num", "card_type", "info"]

admin.site.register(Bank, ControlBank)
admin.site.register(CardInfo, ControlCardInfo)