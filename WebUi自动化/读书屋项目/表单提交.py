from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # 打开谷歌浏览器
url = 'http://novel.hctestedu.com/'
driver.get(url)
