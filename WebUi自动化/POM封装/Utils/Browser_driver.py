import os
from selenium import webdriver
"""
封装浏览器引擎
"""

class BrowserDriver(object):
    def open_browser(self,browser):
        if "Chrome"==browser:
            driver=webdriver.Chrome()

        else:
            driver=webdriver.firefox()