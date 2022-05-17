from selenium import webdriver
from selenium.webdriver.common.by import By
from WebUi自动化.POM封装.PageObject.dushuwu_index import DUshuwuIndex
from time import sleep


class DushuwuFlow(DUshuwuIndex):
    def dushuwu_search(self, selector, keyword): # 搜索操作
        self.open_dushuwu()
        self.type_send(selector, keyword)  # 输入搜索关键字
        sleep(1)
        self.click((By.ID, 'btnSearch'))
        sleep(1)
        result = self.get_page_title()
        return result

    def dushuwu_regist(self): # 尝试下~
        pass
