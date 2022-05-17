# from selenium import webdriver
import time,datetime
# driver = webdriver.Chrome()

# js ='window.open("https://www.baidu.com")'
# driver.execute_script(js)

# print(type(abs(7.1)))

def fun1():
    print('dushuwu.feature1')

def fun2():
    print('222')
    fun1()

# file=open('t1.txt','a+') # 读取文件信息
# con=file.readline()
# print(con)
# print('=======1=========')
# file.write('自动化测试223') #添加新的内容
# file.seek(1) #移动指针
# print(file.readlines()) # 再次读取t4文件内容
# file.close()


dt=datetime.datetime.now()
# print(dt)
# print(dt.year)
# print(dt.time())
# print(dt.weekday())
# print(dt.isoweekday())
print(dt.timestamp())