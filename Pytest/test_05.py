import pytest

"""

pytest 也包含了 setUp 和 teardown 对应的内容
模块级：setup_module/teardown_module
函数级：setup_fuction/teardown_fuction
类级：setup_class/teardown_class
方法级：setup_method/teardown_method
类里面的 setUp、teardown：运行在调用方法的前后

"""

def setup_function():
    print('每个用例前都会执行一次')

def teardown_function():
    print('每个用例后都会执行一次')

def test_one(self):
    pass


def test_two(self):
    pass

def test_three(self):
    pass
