#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2019/2/18 20:16
"""
import sys
import os

reload(sys)
sys.setdefaultencoding('GBK')
if os.path.exists("S:\ip_set.txt"):
    with open('S:\ip_set.txt') as f:
        info = f.read()
    ip = info[0:-1]
    a = ip.split('.', -1)
    a.remove(a[-1])
    temp_ip = '.'.join(a)
    gateway = '{}.1'.format(temp_ip)
    os.system(u"netsh interface ip set address name=本地连接 source=static addr={0} mask=255.255.255.0 "
              u"gateway={1}".format(ip, gateway))
    os.system(u"netsh interface ip set dns name=本地连接 source=static addr=192.168.5.28 register=primary")
    os.system(u"netsh interface ip add dns name=本地连接 addr=192.168.58.95 index=2")
else:
    print("没有上传镜像分配的ip文件")
