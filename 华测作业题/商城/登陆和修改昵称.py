from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait  # 导入显性等待包
from selenium.webdriver.support import expected_conditions as EC  # 导入显性等待包
import random

driver = webdriver.Chrome()
driver.get('http://shop-xo.hctestedu.com/')
# print('第1处driver的值为',driver)

# driver.maximize_window()
# sleep(1)
# 开始登录
driver.find_element(By.XPATH, '/html/body/div[2]/div/ul[1]/div/div/a[1]').click()
sleep(0.5)

# 输入账号密码并登录
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input').send_keys('cm7768181')
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input').send_keys('cm5201314')
driver.find_element(By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button').click()


# ele1 = WebDriverWait(driver, 3).until(EC.presence_of_element_located(locator=(By.CLASS_NAME, 'menu-hd')))
# ele1.click()

# search_ele = driver.find_element(By.ID, "search-input")  # 定位页面元素：搜索输入框
# search_ele.send_keys("手机")  # 在页面元素：搜索输入框 中输入内容
# search_button = driver.find_element(By.ID, "ai-topsearch")  # 定位页面元素： 搜索按钮
# search_button.click()  # 点击页面元素：搜索按钮
#
#
# print('第3处driver的值为',driver)  # 输入False，切换页面后driver值改变了，无法再用此方法定位

# 进入个人中心的个人资料页面
sleep(2)  # 必须要加等待，不然必报错
# driver.find_element(By.CLASS_NAME, 'menu-hd').click()
driver.find_element(By.XPATH,'/html/body/div[2]/div/ul[2]/div[1]/div/a/span').click()

# driver.find_element(By.XPATH, '/html/body/div[2]/div/ul[2]/div[1]/div/a/span').click()
sleep(0.5)
driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div[1]/div[1]/div[2]/a[2]').click()
sleep(0.5)
driver.find_element(By.XPATH,"/html/body/div[4]/div[3]/div/legend/a").click()
sleep(0.5)

# 修改资料
driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/form/div[1]/input').clear()
sleep(1)
driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/form/div[1]/input').send_keys('庐江令狐冲3')
sleep(0.5)

"""
当定位到多个元素，若使用的是find_element,返回的是第一个元素
若使用的是find_elements，则返回一个元素对象的列表

"""
eles=driver.find_elements(By.XPATH,'/html/body/div[4]/div[3]/div/form/div[2]/div/label[2]/span/i[2]')
for i in eles:
    i.screenshot(f"性别选项{eles.index(i)}.png")

ele3=eles[-1]
ele3.click()
sleep(1)


# 生日定位
"""
frame
"""

driver.find_element(By.NAME,'birthday').click()
sleep(2)
frame_ele=driver.find_element(By.XPATH,'/html/body/div[8]/iframe')
driver.switch_to.frame(frame_ele) # 进入frame

driver.find_element(By.ID,'dpTodayInput').click() # 选择日期

driver.switch_to.parent_frame()  # 从frame操作后 必须要出来
driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/form/div[4]/button').click()
sleep(3)
print('完成')

driver.quit()