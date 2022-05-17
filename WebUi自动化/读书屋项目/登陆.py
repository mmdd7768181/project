import requests
from PIL import Image
from selenium import webdriver
import pytesseract
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/')  # 网址必须要合法

# driver.maximize_window()  # 最大化窗口

print('------开始登录------')
driver.find_element_by_xpath('//*[@id="headerUserInfo"]/span/a[1]').click()
sleep(2)
driver.find_element_by_xpath('//*[@id="txtUName"]').send_keys(17621166752)
sleep(1)
driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('cm7768181')
sleep(1)
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()  # 点击登录
sleep(1)

assert '1762116' in driver.find_element_by_xpath('//*[@id="headerUserInfo"]/span/a[1]').text
print('登录成功')

ck=driver.get_cookies()

    # print(ck)
    # print(type(ck))

driver.quit()

"""
登录跳过验证码：
"""
