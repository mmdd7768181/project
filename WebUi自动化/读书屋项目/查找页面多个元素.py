"""
1、功能测试用例 --移交自动化
2、自动化组 对用例进行筛选
3、编写脚本
4、转换成自动化用例
5、执行并输出测试报告

driver.find_elements_by_xx 获取同样条件下的一组元素
返回值是一个列表
"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 打开谷歌浏览器
url = 'http://novel.hctestedu.com/'
driver.get(url)

driver.implicitly_wait(30)
try:
    l1 = driver.find_element_by_xpath('//*[@id="topBooks1"]/dt/a')
    l1.click()
    time.sleep(2)
    assert driver.title != '读书屋_原创小说网站'
    print('title为{}'.format(driver.title))
    time.sleep(2)
    print('测试通过')
    driver.back()
    # time.sleep(2)
    # l2 = driver.find_elements_by_xpath('//*[@id="topBooks1"]/dd/a')
    # print('书本数量为{}'.format(len(l2)))
    # for i in range(len(l2)):
    #     # 来回的点击和返回网页 会使页面元素过期，导致报错，所以需要再次对l2进行赋值
    #     l2 = driver.find_elements_by_xpath('//*[@id="topBooks1"]/dd/a')
    #     time.sleep(2)
    #     l2[i].click()
    #     time.sleep(2)
    #     assert driver.title != '读书屋_原创小说网站'
    #     print('测试通过2')
    #     time.sleep(2)
    #     driver.back()


except Exception as e:
    print('出错了')
finally:
    driver.quit()