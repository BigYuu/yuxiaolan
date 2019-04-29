#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2019/01/24 11:15
"""
from ConfigParser import ConfigParser
from Common.file_dir import *

cp = ConfigParser()
cp.read(parent_dir + "\\server_info.ini")
cp.read(parent_dir + "\\terminal.cfg")


def get_cluster_ip():
    a = len(cp.options('reserve'))
    ip_list = list()
    for i in range(a):
        list1 = cp.items('reserve')
        ip_list.append(list1[i][1])
    return ip_list


# 主机ip
host_ip = cp.items('master')[0][1]
# 虚ip
vm_ip = cp.items('master_vir_ip')[0][1]
# 集群ip
cluster_ip = get_cluster_ip()

# 服务器版本
version = '4.0_R1.79'
# 服务器地址
url = "http://{}/main.html#/login".format(vm_ip)
# 公用登入用户名密码
c_user = 'cheng'
c_pwd = 'admin'

c_user2 ='admin3'
c_pwd2 = 'admin'
# 公用登入windows用户名密码
s_user = "Administrator"
s_pwd = "rcd"

# 登录终端公用密码
t_pwd = '123'

# 获取终端ip列表
idv_ip_list =eval(cp.get('ip_list', 'idv_ip_list'))
vdi_android_ip_list =eval(cp.get('ip_list', 'vdi_android_ip_list'))
vdi_guest_ip_list = eval(cp.get("ip_list", "vdi_guest_ip_list"))
vdi_linux_ip_list = eval(cp.get('ip_list', 'vdi_linux_ip_list'))
idv_single_ip_list = eval(cp.get('ip_list', 'idv_single_ip_list'))
idv_common_ip_list = eval(cp.get('ip_list', 'idv_common_ip_list'))
idv_public_ip_list = eval(cp.get('ip_list', 'idv_public_ip_list'))
idv_guest_ip_list = eval(cp.get('ip_list', 'idv_guest_ip_list'))
# 服务器新密码
server_pwd = 'MjI1ZDY2NjQ'
# 服务器就密码
# server_pwd = r'35w_"{<L'
