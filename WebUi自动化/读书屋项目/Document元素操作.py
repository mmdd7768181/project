import requests
from PIL import Image
from selenium import webdriver
import pytesseract
from selenium.webdriver.common.by import By
from time import sleep
import json

"""
windows.open(url) # js 打开窗口
windows.close() # js 关闭窗口
"""

driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/')  # 网址必须要合法

# js1='windows.open("http://novel.hctestedu.com/")'
# driver.execute_script(js1)
# js = "window.open('http://novel.hctestedu.com/')"
# driver.execute_script(js)

# print(driver.execute_script(js1))
sleep(1)
# js 元素定位跟selenium相同

# id元素定位
# js_id="document.getElementById('searchKey').value='365'"  # 固定写法
# driver.execute_script(js_id)

# #name元素定位
# js_class="document.getElementByName('searchKey')[0].value='江少'"
# driver.execute_script(js_class)
#
# #class元素定位
# js_class="document.getElementByClassName('s_int')[0].value='江少'"
# driver.execute_script(js_class)

# css定位
# js_class="document.querySelector('#searchKey')"
# driver.execute_script(js_class)

# #点击操作
# js_click="document.getElementById('btnsearch')[0].click()'"
# driver.execute_script(js_click)

# 直接定位元素
# js = 'document.querySelector("#navModule > li:nth-child(2) > a").style.display="none"'
# driver.execute_script(js)

# 滑动网页进度条
js ="window.scrollTo(0,document.body.scrollHeight)"
sleep(6)
driver.execute_script(js)

driver.quit()
