"""
http协议本身是无状态的，即服务器无法判断用户身份
cookie是一小段文本信息，客户端向服务器发起请求，如果服务器需要记录该用户的状态，就是使用response向客户端浏览器颁发一个cookie
客户端会把cookie保存起来，当浏览器再请求该网站时，浏览器会把请求的网址联通该cookie一同提交给服务器，服务器会检查cookie，辨认用户状态
通过cookie机制，可以跳过验证码

driver.get_cookie()
driver.delete_cookie()
driver.add_cookie()
"""
from PIL import Image
import time
from selenium import webdriver
import requests
import pytesseract
driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/')  # 网址必须要合法

driver.add_cookie()
driver.get_cookie('http://novel.hctestedu.com/')
# driver.delete_cookie()