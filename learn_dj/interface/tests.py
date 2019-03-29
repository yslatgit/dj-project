from django.test import TestCase
import requests
import unittest


def get(url,data=None):
    res = requests.get(url,data)
    return res.text

class myTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'http://127.0.0.1:8000/interface/get/'
        cls.data = {"name": "ysl", "age": "200"}
        print("start test")

    @classmethod
    def tearDownClass(cls):
        print("end test")

    def test_a(self):
        print('a')
        res = get(self.url,self.data)
        print(res)

    # @unittest.skip
    def test_b(self):
        print('b')
        res = get(self.url,self.data)
        print(res)

if __name__ == '__main__':
    # url = 'http://127.0.0.1:8000/interface/get/'
    # data = {"name":"ysl","age":"200"}
    # print(get(url,data))
    # suite= unittest.TestSuite()
    # # suite.addTest(myTest('test_b'))
    # # suite.addTest(myTest('test_a'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    pass