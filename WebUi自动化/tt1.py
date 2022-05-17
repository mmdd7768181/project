from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.get('https://wenku.baidu.com/view/06a7dd34660e52ea551810a6f524ccbff021ca40.html')
# d1=driver.find_element_by(By.XPATH,'//*[@id="original-creader-canvas-1"]')
# d2=driver.find_element(By.XPATH,'//*[@id="original-creader-canvas-1"]')
print(driver.title)