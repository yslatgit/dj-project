from django.test import TestCase
import requests,json

url = 'http://127.0.0.1:8000/learn/select_all/'
data = {'user':'松林','pwd':'12'}

# content--->返回二进制的数据
req = requests.get(url).content
#text--->返回str的数据
# 转义unicode码decode('unicode-escape')
print(req.decode('unicode-escape'))
