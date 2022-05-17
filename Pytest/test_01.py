"""
文件名必须以 test_* 或者 *_test 命名
函数都以test_开头
test 开头的类，不能带有__init__ 方法
使用 pytest的，包必须带有_init__

-vs 输出详细的信息，包括 print 内容
"""

import pytest


def test_one(self):
    print('打印的内容1')
    str1 = 'huace'


#
def test_two(self):
    x = 'xiaomin'


def test_three(self):
    str = 'xiaohong'
    assert 'xi' in str
