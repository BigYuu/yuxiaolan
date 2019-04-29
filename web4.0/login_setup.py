#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2019/1/8 17:11
"""
from WebPages.UserMangePage import UserMange
from selenium import webdriver
from TestData.Logindata import *
from WebPages.LoginPage import Login
from WebPages.Idvpage import IdvPage
from WebPages.permission_setPage import PermissionSet
from Common.terminal_action import *
from WebPages.ImagePage import Image
from WebPages.AuthenmanagePage import AuthenManage
from Common.serverconn import *
from TestData.basicdata import *
import sys
import os

reload(sys)
sys.setdefaultencoding('GBK')

# vdi用户数据
vdi_group = ["vdi_index2", 'vdi4','cdm_user']
idv_group = ["idv1", "idv2", "idv3","idv_index1", "idv_index2"]
vdi_attribute_name_list = ['idv1_01','ten_user1','ten_user2','ad_vdi1']
idv_attribute_name_list = ['vdi1_01','ad_idv1']
ad_group = 'indexuser'
common_data_upload(host_ip, tdir=u'/测试运营组/自动化数据准备/公用软件安装包', sdir=u'/opt/ftpshare/share/')
common_data_upload(host_ip, tdir=u'/测试运营组/自动化测试镜像', sdir=u'/opt/lessons/')
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
lg = Login(driver)
lg.login(username, passwd)
lg.goto_image_page()
img = Image(driver)
img_ip = img.image_ip_set()
server_type = 'rcd'
for name in ['test_idv_win7_rcd', 'test_idv_restore_win7_rcd']:
    """胖终端镜像编辑"""
    time.sleep(1)
    img.get_ciframe(img.img_manage_frame)
    time.sleep(1)
    img.click_image_edit(name)
    img.select_list_chose(img.image_edit_desktop_type_xpath, '胖终端IDV')
    img.select_list_chose(img.image_edit_os_type_xpath, 'Windows 7')
    img.find_elem(img.image_edit_page_sure_start_xpath).click()
    time.sleep(3)
    img.open_admin_tool()
    if win_conn_useful(img_ip, 'Administrator', 'rcd') == u'winrm可使用':
        time.sleep(120)
        win_conn(img_ip, 'Administrator', 'rcd', 'logout', path='S')
        time.sleep(120)
        win_conn(img_ip, 'Administrator', 'rcd', 'reboot', path='S')
if  server_type == 'rcd':
    for name in ['test_idv_win7_rcd', 'test_vdi_restore_win7_rcd']:
        """瘦终端镜像编辑"""
        time.sleep(1)
        img.get_ciframe(img.img_manage_frame)
        time.sleep(1)
        img.click_image_edit(name)
        img.select_list_chose(img.image_edit_desktop_type_xpath, '瘦终端VDI')
        img.select_list_chose(img.image_edit_os_type_xpath, 'Windows 7')
        img.find_elem(img.image_edit_page_sure_start_xpath).click()
        time.sleep(3)
        img.open_admin_tool()
        if win_conn_useful(img_ip, 'Administrator', 'rcd') == u'winrm可使用':
            time.sleep(120)
            win_conn(img_ip, 'Administrator', 'rcd', 'reboot', path='S')
            time.sleep(120)
            win_conn(img_ip, 'Administrator', 'rcd', 'logout', path='S')
ad = AuthenManage(driver)
ad.goto_adm()
ad.connect_ad_domain()
ad.choose_part(ad_group)
us = UserMange(driver)
time.sleep(5)
us.goto_usermanage_page()
us.import_user()
us.upload(os.path.join(os.getcwd(), 'import_data.xlsx'))
us.start_import()
time.sleep(2)
for name in idv_group:
    us.edit_group1(name)
    if name == 'idv2':
        us.idv_group_set(u'还原')
    else:
        us.idv_group_set()
if  server_type == 'rcd':
    for name in vdi_group:
        us.edit_group1(name)
        if name == 'vdi2':
            us.vdi_group_set(u'还原','test_vdi_restore_win7_rcd')
        else:
            us.vdi_group_set(name='test_vdi_win7_rcd')
time.sleep(2)
for name in idv_attribute_name_list:
    us.search_info(name)
    us.click_edit(name)
    us.idv_group_set()
if  server_type == 'rcd':
    for name in vdi_attribute_name_list:
        us.search_info(name)
        us.click_edit(name)
        us.vdi_group_set(name='test_vdi_win7_rcd')
time.sleep(5)
tp = IdvPage(driver)
if  server_type == 'rcd':
    lg.go_to_vdi_terminal_page()
    for name in ['vdi1', 'vdi2', 'vdi3']:
        tp.vdi_new_group(name)
lg.go_to_idv_terminal_page()
for name in ['idv1', 'idv2', 'idv3','idv_index1','idv_index2']:
    if name == 'idv1':
        tp.idv_new_group(name,desk_type=u'还原')
    else:
        tp.idv_new_group(name)
tp.click_gp_edit_btn(u'未分组')
tp.add_weifenzu_image('test_idv_win7_rcd')
for ip in [idv_single_ip_list[0], idv_public_ip_list[0], idv_common_ip_list[0]]:
    tp.idv_edit_change_group(ip, 'idv3')
ps = PermissionSet(driver)
time.sleep(5)
if  server_type == 'rcd':
    ps.go_admin_setting()
    manger_list = [('test_admin1', 'test_admin1', '123456', '123456', 'vdi1', 'idv1', 'vdi1'),
                   ('adminA', 'adminA', '123456', '123456', 'vdi1', None, None),
                   ('adminB', 'adminB', '123456' ,'123456', None, 'idv1', 'vdi1'),
                   ('del_admin1', 'del_admin1', '123456', '123456', None, 'idv1', 'vdi1'),
                   ('del_admin2', 'del_admin2', '123456', '123456', None, 'idv1', 'vdi1'),
                   ('del_admin3', 'del_admin3', '123456', '123456', None, 'idv1', 'vdi1')]
    for info in manger_list:
        ps.create_new_mannger(info[0], info[1], info[2], info[3], info[4], info[5], info[6])
        if info[0] == 'test_admin1':
            time.sleep(3)
            ps.chose_user_group(info[0],['vdi1',u'2级'])

server_sql_qurey(host_ip,
                 "update idv_user set user_pwd='U2FsdGVkX1+zlIlen5NiUSWMQNPwznuM4CZJvT2yqqc=',is_update_passwd='Y'",
                 qureresult=0)
server_conn(host_ip, 'service tomcat restart')
time.sleep(30)
if __name__ == "__main__":
    pass
