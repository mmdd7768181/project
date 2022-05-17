from selenium import  webdriver
import time
driver1 = webdriver.Chrome()  # 实例1
driver2 = webdriver.Chrome()  # 实例2
driver3 = webdriver.Chrome()  # 实例3

# driver1 打开的浏览器，2,3都不能去操作，因为他们是在不同的线程中

driver1.get('http://www.baidu.com')
driver2.close()  # 线程不会销毁
driver3.quit()   # 线程会销毁，内存回收
