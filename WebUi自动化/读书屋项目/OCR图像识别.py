
from PIL import Image
import time
from selenium import webdriver
import requests
import pytesseract


# 获取图片
def get_img(img_path):
    img = Image.open(img_path)
    return img


# 灰度处理
def image_grayscale_deal(image):
    img = image.convert('L')
    img.show()  # 灰度处理
    return img


# 图片二值化处理
def image_threashoding_method(image):
    threshold = 160
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    image = image.point(table, '1')
    image.show()
    return image


# 图像识别
def captcha_crack(image):
    result = pytesseract.image_to_string(image)
    return result


# 清空文件
# def clear_all_input():
#     lst = driver

# pip install pytesseract

driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/')  # 网址必须要合法

# 找到注册元素
regist_link = driver.find_element_by_link_text('注册')
regist_link.click()  # 点击注册按钮

# 获取验证码
yzm_img = driver.find_element_by_xpath('//*[@id="chkd"]')
yzm_img.screenshot('./验证码5.png')
img_url = yzm_img.get_attribute('src')
# print(img_url)
time.sleep(1)
img_date = requests.get(img_url, stream=True)  # 获取图片的文件流
# print(img_date.content)
# time.sleep(1)
# with open('./读书屋项目/2.png，’wb‘') as f:
#     f.write(img_date.content)

file = open('base14.png', 'wb')
file.write(img_date.content)
driver.quit()
"""
验证码的链接与实际网页页面显示的不一致，需要使用截图进行确认
"""

# 对图片进行灰度处理
img1 = get_img('验证码5.png')
img2 = image_grayscale_deal(img1)

# 对图片进行二值化处理
img3 = image_threashoding_method(img2)
# 最终结果
result = captcha_crack(img3)
num = result.split('\n')
print('根据图像识别，获取的最终结果是：{}'.format(num[0]))
driver.quit()


