"""
命令行：  pytest -vs -hml='路径'/(报告名称).html
cmd 中输入  pytest -vs 脚本.py --html=report.html，即可在的当前目录下生成报告

"""
import pytest
from selenium import webdriver
from py.xml import html

def pytest_html(report):
    # report.
    pass

@pytest.fixture(scope='module')
def open():
    print('打开浏览器')

    yield
    print('执行teardown操作')
    print('关闭浏览器')


def test_s1(open):
    print('搜索江少')
