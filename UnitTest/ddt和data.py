from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest
from ddt import ddt, data,unpack

@ddt()
class Test02(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://novel.hctestedu.com/')

    def tearDown(self) -> None:
        sleep(4)
        self.driver.quit()

    @data('江少', '宠')  # 以元组的方式，将江少,宠 依次传递给txt，并分别运行
    def test_1(self, txt):
        search_input = self.driver.find_element_by_id('searchKey')
        search_input.send_keys(txt)

    @data(('江少', '宠'), ('霸道', '爱'))
    @unpack # 装饰器，用来解data包内的值。适用于需要传多个参数时的解包操作
    def test_1(self, txt,txt1):
        print(txt)
        print(txt1)

    def test_2(self):
        print('b')

    def c(self):
        print('c')


# Test01().setUp()

if __name__ == '__main__':
    unittest.main()
