#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: LinMengYao/houjinqi
@contact: linmengyao@ruijie.com
@software: PyCharm
@time: 2018/12/27 11:25
"""
from TestData.basicdata import *

'''
web中需要vdi_win7_test idv_win7_rcd这两个镜像
'''

image_file_dir = ur'\\172.21.112.136\d\RCD\云办公\测试镜像'
base_file_dir = ur'\\172.21.112.136\D\RCD\测试运营组\自动化测试镜像'
iso_win7_32 = u'cn_windows_7_all_with_sp1_efi_x64_2016.iso'
iso_win7_64 = u"cn_windows_7_professional_with_sp1_vl_build_x86_dvd_u_677939.iso"
iso_win10_32 = u"cn_windows_10_enterprise_version_1703_updated_march_2017_x64_dvd_10194191.iso"
iso_win10_64 = u"cn_windows_10_enterprise_version_1703_updated_march_2017_x86_dvd_10189572.iso"
iso_xp = u"win_xp_sp3.iso"
# 镜像类型
image_type_vdi = u'VDI'
image_type_idv = u"IDV"

image_ty_list = [image_type_vdi, image_type_idv]
image_win10_iso = [iso_win10_32, iso_win7_64]
# 镜像名称
image_name_1 = u'selenium_vdi_win7_x64'
image_name_2 = u'selenium_vdi_win7_x32'
image_name_3 = u"selenium_vdi_win10_x32"
image_name_4 = u"selenium_xp"
name_A1_14_1 = u'imgtest_a1_14_1'  # 标准配置
name_A1_14_2 = u'imgtest_a1_14_2'  # 高性能
name_A1_14_3 = u'imgtest_a1_14_3'  # 自定义
# 操作系统
os_win7 = u'7'
os_win10 = u'10'
os_xp = u"XP"

usr_name_A1_1 = u'vdi1_04'
vdi_base = u'test_vdi_win7_rcd'
idv_base = u'test_idv_win7_rcd'
base_path = ur'\\172.21.112.136\D\RCD\云办公\测试镜像'
upload_idv_base_name = ur'win7_x64_q.base'
img_name_a5_win10 = u"idv_win10"  # 用例执行前需要win10系统idv镜像,在该镜像中需要有winrm idv_action.py支持
img_name_a5_win7 = u"test_vdi_win7_restore_rcd"  # 用例执行前需要win7系统idv镜像,在该镜像中需要有winrm idv_action.py支持
search_idv_terminal = [idv_ip_list[1]]   # 镜像管理测试用例a5_1、2、3、4为终端安装驱动,根据ip搜索不同类型的终端,可根据不同的终端类型ip进行搜索
idv_img_A = u"test_idv_win7_rcd"  # idv镜像
idv_img_B = u"test_idv_restore_win7_rcd"  # idv镜像
idv_terminal_name = u'rcd'  # 终端名称

u"------------------第二次微调所需要的数据------------"
# 镜像发布更新超时时间
vdi_standard_image = "vdi_standard"  # 2.16用例  win7系统
vdi_restore_image = "test_vdi_restore_win7_rcd"  # 基础镜像
vdi_image = "test_vdi_win7_rcd"
vdi_xp_image = u"VDI_winxp"  # xp系统的镜像
img_test_imgA = u"img_test_nameA"  # 普通镜像，win7
img_test_imgC = u"img_test_nameC"  # vdi镜像配置齐全（winrm以及涉及到软件安装）
vdi_not_gt_image = u"uninstall_GT"  # 未安装GT的镜像
vdi_tm_ip_1 = vdi_android_ip_list[0]  # 获取配置文件中安卓终端ip vdi_android_ip_list[0]
vdi_tm_ip_2 = vdi_guest_ip_list[0]  # 获取配置文件中供使用访客登录的终端  vdi_guest_ip_list[0]
idv_tm_ip_1 = idv_ip_list[1]  # 获取配置文件中idv终端ip
idv_tm_ip_2 = idv_ip_list[2]  # 获取配置文件中idv终端ip

