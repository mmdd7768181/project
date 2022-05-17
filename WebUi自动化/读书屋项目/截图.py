"""
运行自动化测试时，测试环境或者第三方环境正在重启而造成用例运行结果不稳定时，需要使用截图功能
get_screenshot_as_file(self,filename)
save_screenshot(self,filename)
filename 以图片格式结尾，如 png
driver.screenshot(filename.png) 也可以直接截元素图片
get_screenshot_as_base364() 截图的是一个文件流
"""


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import base64


driver = webdriver.Chrome()  # 打开谷歌浏览器
url = 'http://sz.ganji.com/'
driver.get(url)

driver.implicitly_wait(10)

pic_url=driver.get_screenshot_as_base64()
# print(pic_url)
img_date=base64.b64decode(pic_url)
file =open('base4.png', 'wb')
file.write(img_date)
file.close()

driver.quit()