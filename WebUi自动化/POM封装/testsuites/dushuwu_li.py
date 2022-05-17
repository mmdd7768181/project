from selenium import webdriver
from selenium.webdriver.common.by import By
from WebUi自动化.POM封装.Flow.dushuwuflow import DushuwuFlow
from WebUi自动化.POM封装.Base.basepage import BasePage
from WebUi自动化.POM封装.Base.browser_driver import BrowserDriver
from WebUi自动化.POM封装.PageObject.dushuwu_index import DUshuwuIndex
from time import sleep


# driver=webdriver.Chrome()
# driver.get('http://novel.hctestedu.com/')

class TestDushuwuSearch():
    def dushuwu_1(self):
        browser = BrowserDriver()
        self.driver = browser.open_browser()
        dushuwu = DushuwuFlow(self.driver)
        result = dushuwu.dushuwu_search((By.ID,"searchKey"), "江少")
        assert result == '全部作品_读书屋'
        print('测试通过')


ts=TestDushuwuSearch()
ts.dushuwu_1()