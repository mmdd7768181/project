from selenium import  webdriver
import time

from selenium.webdriver.common.by import By
"""
selenium官网规定标签名必须是select，但目前大多数公司都会自定义名称
所以需要定位多个元素返回元素列表，再使用属性过滤确定元素对象
定位其上层元素，然后使用元素内定位，找到想要的元素对象
"""
driver = webdriver.Chrome()
driver.get('http://shop-xo.hctestedu.com/') # 网址必须要合法