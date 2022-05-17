from selenium import  webdriver
import time

from selenium.webdriver.common.by import By
"""
/html/body/header/div/div/ul/li[2]/a
"""
driver = webdriver.Chrome()
driver.get('http://shop-xo.hctestedu.com/') # 网址必须要合法

# css 属性过滤
# el=driver.find_element_by_css_selector('html>body>header>div>div>ul>li>a[class=am-dropdown-toggle]')
# el.screenshot('css截图2.png')

# xpath 属性过滤，网址：https://www.runoob.com/xpath
el=driver.find_element_by_xpath('//a[@class=am-dropdown-toggle ]')
el.screenshot('xpath截图1.png')
