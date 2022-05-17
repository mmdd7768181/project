import airtest
from airtest.cli.parser import cli_setup
from airtest.core.api import *
from airtest.core.api import connect_device

"""
trace,这样可以定位哪一行代码出现问题的,使用trace方法需要在文件头部导入traceback库,
"""

import os


# class devices:
#     def get_devices(self):
#         lists = (os.popen('adb devices').read())
#         devices = (lists.strip().split('\n'))
#         devices_list = []
#         for i in range(1, len(devices)):
#             device = (devices[i].split('\t')[0])
#             devices_list.append(device)
#         return devices_list

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=["android://127.0.0.1:5037/127.0.0.1:7555?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MINITOUCH",])


# dev=connect_device('Android://127.0.0.1:5037/127.0.0.1:7555')
# print('成功')
# start_app('com.boke.daimeng.goodfriend')
touch(Template(r"tpl1647340378854.png", record_pos=(0.002, 0.583), resolution=(900, 1600)))

