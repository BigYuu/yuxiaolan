#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/10/22 16:49
"""
from TestData.basicdata import *

# 远程连接共用账号
suser = s_user
syspasswd = s_pwd
# 可用vdi终端ip
common_terminal_ip = '172.21.195.3'
# A1.1用例数据准备
# 其中idv1_01用户的idv和vdi的特性都开启
# 准备的测试数据的终端用户的终端转状态如下idv_user ={"idv1_01":"运行","idv2_02":"运行",
# "idv2_01":"运行","idv3_01":"离线","idv3_02":"离线"}
idv_run_user = ["idv1_01", "idv2_01", u"公用", 'guest']
idv_offline_user = ["idv3_01", "idv3_02"]
# 终端共用密码
cpasswd = t_pwd
# A1.2用例
vdi_run_user = ["vdi1_01", "vdi2_01", "vdi2_02", "vdi3_01"]
vdi_offline_user = ["vdi3_02"]
# A1.3用例的vdi终端的ip和开启idv，vdi双特性的用户名
vdi_ip = vdi_android_ip_list[1]
vname = 'vdi1_01'
# A1.4用例的vdi终端的ip和开启idv，vdi双特性的用户名
idv_ip = idv_ip_list[2]
iname = 'idv1_01'
# A1.6测试用例
net_off_user = ['vdi1_01', 'idv1_01']
# A1.8虚机终端关机用例
run_user = ["idv2_02", "idv2_01", 'vdi1_01', 'vdi2_01', 'vdi2_02']
# A 1.9用户访客身份登入
fill_ip_user = ['vdi2_01', 'vdi3_01']
fip = ["172.21.195.110","172.21.195.111"]
fmask = "255.255.255.0"
fgateway = "172.21.195.1"
fDNS = "192.168.58.110"
# A1.12测试用例变更用户，变更分组名称
vdi_chage_user = [vdi_android_ip_list[0], vdi_android_ip_list[1]]
vdi_group_name = "vdi3"
idv_chage_user = [idv_public_ip_list[0],idv_public_ip_list[1]]
idv_group_name = "idv3"
# A1.50
vdi_drift_name = "vdi1_02"
idv_drif_name = "idv1_02"
vdi_terminal = [ vdi_android_ip_list[1], vdi_android_ip_list[2]]
idv_terminal = [idv_ip_list[0],idv_ip_list[1]]
# A1.25远程协助用户
a_25_user = 'idv1_02'
# A1.30远程协助拒绝用户
reject_user = "vdi3_01"
# A1.31远程协助接受用户
accept_user = "vdi1_02"
# A1.32 访客绑定 Android，linux 利旧客户端访客登入用户账号终端的
guest_user = ['vdi2_01', 'vdi3_01']
# A1.36用户登入后再用访客登入
access_user = "vdi1_03"
# A1.39还原用户访客登入用户
# 需要一个还原镜像并且升级后不编辑镜像更新gestool
auto_user = "vdi3_03"
# A1.40，41用例关机用户
# 在vdi用户里开启无法关机的程序
close_user = ["vdi2_01", "vdi2_02"]
# A42用例，主控ip和全新用户其中vdi2_01为还原用户
restore_vdi_user = ["vdi1_02", 'vdi2_02']
# A43用例，
restore_idv_user = ["idv1_01", "idv2_01"]
mast_ip = host_ip
# A44-47用例，
A44_user = [idv_single_ip_list[0],idv_single_ip_list[1]]
A44_bind_user = {idv_single_ip_list[0]:'idv1_02',idv_single_ip_list[1]:'idv2_01'}
A45_user = ['idv1_02', 'idv2_02']
A46_user = [idv_public_ip_list[-2],idv_public_ip_list[-1]]
A47_user = [idv_common_ip_list[0],idv_common_ip_list[1]]
# 用例48，改变用户绑定镜像,vdi1_01和 idv1_01开始均为win7系统的镜像
change_mirror_user = ['cdm_user_01']
# ,'idv1_01'
# A1.20
search_ip = '172.21.195'
search_name = u'vdi1_01'
# 53,54二级管理员用户A只有用户权限没有终端权限，B只有终端权限，没有用户权限,用vdi1_01的用户登入vdi1终端组
admin_user = ['adminA', 'adminB']
user = 'vdi1_01'
termianl_name = 'VDI_06'
vdi1_ip = '172.21.210.30'
# A1.17
search_data_17 = u"vdi1_01"

# A1.23
search_data_23 = u"vdi1_01"

# A1.2
# dict为 运行、休眠、离线的云桌面，需手动配置
status_dict = {u'运行': u'a11', u'休眠': u'12345678912345678912', u'离线': u'lida'}

vdi = 'vdi'
restore = u'还原'
vdi_image = u'vdi_win7_test_03'  # vdi_win7_test_03
if __name__ == "__main__":
    pass
