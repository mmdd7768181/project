import pytest


# class TestCase():




def test_1(login):
    print('test_1')


def test_2(login):
    print('test_2')


def test_3(login):
    print('test_3')


if __name__ == '__main__':
    pytest.main(['-vs'])


