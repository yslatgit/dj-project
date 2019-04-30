#coding:utf-8
from django.db import models

#Bank-CardInfo  ---->  31 ForeignKey(一对多关系)
class Bank(models.Model):
    """银行信息"""
    bank_name = models.CharField(max_length=50,verbose_name="银行名称")
    city = models.CharField(max_length=30,verbose_name="银行所在城市")
    point = models.CharField(max_length=100,verbose_name="网点")

    class Meta:
        db_table = "Bank"
        verbose_name = "银行"
        verbose_name_plural = "银行管理"

    def __str__(self):
        return self.bank_name

class CardInfo(models.Model):
    """卡信息"""
    card_num = models.CharField(max_length=20,verbose_name="卡号")
    user = models.CharField(max_length=10, default="杨松林",verbose_name="用户")
    card_type = models.CharField(max_length=10,verbose_name="卡类型")
    info = models.ForeignKey(Bank,on_delete=models.CASCADE,verbose_name="选择银行",related_name="bank")

    class Meta:
        db_table = "Card"
        verbose_name = "卡号"
        verbose_name_plural = "卡号管理"

    def __str__(self):
        return self.card_num

#Auther-Book -----> 32 ManyToManyField(多对多关系)
class Auther(models.Model):
    """作者信息"""
    name = models.CharField(max_length=5,verbose_name="姓名")
    address = models.CharField(max_length=100,verbose_name="住址")

    class Meta:
        db_table = "Author"
        verbose_name = "作者"
        verbose_name_plural = "作者管理"

    def __str__(self):
        return self.name

class Book(models.Model):
    """书籍信息"""
    book_name = models.CharField(max_length=20,verbose_name="书名")
    author = models.ManyToManyField(Auther,verbose_name="作者")

    class Meta:
        db_table = "Book"
        verbose_name = "书籍"
        verbose_name_plural = "书籍管理"

    def __str__(self):
        return self.book_name

#   33 OneToOneField(一对一关系)
class CardInfoDetail(models.Model):
    """银行卡详细信息"""
    card = models.OneToOneField(CardInfo,on_delete=models.CASCADE,verbose_name="卡号")
    address = models.CharField(max_length=100,verbose_name="用户地址")
    phone = models.CharField(max_length=11,verbose_name="用户联系方式")

    class Meta:
        db_table = "CardInfoDetail"
        verbose_name = "持卡人详细信息"
        verbose_name_plural = "持卡人详细信息管理"

    def __str__(self):
        return self.card.user