
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 打开谷歌浏览器
url = 'http://sz.ganji.com/'
driver.get(url)

driver.implicitly_wait(10)
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/a/img').click()
# print(driver.current_url)
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/a/img').click()
# print(driver.current_url)
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/a/img').click()
# print(driver.current_url)
# time.sleep(1)
handle1=driver.current_window_handle # 获取当前窗口的句柄
print('当前页面句柄为{}'.format(handle1))

handles=driver.window_handles
# print('当前页面所有句柄为{}'.format(handles))
time.sleep(3)
print(handles[1])
#
driver.switch_to.window((handles[3])) #  切换句柄1
print(handles[3])
# print(driver.current_url)
# driver.switch_to.window((handles[2])) #  切换句柄2
# print(driver.current_url)
# driver.switch_to.window((handles[3])) #  切换句柄3
# print(driver.current_url)
# time.sleep(3)



driver.close()
# print('当前标题是{}'.format(driver.title))  # 运行关闭后的窗口 会报错