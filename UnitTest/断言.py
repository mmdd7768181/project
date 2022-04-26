from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest


class Test01(unittest.TestCase):
    # def setUp(self) -> None:
    #     print('setup')
    #
    # def tearDown(self) -> None:
    #     print('teardown')

    def test_1(self):
        print('a')
        self.assertEqual('1', '2', msg='不一致')

    # def test_2(self):
    #     print('b')
    #
    # def c(self):
    #     print('c')


if __name__ == '__main__':
    unittest.main()
