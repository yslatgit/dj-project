#coding:utf-8
import requests

def req(method,url,params):
    if method == 'get':
        response = requests.get(url,params)
        return response.status_code
    elif method == 'post':
        response = requests.post(url,params)
        return response.status_code