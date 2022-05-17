import unittest


class Test(unittest.TestCase):
    def test_1(self):
        print(self.id())


def test1(self):
    print(self.id())
#
#
# def test2(self):
#     print(self.id())
#
#
setattr(Test, 'test_1', test1)
# setattr(Test, 'test_2', test2)
