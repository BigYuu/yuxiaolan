#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll && LinMengYao
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/12/29 14:30
"""
# A1.1.2.11.12新建终端组测试数据
from TestData.basicdata import *

vdi_new_group_name = ['test', '测试胖终端分组', '12342223', 'test_01', 'vdi_测试分组01', 'he测试组_11_llll11125463652d',
                      'qwew@1%7', '测试数据12345678990bbbaaaaddddddkkktyygyghhh', ' ', '未分组']
idv_new_group_name = ['test', '测试胖终端分组', '12342223', 'test_01', 'vdi_测试分组01', 'he测试组_11_llll11125463652d',
                      'qwew@1%7', '测试数据12345678990bbbaaaaddddddkkktyygyghhh', ' ', '未分组']
# A1.3用例数据，终端名称，用户名称，终端ip，并且终端未登入过
terminal_name = 'AVDI_02'
vdi_user = 'vdi1_02'
vdi_terminal_ip = vdi_android_ip_list[0]  # 获取安卓终端的某个ip
# A1.4终端信息
name = 'VDI_02'
sn = 'G1MD5HN05547A'
version = '1.001.577'
sys = 'Android'
mac = '00:74:9C:8E:37:FB'
cpu = 'rk3188'
men = '1024MB'
mainboard = 'rk30sdk'
bios = ''
storage = '2252M'

# A1.5,6idv终端批量删除,准备vdi终端测试组，测试组中有终端存3个vdi终端，其中一个终端的状态是关机的（1.6用例要在最后执行）
group_name = 'vdi_test1'
close_name = 'vdi2_01'
# A1.4将vdi_test1的用户变更到未分组
# A1.7测试数据，vdi2_01正常用户，vdi2_02关机，vdi2_03外网不可访问
chenck_name_list = [vdi_terminal_ip, 'vdi-01']
# A1.9，10 终端查找
search_info = ['vdi2_01', 'vdi', vdi_terminal_ip, '!!@', u'没有终端']


# ----------LinMengYao----------
# 查询终端使用的镜像
cmd_tm_base = 'ls /opt/lessons/ | grep -e ".*base$"'
# 查询终端的桌面类型
cmd_desk_type = "cd /opt/lessons/RCC_Client && cat dev_policy.ini | grep allow_recovery | awk '{print $3}'"
# 查询虚机Windows系统D盘大小
cmd_c_size = 'wmic logicaldisk where name="C:" get size'
# 查询虚机Windows是否存在D盘
cmd_d_exist = 'wmic logicaldisk where name="D:" get size'
# cmd的返回信息_不存在该盘
info_disk_in_exist = u'No Instance(s) Available.'
# cmd的返回信息_存在该盘
info_disk_exist = u'Size'
# IDV用户
idv_usr_name = 'test_tm_01'
# IDV用户密码
idv_usr_pwd = '123'
# A1.13用例
gp_name_a13 = ['selenium_un_save_a13', 'selenium_save_a13']
desk_type_a13 = ['还原', '个性']
code_a13 = ['1', '0']  # 终端dev_policy文件记录的终端类型，1还原，0个性
idv_type_a13 = ['多用户', '公用']
# A1.14用例
disk_size = ['45']
# A1.16用例
idv_type_a16 = [u'多用户']
# A1.17用例
note_a17 = [u'123456789012345678901234567890123456789012345678901234567890123']
# A1.18用例
tm_ip_a18 = '172.21.3.111'
tm_name_a18 = 'test_my_1'
host_a18 = '172.21.195.50'
# A1.19用例
gp_name_a19 = 'test_tm_02'  # 基础数据
rename_a19 = 'selenium_tm_02'

# 终端名称
idv_tm_name = u"rcd"   # 用户登录的终端，存在差分
idv_tm_name1 = u"idv_test_01"  # 用户未登录的终端，未存在差分，非自定义终端
idv_tm_name2 = u"idv_test_02"  # 用户未登录，自定义终端
idv_tm_name3 = u"idv_test_03"
# 镜像名称
image_name1 = u"test_idv_restore_win7_rcd"
image_name2 = u"test_idv_win7_rcd"

tm_online1 = u"IDV_06"  # 用作终端关机用例，将被关机终端名称1
tm_online2 = u"idv_400w"  # 用作终端关机用例，将被关机终端名称2
tm_reboot = u"terminal_test"  # 用作终端重启用例
tm_outline = u"nwn"  # 离线终端，用例涉及到删除该终端操作d

#
Administrator = "Administrator"
rcd = "rcd"

# 2019/03/13
# a1.34测试数据
test_a1_34_terminal_name = "test_terminal_a1_34"
test_a1_34_error_host_ip = "1.1.1.1"

idv_ip_1 = idv_public_ip_list[0]  # idv公用终端ip--多用户
idv_ip_2 = idv_public_ip_list[2]  # idv公用终端ip--多用户，涉及初始化用例使用
idv_ip_3 = idv_single_ip_list[0]  # idv单用户终端，未绑定用户
idv_ip_4 = idv_guest_ip_list[0]  # 公用终端
# 根据不同型号的终端搜索验证终端
mac_diff = [idv_ip_1, idv_ip_4]
search_terminal = [idv_ip_1]
# 不同模式的终端类型，多用户、公用户以及单用户终端ip
tm_mode = [idv_ip_1, idv_ip_4]
# 在线->离线，用作终端关机操作用例
shut_down_tm = "172.21.210.23"
# vdi终端ip，做关闭终端操作
vdi_shutdown_ip = "172.21.204.15"  # 过程不可逆，具体以连接到服务器ip为准


# 查看终端后台信息
cat_default_info = "cat /opt/lessons/RCC_Client/dev_policy.ini"
cat_logic_ini = "cat /opt/lessons/RCC_Client/logic.ini"
cat_vm_image_info = "cat /opt/lessons/RCC_Client/vm_image_info.ini"
cat_virtul_size = "qemu-img info /opt/lessons/{}.base"

if __name__ == "__main__":
    pass
