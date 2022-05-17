from selenium import webdriver
import pytest
from time import sleep


def test_01(browser):  # 调用了conftest里面的browser方法
    browser.get('http://novel.hctestedu.com/')
    sleep(2)
    t = browser.title
    # assert '读书' in t,'aa不存在'
    browser.quit()
