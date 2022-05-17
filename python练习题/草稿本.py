# while True:
#     f0 = 0
#     f1 = 1
#     f2 = 2
#     if n <= 0:
#         print('有{}种方法'.format(f0))
#     elif n == 1:
#         print('有{}种方法'.format(f1))
#     elif n == 2:
#         print('有{}种方法'.format(f2))
#     else:
#         fn = 0
#         for i in range(3, n + 1):
#             fn = f1 + f2
#             f1 = f2
#             f2 = fn
#         print('有{}种方法'.format(fn))
#     n = int(input('请输入n的值'))
#

# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
#
# # For W3C actions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions import interaction
# from selenium.webdriver.common.actions.action_builder import ActionBuilder
# from selenium.webdriver.common.actions.pointer_input import PointerInput
#
# caps = {}
# caps["appium:deviceName"] = "emulator-5554"
# caps["appium:platformName"] = "Android"
# caps["appium:platformVersion"] = "7.1.2"
# caps["appium:newCommandTimeout"] = 3600
# caps["appium:connectHardwareKeyboard"] = True
#
# driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
#
# el5 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="拼多多")
# el5.click()
# el6 = driver.find_element(by=AppiumBy.ID, value="com.xunmeng.pinduoduo:id/exo")
# el6.click()
# el8 = driver.find_element(by=AppiumBy.ID, value="com.xunmeng.pinduoduo:id/g3r")
# el8.click()
# el9 = driver.find_element(by=AppiumBy.ID, value="com.xunmeng.pinduoduo:id/ee4")
# el9.click()
#
# driver.quit()

# import pyecharts
from pyecharts.charts import Bar
from pyecharts import options

# //导入柱状图-Bar

# //设置行名
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# //设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# //设置柱状图的主标题与副标题
bar = Bar("柱状图", "一年的降水量与蒸发量")
# //添加柱状图的数据及配置项
bar.add("降水量", columns, data1, mark_line=["average"], mark_point=["max", "min"])
bar.add("蒸发量", columns, data2, mark_line=["average"], mark_point=["max", "min"])
# //生成本地文件（默认为.html文件）
bar.render()

# //导入饼图Pie
# from pyecharts.charts import Pie
# # //设置主标题与副标题，标题设置居中，设置宽度为900
# pie = Pie("饼状图", "一年的降水量与蒸发量",title_pos='center',width=900)
# # //加入数据，设置坐标位置为【25，50】，上方的colums选项取消显示
# pie.add("降水量", columns, data1 ,center=[25,50],is_legend_show=False)
# # //加入数据，设置坐标位置为【75，50】，上方的colums选项取消显示，显示label标签
# pie.add("蒸发量", columns, data2 ,center=[75,50],is_legend_show=False,is_label_show=True)
# # //保存图表
# pie.render()