#coding:utf-8
from django.db import models

class Bank(models.Model):
    """银行信息"""
    bank_name = models.CharField(max_length=50,verbose_name="银行名称")
    city = models.CharField(max_length=30,verbose_name="银行所在城市")
    point = models.CharField(max_length=100,verbose_name="网点")

    class Meta:
        db_table = "Bank"
        verbose_name = "银行"
        verbose_name_plural = "银行"

    def __str__(self):
        return self.bank_name

class CardInfo(models.Model):
    """卡信息"""
    card_num = models.CharField(max_length=20,verbose_name="卡号")
    card_type = models.CharField(max_length=10,verbose_name="卡类型")
    info = models.ForeignKey(Bank,on_delete=models.CASCADE,verbose_name="选择银行")

    class Meta:
        db_table = "Card"
        verbose_name = "卡号"
        verbose_name_plural = "卡号"

    def __str__(self):
        return self.card_num

