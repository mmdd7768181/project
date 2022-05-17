from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')  # 网址必须要合法

time.sleep(3)  # 人工操作新建一个标签页
driver.close()  # 关闭标签页，关闭的是driver的实例
driver.quit()  # 退出浏览器
driver.back()  # 后退
driver.forward()  # 前进
driver.refresh()  # 刷新浏览器
driver.maximize_window()  # 最大化窗口
driver.fullscreen_window() # 全屏显示
driver.current_url  # 对url获取后再进行判断
driver.title  # 对title获取后再进行判断
driver.set_window_size(100,500)  # 设置窗口大小
driver.set_window_position(100,500)  # 设置窗口位置
driver.set_window_rect(100,200,300,400) # 同时设置大小和位置，100和200是位置，300和400是大小
driver.switch_to.new_window('tab')# 打开新标签
driver.switch_to.new_window('window') # 打开新窗口


driver.find_element_by_xpath('').get_attribute('属性名')  # 通过传入不同的属性名来回去对应的属性值
driver.find_element_by_xpath('').location  # 获取元素坐标
driver.find_element_by_xpath('').text  # 获取文本信息，如果是标签中的value值，不可用此种方法来获取
driver.find_element_by_xpath('').size  # 获取元素的尺寸

# 开启无头模式
options=webdriver.ChromeOptions()
options.headless=True
driver = webdriver.Chrome(options=options)

driver.set_script_timeout() # 设置所有资源的加载时间