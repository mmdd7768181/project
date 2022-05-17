import requests
from PIL import Image
from selenium import webdriver
import pytesseract
from selenium.webdriver.common.by import By
from time import sleep


# 获取图片   pip install --upgrade pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
def get_img(img_path):
    img = Image.open(img_path)
    return img


# 对图片进行灰度处理
def image_grayscale_deal(image):
    img = image.convert('L')
    # img.show()
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
    # image.show()
    return image


# 图像识别
def captcha_crack(image):
    result1 = pytesseract.image_to_string(image)
    return result1


# 清空文件 : 也可以使用 refresh 刷新网页
def clear_all_input():
    lst = driver.find_elements(By.TAG_NAME, 'input')
    for i in range(1, 4):
        print(len(lst))
        lst[i].clear()


driver = webdriver.Chrome()
driver.get('http://novel.hctestedu.com/')  # 网址必须要合法

print('------开始获取验证码------')
# 找到注册元素
regist_link = driver.find_element_by_link_text('注册')
sleep(1)
regist_link.click()  # 点击注册按钮
sleep(1)

# 获取验证码
yzm_img = driver.find_element_by_xpath('//*[@id="chkd"]')
sleep(1)
yzm_img.screenshot('./image/验证码1.png')
sleep(3)

"""
验证码的链接与实际网页页面显示的不一致，需要使用截图进行确认
"""
# 对图片进行灰度处理
img1 = get_img('Image/验证码1.png')
img2 = image_grayscale_deal(img1)

# 对图片进行二值化处理
img3 = image_threashoding_method(img2)
# 最终结果
result = captcha_crack(img3)

num = result.split('\n')
print('验证码为：{}'.format(num[0]))
sleep(2)
# 注册的测试用例
print('开始执行测试用例')
# driver.find_element_by_xpath('//*[@id="txtUName"]').send_keys('17621166752')
# sleep(1)
# driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('')
# sleep(1)
# driver.find_element_by_xpath('//*[@id="TxtChkCode"]').send_keys(num[0])
# sleep(1)
# driver.find_element_by_xpath('//*[@id="btnRegister"]').click()
# sleep(1)
# assert '密码不能为空' in driver.find_element_by_xpath('//*[@id="LabErr"]').text
# # sleep(1)
# print('测试通过')
# driver.refresh()
# sleep(2)
#
# driver.find_element_by_xpath('//*[@id="txtUName"]').send_keys('1762116675')
# sleep(1)
# driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('cm7768181')
# sleep(1)
# driver.find_element_by_xpath('//*[@id="TxtChkCode"]').send_keys(num[0])
# sleep(1)
# driver.find_element_by_xpath('//*[@id="btnRegister"]').click()
# sleep(1)
# assert '手机号格式不正确' in driver.find_element_by_xpath('//*[@id="LabErr"]').text
# # sleep(1)
# print('测试通过')
# # clear_all_input()
# driver.refresh()
# sleep(2)

driver.find_element_by_xpath('//*[@id="txtUName"]').send_keys('17621166752')
sleep(1)
driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys('cm7768181')
sleep(1)
driver.find_element_by_xpath('//*[@id="TxtChkCode"]').send_keys(num[0])
sleep(1)
driver.find_element_by_xpath('//*[@id="btnRegister"]').click()
sleep(5)
# assert '验证码' in driver.find_element_by_xpath('//*[@id="LabErr"]').text
# sleep(1)
print('注册成功！！！')

driver.quit()
print("用户注册--测试完成")
