"""
封装配置

"""
import pytest


@pytest.fixture()
def login():
    print('登陆成功')
