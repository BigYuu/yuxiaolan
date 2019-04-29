#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/11/7 9:52
"""
import time
import os
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import win32gui
import uiautomation as ua
import win32con
import sys
reload(sys)
sys.setdefaultencoding('GBK')

os.system(r"echo .>C:\access.log")



win =ua.WindowControl(Classname='CAutoUpgradeDlg')
if win.Exists(maxSearchSeconds=10):
    print '1111111111111111222222222222222222'


def clear_info():
    """清除信息"""
    k = PyKeyboard()
    k.press_keys([k.control_key, 'a'])
    k.tap_key(k.delete_key)


offset_file = open(r'C:\access.log')
while 1:
    where = offset_file.tell()
    info = offset_file.readline()
    m = PyMouse()
    k = PyKeyboard()
    x_dim, y_dim = m.screen_size()
    if info.__contains__('lock'):
        """idv锁屏PyUserInput"""
        m.move(x_dim / 2, 0)
        time.sleep(0.2)
        m.click(x_dim / 2, 0, 1)
        time.sleep(0.1)
        m.click(int(x_dim * 0.48), int(y_dim * 0.02), 1)
        with open(r'C:\access.log', 'w+')as f:
            f.write('0')
    elif info.__contains__('login'):
        """idv锁屏后再次登入"""
        m.click(int(x_dim * 0.43), int(y_dim * 0.46), 1)
        time.sleep(0.2)
        k.type_string('123')
        time.sleep(0.3)
        k.tap_key(k.enter_key)
        time.sleep(1)
        with open(r'C:\access.log', 'w+')as f:
            f.write('0')
    elif info.__contains__('logout'):
        """退出登入"""
        m.move(x_dim / 2, 0)
        time.sleep(0.2)
        m.click(x_dim / 2, 0, 1)
        time.sleep(0.5)
        m.click(int(x_dim * 0.52), int(y_dim * 0.02), 1)
        time.sleep(0.5)
        button = ua.ButtonControl(AutomationId="1000")
        button.Click()
        with open(r'C:\access.log', 'w+')as f:
            f.write('0')
        time.sleep(1)

    elif info.__contains__("vm_ip_mac"):
        info = os.popen("ipconfig")
        s1 = info.read()
        b = s1.splitlines()[2]
    elif info.__contains__('networkoff'):
        """断网"""
        os.system(u'netsh interface set interface "本地连接" disabled')
        time.sleep(36)
        os.system(u'netsh interface set interface "本地连接" enabled')
        with open(r'C:\access.log', 'w+')as f:
            f.write('0')
    elif info.__contains__('close'):
        """终端关机，关闭虚机"""
        with open(r'C:\access.log', 'w+')as f:
            f.write('0')
        k.tap_key(k.windows_l_key)
        time.sleep(0.5)
        m.click(int(x_dim * 0.15), int(y_dim * 0.93), 1)

    elif info.__contains__('reboot'):
        """终端重启"""
        with open(r'C:\access.log', 'w+')as f:
            f.write('0')
        os.system('shutdown -r -t 00 -f')
    elif info.__contains__('dialog'):
        """终端远程协助弹出框判断"""
        try:
            dialog = win32gui.FindWindow("REMOTE_WND", u"RemoteWnd")
            with open(r'C:\access.log', 'w+')as f:
                f.write('exist')
        except Exception as e:
            print(e)
            with open(r'C:\access.log', 'w+')as f:
                f.write(u'no exist')
            pass

    elif info.__contains__('assistance'):
        """接受远程协助"""
        try:
            dialog = win32gui.FindWindow("REMOTE_WND", u"RemoteWnd")
            a = win32gui.GetWindowRect(dialog)
            with open(r'C:\access.log', 'w+')as f:
                f.write('accept')
            m.click(int(a[0] + 280 * 0.33), int(a[1] + 190 * 0.81), 1)
        except Exception as e:
            print(e)
            with open(r'C:\access.log', 'w+')as f:
                f.write(u'no exist')
            pass
    elif info.__contains__('reject'):
        """拒绝远程协助"""
        try:
            dialog = win32gui.FindWindow("REMOTE_WND", u"RemoteWnd")
            a = win32gui.GetWindowRect(dialog)
            with open(r'C:\access.log', 'w+')as f:
                f.write('success')
            m.click(int(a[0] + 280 * 0.67), int(a[1] + 190 * 0.81), 1)
        except Exception as e:
            print(e)
            with open(r'C:\access.log', 'w+')as f:
                f.write('fail')
    elif info.__contains__('send_message'):
        """判断是否接收到发送的消息"""
        a = win32gui.FindWindow('INFO_WND', "InfoDlg")
        if a != 0:
            with open(r'C:\access.log', 'w+')as f:
                f.write('get_info')
        else:
            with open(r'C:\access.log', 'w+' )as f:
                f.write('do not get_info')

    elif info.__contains__('create_new_file'):
        """在x盘创建大文件,用逗号隔开输入文件路径和文件大小为k"""
        with open(r'C:\access.log', 'w+')as f:
            f.write('0')
        file_path = info.split(',')[1]
        size = info.split(',')[2]
        os.system(r"fsutil file createnew {0} {1}".format(file_path, size))

    elif info.__contains__('x info'):
        """在x盘创建大文件,用逗号隔开输入文件路径和文件大小为k"""
        info = os.popen(r'wmic LogicalDisk where "Caption="X:"" get FreeSpace,Size /value')
        size_info = info.read()
        with open(r'C:\access.log', 'w+')as f:
            f.write(str(size_info))
    offset_file.seek(where)
