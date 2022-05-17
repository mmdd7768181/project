import pytest
class Test_Case06():
    def setup(self):
        print('每个用例前执行setup')

    def teardown(self):
        print('，每个用例结束后执行teardown')

    def setup_class(self):
        print('所有用例执行前执行setupclass')

    def teardown_class(self):
        print('所有用例结束后执行teardownclass')
    def setup_method(self):
        print('每个用例开始前执行setupmethod ')

    def teardown_method(self):
        print('每个用例结束后执行teardown_method ')

    def test_one(self):
        print('第一个用例')

    def test_two(self):
        print('第二个用例')

    def test_three(self):
        print('第三个用例')

if __name__ == '__main__':
    pytest.main(['-vs'])
