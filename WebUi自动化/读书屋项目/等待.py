"""
隐形等待：implicitly_wait()
设置一个最长等待时间，如果在规定时间内 网页加载完成，则执行下一个操作
否则一直等到时间截止，才会执行下一步

显性等待：from selenium.webdriver.support.wait import WebDriverWait
class WebDriverWait(object):
    def __init__(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None):
poll_frequency：间隔时间，默认0.5s
ignored_exceptions：一旦发生了定义的异常，不会中断代码

until方法：def until(self, method, message=''):
method:在等待期间，每隔一段时间就调用当前方法，如果不能执行，返回 False,否则返回 true
message:如果超时，TimeoutException，把message传入异常

not until：当某条件不成立则继续进行
"""

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/')  # 网址必须要合法

# driver.implicitly_wait(30)#针对dricer设置等待时间
locator = (By.XPATH, '//*[@id="navModule"]/li[4]/a')  # 这里不可使用find_element方法
WebDriverWait(driver, 20).until(EC.presence_of_element_located(locator), '未获取到对应元素')
print('当前页面元素已被捕捉')
driver.quit()
