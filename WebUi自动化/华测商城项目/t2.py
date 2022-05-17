# -*- coding: utf-8 -*-

# author: 华测-长风老师


"""

元素定位课后作业内容：



需要用的的内容：

华测教育商城网址：http://shop-xo.hctestedu.com/

请使用python+selenium构建一个脚本实现以下内容：



1、完成登录操作

2、完成首页搜索操作

3、完成个人信息-昵称的修改

4、完成个人信息-性别的修改

"""

# 导包

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.relative_locator import locate_with, with_tag_name

time.sleep(3)

driver = webdriver.Chrome()  # 实例化浏览器并赋值给driver

driver.get("http://shop-xo.hctestedu.com/")  # 使用浏览器实例对象driver去打开一个网址

login_ele = driver.find_element(By.LINK_TEXT, "登录")  # 定位页面元素：登录

# login_ele.screenshot("登录.png")  # 截图页面元素：登录

login_ele.click()  # 点击页面元素：登录

time.sleep(1)  # 进程休眠 3秒

username_ele = driver.find_element(By.NAME, "accounts")  # 定位页面元素：用户名输入框

# username_ele.screenshot("用户名输入框.png")  # 截图页面元素：用户名输入框

username_ele.send_keys("test_changfeng")  # 在页面元素：用户名输入框 中输入内容

password_ele = driver.find_element(By.NAME, "pwd")  # 定位页面元素：密码输入框

# password_ele.screenshot("密码输入框.png")  # 截图页面元素：密码输入框

password_ele.send_keys("changfeng")  # 在页面元素： 密码输入框 中输入内容

login_button = driver.find_element(By.CLASS_NAME, "btn-loading-example")  # 定位页面元素： 登录按钮

login_button.screenshot("登录按钮.png")  # 截图页面元素：登录按钮

login_button.click()  # 点击页面元素： 登录按钮

time.sleep(1)  # 进程休眠 3秒

search_ele = driver.find_element(By.ID, "search-input")  # 定位页面元素：搜索输入框

# search_ele.screenshot("搜索框.png")  # 截图页面元素：搜索输入框

search_ele.send_keys("手机")  # 在页面元素：搜索输入框 中输入内容

search_button = driver.find_element(By.ID, "ai-topsearch")  # 定位页面元素： 搜索按钮

# search_button.screenshot("搜索按钮.png")  # 截图页面元素：搜索按钮

search_button.click()  # 点击页面元素：搜索按钮

time.sleep(1)  # 进程休眠 3秒

quit_ele = driver.find_element(By.LINK_TEXT, "退出")  # 定位页面元素：退出

# quit_ele.screenshot("退出按钮.png")  # 截图页面元素：退出

mall_homepage_ele = driver.find_element(with_tag_name("span").to_right_of(quit_ele))  # 定位页面元素： 商城首页

# mall_homepage_ele.screenshot("商城首页.png")  # 截图页面元素： 商城首页

user_center = driver.find_element(with_tag_name("span").to_right_of(mall_homepage_ele))  # 定位页面元素： 个人中心

# user_center.screenshot("个人中心.png")  # 截图页面元素： 个人中心

mall_homepage_ele.click()  # 点击页面元素： 个人中心

time.sleep(3)  # 进程休眠 3秒
#
#
#
change_data = driver.find_element(By.LINK_TEXT, '修改资料')  # 定位页面元素： 修改资料

change_data.screenshot("修改资料.png")  # 截图页面元素： 修改资料

change_data.click()  # 点击页面元素： 修改资料

time.sleep(3)  # 进程休眠 3秒

# edit_ele = driver.find_element(By.LINK_TEXT, "编辑")  # 定位页面元素： 编辑
#
# edit_ele.screenshot("编辑.png")  # 截图页面元素： 编辑
#
# edit_ele.click()  # 点击页面元素： 编辑
#
# time.sleep(3)  # 进程休眠 3秒
#
#
#
# nickname_ele = driver.find_element(By.NAME, "nickname")  # 定位页面元素：昵称输入框
#
# nickname_ele.screenshot("昵称输入框.png")  # 截图页面元素： 昵称输入框
#
# nickname_ele.send_keys("长风")  # 在页面元素：昵称输入框 中输入内容
#
# sex_elements = driver.find_elements(By.CLASS_NAME, 'am-icon-checked')  # 定位所有的性别选项
#
# for i in sex_elements:  # 遍历所有的性别选项
#
#     i.screenshot(f"性别选项{sex_elements.index(i)}.png")  # 截图页面元素：性别选项
#
#
#
# sex_man_ele = sex_elements[-1]  # 取得所有性别选项元素列表中的最后一个（性别：男）
#
# sex_man_ele.screenshot("男性选项.png")  # 截图页面元素： 性别男
#
# sex_man_ele.click()  # 点击页面元素：性别男
#
# time.sleep(3)  # 进程休眠 3秒
#
#
#
# save_button = driver.find_element(By.CSS_SELECTOR, "button.am-btn-block")  # 定位页面元素：保存按钮
#
# save_button.screenshot("保存.png")  # 截图页面元素： 保存按钮
#
# save_button.click()  # 点击页面元素： 保存按钮
#
# time.sleep(3)  # 进程休眠 3秒
#
# driver.quit()  # 退出浏览器
