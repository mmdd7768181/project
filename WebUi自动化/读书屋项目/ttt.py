from selenium import webdriver
import requests
import pytesseract
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/')  # 网址必须要合法

driver.find_element_by_xpath('//*[@id="headerUserInfo"]/span/a[2]').click()
sleep(2)

driver.find_element_by_xpath('//*[@id="btnRegister"]').click() # 点击注册按钮
sleep(2)

# print(a)
assert "手机号不能为空" in driver.find_element_by_xpath('//*[@id="LabErr"]').text
print('测试通过')

driver.quit()