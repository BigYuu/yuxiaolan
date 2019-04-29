#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/11/15 16:18
"""
from ConfigParser import ConfigParser
from Common import file_dir
# 测试用A1.1新建用户组
from TestData.basicdata import idv_single_ip_list, vdi_android_ip_list, vdi_guest_ip_list

group_name = ['vdi_personal','idv_personal','vdi_restore','idv_restore']
ip='172.21.3.12'
mask='255.255.255.0'
gateway='172.21.3.1'
dns='114.114.114.114'

# -------------------------------------------------------陈依琳----------------------------------------------------------------
# 默认vdi镜像
vdi_default_mirror = u'test_vdi_win7_rcd'
#           76/79/89、64  63
run_user = ['vdi4_01', 'vdi4_04']
#         14/78/80/73(个性)、76、     37/34(个性),34(还原)
norun_user = ['vdi4_02', 'vdi4_03', 'vdi4_05', 'vdi4_06']

# 76/37
vdi_group_name = "vdi4"
# 64

trans = u'禁止传输'
ip1 = '172.21.112.10'
subnet_mask1 = '255.255.255.0'
gateway1 = '172.21.112.1'
main_DNS1 = '172.21.112.10'
prepare_DNS1 = '172.21.112.11'
# 63/# 88 #冲突ip
ip2 = '172.21.112.12'
subnet_mask2 = '255.255.255.0'
gateway2 = '172.21.112.1'
main_DNS2 = '172.21.112.12'
prepare_DNS2 = '172.21.112.13'
# 86 跨网段ip填充起始值
ip3 = '172.21.199.254'
subnet_mask3 = '255.255.255.0'
gateway3 = '172.21.199.1'
main_DNS3 = '172.21.199.254'

# 14
vlan_max = '4095'
vlan = ['vlan', '', '-1']
# 34
cdesk_val_increase = '50'
ddesk_val_increase = '50'

cdesk_val_dncrease = '10'
ddesk_val_dncrease = '10'

# 82/83
# 用户组模板
usermodel_xlsx = u"\\\\172.21.112.136\\d\\RCD\\测试运营组\\自动化数据准备\\导入用户数据\\import_model.xlsx"
vdi_model_group_name = 'import_model'
# vdi模板(空间不足，无法导入)
usermodel_xlsx3 = u"\\\\172.21.112.136\\d\\RCD\\测试运营组\\自动化数据准备\\导入用户数据\\import_model (3).xlsx"
# 84
# 开启vdi特性的用户组组名(自建)
vdiGroupName = "vdi4_vdi"
# 73终端vdi的ip
android_vdi_ip = '172.21.3.200'  # 172.21.3.103
vdi_desktop_ip = '172.21.195.130'
xdisk_increase = '5'
xdisk_decrease1 = '2'
xdisk_decrease2 = '3'
# 72
xdisk_increase1 = '7'
xdisk_increase2 = '10'
# 18
# 标配镜像
standard_mirror = 'vdi_win7_test_01'  # test_idv_restore_win7_rcd
# 高配镜像
senior_mirror = 'vdi_win7_test_02'  # test_idv_restore_win7_rcd
# A1.76
vdi_init_pwd="123456"
# 30
# 需要提前导入的模板
model = u"\\\\172.21.112.136\d\RCD\测试运营组\自动化数据准备\导入用户数据\model.xlsx"

# --------------------------------------------------------吴少锋---------------------------------------------------------------------------

# 用户管理
# 用户组名称用户组描述 [0]全英文 [1]全中文 [2]全数字 [3]混入特殊符号
user_name_describe_list = ["asdqweqwe", u"哈哈哈哈", "123456789", u"混合12_q@w.7-特殊", "_mac", "1#2$3%4",
                           "0123456789012345678901234567890123456789012345678901234567890123456789", u"描述为空"]
del_group_list = ["asdqweqwe", u"哈哈哈哈", "123456789", u"混合12_q@w.7-特殊",
                           "01234567890123456789012345678901", u"描述为空"]
# vlan列表   英文 负数 越界
vlan_list = ['qdqdas', '-4090', '4100']
# 用户组名列表
userGroup_name_list = [u"web用户管理A1.5用例", 'idvSystemDisk', 'vlan4094', 'vlan_other', 'userImage', 'systemDisk',
                       'userCharacter', 'vdiVlan',
                       'idvUG_Character', 'deleteUserGroup', 'createUser', 'userChooseUsergroup', 'vdiswitch',
                       'idvSwitch', 'userDetail',
                       'userDefine', 'IpFill', 'userDefineCharacter']
# 用户名列表
user_list = ['111', '222', '333', '444', '555', '666', '777', '888', '999', '000', 'aaa', 'bbb', 'ccc', 'ddd', 'eee',
             'fff', 'ggg']

# 镜像名
vdi_default_image = u'test_vdi_win7_rcd'  #VDI_win7_X86_安装GT
idv_default_image = u'test_idv_win7_rcd'  # IDV_WIN7_RCD
idv_default_image_sysDiskSize = '40'
vdi_image = u'test_vdi_restore_win7_rcd'  # VDI_win7_X86_安装GT
idv_image = 'test_idv_restore_win7_rcd'  # IDV_WIN7_02

# 相关用例提示与告警信息
userGroup_createSuccessfully_info = u"用户组创建成功！"
user_createSuccessfully_info = u"用户创建成功！"
open_info = u'已开启'
close_info = u'已关闭'
ungrouped = u"未分组"
chooseImage_info = u'请选择1个镜像'
idvimage_bind_errormsg_info = u'必填项'
vdiCharacterError_info = u'将无法登陆VDI桌面'
idvCharacterError_info = u"将无法登陆IDV终端"
spaceCharacterError_info = u"未勾选启用个人云盘，将删除用户原有云盘数据"
idvError_info = u"未勾选IDV云终端设置，将无法登录IDV终端"
vdiError_info = u"未勾选VDI云终端设置，将无法登录VDI终端"
desktopStyleChanged_PR_info = u"IDV云终端桌面类型[个性--->还原]"
delUserGroup_info = u"删除用户组会把该组下的所有用户转移到未分组"
search_info = u"用户名/姓名/终端名称/IP地址"
searchNoData = u"暂无数据"
searchCountIsZero = u"共 0 条"
searchContent = u"111"
userDefineInfo = u'该用户的配置与用户所在组不同'
noUserFillIp_Info = u"请选择一条数据"
noVdiFillIp_Info = u"未选择开启VDI特性的用户，无法填充，请重新选择"
ipFillSuccess_info = u"IP填充成功！"
info_list=[idvError_info,spaceCharacterError_info,vdiError_info]
# vlan相关用例后台查看端口命令
command1 = 'ifconfig bond0.4094'
command2 = 'ifconfig brv4094_bond0'
command3 = 'ifconfig bond0.5'
command4 = 'ifconfig brv5_bond0'
# 桌面类型
personality = u'个性'
restore = u'还原'
# 用户详情相关
characterStatusOpenDetail = u"已开启 \n      (组的配置：已关闭)\n"
cpusize = '6'
cpuContent_info = u"4 (组的配置：%s)" % cpusize
memContent_info = u"2 (组的配置：10)"
systemDiskContent_info = u"50 (组的配置：60)"
perDiskContent_info = u"20 (组的配置：50)"
desktopStyleContent_info = u"个性 \n      (组的配置：还原)"
imageBindContent_info = u"%s (组的配置：%s)" % (vdi_default_image, vdi_image)
imageIdvBindContent_info = u"%s \n      (组的配置：%s)\n" % (idv_default_image, idv_image)

idv = 'idv'
vdi = 'vdi'
all = 'all'
space = 'space'
confire = 'confire'
delete = 'delete'
yes = u'是'
noDNS = 'noDNS'
noIP = 'noIP'
# 填充IP
ip_fill = "172.21.112.159"
subnetMask = "255.255.255.0"
gateWay = '172.21.112.1'
dns_fill = '114.114.114.114'

#A1.47
idv_restore_userGroup=u"IDV还原组"
idv_restore_user=u"IDV还原用户"
idv_restore_images=["test_idv_restore_win7_rcd","test_idv_restore_win7_2"]
idv_personality_images=["test_idv_win7_rcd"]
#A1.44  70
newfile = 'test44_70'
#40 41用例用户组名与用户名
idv_tm = "idv_tm"
user_idv_tm = "user_idv_tm"
myidv = 'ltl'



cp = ConfigParser()
pf = cp.read(file_dir.config_dir + "\\linux_conn.cfg")
# 登入服务器web界面的账号密码
login_user = {"name": "hqf", "passwd": "admin"}
# 新建用户所需的姓名
test_username = "hhh"
# 二级用户组
user_group = "vdi_A"
# 三级用户组
user_group_name = ["vdi_A159_1", "vdi_A159_2", "vdi_A133"]
# 个性用户登入虚机密码
sys_pwd = 'rcd'

# A1.81
name = "respasswd"
# A1.59
user_A159= "A159"
user_A259="A259"
# A1.60
user_A160="A160"
# A1.15
user_A1151="A115_1"
user_A1152="A115_2"

 #A1.61
user_A161="A161"
select = {"sys": u"系统盘(GB)：", "disk": u"个人盘(GB)：", "net": u"云盘：", "inc": "increase", "dec": "decrease"}
# A1.62
user_A162="A162"
# A1.33
user_A133="A133"
# A1.21
username = {u"个性用户": "A121_1", u"还原用户": "A121_1"}
# A1.17
u_group_name = {"user_group": "vdi_A117", "user": "A117"}
select_vdi_image = {"标配vdi镜像":"vdi_win7_test_01","高配vdi镜像": r"vdi_win7_test_02","自定义vdi镜像": r"vdi_win7_test_03"}

# 共用数据
# 云桌面类型可选项
vdi_type = [u"个性", u"还原"]
select_vdi_restore_image = [r"win7_restore_rcd",r"win7_restore_rcd_2"]
# 确认框可选项
confirm_button_type = [u"新建用户", u"编辑用户", u"编辑用户组"]
#CPU选项
cpu_number = ["1", "2", "4", "6", "8"]
#内存可选项
memory_size = ["1", "2", "3", "4", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]

# A1.35
group_name1 = 'vdi5'
user_name1 = "vdi5_01"
img_name1 = "test_usermanage_35"
img_name2 = "test_usermanage_351"
user_name2 = " vdi5_02"
file_dir = ur'\\172.21.112.136\d\RCD\云办公\测试镜像'
iso = u'cn_windows_7_all_with_sp1_efi_x64_2016.iso'
type = u'VDI'
name_A1_1 = u'selenium_vdi_win7_x64'
os = u'7'

# A1.6
idv_test_user1 = "idv1_04"
idv_test_user2 = "idv2_04"
ip4 = "172.21.3.15"
pwd="123"
login_idv_name="IDV_O1"
# A1.47
select_idv_restore_image = [r"test_idv_restore_win7_rcd",r"test_idv_restore_win7_2"]
user_group1 = "idv4"
select_idv_personality_images = ["test_idv_win7_rcd"]
# A1.69
idv_user_group2 = "idv5"
# A1.49
idv_user_group3 = "idv6"
idv_user_group4= "idv7"

# 需提前准备的镜像
image_name = "test_idv_restore_win7_rcd"
image_name2 = "test_idv_win7_rcd"
image_name3 = "test_vdi_win7_rcd"  # vdi需要镜像

# 还原镜像
restore_vdi_base = "img_test_nameC"
vdi_base = "img_test_nameA"
vdi_standard_image = "vdi_standard"
single_tm_ip = idv_single_ip_list[2]  # 单用户未绑定用户的终端
single_tm_ip2 = idv_single_ip_list[3]  # 单用户未绑定用户的终端
vdi_tm_ip_1 = vdi_android_ip_list[0]  # 获取配置文件中安卓终端ip
vdi_tm_ip_2 = vdi_android_ip_list[1]  # 获取配置文件中供使用访客登录的终端


if __name__ == "__main__":
    pass
