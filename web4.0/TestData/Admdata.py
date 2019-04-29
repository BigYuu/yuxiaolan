#!/usr/bin/python
# -*- coding: UTF-8 -*-

from TestData.basicdata import *


# 数据1
ad_domain_name = u"test"
ad_domain_ip = "172.21.192.201"
ad_domain_port = "389"
ad_domain_admin_username = u"administrator@ruijiercd.com.cn"
ad_domain_admin_upper_username = u"ADMINISTRATOR@RUIJIERCD.COM.CN"
ad_domain_admin_pwd = u"1"

# 数据2
ad_domain_ip_2 = "172.21.3.144"
# ad_domain_port = "389"
ad_domain_admin_username2 = u"Administrator@ruijiecll.com.cn"
# ad_domain_admin_upper_username = u"ADMINISTRATOR@RUIJIERCLL.COM.CN"
ad_domain_admin_user_pwd = u"ad@2008"

ad_user_name = "test2"  # ad_group 下的用户
ad_user_list = [u'test2']
ad_group = u'AD域认证测试'
ad_user_group = u"AD域用户组"
mapping_group = u'mapping_group_test'
unselectable_group = u'Domain Controllers'
ad_user_group_1 = u"chstest"
ad_user_1 = u"chs"
ad_user_2 = u"chs1"
upload_file_path = r"D:\webdata\admdata"
file_1 = u"\\\\172.21.112.136\\d\\RCD\\测试运营组\\自动化数据准备\\导入用户数据\\user_model.xlsx"  # 为 t分组下的chs1用户
file_2 = u"\\\\172.21.112.136\\d\\RCD\\测试运营组\\自动化数据准备\\导入用户数据\\user_model_1.xlsx"  # t分组下的ljm1用户 (ljm1用户为未配置映射的AD域分组用户)
ad_user_3 = "ljm1"
ad_group_batch_list = [u'测试', u'测试10组']


# AD域控上的管理员账号和密码
ad_domain_admin_user_name = u'Administrator'
ad_domain_admin_user_3name = u"123"
ad_domain_admin_user_100name = u"12345678901234567890123456789012345678901234567890123456789012345678901234567890123"
ad_domain_admin_user_32pwd = u"ad@12345678901234567890123456789"

ad_domain = 'ruijiecll'
# 添加域控组织单位
ad_domain_ad_ou = 'dsadd ou "ou={},DC=ruijiercd,DC=com,DC=cn"'

# 在*users下添加1个域用户
ad_domain_add_user_name = 'A_1'
ad_domain_add_user = 'dsadd user "cn={0}, ou={1},dc=ruijiecll, dc=com, dc=cn" -upn {0}@ruijiecll.com.cn  -samid ' \
                     '{0} -pwd ad@2008 -display idv -dept it -company two -office tell -tel 18256352541  -disabled no'
# 在*users下批量添加域用户
ad_domain_add_some_users = r'for /f "skip=1 eol=; tokens=1-7 delims=," %a in (D:\{0}.csv)do dsadd user "cn=%a, ' \
                           'ou={0},DC=ruijiecll,DC=com,DC=cn" -upn %b@ruijiecll.com.cn  -samid %b -pwd %c ' \
                           '-display %a -dept %f -company %e -office %f -tel %f  -disabled no'
# 删除某组织下的所有域用户
ad_domain_rm_ou_users = 'dsrm -subtree -exclude -noprompt -c "ou={},dc=ruijiecll,dc=com,dc=cn"'
# 删除某组织下的某个域用户
ad_domain_rm_user = 'dsrm -noprompt -c "CN={0}，ou={1},dc=ruijiecll,dc=com,dc=cn"'

# 禁用某组下的用户
ad_domain_user_disable = 'dsmod user cn={0},ou={1},DC=ruijiecll,DC=com,DC=cn -disabled yes'
# 启用某组下的用户
ad_domain_user_able = 'dsmod user cn={0},ou={1},DC=ruijiecll,DC=com,DC=cn -disabled no'
# ad_domain_admin_pwd = u"ad_2008@"


android_vdi_terminal_ip =vdi_android_ip_list[3]
android_vdi_user_name = u"h1"
android_vdi_user_passwd = u"ad@2008"
android_vm_user_name = s_user
android_vm_user_passwd = s_pwd

# 在postgresql数据库查找用户的虚机IP语句
find_vdi_vm_ip_in_sql = "SELECT vm_ip FROM lb_seat_info WHERE user_name = '{}' "
# 在postgresql数据库查找用户的终端IP语句
find_vdi_terminal_ip_in_sql = "SELECT terminal_ip FROM lb_seat_info WHERE  user_name = '{}' "
# 在用户的虚机中查找是否加域的DOS语句
find_vm_whether_in_domain = r'net user Administrator /domain'
# 绑定还原镜像的名称
restore_base_name = u"test_vdi_restore_win7_rcd"
# 绑定个性镜像的名称
single_base_name = u"test_vdi_win7_rcd"

# 文件类型
file_type = ['txt', 'bmp', 'rtf', 'docx', 'pptx', 'xlsx']



