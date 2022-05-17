import unittest
"""
SetUp：每个用例执行前都会运行的前置条件
TearDown:每个用例执行后都会运行的后置处理
SetUpClass:一个用例执行前都会运行的前置条件，需要装饰器处理
TearDown：一个用例执行后都会运行的后置处理，需要装饰器处理
"""

class Test01(unittest.TestCase):

    def setUp(self) -> None:  # 前置

        print('setUp')

    def tearDown(self) -> None:  # 后置
        print('tearDown')

    def test_1(self):
        print('a')

"""
运行结果：
setUp
a
tearDown
必须是先执行前置函数，最后执行后置函数，可以不用实例化，可直接执行


"""