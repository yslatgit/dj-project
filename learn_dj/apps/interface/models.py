#coding:utf-8
from django.db import models

class Apis(models.Model):
    apiname = models.CharField('接口名称',max_length=30)
    apiurl = models.CharField('接口地址',max_length=200)
    apiparam = models.CharField('请求参数',max_length=800)
    apimethod = models.CharField('请求方法',max_length=100)
    apiresult = models.CharField('预期结果',max_length=200)
    apistatus = models.BooleanField('是否通过')
    create_time = models.DateTimeField('创建时间',null=True)
    depend_case = models.ForeignKey(to='self',null=True,blank=True,on_delete=models.SET_NULL)
    # depend_case = models.ForeignKey('self',to_field='id',null=True,blank=True,on_delete=models.SET_NULL,default=1)

    def __str__(self):
        return "%s"%self.id

    class Meta:
        verbose_name='简历流转接口'
        verbose_name_plural='接口管理'

class Types(models.Model):
    types_id = models.IntegerField(primary_key=True,default=1,verbose_name='主键')
    TYPE_CHOICES = ((0,'超级管理员'),(1,'管理员'),(2,'导师'),(3,'成员'),(4,'游客'))
    name = models.CharField(max_length=20,verbose_name='名称')
    email = models.EmailField(max_length=30,null=True,blank=True)
    email2 = models.EmailField(max_length=30,default='yangsonglin@qq.com')
    ip = models.GenericIPAddressField(protocol='ipv4',null=True,blank=True)
    types = models.IntegerField(default=4,help_text='选择用户类型的编号',verbose_name='用户类型',choices=TYPE_CHOICES)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)

    class Meta:
        verbose_name='人员'
        verbose_name_plural='人员管理'