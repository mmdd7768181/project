import pytest
from pytest_bdd import given, when, then, parsers, scenario
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
url = 'http://novel.hctestedu.com/'
driver.get(url)

# driver.get(url)

@given(parsers.parse('用户名 {username} 密码 {password}'), target_fixture='user')
# @given(parsers.parse('用户名 <username> 密码 <password>',target_fixture='user'))  # 或者用下面的写法
def user(username, password):
    return dict(username=username, password=password)


# @when(parsers.parse('打开登录 {url}'))
# def go_to_url(url, browser):
#     browser.get(url)
#     browser.find_element_by_link_text('登录').click()

@when('打开登录')
def go_to_url():
    # driver.get(url)
    driver.find_element_by_link_text('登录').click()


@when('输入用户名')
def input_username(driver, user):
    sleep(2)
    driver.find_element_by_xpath('//*[@id="txtUName"]').send_keys(user['username'])


@when('输入密码')
def input_password(driver, user):
    sleep(2)
    driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(user['password'])


@when('点击登录按钮')
def input_password(driver):
    sleep(2)
    driver.find_element_by_xpath('//*[@id="btnLogin"]').click()


@then(parsers.parse('页面中应包含登出链接，文字为{logout_text}'))
def click_login(logout_text, driver):
    sleep(2)
    text = driver.find_element_by_xpath('//*[@id="headerUserInfo"]/span/a[2]').text

    assert text == logout_text


@scenario('dushuwu.feature', '场景1--正常登陆')
def test_dushuwu_login():
    pass
