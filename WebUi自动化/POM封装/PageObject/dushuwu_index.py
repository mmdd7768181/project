from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from WebUi自动化.POM封装.Base.basepage import BasePage

"""
封装读书屋首页
1、打开读书屋
2、搜索关键词--江少
3、获取title--判断属性与预期是否一致

页面类：
封装在当前页面或者这个流程上的基本方法
便于后续的复用以及维护
"""


class DUshuwuIndex(BasePage):
    def open_dushuwu(self):
        self.get_url('http://novel.hctestedu.com/')

    def type_send(self, selector, text):
        self.text_send(selector, text)

    def click(self, selector):
        self.click_option(selector)

driver=webdriver.Chrome()
driver.find_element