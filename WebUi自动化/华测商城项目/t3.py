from time import sleep

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait  # 导入显性等待包
from selenium.webdriver.support import expected_conditions as EC  # 导入显性等待包

from selenium.webdriver.support.relative_locator import locate_with, with_tag_name

driver = webdriver.Chrome()
# driver.get("http://shop-xo.hctestedu.com/")  # 使用浏览器实例对象driver去打开一个网址


# driver.set_script_timeout(3)
# driver.get("http://www.baidu.com/")
# driver.get("http://shop-xo.hctestedu.com/")
# driver.fullscreen_window()
# driver.set_window_rect(100,200,300,400)


driver.switch_to.new_window('tab')# 打开新标签
driver.get("http://www.baidu.com/")
driver.switch_to.window(driver.window_handles[0])
print(driver.title)
sleep(1)

driver.switch_to.new_window('tab') # 打开新窗口
driver.get("http://shop-xo.hctestedu.com/")
sleep(1)
driver.switch_to.window(driver.window_handles[1])
print(driver.title)

driver.quit()