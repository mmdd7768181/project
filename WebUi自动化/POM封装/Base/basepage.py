"""

POM:页面对象模型，减肥繁琐的操作封装到POM中，只对外提供必要的接口操作，是一种封装思想
核心思想是分层，实现松耦合，实现脚本的重复利用，实现脚本的易维护性
page 页面
object 对象
model 模型

基础层（BasePage）：封装基础的selnium原生的api方法，元素定位，框架跳转等
PO层（PageClass）：元素定位，获得元素对象，页面操作，主要是操作层面
测试用例层（Testcase）：业务逻辑层，数据驱动 三者的关系：PO层继承基础层，测试用例层调用PO层

ps：当前的 Base 包会将所有的基础操作，如打开关闭浏览器、点击、输入等，不会改变的逻辑进行封装
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        # self.driver=webdriver.Chrome()
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()

    # 获取元素
    def findElement(self, selector):
        ele = self.driver.find_element(*selector)  # 解包的概念
        return ele

    # 输入字符
    def text_send(self, selector, text):
        ele = self.findElement(selector) # 调用了上面的findElement方法
        ele.clear()
        ele.send_keys(text)

    # 清空
    def clear(self, selector):
        ele = self.findElement(selector)
        ele.clear

    # 点击
    def click_option(self, selector):
        ele = self.findElement(selector)
        ele.click()

    # 获取页面title
    def get_page_title(self):
        return self.driver.title

    # 获取页面url断言
    def get_page_url(self):
        return self.driver.current_url

    # 切换到新的窗口
    def switch_handle(self, num):
        handles = self.driver.window_handles

        self.driver.switch_to.window(handles[num])
