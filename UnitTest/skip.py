from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

"""
对于不需要执行或者需要在特定条件下才会运行的case 使用skip方法

"""

condition = True


class Test04(unittest.TestCase):

    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    @unittest.skip('不执行此用例1')
    def test_1(self):
        print('a')

    @unittest.skipIf(condition, '此用例不执行')
    def test_2(self):
        print('b')

    def test_3(self):
        contition = False

    def test_4(self):
        print('test_4')


# Test01().setUp()

if __name__ == '__main__':
    unittest.main()
