from WEBUI自动化.读书屋项目 import OCR图像识别 as ocr
from PIL import Image
import time
from selenium import webdriver
import requests
import pytesseract
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/')  # 网址必须要合法


# 图片二值化处理
# def image_threashoding_method(image):
#     threshold = 160
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#
#     image = image.point(table, '1')
#     image.show()
#     return


# ima1 = ocr.get_img('./验证码5.png')
# ima2 = ocr.image_grayscale_deal(ima1)
# im3 = ocr.image_threashoding_method(ima2)
# print(im3)


# driver.find_element_by_xpath('//*[@id="headerUserInfo"]/span/a[2]').click()
# sleep(2)
# driver.find_elements_by_xpath('//*[@id="txtUName"]').send_keys('17621166752')
# sleep(1)
# driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('')
# sleep(1)

# driver.find_element_by_xpath('//*[@id="btnRegister"]') # 点击注册按钮
# sleep(2)
# assert "手机号不能为空" in driver.find_element_by_xpath('//*[@id="LabErr"]')
# print('测试通过')