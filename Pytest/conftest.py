# """
# 封装配置
# 全局共用
# 可以跨.py文件调用
#
# 模块级：setup_module/teardown_module，每个.py文件只执行一次
# 函数级：scope=function ,每个函数或者方法调用会执行一次
# 类级别：scope=class，每个类只执行一次
# 模块级：scope=module。每个.py文件只执行一次
# 会话级：session ，每次会话只执行一次，会话内的所有方法类，都在共享
#
# yield 模拟teardown
# """
import pytest
from selenium import webdriver
import html


@pytest.fixture()
def login():
    print('登陆成功')
#
#
# @pytest.fixture(scope='session', autouse=True)
# def browser(request):
#     global driver
#     driver = webdriver.Chrome()
#     driver.get('http://novel.hctestedu.com/')
#     return driver
#
#
def pytest_html_report_title(report):
    report.title = '华测教育-自动化测试报告'
#
#
# def pytest_config(config):
#     config.metadata['项目名称'] = "读书屋项目"
#     # java_home 删除
#     config.metadata.pop('JAVA_HOME')
#
#
# @pytest.mark.optionalhook
# def pytest_result(prefix):
#     prefix.extend([html.p('所属部门')])
#     prefix.extend([html.p('测试人')])
#
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#
#     """
#     item ： 测试的对象
#     call ： 测试的步骤
#     执行完钩子函数后 返回 report，有个属性report.when
#     """
#     pytest_html=item.config.pluginmanager.getplugin('html')
#     outcome=yield
#     report=outcome.get_result()
#     extra=getattr(report,'extra',[])
#
#     if report.when=='call': # 进行截图
#         # screen_img=_capture_screenshoot()
#         pass
#
