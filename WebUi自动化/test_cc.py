from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By

dri = webdriver.Chrome()  # 打开谷歌浏览器
url = 'https://www.baidu.com/'
dri.get(url)


# ele_link_text=dri.find_elements_by_xpath('//*[@id="doc-topbar-collapse"]/ul/li[4]/a')
# time.sleep(3)
# print(ele_link_text)
# dri.quit()

@pytest.fixture(scope='function')
def test_01():
    ele4 = dri.find_element_by_xpath('//*[@id="s-top-left"]/a[1]')
    print(ele4.text)
    time.sleep(2)
    dri.quit()


