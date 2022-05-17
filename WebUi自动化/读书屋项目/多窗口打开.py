"""
selenium 在点击某个链接时，某些情况下会生成一个tab页，也就是窗口，此时需要进行多窗口切换处理
句柄：每个窗口都有一个属性，使用 handle 去标识该窗口，即程序聚焦在哪个窗口
使用 current_windows_handle 来获取当前窗口的句柄
使用 driver.window_handles 来获取当前窗口所有的的句柄
使用 switch_to.window 来切换句柄
"""


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 打开谷歌浏览器
url = 'http://sz.ganji.com/'
driver.get(url)

driver.implicitly_wait(5)
time.sleep(1)
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/a/img').click()

print(driver.title)
handle1=driver.current_window_handle # 获取当前窗口的句柄
handles=driver.window_handles
print('当前页面句柄为{}'.format(handle1))
print('当前页面所有句柄为{}'.format(handles))

driver.switch_to.window((handles[1])) #  切换句柄
print('切换句柄后的title是{}'.format(driver.title))
driver.close()
print('当前标题是{}'.format(driver.title))  # 运行关闭后的窗口 会报错




# print('当前页面2句柄为{}'.format(handle2))
# print('当前页面所有句柄为{}'.format(handles))

# ele2=driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div[2]/a[1]').click()
# time.sleep(2)
# ele2.screenshot('截图1.png')
# print(driver.title)
# driver.close()
# time.sleep(2)
# driver.switch_to.window(handle1) # 切换句柄
# print('关闭窗口，切换句柄，打印当前标题{}'.format(driver.title))

time.sleep(2)
# ele1.click()
# print(driver.title)
# time.sleep(2)


# driver.quit()