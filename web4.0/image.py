#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2019/2/18 20:16
"""
import win32api
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import uiautomation as automation
import time
import os
import sys
import re

reload(sys)
sys.setdefaultencoding('GBK')

os.system(r"echo .>S:\access.log")
offset_file = open(r'S:\access.log')
while 1:
    where = offset_file.tell()
    info = offset_file.readline()
    m = PyMouse()
    k = PyKeyboard()
    x_dim, y_dim = m.screen_size()
    if info.__contains__('software_install'):
        """编辑镜像安装火狐浏览器，安装成功返回install_success,失败返回install_fail"""
        filename = r'S:\Firefox-latest.exe'
        k = PyKeyboard()
        win32api.ShellExecute(0, 'open', filename, '', '', 0)
        time.sleep(3)
        k.press_keys([k.alt_key, 'i'])
        n = 0
        flag = ''
        while n < 30:
            button = automation.ButtonControl(Name=u'火狐主页，推荐使用 Firefox 火狐浏览器访问！ - Mozilla Firefox')
            if button.Exists():
                flag = 'install_success'
                break
            else:
                time.sleep(3)
                flag = 'install_fail'
            n = n + 1
        with open(r'S:\access.log', 'w+')as f:
            f.write(flag)

    elif info.__contains__('software_uninstall'):
        """编辑镜像卸载火狐浏览器，卸载成功返回uninstall_success,失败返回uninstall_fail"""
        unstallpath = r'C:\Program Files (x86)\Mozilla Firefox\uninstall\helper.exe'
        local_path = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
        k = PyKeyboard()
        win32api.ShellExecute(0, 'open', unstallpath, '', '', 0)
        time.sleep(3)
        k.press_keys([k.alt_key, 'n'])
        time.sleep(3)
        k.press_keys([k.alt_key, 'u'])
        time.sleep(3)
        k.press_keys([k.alt_key, 'f'])
        if os.path.exists(local_path):
            flag = 'uninstall_fail'
        else:
            flag = 'uninstall_success'
        with open(r'S:\access.log', 'w+')as f:
            f.write(flag)
    elif info.__contains__('sunny_install'):
        """安装sunny 成功返回 install_success，失败返回install_fail"""
        file_path = r'E:\RG-ClassManagerSunny_Upgrade.exe'
        win32api.ShellExecute(0, 'open', file_path, '', '', 0)
        win = automation.PaneControl(Name='RG-ClassManagerSunny V4.0_R1.29 安装')
        time.sleep(60)
        if os.path.exists(r'C:\Program Files (x86)\RG-ClassManagerSunny\ClassManagerSunnyApp.exe'):
            flag = 'install_success'
        else:
            flag = 'install_fail'
        with open(r'S:\access.log', 'w+')as f:
            f.write(flag)
        win.Click(0.5, 0.75)

    elif info.__contains__('guet_tool_install'):
        """安装guest_tool安装成功返回guest_install 失败返回guest_install_fail"""
        file_path = r'E:\RCC_Guest_Tool_General_Setup.exe'
        guest_version = 'RCC_Guest_Tool_4.0_R1.29_Setup.exe'
        win32api.ShellExecute(0, 'open', file_path, '', '', 0)
        win = automation.PaneControl(Name='RCC-Guest-Tool V4.0.0.29 安装')
        win.Click(0.9, 0.93)
        time.sleep(60)
        win.Click(0.5, 0.76)
        os.system(r'cd C:\Program Files (x86)\RCC-Guest-Tool\&type version_guesttool.ini')
        version = re.findall('.*?ruijie.rcc.guesttool.exefile=(.*exe).*', info)[0]
        if version == guest_version:
            flag = 'guest_install'
        else:
            flag = 'guest_install_fail'
        with open(r'S:\access.log', 'w+')as f:
            f.write(flag)

    elif info.__contains__('logout'):
        with open(r'S:\access.log', 'w+')as f:
            f.write('0')
        os.system("shutdown -s -t 00 -f")

    elif info.__contains__('reboot'):
        with open(r'S:\access.log', 'w+')as f:
            f.write('0')
        os.system("shutdown -r -t 00 -f")
    offset_file.seek(where)
