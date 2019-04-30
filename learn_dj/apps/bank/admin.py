#coding:utf-8
from django.contrib import admin
from .models import *

class MoreInfo(admin.TabularInline):
    model = CardInfoDetail
    #TabularInline（横向显示）---StackedInline（纵向显示）

class ControlBank(admin.ModelAdmin):
    #显示的字段
    list_display = ["bank_name","point","city"]

class ControlCardInfo(admin.ModelAdmin):
    # 显示的字段
    list_display = ["card_num", "card_type", "info","地址"]
    def 地址(self,obj):
        return obj.cardinfodetail.address
    #在card页面展示更多详细信息
    inlines = [MoreInfo]

class ControlAuthor(admin.ModelAdmin):
    list_display = ["name","address"]

class ControlBook(admin.ModelAdmin):
    list_display = ["book_name","作者"]
    def 作者(self,obj):
        return [a.name for a in obj.author.all()]

admin.site.register(Bank, ControlBank)
admin.site.register(CardInfo, ControlCardInfo)
admin.site.register(Auther, ControlAuthor)
admin.site.register(Book, ControlBook)