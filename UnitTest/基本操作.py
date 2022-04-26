from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class Test01(unittest.TestCase):
    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    def test_1(self):
        print('a')

    def test_2(self):
        print('b')

    def c(self):
        print('c')


# Test01().setUp()

if __name__ == '__main__':
    unittest.main()
"""
执行结果如下：
setup
a
teardown
setup
b
teardown

即：setup和teardown会出现在每个用例的前后端
注意：unittest只会自动执行 test_ 命名的方法，不过可以在正确命名的方法里调用该不正规命名的方法
"""
