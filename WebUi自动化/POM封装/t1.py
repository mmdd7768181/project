from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# # from WebUi自动化.POM封装.t2 import open_dushuwu



class aa(object):
    driver = webdriver.Chrome()


    def get_url(self,url):
        # self.driver=webdriver.Chrome()
        self.driver.get(url)
    def open_dushuwu(self):

        self.get_url('http://novel.hctestedu.com/')

q=aa()
q.open_dushuwu()
