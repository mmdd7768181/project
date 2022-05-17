import os
from selenium import webdriver

driver = webdriver.Chrome()
from time import sleep

driver.get(f"file://{os.getcwd()}/t1.html")  # 打开这个html网页

driver.find_element('id', 'alert').click()
sleep(2)
print(driver.switch_to.alert.text)
driver.switch_to.alert.accept()  # 确认
sleep(2)
driver.refresh()

driver.find_element('id', 'confirm').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()  # 取消
sleep(2)

driver.find_element('id', 'prompt').click()
print(driver.switch_to.alert.text)
sleep(2)
driver.switch_to.alert.send_keys('aaa')
driver.switch_to.alert.accept()

driver.switch_to.alert.accept()  # 确认
driver.switch_to.alert.dismiss()  # 取消
driver.switch_to.alert.send_keys()  # 发送信息
driver.switch_to.alert.text  # 获取弹窗的内容
