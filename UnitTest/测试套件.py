import unittest
from UnitTest.基本操作 import Test01
from UnitTest.ddt和data import Test02
from UnitTest.skip import Test04

suite=unittest.TestSuite() # 获取对应的测试套件，是一个列表

suite.addTest(Test01('test_1'))
# suite.addTest(Test02('test_2'))
suite.addTest(Test04('test_4'))

runner=unittest.TextTestRunner()
runner.run(suite)