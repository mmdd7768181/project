from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class BrowserDriver(object):
    def open_browser(self):

        driver = webdriver.Chrome()
        return driver
