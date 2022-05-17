from selenium import  webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://shop-xo.hctestedu.com/') # 网址必须要合法
"""
find_element（by,value）中的by可以使用By.XXX来代替,比如By.NAME
"""


# 通过id定位
# ele_id=driver.find_element(by='id',value='search-input') # 方法1
# ele_id=driver.find_element(By.ID,'search-input') # 方法2
# ele_id=driver.find_element_by_id('search-input') # 方法3

# ele_id.send_keys('手机','壳') # 对元素进行写的方法

# 通过name定位
# ele_name=driver.find_element(by='name',value='wd')  # 方法1
# ele_name=driver.find_element_by_name('wd') # # 方法2
# ele_name.send_keys('手机','壳') # 对元素进行写的方法

#通过class name 定位
# ele_class_name=driver.find_element(by='class name',value='submit am-btn') #class name有2个属性值
# ele_class_name=driver.find_element(by='class name',value='submit') # 方法1：class name有2个属性值，但只需要前一个
# ele_class_name=driver.find_element_by_class_name('submit') # 方法2
# ele_class_name.screenshot('bbb.png')

# 通过tag_name定位
# ele_tag_name=driver.find_element(by='tag_name',value='')
# ele_tag_name=driver.find_element_by_tag_name('')

# 通过link text 定位，定位的是a标签中的文本链接（text 属性），不用管标签
# ele_link_text=driver.find_element(By.LINK_TEXT,'登录')
ele_link_text=driver.find_elements_by_link_text('登录')
print(len(ele_link_text))
# ele_link_text.click()
# driver.quit()
# print('操作成功')

# 通过partial_link_text 定位 link text的模糊匹配
# ele_partial_link_text=driver.find_elements_by_partial_link_text('总裁')


"""
路径定位：相对路径和绝对路径
css的路径与xpath相同，只是符号不一样，css用> ，xpath用/
"""
# 通过css定位,使用标签名表示层级名称，即当前路径名称，使用>符号来表示路径：html>body>div[3]>div>div[3]>form>div>input
# ed=driver.find_elements_by_css_selector('')

#通过xpath定位，html/body/div[3]/div/div[3]/form/div/input
# ele_xpath=driver.find_element_by_xpath('html/body/div[3]/div/div[3]/form/div/input') # 绝对路径
# ele_xpath=driver.find_element_by_xpath('//search-input') #相对路径 ，//表示忽略前面所有的层级
# ele_xpath.screenshot('xpath截图.png')
# ele_xpath.screenshot('xpath截图2')

#<a href="http://hctestedu.com" target="_blank" title="华测教育官网">华测教育官网</a>