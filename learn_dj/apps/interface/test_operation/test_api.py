#coding:utf-8
"""测试类"""
import unittest
import paramunittest

@paramunittest.parametrized(*login_data)
class Api(unittest.TestCase):

    pass