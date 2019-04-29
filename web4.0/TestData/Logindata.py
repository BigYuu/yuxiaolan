#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/8/26 15:13
"""
from TestData.basicdata import *

# 登入网址
# url = "http://{}/main.html#/login".format(vm_ip)
# 共用账号密码
username = c_user
passwd = c_pwd
# 用户初始密码
cpasswd = t_pwd
# 集群ip
server_ip = cluster_ip
# 主控 ip或虚ip
mainip = host_ip
# 用例A1.1和2
# 用户名为空信息提示
null_messg_info = u"必填项"
# 用户名密码为空错误提示
error_messg_info = u"用户名或密码错误"
# 正确的用户名密码
login_user_succ = {"name": c_user, "passwd": c_pwd, "user_info": u"欢迎您，{}".format(c_user)}
# 错误的用户名密码
login_user_fail = {"name": "33", "passwd": "admin"}
# 用例A1.4利旧客户端和HALO工具下载
# 下载利旧客户端时长设置单位秒
rtime = 5
# 文件下载路径
rloadpath = "D:\\RG-RCC-OA_Client_V4.0_R1.23_X.exe"
# 下载HALO工具时长设置单位秒
htime = 60
# 文件下载路径
hloadpath = "D:\\RG-RCD_Halo_V2.1.13.zip"
# 文件下载路径
admintoolpath = "D:\\RG-RCC_Admin_Tool_V4.0_R1.79.exe"

# 用例A1.6智能客服
# 选择要产品（li下标）
lindex = 4
# 输入咨询内容
# 输入咨询内容
questions = u"什么是云办公"

# 用例A1.5技术论坛支持
webtitle = u"锐捷社区 – 专业的数据通信解决方案互动社区 - Powered by Discuz!"

# 测试用例A1.22,23
running_vdi_name = ['vdi_index1_01','vdi_index2_01','vdi_index2_02']
running_vdi_group_name = ['vdi_index1','vdi_index2']
vdi_user_running = {'vdi_index1':1,'vdi_index2':2}
# idv用户数据
running_idv_name = ['idvindex1_01','idvindex2_01','idvindex2_02']
running_idv_group_name = ['idv_index1','idv_index2']
idv_user_running = {'idv_index1':1,'idv_index2':2}
# 测试用例A1.26
# 关闭虚机用户组
running_idv_name_26 = ['vdi_index1_01','vdi_index1_02','vdi_index1_03']
colse_runvdi_groupname = "vdi_index1"

# 环境中服务器个数
server_count = len(server_ip)
com_slp = 0.8  # 公共休眠时间
# A1.9 web登入后等待时间
login_time_config = 10
# A1.10 信息配置-服务器的版本号、支持的浏览器、分辨率支持、技术支持论坛、技术服务ID、技术服务热线、SVN Reversion信息
browser_support = u'Chrome浏览器、Firefox'
support_bbs = 'bbs.ruijie.com.cn'
support_tel = '4008-111-000'
support_id = 'NA'
svn_reversion = '18665'
# A1.37/38
# 搜索数据
search_jump_smart_list = ['1', 's', 'elenium', '01']

# A1.36
# 搜索数据 需要导入selenium分组用户
search_jump_list = ['selenium01', '172.21.204.17', '172.21.195']

# A1.43 AD域
ad_vdi_list = ['indexuser']

# A1.26
vdi_group_list = ['ad_vdi1']
