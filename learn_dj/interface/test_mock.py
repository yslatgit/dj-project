#coding:utf-8
from unittest import mock
import requests

def mk(url):
    return requests.get(url).json()


def test(response_data,url):
    mk = mock.Mock(response_data)
    return mk(url)

if __name__ == '__main__':
    # url = 'http://127.0.0.1:8000/interface/get/'
    # data = {"mock":mock}
    # print(test(response_data=data,url=url))
    url = 'http://127.0.0.1:12345/mock'
    print(mk(url))
