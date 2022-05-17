from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait  # 导入显性等待包
from selenium.webdriver.support import expected_conditions as EC  # 导入显性等待包

driver=webdriver.Chrome()
driver.get("http://shop-xo.hctestedu.com/")

driver.find_element(By.XPATH,'//*[@id="floor1"]/div[2]/div[2]/div[1]').click()
sleep(1)
h1=driver.current_window_handle() # 获取当前窗口句柄

driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[2]/div/div[2]/ul/li[2]/div').click()
sleep(1)


"""
//*[@id="1"]/div/div[1]/div[1]
//*[@id="6"]/div/div/h3/a
//*[@id="7"]/div/div[1]/h3/a
//*[@id="9"]/div/div[1]/h3/a
"""


# driver.find_element(By.XPATH,'//*[@id="3001"]/div/div/div/div[1]/h3/div/a').click()
# open_short=list()
# for i in as_:
#     print(i.get_attribute('text'))
#     # print(driver.window_handles)
#     open_short.append(i.get_attribute('text'))
#     i.click()
# switch_short=list()
#
# for i in driver.window_handles:
#     driver.switch_to.window(i)
#     print(driver.title)
#     switch_short.append(driver.title)
#
# print('打开的顺序', open_short)
# print('切换的顺序', switch_short)


# def get_baidu_top(keyword, num=5):
#     keyword = keyword.strip()
#     driver = webdriver.Chrome()
#     driver.get('https://www.baidu.com/')  # 打开百度
#     driver.find_element(By.ID,'kw').send_keys(keyword)  # 输入内容
#     driver.find_element(By.ID,'su').click()  # 点击
#     sleep(2)
#
#     index = 1
#     while index <= num:
#         index += 1
#         content = driver.page_source  # HTML内容
#         contentx = etree.HTML(content)  # lxml解析
#
#         c = contentx.xpath('//div[contains(@class, "c-container")]')
#
#         for i in c:
#             data = {
#                 'id': i.get('id'),  # 编号
#                 'title': ''.join(i.find('h3').itertext()).strip(),  # 标题
#             }
#             print(data)
#
#         if index != num:
#             sleep(2)
#             pc = driver.find_elements(By.CLASS_NAME,'pc')  # 跳转页面按钮
#             pc[index].click()  # 点击下一页
#             sleep(5)
#
#
# if __name__ == '__main__':
#     keyword = input('input keyword ->  ')
#     print()
#     get_baidu_top(keyword)