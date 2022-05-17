"""
js ： 提供交互
css :提供样式功能
html ：提供框架
用 js 和 html 进行绑定，用 css 进行填充，形成一个完成的页面显示
"""
import time

"""
页面加载---加载资源：js,css,图片资源（gift,pnd等），数据资源（json)
页面渲染
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait  # 导入显性等待包
from selenium.webdriver.support import expected_conditions as EC  # 导入显性等待包

driver = webdriver.Chrome()
driver.get('http://shop-xo.hctestedu.com/')

# driver.implicitly_wait() # 隐形等待，只需要写一次，不会保证页面所有元素都可以加载完，等到这个时间点，就去执行下一步
# time.sleep()  # 强制等待，必须等待这么长的时间，然后执行下一步

# 显性等待
"""
等待元素达成某种要求，每次使用时都需要重新创建一个
1、找不到元素除法NotFound
2、每次找元素，应该有时间控制
3、找到元素就不找了

ps:元素的存在
1、存在于html中但没有显示出来
2、存在于html中且显示在界面中
3、find_element 寻找的对象是html，可能不会显示在html中
公约：页面元素如果不在界面中，则无法对其进行操作，如click，send_keys
"""

# by=''
# value=''
# defualt=True
# default_time=time.time()
#
# # 假设只等待3秒
# while defualt:
#     try:
#         ele=driver.find_element(by,value)
#         if ele.XXX=="XXX":
#             defualt=False
#     except ModuleNotFoundError:
#         last_time=time.time()
#
#         if last_time-default_time>3:
#             break
# 将上面的代码封装,再加上显性等待

# until :参考某个条件达成
# located :是元素定位的方式和值的元组/列表/包的形式
ele1 = WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator=('id', 'search-input')))


def aa(wait_time, locator, except_type, drivel, XXX):
    defualt = True
    default_time = time.time()
    while defualt:
        try:
            ele = driver.find_element(*locator)  # locator =by，value
            if ele.XXX == XXX:
                defualt = False
        except except_type:  # 异常类型
            last_time = time.time()

            if last_time - default_time > wait_time:
                break
