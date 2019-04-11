#coding:utf-8
"""获取测试数据"""
import requests
import json

def post_main(url,data=None):
    # cookie_jar = RequestsCookieJar()
    # cookie_jar.set("JSESSIONID","=D63D805C2C60A3FA5C2FF7530A1B36D1")
    # cookie_jar.set("accountToken","=yangsonglin@mofanghr.com|A2F2220D9F4B86EB283410E03A6C88D6")
    res = requests.get(url,data)
    return res

def data():
    url='http://127.0.0.1:8000/interface/get_data/'
    res = requests.get(url).json()
    res = json.loads(res)
    data_list = []
    for i in res:
        data_list.append([i['apiurl'],i['apimethod'],i['apiparam'],str(i['id'])])
    print(data_list)
    return data_list

def get(id):
    url = 'http://127.0.0.1:8000/interface/change_data/%s'%id
    requests.get(url)














if __name__ == '__main__':
    data()