from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/') # 网址必须要合法


# ele1=driver.find_element_by_xpath('//*[@id="btnSearch"]')
# ele1.screenshot('ele1截图.png')

# ele2=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/label')
# ele2.screenshot('ele2截图.png')

# ele3=driver.find_element_by_xpath('//*[@id="searchKey"]')
# time.sleep(2)
# ele3.send_keys('江少')
# time.sleep(2)



# css 定位
# ele3=driver.find_element_by_css_selector('#searchKey')
# time.sleep(2)
# ele3.send_keys('斗破苍穹')
# time.sleep(2)

ele4=driver.find_element_by_xpath('//*[@id="navModule"]/li[4]/a')
# print(ele4.size)
print(ele4.text)
print(ele4.tag_name)
# driver.quit()
# print(ele4.location)
# print(ele4.parent)
# time.sleep(2)
# ele4.click()
# time.sleep(7)

# assert driver.find_element_by_xpath('//*[@id="bookList"]/tr/td[3]/a') != None
# print('测试通过')
# # //*[@id="bookList"]/tr/td[1]/i   //*[@id="bookList"]/tr[1]/td[1]/i
