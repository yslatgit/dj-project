# from django.test import TestCase
# import requests
# from requests.cookies import RequestsCookieJar
# import unittest
#
#
#
# # class myTest(unittest.TestCase):
# #
# #     @classmethod
# #     def setUpClass(cls):
# #         cls.url = 'http://127.0.0.1:8000/interface/get/'
# #         cls.data = {"name": "ysl", "age": "200"}
# #         print("start test")
# #
# #     @classmethod
# #     def tearDownClass(cls):
# #         print("end test")
# #
# #     def test_a(self):
# #         print('a')
# #         res = get(self.url,self.data)
# #         print(res)
# #
# #     # @unittest.skip
# #     def test_b(self):
# #         print('b')
# #         res = get(self.url,self.data)
# #         print(res)
#
#
#
#
# if __name__ == '__main__':
#     # url = 'http://127.0.0.1:8000/interface/get/'
#     # data = {"name":"ysl","age":"200"}
#     # print(get(url,data))
#     # suite= unittest.TestSuite()
#     # # suite.addTest(myTest('test_b'))
#     # # suite.addTest(myTest('test_a'))
#     # runner = unittest.TextTestRunner()
#     # runner.run(suite)
#     url = "http://account.mofanghr.com/login.action"
#     data = {'action':'login','account':'yangsonglin@mofanghr.com','password':'1234'}
#     print(post_main(url=url,data=data).text)

#coding:utf-8
"""测试类"""
import requests
import unittest
import paramunittest
from data_for_test import *


login_data = data()

@paramunittest.parametrized(*login_data)
class ApiTest(unittest.TestCase):
    def setParameters(self,apiurl,apimethod,apiparam,key):
        self.apiurl=apiurl
        self.apimethod=apimethod
        self.apiparam=apiparam
        self.key=key

    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

    def test_login(self):
        if self.apimethod == 'post':
            res = post_main(url=self.apiurl,data=self.apiparam).text
            print(res)
            if '杨松林'in res:
                get(self.key)
        else:
            print("测试方法不对")


if __name__ == '__main__':
    unittest.main()
    # url = "http://account.mofanghr.com/login.action"
    # data = {'action':'login','account':'yangsonglin@mofanghr.com','password':'1234'}
    # print(post_main(url=url,data=data).text)