"""
文件名必须以 test_* 或者 *_test 命名
函数都以test_开头
test 开头的类，不能带有__init__ 方法
使用 pytest的，包必须带有_init__
"""

import pytest


def test_one(self):
    print('打印的内容1')
    str = 'huace'

#
# def test_two(self):
#     x = 'xiaomin'
#
#
# def test_three(self):
#     str = 'xiaohong'
#     assert 'xi' in str


if __name__ == '__main__':
    pytest.main(['-vs','test_01'])

