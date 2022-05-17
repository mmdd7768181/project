import pytest
from selenium import webdriver
from time import sleep

"""
全局共用：conftest.py
可以跨.py文件调用
fixture 参数：
SCOPE：定义生效的级别 ，setup/teardown  function（函数级别）
函数级：scope=function 每一个函数或者方法调用
类别及：class 每个测试类只执行一次
模块级： module 每个模块
会话级：session 每次会话只运行一次，程序从开始到结束为一次会话

yield：进行前后端的分隔，上面的代码是前端，后面的代码是后端
"""
driver=None
@pytest.fixture(scope='',)
def browser(res):
    global driver
    if driver is None:
        driver=webdriver.Chrome()

    def end():
        driver.quit()
    res.addfinalzer(end)
    return driver

@pytest.fixture(scope='module')
def open():
    print('打开浏览器')

    yield
    print('执行teardown操作')
    print('关闭浏览器')

def test_s1(open):
    print('搜索江少')