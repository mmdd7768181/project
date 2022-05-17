import pytest


# @pytest.fixture()
# def login():
#     print('登陆成功')


# class TestCase():
def test_1(login):
    print('执行test_1')


def test_2():
    print('执行test_2')


def test_3():
    print('执行test_3')


# if __name__ == '__main__':
#     pytest.main()

if __name__ == '__main__':
    pytest.main(['-vs', '--html=report.html'])
