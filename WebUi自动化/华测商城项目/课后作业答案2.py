# -*- coding: utf-8 -*-
# author: 华测-长风老师
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

start_time = time.strftime("%Y%m%d%H%M%S")
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(20)
driver.get("http://shop-xo.hctestedu.com/")
goods_locator = (By.XPATH, '//*[@id="floor1"]/div[2]/div[2]/div/div/div/a')
goods_elements = driver.find_elements(*goods_locator)

goods_open_list = list()
price_list = list()
goods_name_list = list()

for i in goods_elements:
    goods_name_list.append(i.text)
    i.click()
    driver.switch_to.window(driver.window_handles[-1])
    ele = driver.find_element(By.CSS_SELECTOR, ".detail-title")
    ele_price = driver.find_element(By.CSS_SELECTOR, ".stock")
    goods_open_list.append(ele.text)
    price_list.append(ele_price.get_attribute("data-original-stock"))
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

print(goods_open_list, "\n", goods_name_list)
print(goods_open_list == goods_name_list)
print(list(zip(goods_open_list, price_list)))

end_time = time.strftime("%Y%m%d%H%M%S")
print(f"总耗时：{int(end_time) - int(start_time)}")
