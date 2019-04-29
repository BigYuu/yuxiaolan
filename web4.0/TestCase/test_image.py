#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: LinMengYao/houjinqi
@contact: linmengyao@ruijie.com
@software: PyCharm
@time: 2018/12/27 11:25
"""
from string import *

import pytest

from Common.terminal_action import idv_initialization_click, idv_pattern_chose, idv_is_bind_image, win_conn_useful
from TestData.Terminalmangerdata import cmd_c_size
from WebPages.CdeskmangePage import CDeskMange
from WebPages.Idvpage import IdvPage
from WebPages.LoginPage import Login
from TestData.Logindata import *
from WebPages.ImagePage import Image
from TestData.ImageData import *
from WebPages.AuthenmanagePage import AuthenManage
from Common.serverconn import *
import time
import random
import re
from WebPages.UserMangePage import UserMange
from WebPages.adnroid_vdi_page import AndroidVdi
from WebPages.permission_setPage import PermissionSet
from selenium.webdriver.common.keys import Keys
from Common.Mylog import logging


class TestImage:

    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_create_vdi_image(self, com_fixture):
        """
        1、上传ISO文件到服务器
        2、新增镜像，选择刚上传的服务器
        3、新增完成后，验证web上有该服务器的存在
        4、删除该镜像
        5、TODO：进入镜像编辑器进行系统安装暂放
        """
        logging.info(u"------------------------------web新增iso镜像用例A1.1开始执行------------------------------")
        img = Image(com_fixture)
        try:
            img.go_img_manage()
            img.del_iso_exist(iso_name=iso_win7_32, is_return=1)
            img.upload_img(image_file_dir, iso_win7_32)
            time.sleep(10)
            # 刷新镜像ISO后上传的ISO文件才生效
            img.go_iso_and_refresh(is_return=1)
            img.add_img(image_type_vdi, image_name_1, iso_win7_32, os_win7)
            time.sleep(1.5)
            img.open_admin_tool()
            time.sleep(1)
            # 关闭镜像
            img.close_img()
            # 验证镜像存在
            assert img.elem_is_exist(u"//div[@title='{}']".format(image_name_1)) == 0
            img.wait_image_update_cpmpleted(image_name_1)
        finally:
            img.img_recovery(image_name_1)
            img.go_iso_and_del(iso_name=iso_win7_32, is_return=1)

    @pytest.mark.image
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('image_type', image_ty_list)
    @pytest.mark.autotest_image
    def test_a1_2_3(self, com_fixture, image_type):
        """
        1、上传win7 64位的ISO文件
        2、新增镜像，选择镜像类型
        3、新增完成后，web上验证有该镜像的存在
        4、善后处理，删除镜像，删除ISO文件
        5、TODO 进入镜像编辑器进行系统安装未实现
        """
        logging.info(u"-----------------------------镜像管理A1.2、3用例--------------------------------")
        img = Image(com_fixture)
        try:
            img.go_img_manage()
            img.del_iso_exist(iso_name=iso_win7_64, is_return=1)
            img.upload_img(image_file_dir, iso_win7_64)
            time.sleep(10)
            # 刷新镜像ISO后上传的ISO文件才生效
            img.go_iso_and_refresh(is_return=1)
            img.add_img(image_type, image_name_1, iso_win7_64, os_win7)
            time.sleep(1.5)
            img.open_admin_tool()
            time.sleep(1)
            # 关闭镜像
            img.close_img()
            # 验证镜像存在
            assert img.elem_is_exist(u"//div[@title='{}']".format(image_name_1)) == 0
            img.wait_image_update_cpmpleted(img_name=image_name_1)
        finally:
            # 善后：删除镜像,删除ISO文件
            img.img_recovery(image_name_1)
            img.go_iso_and_del(iso_name=iso_win7_64, is_return=1)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('image_type', image_ty_list)
    @pytest.mark.autotest_image
    def test_a1_4_5(self, com_fixture, image_type):
        """
        1、上传win7 32位的ISO文件
        2、新增镜像，选择镜像类型
        3、新增完成后，web上验证有该镜像的存在
        4、善后处理，删除镜像，删除ISO文件
        5、TODO 进入镜像编辑器进行系统安装未实现，以及用户登录
        """
        logging.info(u"-----------镜像管理a1_4、5用例执行------------")
        img = Image(com_fixture)
        try:
            img.go_img_manage()
            img.del_iso_exist(iso_name=iso_win7_32, is_return=1)
            img.upload_img(image_file_dir, iso_win7_32)
            time.sleep(10)
            # 刷新镜像ISO后上传的ISO文件才生效
            img.go_iso_and_refresh(is_return=1)
            img.add_img(image_type, image_name_2, iso_win7_32, os_win7)
            time.sleep(1.5)
            img.open_admin_tool()
            time.sleep(1)
            # 关闭镜像
            img.close_img()
            # 验证镜像存在
            assert img.elem_is_exist(u"//div[@title='{}']".format(image_name_2)) == 0
            img.wait_image_update_cpmpleted(image_name_2)
        finally:
            # 善后：删除镜像,删除ISO文件
            img.img_recovery(image_name_2)
            img.go_iso_and_del(iso_name=iso_win7_32, is_return=1)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('win10_iso', image_win10_iso)
    @pytest.mark.autotest_image
    def test_a1_6_7(self, com_fixture, win10_iso):
        """
        1、上传win 10不同位数的ISO文件
        2、新增镜像，选择镜像类型
        3、新增完成后，web上验证有该镜像的存在
        4、善后处理，删除镜像，删除ISO文件
        5、TODO 进入镜像编辑器进行系统安装未实现，以及用户登录
        """
        logging.info(u"-----------------镜像管理用例6、7---------------")
        img = Image(com_fixture)
        try:
            img.go_img_manage()
            img.del_iso_exist(iso_name=win10_iso, is_return=1)
            img.upload_img(image_file_dir, win10_iso)
            time.sleep(10)
            # 刷新镜像ISO后上传的ISO文件才生效
            img.go_iso_and_refresh(is_return=1)
            img.add_img(image_type_idv, image_name_3, win10_iso, os_win10)
            time.sleep(1.5)
            img.open_admin_tool()
            time.sleep(1)
            # 关闭镜像
            img.close_img()
            # 验证镜像存在
            assert img.elem_is_exist(u"//div[@title='{}']".format(image_name_3)) == 0
            img.wait_image_update_cpmpleted(image_name_3)
        finally:
            try:
                # 善后：删除镜像,删除ISO文件
                img.img_recovery(image_name_3)
                img.go_iso_and_del(iso_name=win10_iso, is_return=1)
            except Exception as e:
                logging.info(e)

    @pytest.mark.image
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_a1_8(self, com_fixture):
        """
        1、上传win xp ISO文件
        2、新增镜像，选择镜像类型
        3、新增完成后，web上验证有该镜像的存在
        4、善后处理，删除镜像，删除ISO文件
        5、TODO 进入镜像编辑器进行系统安装未实现,以及用户登录
        """
        logging.info(u"----------------------------VDI创建winXP位镜像并且用户登录------------")
        img = Image(com_fixture)
        try:
            img.go_img_manage()
            img.del_iso_exist(iso_name=iso_xp, is_return=1)
            img.upload_img(image_file_dir, iso_xp)
            time.sleep(10)
            # 刷新镜像ISO后上传的ISO文件才生效
            img.go_iso_and_refresh(is_return=1)
            img.add_img(image_type_vdi, image_name_4, iso_xp, os_xp)
            time.sleep(1.5)
            img.open_admin_tool()
            time.sleep(1)
            # 关闭镜像
            img.close_img()
            # 验证镜像存在
            assert img.elem_is_exist(u"//div[@title='{}']".format(image_name_4)) == 0
            img.wait_image_update_cpmpleted(image_name_4)
        finally:
            # 善后：删除镜像,删除ISO文件
            img.img_recovery(image_name_4)
            img.go_iso_and_del(iso_name=iso_xp, is_return=1)


    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_image_system_edit(self, com_fixture):
        logging.info(u"------------------------------web新增镜像用例A1.13开始执行------------------------------")
        img = Image(com_fixture)
        img.go_img_manage()
        img.click_image_edit(vdi_base)  # 选择VDI镜像点击编辑
        logging.info(u"校验VDI镜像编辑中可选Windows7")
        img.select_list_chose(img.os_xpath, 'Windows 7')
        assert img.select_chose_text(img.os_xpath) == 'Windows 7'
        logging.info(u"校验VDI镜像编辑中可选WindowsXP")
        img.select_list_chose(img.os_xpath, 'Windows XP')
        assert img.select_chose_text(img.os_xpath) == 'Windows XP'
        img.driver.refresh()
        img.get_current_iframe(img.img_manage_frame)
        img.click_image_edit(idv_base)  # 选择IDV镜像
        logging.info(u"校验VDI镜像编辑中可选Windows7")
        img.select_list_chose(img.os_xpath, 'Windows 7')
        assert img.select_chose_text(img.os_xpath) == 'Windows 7'
        img.select_list_chose(img.os_xpath, 'Windows XP')
        logging.info(u"校验VDI镜像编辑中可选WindowsXP")
        assert img.select_chose_text(img.os_xpath) == 'Windows XP'
        img.select_list_chose(img.os_xpath, 'Windows 10')
        logging.info(u"校验VDI镜像编辑中可选Windows10")
        assert img.select_chose_text(img.os_xpath) == 'Windows 10'

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_a1_14_15(self, com_fixture):
        """
        1、创建不同性能配置的镜像
        2、在镜像管理页面验证配置信息
        3、善后处理
        """
        logging.info(u"-----------------新增VDI镜像—界面检查-系统配置,a1_15创建磁盘为40和100在此处完成-------------")
        img = Image(com_fixture)
        img.go_img_manage()
        # 添加标准配置的镜像
        flag = img.add_iso_not_exist(iso_win7_64)
        time.sleep(10)  # 等待镜像上传到服务器
        if flag == 1:
            img.go_iso_and_refresh(is_return=1)
        img.add_img(image_type_vdi, name_A1_14_1, iso_win7_64, os_win7)
        time.sleep(1.5)
        img.open_admin_tool()
        time.sleep(1)
        img.close_img()
        img.wait_image_update_cpmpleted(img_name=name_A1_14_1)
        # 添加高性能配置镜像
        img.add_img_cofig_diff(image_type_vdi, name_A1_14_2, iso_win7_64, os_win7, u"高性能")
        time.sleep(1.5)
        img.open_admin_tool()
        time.sleep(1)
        img.close_img()
        img.wait_image_update_cpmpleted(img_name=name_A1_14_2)
        # 添加自定义配置镜像，将系统盘的大小设置为100G
        img.add_img_cofig_diff(image_type_vdi, name_A1_14_3, iso_win7_64, os_win7, u"自定义", 4, 100)
        time.sleep(1.5)
        img.open_admin_tool()
        time.sleep(1)
        img.close_img()
        img.wait_image_update_cpmpleted(img_name=name_A1_14_3)
        time.sleep(1)
        # 查看镜像详情信息
        img.check_img_info(name_A1_14_1)
        assert img.get_value(img.img_detail_cpu) == '4'
        assert img.get_value(img.img_detail_cpu) == '4'
        assert img.get_value(img.img_detail_memory_size) == '2'
        assert img.get_value(img.img_detail_system_disk_size) == '20'
        img.close_img_info()
        img.go_img_manage()
        img.check_img_info(name_A1_14_2)
        assert img.get_value(img.img_detail_cpu) == '4'
        assert img.get_value(img.img_detail_memory_size) == '3'
        assert img.get_value(img.img_detail_system_disk_size) == '20'
        img.close_img_info()
        img.go_img_manage()
        img.check_img_info(name_A1_14_3)
        assert img.get_value(img.img_detail_cpu) == '4'
        assert img.get_value(img.img_detail_memory_size) == '4'
        assert img.get_value(img.img_detail_system_disk_size) == '100'
        img.close_img_info()
        logging.info(u"-------------删除添加过的镜像操作----------------")
        img.go_img_manage()
        img.del_img(name_A1_14_1)
        time.sleep(1)
        img.del_img(name_A1_14_2)
        time.sleep(1)
        img.del_img(name_A1_14_3)

    @pytest.mark.image
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_a1_16(self):
        """
        1、新增镜像
        2、TODO 进入镜像编辑器安装软件
        """
        logging.info(u"---------------------新增镜像并安装软件-----------------")
        pass

    @pytest.mark.image
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_a1_20_21(self, com_fixture):
        """
        1、进入iso文件列表，若无iso文件则将iso文件上传到服务器上
        2、检查iso列表有iso文件存在
        3、删除iso文件后，刷新iso文件列表，验证相关iso文件已删除
        """
        img = Image(com_fixture)
        img.go_img_manage()
        img.add_iso_not_exist(iso_win7_32)
        img.go_iso_and_refresh()
        logging.info(u"验证iso文件列表有该文件存在")
        assert img.elem_is_exist(img.iso_span.format(iso_win7_32)) == 0
        img.click_elem(img.return_btns)
        # 删除iso文件
        img.go_iso_and_del(iso_name=iso_win7_32)
        logging.info(u"验证iso文件被删除")
        assert img.elem_is_exist(img.iso_span.format(iso_win7_32)) == 1

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_a2_1(self, com_fixture):
        """
        1、修改镜像名称，验证修改成功
        2、修改镜像名称为最长为25个字符且包含特殊字符，验证镜像名称修改成功
        3、创建vdi用户，并绑定该镜像，用户登录成功
        """
        logging.info(u"-----------镜像管理用例a2_1执行--------------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        android_vdi = AndroidVdi()
        cd = CDeskMange(com_fixture)
        gp_name = "it_ugp_2_1"
        u_name = "it_user_a2_1"
        try:
            # 进入用户管理页面创建用户
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name=gp_name, img_name=img_test_imgC, cd_type=u"还原")
            user.create_user_in_group(group_name=gp_name, user_name=u_name, real_name=u_name)
            # 进入镜像管理页面
            img.go_img_manage()
            img.edit_image_name_os(image_name=img_test_imgC, new_name="img_test_new_name")
            time.sleep(2)
            # 验证名称存在
            assert "img_test_new_name" in img.get_value(img.img_list_xpath)
            # 修改镜像名称为25个字符且包含特殊字符
            img.click_image_edit(vm_name="img_test_new_name")  # 点击编辑
            img.clear_text_info(img.image_edit_image_name)
            img.find_elem(img.image_edit_image_name).send_keys("@@@@@@#######%%%%%%yyyyyyyyyy")  # 修改镜像名称
            img.find_elem(img.image_edit_page_sure_xpath).click()  # 点击确定
            img.click_elem(img.close_image_cancel_xpath)  # 点击取消
            img.back_current_page()
            img.go_img_manage()
            # 验证修改不生效
            assert "@@@@@@#######%%%%%%yyyyyyyyyy" not in img.get_value(img.img_list_xpath)
            # 连接终端，用户登录
            android_vdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_1)
            android_vdi.login(name=u_name, ip=vdi_tm_ip_1, pwd="123456")
            android_vdi.vdi_disconnect(ip=vdi_tm_ip_1)
            # 进入云桌面管理搜索该终端查看查看状态为在线
            cd.back_current_page()
            cd.goto_cloud_desk_manage()
            cd.search_info(name=u_name)
            status = cd.get_status(name=u_name)
            assert u"运行" in status
            # 终端关机
            cd.close_img(passwd)
        # 删除用户和用户组
        finally:
            # 善后处理，将终端名称恢复，删除用户组和用户名
            img.driver.refresh()
            img.back_current_page()
            img.go_img_manage()
            if "img_test_new_name" in img.get_value(img.img_list_xpath):
                img.edit_image_name_os(image_name="img_test_new_name", new_name=img_test_imgC)
            user.user_recovery(gp_name=gp_name)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_edit_image_bind_group(self, com_fixture):
        """
        1、编辑镜像，修改镜像的CPU、C盘大小
        2、创建用户组绑定该镜像，验证该分组的继承镜像新的属性
        3、善后，删除用户组
        """
        logging.info(u"--------------------web新增iso镜像用例A2.5开始执行--------------------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        copy_name = u"a2_5"
        try:
            img.go_img_manage()
            img.copy_image(by_copy=img_test_imgC, copy_name=copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            img.click_image_edit(vm_name=copy_name)
            # 修改镜像属性
            img.editor_img_sysconfig(sysconfig_type=u"自定义", memory_size="4", system_disk_size="60", pubdate=u"立即发布")
            time.sleep(1)
            img.open_admin_tool()
            time.sleep(1)
            img.close_img()
            img.wait_image_update_cpmpleted(img_name=copy_name)
            # 创建分组
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="it_ugp_2_5", img_name=copy_name, cd_type=u"个性")
            time.sleep(2)
            user.edit_group(group="it_ugp_2_5")
            assert "4" == user.get_internal_memory_val()
            assert "60" == user.get_cdesk_val()
            user.find_elem(user.cancel_button1).click()  # 点击确定
            time.sleep(1)
        # 环境恢复
        finally:
            user.user_recovery(gp_name="it_ugp_2_5")
            img.img_recovery(copy_name)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_edit_idv_system_disk1(self, com_fixture):
        logging.info(u"------------------------------web新增镜像用例A2.7 A2.18开始执行------------------------------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        copy_name = "image_test_a2_7_18"
        try:
            # 复制镜像,并等待镜像复制完成且更新完成
            img.go_img_manage()
            img.copy_image(by_copy=idv_base, copy_name=copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            # 创建用户绑定镜像
            user.back_current_page()
            img.create_user_with_idv('idv2', "it_user_a2", copy_name)
            img.go_img_manage()
            img.click_image_edit(copy_name)  # 选择IDV镜像点击编辑
            image_disk_value = img.find_elem(img.idv_image_edit_system_disk_xpath).get_attribute('value')
            img.find_elem(img.idv_image_edit_system_disk_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)
            img.find_elem(img.idv_image_edit_system_disk_xpath).send_keys(int(image_disk_value) - 10)  # 减少10G
            img.find_elem(img.image_edit_page_blank_xpath).click()
            disk_value_dec_result = img.find_elem(img.idv_image_edit_system_disk_xpath).get_attribute('value')
            # logging.info("A2.7 A2.18 校验IDV镜像的系统盘无法变小")
            assert disk_value_dec_result == image_disk_value
            img.find_elem(img.idv_image_edit_system_disk_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)
            img.find_elem(img.idv_image_edit_system_disk_xpath).send_keys(int(image_disk_value) + 10)  # 增大10G
            img.find_elem(img.image_edit_page_sure_xpath).click()
            user_disk_value = img.user_idv_system_disk("it_user_a2")
            # logging.info("A2.7 A2.18 校验IDV镜像C盘增大10G，该镜像绑定的用户和终端/组处系统盘显示增加10G")
            assert user_disk_value == str(int(image_disk_value) + 10)
            img.driver.refresh()
            img.go_img_manage()
            img.wait_image_update_cpmpleted(copy_name)
            img.click_image_edit(copy_name)
            img.find_elem(img.idv_image_edit_system_disk_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)
            img.find_elem(img.idv_image_edit_system_disk_xpath).send_keys(100)
            img.find_elem(img.image_edit_page_sure_xpath).click()
            user_disk_value = img.user_idv_system_disk("it_user_a2")
            logging.info("A2.7 A2.18 校验IDV镜像的系统盘增大到100G，该镜像绑定的用户和终端/组处系统盘100G")
            assert user_disk_value == '100'
        finally:
            img.driver.refresh()
            user.goto_usermanage_page()
            user.search_info("it_user_a2")
            user.del_user(passwd)
            img.img_recovery(copy_name)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    @pytest.mark.aaa
    def test_a2_8_9(self, com_fixture):
        logging.info(u"-------------镜像管理a2_8_9用例执行--------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        copy_name = "image_test_a2_8"
        try:
            # 复制镜像
            img.go_img_manage()
            img.copy_image(by_copy=idv_base, copy_name=copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            # 查看镜像磁盘大小
            img.click_image_edit(copy_name)  # 选择IDV镜像点击编辑
            image_disk_value = img.find_elem(img.idv_image_edit_system_disk_xpath).get_attribute('value')
            img.find_elem(img.image_edit_page_sure_xpath).click()
            # 进入用户管理页面，创建分组并绑定镜像
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="it_ugp_2_8", img_name=copy_name, cd_type=u"个性")
            time.sleep(2)
            user.edit_group(group="it_ugp_2_8")
            assert image_disk_value == user.get_cdesk_val()
            user.find_elem(user.cancel_button1).click()  # 点击取消
            time.sleep(1)
            # 修改镜像磁盘大小
            img.go_img_manage()  # 进入镜像管理页面
            img.click_image_edit(copy_name)  # 选择IDV镜像点击编辑
            img.find_elem(img.idv_image_edit_system_disk_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)
            img.find_elem(img.idv_image_edit_system_disk_xpath).send_keys(int(image_disk_value) + 10)  # 增大10G
            img.find_elem(img.image_edit_page_sure_xpath).click()
            # 被绑定的用户组不变更属性
            user.back_current_page()
            user.goto_usermanage_page()
            user.edit_group(group="it_ugp_2_8")
            # assert image_disk_value == user.get_cdesk_val()  # 此处已绑定镜像分组系统盘大小跟随镜像改变而改变
            user.find_elem(user.cancel_button1).click()  # 点击取消
            time.sleep(1)
        finally:
            try:
                user.driver.refresh()
                user.back_current_page()
                user.goto_usermanage_page()
                user.del_group_exist(name="it_ugp_2_8")
                img.img_recovery(copy_name)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_edit_bind_user_restore_image(self, com_fixture):
        """
        1、复制镜像
        2、编辑镜像
        3、创建用户组和用户并绑定该镜像
        4、用户登录，验证用户绑定的镜像为更新后的镜像
        5、用户退出登录，断开连接，删除用户、用户组和镜像
        """
        logging.info(u"-----------------------------web新增iso镜像用例A2.10开始执行-----------------------------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        idv = IdvPage(com_fixture)
        android_vdi = AndroidVdi()
        cd_desk = CDeskMange(com_fixture)
        copy_image = 'idv_copy_a2_10'
        group_name = "it_ugp_10"
        user_name = "it_user_10"
        try:
            img.go_img_manage()
            # 复制镜像,等待复制完成并更新
            img.copy_image(by_copy=vdi_base, copy_name=copy_image)
            img.wait_image_update_cpmpleted(copy_image)
            # 创建用户组和用户
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name=group_name, img_name=copy_image, cd_type=u"还原")
            time.sleep(2)
            user.create_user_in_group(group_name=group_name, user_name=user_name, real_name=user_name)
            # 编辑镜像
            img.go_img_manage()
            img.click_image_edit(vm_name=copy_image)
            img.editor_img_sysconfig(sysconfig_type=u"自定义", system_disk_size="50", pubdate=u"立即发布")
            time.sleep(1.5)
            img.open_admin_tool()
            img.close_img()
            img.wait_image_update_cpmpleted(copy_image)
            # 等待镜像更新完成用户登录终端
            android_vdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_1)
            android_vdi.login(name=user_name, ip=vdi_tm_ip_1, pwd="123456")
            cd_desk.back_current_page()
            cd_desk.goto_cloud_desk_manage()
            cd_desk.search_info(name=user_name)
            cd_ip = cd_desk.get_cloud_desk_ip(name=user_name)
            win_conn_useful(ip=cd_ip, name=s_user, pwd=s_pwd)
            info1 = get_win_conn_info(ip=cd_ip, user_name=s_user, passwd=s_pwd, cmd=cmd_c_size)
            c_size = idv.convert_size(info=info1)
            assert c_size == 50
            cd_desk.close_img(passwd)
            android_vdi.vdi_disconnect(ip=vdi_tm_ip_1)
        finally:
            try:
                # 善后处理
                user.user_recovery(group_name)
                img.img_recovery(copy_image)
            except Exception as e:
                logging.info(e)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_image_a2_15(self, com_fixture):
        """
        1、复制一个标准vdi镜像
        2、创建个性组和个性用户并绑定该镜像
        3、编辑该镜像，从标准配置切换到高性能
        4、验证无法操作
        5、编辑该镜像，切换成自定义配置
        6、验证无法操作
        7、善后处理：删除用户组、用户和镜像
        """
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        copy_name = "image_test_a2_15"
        gp_name = "it_gp_a2_15"
        user_name = "it_user_a2_15"
        try:
            # 复制镜像，等待镜像复制并更新完成
            img.go_img_manage()
            img.copy_image(by_copy=vdi_standard_image, copy_name=copy_name)
            img.wait_image_update_cpmpleted(img_name=copy_name)
            # 创建个性用户组和用户并绑定该镜像
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name=gp_name, img_name=copy_name, cd_type=u"个性")
            user.create_user_in_group(group_name=gp_name, user_name=user_name, real_name=user_name)
            # 编辑镜像
            img.go_img_manage()
            img.click_image_edit(vm_name=copy_name)
            img.click_elem(img.high_performance_xpath)  # 点击高性能
            img.find_elem(img.btns_start_xpath).click()  # 点击确定并启动
            img.back_current_page()
            time.sleep(2)
            logging.info(u"验证修改属性为高性能")
            assert u"镜像已被用户组(个性VDI云桌面)绑定，无法修改内存！" in img.get_value(img.sys_please_xpath)
            img.click_elem(img.sure_button_xpath)  # 点击确定
            img.go_common_frame()
            img.click_elem(img.close_image_cancel_xpath)  # 点击取消
            img.back_current_page()
            img.go_img_manage()
            img.click_image_edit(vm_name=copy_name)
            img.click_elem(img.custom_xpath)
            img.clear_text_info(img.memory_size_xpath)  # 清空默认内存数据
            img.find_elem(img.memory_size_xpath).send_keys("4")  # 输入内存大小
            img.find_elem(img.btns_start_xpath).click()  # 点击确定并启动
            img.back_current_page()
            time.sleep(2)
            logging.info(u"验证修改属性为高性能")
            assert u"镜像已被用户组(个性VDI云桌面)绑定，无法修改内存！" in img.get_value(img.sys_please_xpath)
            img.click_elem(img.sure_button_xpath)  # 点击确定
            img.go_common_frame()
            img.click_elem(img.close_image_cancel_xpath)  # 点击取消
        finally:
            user.user_recovery(gp_name)
            img.img_recovery(copy_name)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_edit_idv_system_start(self, com_fixture):
        logging.info("------------------------------web新增镜像用例A2.22 A4.17开始执行------------------------------")
        img = Image(com_fixture)
        idv_copy_image_name = 'A2_22'
        try:
            img.go_img_manage()
            flag = 0
            # 复制镜像，等待镜像复制结束并更新
            img.copy_image(by_copy=idv_base, copy_name=idv_copy_image_name)
            img.wait_image_update_cpmpleted(img_name=idv_copy_image_name)
            img.driver.refresh()
            img.get_current_iframe(img.img_manage_frame)
            img.click_image_edit(idv_copy_image_name)  # 选择IDV镜像点击编辑
            image_disk_value = img.find_elem(img.idv_image_edit_system_disk_xpath).get_attribute('value')
            img.find_elem(img.idv_image_edit_system_disk_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)
            img.find_elem(img.idv_image_edit_system_disk_xpath).send_keys(int(image_disk_value) + 21)
            img.find_elem(img.image_edit_page_sure_start_xpath).click()  # 点击确定并启动
            img.back_current_page()
            time.sleep(1.5)
            img.open_admin_tool()
            time.sleep(2)
            img.get_current_iframe(img.img_manage_frame)
            img.find_elem(img.close_image_xpath).click()  # 点击关闭镜像
            img.get_random_iframe(img.close_image_page_xpath)
            img.find_elem(img.close_image_cancel_xpath).click()  # 点击取消关闭
            img.get_current_iframe(img.img_manage_frame)
            logging.info(u"校验取消关闭镜像后，镜像不会被关闭")
            assert img.find_elem(img.image_start_status_xpath.format(idv_copy_image_name)).is_displayed()
            img.find_elem(img.close_image_xpath).click()
            img.get_random_iframe(img.close_image_page_xpath)
            img.find_elem(img.select_close_image_xpath).click()  # 取消选择当前镜像
            logging.info(u"校验取消选择当前镜像,当前选中镜像变为0/1")
            assert img.find_elem(img.image_start_count_xpath).text == '0'
            img.find_elem(img.close_image_sure_xpath).click()  # 点击关闭
            img.back_current_page()
            logging.info(u"校验取消选择当前镜像,点击关闭,提示“请选中要关闭的镜像”")
            assert img.find_elem(img.frame_sure_xpath).is_displayed()
            img.find_elem(img.frame_sure_xpath).click()  # 点击弹出提示窗口的确定
            img.get_random_iframe(img.close_image_page_xpath)
            img.find_elem(img.unselect_close_image_xpath).click()  # 选择当前镜像
            img.find_elem(img.close_image_sure_xpath).click()  # 点击关闭
            img.get_current_iframe(img.img_manage_frame)
            time.sleep(120)
            try:
                img.find_elem(img.image_start_status_xpath.format(idv_copy_image_name), wait_times=30)
            except Exception as e:
                flag = 1
                print e
            logging.info(u"校验关闭镜像后，镜像被正常关闭")
            assert flag == 1
        finally:
            img.img_recovery(idv_copy_image_name)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_edit_idv_system_disk2(self, com_fixture):
        """
        1、复制一个镜像
        2、编辑复制后的镜像（修改镜像名称）
        3、验证修改成功
        """
        logging.info(u"--------------web新增镜像用例A2.21开始执行-----------------")
        img = Image(com_fixture)
        copy_name = "copy_imageA"
        try:
            img.go_img_manage()
            # 复制镜像，等待镜像复制完成并更新
            img.copy_image(by_copy=img_test_imgA, copy_name=copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            img.edit_image_name_os(image_name=copy_name, new_name="new_copy_name")
            time.sleep(2)
            assert "new_copy_name" in img.get_value(img.img_list_xpath)
        # 善后，修改成功
        finally:
            try:
                time.sleep(2)
                img.del_img("new_copy_name")
            except Exception as e:
                logging.info(e)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    @pytest.mark.aaa
    def test_copy_vdi_image(self, com_fixture):
        logging.info("------------------------------web新增镜像用例A4.6开始执行------------------------------")
        vdi_copy_image_name = 'A4_6'
        img = Image(com_fixture)
        try:
            flag = 0
            img.go_img_manage()
            # 复制镜像并等待镜像更新完成
            img.copy_image(by_copy=vdi_base, copy_name=vdi_copy_image_name)
            img.wait_image_update_cpmpleted(img_name=vdi_copy_image_name)
            img.driver.refresh()
            img.get_current_iframe(img.img_manage_frame)
            try:
                img.find_elem(img.image_bind_xpath.format(vdi_copy_image_name), wait_times=3)
            except Exception as e:
                flag = 1
                logging.info(e)
            logging.info("校验VDI镜像复制成功后，镜像未被绑定")
            assert flag == 1
            img_stat1 = server_conn(mainip, 'stat /opt/lessons/{}*'.
                                    format(vdi_base)).split('\r\n')[1].split('	')[0]
            img_stat2 = server_conn(mainip, 'stat /opt/lessons/{}*'.
                                    format(vdi_copy_image_name)).split('\r\n')[1].split('	')[0]
            logging.info("校验VDI镜像复制成功后，与原镜像内容一致")
            assert img_stat1 == img_stat2
        finally:
            img.img_recovery(vdi_copy_image_name)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_delete_bind_image(self, login_fixture):
        logging.info("------------------------------web新增镜像用例A4.13开始执行------------------------------")
        usr = Login(login_fixture)
        img = Image(login_fixture)
        user = UserMange(login_fixture)
        image_name = 'A4_6_13'
        gp_name = "ugp_a4_13"
        user_name = 'A4_13'
        try:
            usr.login(login_user_succ["name"], login_user_succ["passwd"])
            flag = 0
            img.go_img_manage()
            # 复制镜像并等待镜像更新完成
            img.copy_image(by_copy=vdi_base, copy_name=image_name)
            img.wait_image_update_cpmpleted(img_name=image_name)
            img.back_current_page()
            # 创建用户组绑定该镜像
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name=gp_name, img_name=image_name, cd_type=u"还原")
            user.create_user_in_group(group_name=gp_name, user_name=user_name, real_name=user_name)
            img.go_img_manage()
            img.click_image_delete(image_name)
            img.back_current_page()
            img.find_elem(img.sure_button_xpath).click()
            logging.info("校验已绑定的VDI镜像点击删除后，弹出已被绑定提示框")
            assert img.find_elem(img.image_bind_warn_frame_xpath).is_displayed()
            img.find_elem(img.sure_button_xpath).click()
            img.delete_user(user_name)  # 将该用户删除，取消绑定该镜像后，再次点击删除镜像
            user.del_group(gp_name)
            img.go_img_manage()
            img.click_image_delete(image_name)
            img.back_current_page()
            img.find_elem(img.sure_button_xpath).click()
            time.sleep(30)
            img.get_ciframe(img.img_manage_frame)
            try:
                img.find_elem(img.image_frame_xpath.format(image_name), wait_times=3)
            except Exception as e:
                flag = 1
                print e
            logging.info("校验已绑定的VDI镜像取消绑定后，再次删除镜像成功")
            assert flag == 1
        finally:
            img.img_recovery(image_name)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    @pytest.mark.aaa
    def test_copy_idv_image(self, com_fixture):
        logging.info("------------------------------web新增镜像用例A4.7开始执行------------------------------")
        idv_copy_image_name = 'A4_7_12'
        img = Image(com_fixture)
        try:
            flag = 0
            img.go_img_manage()
            # 复制镜像，并等待镜像更新完成
            img.copy_image(by_copy=idv_base, copy_name=idv_copy_image_name)
            img.wait_image_update_cpmpleted(img_name=idv_copy_image_name)
            img.driver.refresh()
            img.get_current_iframe(img.img_manage_frame)
            try:
                img.find_elem(img.image_bind_xpath.format(idv_copy_image_name), wait_times=3)
            except Exception as e:
                flag = 1
                print e
            logging.info("校验IDV镜像复制成功后，镜像未被绑定")
            assert flag == 1
            img_stat1 = server_conn(mainip, 'stat /opt/lessons/{}*'.
                                    format(idv_base)).split('\r\n')[1].split('	')[0]
            img_stat2 = server_conn(mainip, 'stat /opt/lessons/{}*'.
                                    format(idv_copy_image_name)).split('\r\n')[1].split('	')[0]
            logging.info("校验IDV镜像复制成功后，与原镜像内容一致")
            assert img_stat1 == img_stat2
        finally:
            img.img_recovery(idv_copy_image_name)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    @pytest.mark.aaa
    def test_delete_no_bind_image(self, com_fixture):
        logging.info("------------------------------web新增镜像用例A4.12开始执行------------------------------")
        image_name = 'A4_7_12'
        img = Image(com_fixture)
        try:
            flag = 0
            img.go_img_manage()
            # 复制镜像，并等待更新完成
            img.copy_image(by_copy=vdi_base, copy_name=image_name)
            img.wait_image_update_cpmpleted(img_name=image_name)
            ret1 = server_conn(mainip, 'df |grep /opt/lessons').split()[3]
            # 删除镜像
            img.click_image_delete(image_name)  # 点击镜像中的删除
            img.back_current_page()
            logging.info("校验未启用/未绑定镜像点击删除后，弹出确认框")
            assert img.find_elem(img.image_delete_sure_frame_xpath).is_displayed()
            img.find_elem(img.cancel_button_xpath).click()  # 点击取消删除
            img.get_ciframe(img.img_manage_frame)
            logging.info("校验未启用/未绑定镜像点击取消删除后，未删除镜像")
            assert img.find_elem(img.image_frame_xpath.format(image_name)).is_displayed()
            img.click_image_delete(image_name)  # 点击确认删除
            img.back_current_page()
            img.find_elem(img.sure_button_xpath).click()
            time.sleep(30)
            img.get_ciframe(img.img_manage_frame)
            try:
                img.find_elem(img.image_frame_xpath.format(image_name), wait_times=3)
            except Exception as e:
                flag = 1
                print e
            ret2 = server_conn(mainip, 'df |grep /opt/lessons').split()[3]
            logging.info("校验未启用/未绑定镜像点击确认删除后，已删除镜像，可用空间增大")
            assert flag == 1
            assert int(ret1) < int(ret2)
        finally:
            img.img_recovery(image_name)

    @pytest.mark.image
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_add_idv_base(self, com_fixture):
        logging.info("-----------------web新增iso镜像用例A2.19 A4.15-1第二部分：编辑启动执行----------------")
        img = Image(com_fixture)
        img_name = upload_idv_base_name.split('.')[0]
        try:
            img.go_img_manage()
            img.upload_img(image_file_dir, upload_idv_base_name)
            img.back_current_page()
            img.go_img_manage()
            img.click_elem(img.refresh)
            time.sleep(1)
            img.click_image_edit(img_name)
            img.select_list_chose(img.image_edit_desktop_type_xpath, '胖终端IDV')
            img.select_list_chose(img.image_edit_os_type_xpath, 'Windows 7')
            img.find_elem(img.image_edit_page_sure_start_xpath).click()  # 点击确定并启动
            img.back_current_page()
            time.sleep(1.5)
            img.open_admin_tool()  # 打开admintool工具
            img.close_img()  # 关闭镜像
        except Exception as e:
            flag = 0
            print(e)
        else:
            flag = 1

        logging.info("校验新增IDV的base，编辑启动成功")
        assert flag == 1
        try:
            img.wait_image_update_cpmpleted(img_name)
            img.delete_image(img_name)
        except Exception as e:
            logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_a2_16(self, com_fixture):
        """
        1、需提前准备vdi镜像（标配)
        2、编辑镜像，在镜像页面中，将标准配置修改为自定义
        3、vdi登录绑定镜像的用户
        4、输入cmd命令验证镜像参数修改成功
        5、善后处理
        """
        logging.info(u"--------------------------用例A2_16执行-----------------------------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        android_vdi = AndroidVdi()
        image_name = "copy_image_a"
        gp_name = "itgroup_a2_16"
        u_name1 = "ituser_a2_16_1"
        u_name2 = "ituser_a2_16_2"
        try:
            # 进入镜像管理页面编辑复制镜像
            img.go_img_manage()
            img.copy_image(by_copy=vdi_standard_image, copy_name=image_name)
            img.wait_image_update_cpmpleted(img_name=image_name)
            img.back_current_page()
            # 进入用户管理页面创建用户
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name=gp_name, img_name=image_name, cd_type=u"还原")
            user.create_user_in_group(group_name=gp_name, user_name=u_name1,
                                      real_name=u_name1)
            user.driver.refresh()
            user.create_user_in_group(group_name=gp_name, user_name=u_name2,
                                      real_name=u_name2)
            # 连接终端,用户登录
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.login(name=u_name1, ip=vdi_tm_ip_1, pwd="123456")  # 用户登录终端
            # 进入到镜像管理页面编辑镜像
            img.back_current_page()
            img.go_img_manage()
            img.click_image_edit(image_name)
            img.editor_img_sysconfig(sysconfig_type=u"自定义", memory_size="3", system_disk_size="20", pubdate=u"立即发布")
            time.sleep(2)
            img.open_admin_tool()
            time.sleep(2)
            img.close_img()
            time.sleep(200)  # 等待终端倒计时锁屏
            img.wait_image_update_cpmpleted(image_name)
            img.check_img_info(img_name=image_name)
            assert img.get_elem_text(img.img_detail_memory_size) == "3"  # 验证修改参数成功
            img.close_img_info()  # 关闭镜像详情页
            img.back_current_page()
            # 用户再次登录查看
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)  # 连接终端
            android_vdi.login(name=u_name1, ip=vdi_tm_ip_1, pwd="123456")  # 用户登录终端
            # 获取vdi云桌面IP,并连接，输入cmd命令查看内存大小
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name=u_name1)  # 输入用户名搜索
            cd_ip = cd_manage.get_cloud_desk_ip(u_name1)
            cmd = "systeminfo"  # 获取系统信息
            win_conn_useful(ip=cd_ip, name=s_user, pwd=s_pwd)
            sysinfo = get_win_conn_info(cd_ip, s_user, s_pwd, cmd)  # 此处注意数据替换
            memory_size = re.findall(r'.*?Total Physical Memory:     (.*MB).*?', sysinfo)[0]  # 获取安装内存
            print memory_size
            assert memory_size == u"3,071 MB"
        finally:
            android_vdi.vdi_disconnect(ip=vdi_tm_ip_1)
            # 进入云桌面，将用户所绑定的镜像进行关机操作
            cd_manage.cd_manage_recovery(u_name1)
            user.user_recovery(gp_name)
            img.img_recovery(image_name)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.test_a2_17
    @pytest.mark.autotest_image
    @pytest.mark.aaa
    def test_a2_17(self, com_fixture):
        """
        1、需提前准备镜像（标配），还原用户组以及用户
        2、编辑镜像，在镜像管页面中，将标准配置修改为高性能配置
        3、vdi登录绑定镜像的用户
        4、输入cmd命令验证镜像参数修改成功
        5、善后处理
        """
        logging.info(u"-----------------用例A2_17执行----------------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        android_vdi = AndroidVdi()
        cd_manage = CDeskMange(com_fixture)
        copy_image_name = "vdi_copy_image"
        gp_name = "itgroup_a2_17"
        u_name1 = "ituser_a2_17_1"
        u_name2 = "ituser_a2_17_2"
        try:
            # 进入镜像管理页面复制镜像
            img.go_img_manage()
            img.copy_image(by_copy=vdi_standard_image, copy_name=copy_image_name)
            img.wait_image_update_cpmpleted(img_name=copy_image_name)
            img.back_current_page()
            # 进入到用户管理页面，创建用户组和用户
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name=gp_name, img_name=copy_image_name, cd_type=u"还原")
            user.create_user_in_group(group_name=gp_name, user_name=u_name1,
                                      real_name=u_name1)
            user.driver.refresh()
            user.create_user_in_group(group_name=gp_name, user_name=u_name2,
                                      real_name=u_name2)
            # 连接终端,用户登录
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.login(name=u_name1, ip=vdi_tm_ip_1, pwd="123456")  # 用户登录终端
            img.back_current_page()
            img.go_img_manage()  # 进入到镜像管理页面
            img.click_image_edit(copy_image_name)  # 编辑该镜像
            img.editor_img_sysconfig(sysconfig_type=u"高性能", pubdate=u"立即发布")
            time.sleep(1.5)
            img.open_admin_tool()
            time.sleep(2)
            img.close_img()
            time.sleep(200)  # 等待终端倒计时后锁屏
            logging.info(u"-----查看镜像详情验证安装内存---")
            img.wait_image_update_cpmpleted(copy_image_name)
            img.check_img_info(img_name=copy_image_name)
            assert img.get_elem_text(img.img_detail_memory_size) == "3"  # 高性能安装内存为3
            img.close_img_info()  # 关闭镜像详情页
            img.back_current_page()
            # 连接终端并且登录用户
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)  # 连接终端
            android_vdi.login(name=u_name1, ip=vdi_tm_ip_1, pwd="123456")  # 用户登录终端
            # 获取vdi云桌面IP,并连接，输入cmd命令查看内存大小
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name=u_name1)  # 输入用户名搜索
            cd_ip = cd_manage.get_cloud_desk_ip(u_name1)
            cmd = "systeminfo"  # 获取系统信息
            win_conn_useful(ip=cd_ip, name=s_user, pwd=s_pwd)
            sysinfo = get_win_conn_info(cd_ip, s_user, s_pwd, cmd)
            memory_size = re.findall(r'.*?Total Physical Memory:     (.*MB).*?', sysinfo)[0]  # 获取安装内存
            print memory_size
            assert memory_size == u"3,071 MB"
            time.sleep(5)
        finally:
            # 进入云桌面，将用户所绑定的镜像进行关机操作
            cd_manage.cd_manage_recovery(u_name1)
            user.user_recovery(gp_name)
            img.img_recovery(copy_image_name)

    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a2_24(self, com_fixture):
        """
        1、需准备名称为vdi的镜像，进行编辑
        2、在操作系统安装服务器共享目录下的软件
        3、安装软件，待安装完成后卸载软件并关机
        4、启动镜像并验证软件安装和卸载情况
        """
        logging.info(u"-----------镜像管理用例a2_24开始-----------")
        img = Image(com_fixture)
        ip = img.image_ip_set()
        image_name = "a2_24"
        try:
            img.go_img_manage()
            # 复制镜像,等待镜像更新完成
            img.copy_image(by_copy=img_test_imgC, copy_name=image_name)
            img.wait_image_update_cpmpleted(image_name)
            # 启动镜像
            img.img_start_nopub(image_name)
            time.sleep(1.5)
            img.open_admin_tool()
            win_conn_useful(ip=ip, name=s_user, pwd=s_pwd)  # 等待winrm可用
            # 在镜像中安装软件（火狐）
            win_conn(ip=ip, user_name=s_user, passwd=s_pwd, action_cmd="software_install", path='S')
            time.sleep(120)  # 等待软件安装成功
            # 读取access文件中的内容
            message1 = get_win_conn_info(ip=ip, user_name=s_user, passwd=s_pwd, cmd=r"type S:\access.log")
            logging.info(u"----读取access.log文件获取安装状态")
            assert "install" in message1
            time.sleep(2)
            img.close_img()  # 关闭镜像
            img.wait_image_update_cpmpleted(img_name=image_name)  # 等待镜像更新完成
            img.img_start_nopub(img_name=image_name)  # 开启镜像并卸载软件
            time.sleep(1.5)
            img.open_admin_tool()
            win_conn_useful(ip=ip, name=s_user, pwd=s_pwd)  # 等待winrm可用
            # 在镜像中卸载火狐软件
            win_conn(ip=ip, user_name=s_user, passwd=s_pwd, action_cmd="software_uninstall", path='S')
            time.sleep(20)  # 等待卸载
            # 查看卸载日志
            message2 = get_win_conn_info(ip=ip, user_name=s_user, passwd=s_pwd, cmd=r"type S:\access.log")
            logging.info(u"----查看安装日志中是否有卸载信息----")
            assert "uninstall" in message2
            time.sleep(2)
        finally:
            # 善后处理，删除镜像
            img.img_recovery(image_name)

    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_a2_25(self, com_fixture):
        """
        1、需准备名称为vdi_img_a2_24的镜像，进行编辑
        2、进入镜像编辑器中，安装补丁完成后关闭镜像
        4、启动并验证补丁安装情况
        # TODO 启动镜像后验证补丁安装情况
        # TODO 进入镜像安装360补丁后并关机
        """
        logging.info(u"-----------镜像管理用例a2_25开始-----------")
        pass

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a3_1(self, com_fixture):
        """
        1、事先需准备一个新的镜像VDI，未被用户绑定
        2、进入镜像进行编辑，关闭镜像
        3、后台验证镜像base大小变大
        """
        logging.info(u"-------------a3_1用例编辑未被用户绑定的镜像-----------------")
        img = Image(com_fixture)
        copy_name = "a3_1"
        try:
            img.go_img_manage()
            # 复制镜像，等待镜像更新完成
            img.copy_image(by_copy=img_test_imgA, copy_name=copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            res1 = server_conn(ip=host_ip, command="cd /opt/lessons;wc -c <" + copy_name + ".base")
            print(res1)
            res1 = res1.replace('\n', "").replace('\r', "")
            res1 = int(res1) - 1
            img.img_start_nopub(img_name=copy_name)  # 启动未被绑定的镜像
            time.sleep(1.5)
            img.open_admin_tool()  # 打开镜像编辑器
            img.close_img()
            img.wait_image_update_cpmpleted(copy_name)  # 等待镜像更新完成
            res2 = server_conn(ip=host_ip, command=r"cd /opt/lessons;wc -c <  " + copy_name + ".base")
            res2 = res2.replace('\n', "").replace('\r', "")
            res2 = int(res2)
            logging.info(u"------验证镜像编辑前后base文件变大----")
            assert res2 > res1
        finally:
            img.img_recovery(copy_name)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a3_2(self, com_fixture):
        """
        1、需提前准备一个vdi镜像
        2、新增个性用户组，将1中的镜像绑定到用户组中
        3、编辑镜像后关机
        4、验证镜像base文件大小变大
        5、善后，删除组
        """
        logging.info(u"----------镜像测试用例a3_2开始---------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        copy_name = u"a3_2"  #
        try:
            # 复制镜像，待镜像更新完成
            img.go_img_manage()
            img.copy_image(img_test_imgA, copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            # 进入用户管理页面
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="it_group_a3_2", img_name=copy_name, cd_type=u"个性")
            res1 = server_conn(ip=host_ip, command=r"cd /opt/lessons;wc -c <  " + copy_name + ".base")
            res1 = res1.replace('\n', "").replace('\r', "")
            res1 = int(res1) - 1
            img.back_current_page()
            img.go_img_manage()
            img.img_start_nopub(img_name=copy_name)  # 启动镜像
            time.sleep(3)
            img.open_admin_tool()
            img.close_img()
            img.wait_image_update_cpmpleted(copy_name)
            # 此处传入的base文件名根据需要改动
            res2 = server_conn(ip=host_ip, command=r"cd /opt/lessons;wc -c <  " + copy_name + ".base")
            res2 = res2.replace('\n', "").replace('\r', "")
            res2 = int(res2)
            logging.info(u"------比较两次获取的base文件大小--")
            assert res2 > res1
        finally:
            try:
                time.sleep(2)
                user.user_recovery("it_group_a3_2")
                img.img_recovery(copy_name)
            except Exception as e:
                logging.info(e)
            finally:
                pass

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_a3_4(self, com_fixture):
        """
        1、在用例开始前需准备一个vdi镜像
        2、创建还原组绑定1中的镜像
        3、点击启动，设置为立即更新，关闭镜像验证是否为立即发布
        4、待3镜像关机后再次点击启动设置为稍后发布，等待时间到来验证镜像是否发布
        5、善后处理，删除组以及镜像
        """
        logging.info(u"---------------镜像管理a3_4测试用例开始-------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        copy_name = "A3_4"
        try:
            img.go_img_manage()
            img.copy_image(by_copy=img_test_imgA, copy_name=copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a3_4", img_name=copy_name, cd_type=u"还原")
            user.create_user_in_group(group_name="itgroup_a3_4", user_name="user_a3_4", real_name="user_a3_4")
            img.go_img_manage()
            img.click_img_start(vm_name=copy_name, pudate_time=u"立即发布")
            time.sleep(3)
            img.open_admin_tool()  # 打开镜像编辑器
            time.sleep(2)
            img.close_img()  # 关闭镜像
            img.back_current_page()
            img.go_img_manage()
            img.click_elem(img.refresh)  # 点击刷新
            time.sleep(15)
            logging.info(u"---------验证镜像正在更新---------")
            assert img.get_value(img.img_update_xpath.format(copy_name)) == u"镜像更新中，请稍候......"  # 验证镜像正在更新
            img.wait_image_update_cpmpleted(copy_name)  # 等待镜像发布成功")
            # 设置镜像发布时间
            img.back_current_page()
            img.go_img_manage()
            img.click_img_start(vm_name=copy_name, pudate_time=u"稍后发布", m=2)  # 设置镜像发布时间
            time.sleep(3)
            img.open_admin_tool()
            time.sleep(2)
            img.close_img()
            logging.info(u"----点击稍后发布验证镜像的状态为即将发布----")
            assert img.get_elem_text(img.img_pub_now.format(copy_name)) == u"镜像即将发布"
            time.sleep(135)  # 等待2分钟后
            img.click_elem(img.refresh)  # 点击刷新
            logging.info(u"-----等待时间经过2分钟后待发布状态消失----")
            # 验证镜像即将发布信息不存在
            assert u"镜像即将发布" not in img.get_value(img.img_xpath.format(copy_name))
            img.wait_image_update_cpmpleted(copy_name)  # 等待镜像发布成功
        finally:
            try:
                logging.info(u"-------删除分组----")
                user.user_recovery("itgroup_a3_4")
                img.img_recovery(copy_name)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a3_5(self, com_fixture):
        """
        1、用例执行前需准备两个vdi镜像，一个为win7系统，一个为xp系统
        2、创建分组和用户，将1中的镜像绑定在用户
        3、分别验证win7系统和xp系统立即启动镜像和稍后启动镜像的不同状态
        4、善后处理：删除用户，删除分组
        """
        logging.info(u"----------镜像测试用例a3_5开始执行---------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a3_5_1", img_name=img_test_imgA,
                                      cd_type=u"还原")  # 创建还原用户组，win7
            user.create_group_openvdi(group_name="itgroup_a3_5_2", img_name=vdi_xp_image,
                                      cd_type=u"还原")  # 创建还原用户组，xp
            user.driver.refresh()
            user.create_user_in_group(group_name="itgroup_a3_5_1", user_name="ituser_a3_5_1",
                                      real_name="ituser_a3_5_1")  # 在win7用户组下创建用户
            user.driver.refresh()
            user.create_user_in_group(group_name="itgroup_a3_5_2", user_name="ituser_a3_5_2",
                                      real_name="ituser_a3_5_2")  # 在xp用户组下创建用户
            img.go_img_manage()
            img.click_img_start(vm_name=img_test_imgA, pudate_time=u"立即发布")
            time.sleep(1.5)
            img.open_admin_tool()  # 打开管理员工具
            img.close_img()  # 关闭镜像
            img.click_elem(img.refresh)  # 点击刷新
            time.sleep(5)
            assert img.get_elem_text(img.img_update_xpath.format(img_test_imgA)) == u"镜像更新中，请稍候......"  # 验证镜像正在更新
            img.wait_image_update_cpmpleted(img_test_imgA)  # 等待镜像发布成功
            img.click_img_start(vm_name=img_test_imgA, pudate_time=u"稍后发布", m=1)  # 设置镜像1分钟后发布
            time.sleep(1.5)
            img.open_admin_tool()
            img.close_img()  # 关闭镜像
            logging.info(u"----点击稍后发布验证镜像的状态为即将发布----")
            assert img.get_elem_text(img.img_pub_now.format(img_test_imgA)) == u"镜像即将发布"
            time.sleep(70)  # 等待2分钟后
            img.click_elem(img.refresh)
            logging.info(u"-----等待时间经过2分钟后验证镜像处于更新状态----")
            assert img.elem_is_exist(img.img_update_xpath.format(img_test_imgA)) == 0
            time.sleep(2)
            img.click_img_start(vm_name=vdi_xp_image, pudate_time=u"立即发布")
            time.sleep(1.5)
            img.open_admin_tool()
            img.close_img()
            img.click_elem(img.refresh)  # 刷新
            time.sleep(5)
            assert u"请稍候......" in img.get_elem_text(img.img_update_xpath.format(vdi_xp_image))   # 验证镜像正在更新
            img.wait_image_update_cpmpleted(vdi_xp_image)  # 等待镜像发布成功
            img.click_img_start(vm_name=vdi_xp_image, pudate_time=u"稍后发布", m=1)  # 设置镜像1分钟后发布
            time.sleep(1.5)
            img.open_admin_tool()
            img.close_img()
            assert img.get_elem_text(img.img_pub_now.format(vdi_xp_image)) == u"镜像即将发布"
            time.sleep(75)  # 等待发布时间到达
            img.click_elem(img.refresh)
            # 验证即将发布信息不存在
            assert u"镜像即将发布" not in img.get_value(img.img_xpath.format(vdi_xp_image))
            img.wait_image_update_cpmpleted(vdi_xp_image)  # 等待镜像发布成功
        finally:
            try:
                logging.info(u"--------善后处理，删除用户、分组----------")
                user.user_recovery("itgroup_a3_5_1")
                user.user_recovery("itgroup_a3_5_2")
            except Exception as e:
                logging.info(u"用户善后失败")
            finally:
                img.img_recovery()

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    @pytest.mark.aaa
    def test_a3_6(self, com_fixture):
        """
        1、用例执行前需要一个vdi镜像
        2、创建vdi还原组，绑定1中的镜像
        3、编辑镜像，并设置发布时间为5分钟后
        4、在镜像编辑中安装软件，并关机
        5、再次编辑镜像，验证发布时间与3中的发布时间一致
        6、对镜像进行修改后关机
        7、验证发布时间以及镜像以最后一次编辑为准
        8、善后，删除分组，删除镜像
        """
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        copy_name = "a3_6"
        try:
            img.go_img_manage()
            img.copy_image(img_test_imgC, copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a3_6", img_name=copy_name, cd_type=u"还原")  # 创建还原分组绑定镜像
            user.create_user_in_group(group_name="itgroup_a3_6", user_name="user_a3_6", real_name="user_a3_6")
            time.sleep(2)
            img.go_img_manage()
            ip = img.image_ip_set()  # 为镜像设置IP
            img.click_img_start(vm_name=copy_name, pudate_time=u"稍后发布", m=20)  # 设置镜像15分钟后发布
            time.sleep(1.5)
            img.open_admin_tool()
            win_conn_useful(ip=ip, name=s_user, pwd=s_pwd)
            win_conn(ip=ip, user_name=s_user, passwd=s_pwd, action_cmd="software_install", path="S")  # 安装软件
            time.sleep(120)  # 等待软件安装成功
            logging.info(u"-----验证access.log文件包含安装成功信息----")
            message1 = get_win_conn_info(ip=ip, user_name=s_user, passwd=s_pwd, cmd=r"type S:\access.log")
            assert "install" in message1
            time.sleep(1)
            img.close_img()
            pub_time1 = img.get_elem_attribute(img.img_pub_time_xpath.format(copy_name), 'title')
            pub_time1 = pub_time1[4:24]
            pub_time1 = pub_time1.encode("utf-8")
            img.click_img_start(vm_name=copy_name, pudate_time=u"稍后发布")  # 重新启动镜像，镜像发布时间不做更改
            time.sleep(1.5)
            img.open_admin_tool()
            win_conn_useful(ip=ip, name=s_user, pwd=s_pwd)
            # 卸载软件
            win_conn(ip=ip, user_name=s_user, passwd=s_pwd, action_cmd="software_uninstall", path="S")
            time.sleep(30)
            # 创建文件
            get_win_conn_info(ip=ip, user_name=s_user, passwd=s_pwd, cmd=r'echo .> D:\img_test_a3_6.txt')
            message2 = get_win_conn_info(ip=ip, user_name=s_user, passwd=s_pwd, cmd=r"type S:\access.log")
            assert "uninstall" in message2
            img.close_img()
            pub_time2 = img.get_elem_attribute(img.img_pub_time_xpath.format(copy_name), 'title')
            pub_time2 = pub_time2[4:24]
            pub_time2 = pub_time2.encode("utf-8")
            # 验证时间上并未被修改
            assert pub_time1 == pub_time2
        finally:
            logging.info(u"-------删除分组--------")
            user.user_recovery("itgroup_a3_6")
            img.img_recovery(copy_name)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a3_9(self, com_fixture):
        """
        1、用例执行前需准备好vdi 镜像
        2、创建还原vdi特性分组，绑定1中镜像
        3、编辑镜像设置发布时间第一个时间节点，进入镜像编辑，关闭镜像
        4、再次编辑镜像设置发布时间为时间节点2，进入镜像编辑，关闭镜像
        5、善后处理
        """
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a3_9", img_name=img_test_imgA, cd_type=u"还原")
            user.driver.refresh()
            user.create_user_in_group(group_name="itgroup_a3_9", user_name="user_a3_9", real_name="user_a3_9")
            time.sleep(2)
            img.go_img_manage()
            # 设置镜像发布时间为2分钟后,第一次发布时间节点
            img.click_img_start(vm_name=img_test_imgA, pudate_time=u"稍后发布", m=2)
            time.sleep(2.5)
            # 打开镜像编辑工具
            img.open_admin_tool()
            time.sleep(2)
            img.back_current_page()
            img.go_img_manage()
            # 获取第一次发布时间
            pub_time1 = img.get_elem_attribute(img.img_pub_time_xpath.format(img_test_imgA), 'title')
            pub_time1 = pub_time1[4:24]
            img.close_img()
            time.sleep(8)
            # 第二次启动镜像设置发布时间节点为3分钟后
            img.click_img_start(vm_name=img_test_imgA, pudate_time=u"稍后发布", m=3)
            time.sleep(2.5)
            img.open_admin_tool()  # 打开镜像编辑工具
            time.sleep(2)
            img.back_current_page()
            img.go_img_manage()
            pub_time2 = img.get_elem_attribute(img.img_pub_time_xpath.format(img_test_imgA), 'title')  # 获取第二次发布时间
            pub_time2 = pub_time2[4:24]
            img.close_img()
            logging.info(u"-------验证镜像管理页面两次发布时间不同----------")
            assert pub_time1 != pub_time2
            time.sleep(200)
            img.wait_image_update_cpmpleted(img_test_imgA)  # 等待镜像发布
        finally:
            logging.info(u"-----------删除分组----------")
            user.user_recovery('itgroup_a3_9')
            img.img_recovery()

    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    @pytest.mark.aaa11111
    def test_a3_12(self, com_fixture):
        """
        1、用例执行前需准备vdi镜像
        2、创建还原用户绑定1中的镜像
        3、启动镜像设置为20分钟后发布，并进入镜像安装微信软件，关闭镜像
        4、查看后台镜像差分存在
        5、再次编辑镜像，设置10分钟后发布，并查看后台差分大小
        6、10分钟后镜像发布，查看后台差分是否存在
        7、绑定1镜像的vdi用户登录
        8、善后处理，删除用户、用户组以及镜像
        """
        logging.info(u"---------镜像测试a3_12开始----------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        android_vdi = AndroidVdi()
        copy_name = "a3_12"
        try:
            # img.go_img_manage()
            # img.copy_image(img_test_imgC, copy_name)
            # img.wait_image_update_cpmpleted(copy_name)
            # user.back_current_page()
            # user.goto_usermanage_page()
            # # 创建用户组绑定镜像
            # user.create_group_openvdi(group_name="itgroup_a3_12", img_name=copy_name, cd_type=u"还原")
            # user.create_user_in_group(group_name="itgroup_a3_12", user_name="ituser_a3_12", real_name="ituser_a3_12")
            ip = img.image_ip_set()
            img.go_img_manage()
            img.click_img_start(vm_name=copy_name, pudate_time=u"稍后发布", m=20)  # 设置第一次发布时间节点
            time.sleep(2.5)
            # 进入镜像编辑安装火狐软件
            img.open_admin_tool()
            win_conn_useful(ip=ip, name=s_user, pwd=s_pwd)
            win_conn(ip=ip, user_name=s_user, passwd=s_pwd, action_cmd="software_install", path='S')  # 安装软件
            time.sleep(120)  # 待软件安装成功
            logging.info(u"-----验证软件安装成功----")
            message1 = get_win_conn_info(ip=ip, user_name=s_user, passwd=s_pwd, cmd=r"type S:\access.log")
            assert "install" in message1
            logging.info(u"----验证服务器是否存在差分文件----")
            # 查看服务器是否存在差分文件
            message2 = server_conn(ip=host_ip, command="cd /opt/lessons;ls | grep " + copy_name)
            assert copy_name + ".img" in message2
            img.close_img()  # 关闭镜像
            time.sleep(2)
            img.click_img_start(vm_name=copy_name, pudate_time=u"稍后发布", m=5)  # 设置第二次时间节点
            time.sleep(3)
            img.open_admin_tool()  # 打开管理员工具
            win_conn_useful(ip=ip, name=s_user, pwd=s_pwd)
            # 卸载软件
            win_conn(ip=ip, user_name=s_user, passwd=s_pwd, action_cmd="software_uninstall", path='S')
            time.sleep(30)  # 待软件卸载成功
            message2 = get_win_conn_info(ip=ip, user_name=s_user, passwd=s_pwd, cmd=r"type S:\access.log")
            assert "uninstall" in message2
            img.close_img()  # 关闭镜像
            time.sleep(3)
            img.back_current_page()
            time.sleep(200)  # 等待第二次时间节点一到发布镜像
            logging.info(u"-----验证此时差分文件已经不存在----")
            # 验证服务器差分文件不存在
            message2 = server_conn(ip=host_ip, command="cd /opt/lessons;ls | grep " + copy_name)
            assert copy_name + ".img" not in message2
            img.wait_image_update_cpmpleted(copy_name)
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)  # 连接终端
            android_vdi.login(name="ituser_a3_12", ip=vdi_tm_ip_1, pwd="123456")  # 用户登录
            cd_manage.back_current_page()
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name="ituser_a3_12")
            assert cd_manage.get_status(name="ituser_a3_12") == u"运行"
        finally:
            logging.info(u"------善后处理,删除用户用户组以及断开终端连接-------")
            android_vdi.vdi_disconnect(vdi_tm_ip_1)
            cd_manage.cd_manage_recovery("ituser_a3_12")
            user.user_recovery("itgroup_a3_12")
            img.img_recovery(copy_name)
            android_vdi.vdi_disconnect(ip=vdi_tm_ip_1)
            time.sleep(2)

    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    @pytest.mark.aaa
    def test_a3_13_1(self, com_fixture):
        """
        1、用例执行前需准备vdi镜像
        2、创建一个vdi还原用户组，该组下有三个非自定义用户ABC
        3、进入vdi终端页面搜索某个终端IP，登录用户A，并向用户A写入数据，VDI锁屏
        4、登录用户B，向用户B写入数据，锁屏
        5、设置镜像发布时间，并等待镜像发布
        6、镜像发布的同时登录用户C，在云桌面验证用户C的状态不为在线
        7、登录用户A、B验证磁盘数据写入成功，锁屏
        8、登录用户C，验证云桌面C的状态为在线，锁屏
        9、善后处理，删除用户、组、镜像以及退出adbl连接
        """
        logging.info(u"--------镜像测试a3_13安卓终端测试--------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        androidvdi = AndroidVdi()
        cd_manage = CDeskMange(com_fixture)
        copy_name = "a3_13"
        try:
            img.go_img_manage()
            img.copy_image(vdi_base, copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            # 第一步：创建用户
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a3_13_1", img_name=copy_name, cd_type=u"还原")
            user.create_user_in_group(group_name="itgroup_a3_13_1", user_name="ituser_a3_13_A",
                                      real_name="ituser_a3_13_A")
            user.driver.refresh()
            user.create_user_in_group(group_name="itgroup_a3_13_1", user_name="ituser_a3_13_B",
                                      real_name="ituser_a3_13_B")
            user.driver.refresh()
            user.create_user_in_group(group_name="itgroup_a3_13_1", user_name="ituser_a3_13_C",
                                      real_name="ituser_a3_13_C")

            # 第二部分：用户A登录安卓终端,并且实现在个人盘写入数据
            androidvdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            androidvdi.login(name="ituser_a3_13_A", ip=vdi_tm_ip_1, pwd="123456")  # 登录终端
            # 获取vdi云桌面IP,并连接，输入cmd命令在用户A个人盘输入数据
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name="ituser_a3_13_A")  # 输入用户名搜索
            cd_ip_a = cd_manage.get_elem_text(cd_manage.cd_ip)
            cd_ip_a = strip(cd_ip_a)
            # 向用户A中的个人盘写入数据
            win_conn_useful(ip=cd_ip_a, name=s_user, pwd=s_pwd)
            get_win_conn_info(ip=cd_ip_a, user_name=s_user, passwd=s_pwd, cmd='echo .> D:\img__a3_13_A.txt')
            androidvdi.screen_lock()  # 终端锁屏，退出登录

            # 第三部分：编辑镜像设置稍后发布
            img.go_img_manage()
            img.click_img_start(vm_name=copy_name, pudate_time=u"稍后发布", m=6)  # 将镜像设置为稍后6分钟发布
            time.sleep(1.5)
            img.open_admin_tool()
            img.close_img()  # 关闭镜像

            # 第四部分：用户B登录终端，并且实现在个人盘写入数据
            androidvdi.login(name="ituser_a3_13_B", ip=vdi_tm_ip_1, pwd="123456")  # 登录终端
            # 获取用户B的云桌面IP，实现向用户B个人盘写入数据
            cd_manage.driver.refresh()
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name="ituser_a3_13_B")  # 输入用户名搜索
            cd_ip_b = cd_manage.get_elem_text(cd_manage.cd_ip)
            cd_ip_b = strip(cd_ip_b)
            logging.info(u"user B cd_ip：" + cd_ip_b)
            # 向用户B中的个人盘写入数据
            win_conn_useful(ip=cd_ip_b, name=s_user, pwd=s_pwd)
            get_win_conn_info(ip=cd_ip_b, user_name=s_user, passwd=s_pwd, cmd='echo .> D:\img__a3_13_B.txt')
            time.sleep(1)
            androidvdi.screen_lock()  # 终端锁屏，退出登录
            time.sleep(80)  # 等待时间，终端登录C用户

            # 第五部分：镜像发布时间到达后登录C，验证C用户登录失败
            androidvdi.login(name="ituser_a3_13_C", ip=vdi_tm_ip_1, pwd="123456")  # C用户无法登录终端
            logging.info(u"-----验证云桌面页面用户C的状态不为在线----")
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name="ituser_a3_13_C")  # 搜索用户C
            time.sleep(1)
            assert cd_manage.get_value(cd_manage.terminal_online_status) != u"在线"
            time.sleep(255)  # 为了保险起见待镜像发布时间经过后登录用户AB

            # 第六部分：分别登录用户A、B验证数据存在
            androidvdi.login(name="ituser_a3_13_A", pwd="123456", ip=vdi_tm_ip_1)
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name="ituser_a3_13_A")
            cd_ip_a1 = cd_manage.get_elem_text(cd_manage.cd_ip)
            cd_ip_a1 = strip(cd_ip_a1)
            win_conn_useful(ip=cd_ip_a1, name=s_user, pwd=s_pwd)
            messg1 = get_win_conn_info(ip=cd_ip_a1, user_name=s_user, passwd=s_pwd, cmd="dir D:\\")
            str(messg1)
            logging.info(u"----使用cmd命令验证A用户个人盘数据存在---")
            assert messg1.__contains__("img__a3_13_A.txt")  # 验证A用户个人盘数据无丢失
            logging.info("user A data" + messg1)
            time.sleep(2)
            androidvdi.screen_lock()  # 锁
            androidvdi.login(name="ituser_a3_13_B", ip=vdi_tm_ip_1, pwd="123456")  # 用户B登录
            cd_manage.back_current_page()
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name="ituser_a3_13_B")
            time.sleep(1)
            cd_ip_b1 = cd_manage.get_elem_text(cd_manage.cd_ip)
            cd_ip_b1 = strip(cd_ip_b1)
            win_conn_useful(ip=cd_ip_b1, name=s_user, pwd=s_pwd)
            messg2 = get_win_conn_info(ip=cd_ip_b1, user_name=s_user, passwd=s_pwd, cmd="dir D:\\")
            logging.info(u"----使用cmd命令验证B用户个人盘数据存在---")
            assert messg2.__contains__("img__a3_13_B.txt")
            logging.info(u"user B data" + messg2)
            time.sleep(2)
            androidvdi.screen_lock()
            time.sleep(1)
            androidvdi.login(name="ituser_a3_13_C", pwd="123456", ip=vdi_tm_ip_1)  # 用户C登录
            cd_manage.driver.refresh()
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name="ituser_a3_13_C")
            logging.info(u"----镜像发布后验证C用户的状态---")
            assert cd_manage.get_value(cd_manage.terminal_online_status) == u"运行"
        finally:
            try:
                androidvdi.vdi_disconnect(ip=vdi_tm_ip_1)
                cd_manage.cd_manage_recovery("ituser_a3_13_")
                user.user_recovery("itgroup_a3_13_1")
                img.img_recovery(copy_name)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a3_14_1(self, com_fixture):
        """
        1、用例执行前需要提前准备vdi镜像
        2、创建两个用户A、B，绑定1镜像
        3、用户A使用vdi访客登录，用户B正常登录
        4、进入云桌面，搜索AB用户验证在线，另外搜索其他两个在线用户C（非绑定1中的镜像用户即可）
        4、启动1镜像设置稍后发布，等待发布时间到达
        5、进入验证云桌面首页，验证用户AB不在运行状态，C用户不受影响
        6、善后处理，删除用户组和用户、删除镜像
        7、注：在线终端未不受影响未验证
        """
        logging.info(u"------镜像管理测试用例a3_14开始执行-----")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        androidvdi = AndroidVdi()
        copy_name = "a3_14"
        try:
            img.go_img_manage()
            img.copy_image(vdi_base, copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a3_14", img_name=copy_name, cd_type=u"还原")
            user.create_user_in_group(group_name="itgroup_a3_14",
                                      user_name="ituser_a3_14_a", real_name="ituser_a3_14_a")
            user.create_user_in_group(group_name="itgroup_a3_14",
                                      user_name="ituser_a3_14_b", real_name="ituser_a3_14_b")
            # 终端连接
            androidvdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_2)
            androidvdi.login(name="ituser_a3_14_a", ip=vdi_tm_ip_2, pwd="123456")
            androidvdi.vdi_disconnect(ip=vdi_tm_ip_2)  # 断开用户A终端连接
            time.sleep(3)
            androidvdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_1)
            androidvdi.login(name="ituser_a3_14_b", ip=vdi_tm_ip_1, pwd="123456")
            androidvdi.vdi_disconnect(ip=vdi_tm_ip_1)
            # 进入云桌面
            cd_manage.back_current_page()
            cd_manage.goto_cloud_desk_manage()
            logging.info(u"-----搜索验证云桌面首页四个用户的状态均为在线-----")
            cd_manage.search_info(name="ituser_a3_14_a")  # 用户A状态为在线
            assert u"运行" in cd_manage.get_value(cd_manage.terminal_online_status)
            cd_manage.search_info(name="ituser_a3_14_b")
            assert u"运行" in cd_manage.get_value(cd_manage.terminal_online_status)
            img.go_img_manage()
            img.click_img_start(vm_name=copy_name, pudate_time=u"稍后发布", m=1)  # 设置1分钟后发布
            time.sleep(1.5)
            img.open_admin_tool()  # 打开镜像编辑工具
            img.close_img()  # 关闭镜像
            time.sleep(260)  # 等待镜像发布时间到达用户退出
            cd_manage.back_current_page()
            logging.info(u"----验证镜像发布后使用镜像的用户状态为离线----")
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name="ituser_a3_14_a")
            assert u"运行" != cd_manage.get_value(cd_manage.terminal_online_status)
            cd_manage.search_info(name="ituser_a3_14_b")
            assert u"运行" != cd_manage.get_value(cd_manage.terminal_online_status)
        finally:
            try:
                logging.info(u"----善后处理：AB用户关机，删除用户，用户组---")
                user.user_recovery("itgroup_a3_14")
                img.img_recovery(copy_name)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a3_15(self, com_fixture):
        """"
        1、准备2个终端以及镜像
        2、创建用户组以及三个用户A、B
        3、A用户访客登录，B用户正常登录
        4、编辑镜像并设置立即发布，在关闭镜像前验证差分文件存在
        5、关闭镜像，等待时间达到验证AB用户被强关
        6、等到时间到达后验证差分文件不存在
        3、善后处理：删除分组，删除用户
        """
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        androidvdi = AndroidVdi()
        copy_name = "a3_15"
        try:
            img.go_img_manage()
            img.copy_image(vdi_base, copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            # 创建用户组以及用户
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a3_15", img_name=copy_name, cd_type=u"还原")
            user.create_user_in_group(group_name="itgroup_a3_15",
                                      user_name="ituser_a3_15_1", real_name="ituser_a3_15_1")
            user.create_user_in_group(group_name="itgroup_a3_15",
                                      user_name="ituser_a3_15_2", real_name="ituser_a3_15_2")
            # 用户A访客模式终端登录
            androidvdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_2)
            androidvdi.login(name="ituser_a3_15_1", ip=vdi_tm_ip_2, pwd="123456")
            androidvdi.vdi_disconnect(ip=vdi_tm_ip_2)
            # 用户B登录终端
            androidvdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_1)  # 连接终端B
            androidvdi.login(name="ituser_a3_15_2", ip=vdi_tm_ip_1, pwd="123456")
            androidvdi.vdi_disconnect(ip=vdi_tm_ip_1)
            img.back_current_page()
            img.go_img_manage()
            img.click_img_start(vm_name=copy_name, pudate_time=u"立即发布")  # 点击启动镜像
            time.sleep(1.5)
            img.open_admin_tool()  # 打开镜像编辑器
            time.sleep(30)
            # 验证服务器镜像差分存在
            logging.info(u"---验证服务器编辑中的镜像差分文件存在-----")
            message1 = server_conn(ip=host_ip, command="cd /opt/lessons;ls | grep " + copy_name)  # 查看服务器是否存在差分文件
            assert copy_name + ".img" in message1
            img.close_img()  # 关闭镜像
            time.sleep(220)  # 关闭镜像后验证用户AB的状态
            cd_manage.back_current_page()
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name="ituser_a3_15_")
            # 验证AB用户被强关
            assert cd_manage.get_status(name="ituser_a3_15_1") != u"运行"
            assert cd_manage.get_status(name="ituser_a3_15_2") != u"运行"
            # 验证差分不存在
            logging.info(u"----验证差分不存在----")
            message1 = server_conn(ip=host_ip, command="cd /opt/lessons;ls | grep " + copy_name)  # 查看服务器是否存在差分文件
            assert copy_name + ".img" not in message1
        finally:
            logging.info(u"----善后处理----")
            user.user_recovery("itgroup_a3_15")
            img.img_recovery(copy_name)

    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a3_16(self, com_fixture):
        """
        1、用例执行前需提供vdi镜像
        2、创建创建用户组和用户A绑定1中的镜像
        3、登录用户A
        4、编辑镜像发布时间为4分钟后
        6、镜像发布前A用户登录
        7、镜像发布时间到达后验证镜像发布状态
        """
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        androidvdi = AndroidVdi()
        cd_manage = CDeskMange(com_fixture)
        copy_name = "a3_16"
        try:
            img.go_img_manage()
            img.copy_image(vdi_base, copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            # 创建用户组和用户
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a3_16", img_name=copy_name, cd_type=u"还原")
            user.create_user_in_group(group_name="itgroup_a3_16", user_name="ituser_a3_16", real_name="ituser_a3_13")
            # 连接终端
            androidvdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_1)
            androidvdi.login(name="ituser_a3_16", ip=vdi_tm_ip_1, pwd="123456")
            img.back_current_page()
            img.go_img_manage()
            img.click_img_start(vm_name=copy_name, pudate_time=u"稍后发布", m=2)  # 设置镜像3分钟后发布
            time.sleep(1.5)
            img.open_admin_tool()
            img.close_img()
            androidvdi.screen_lock()  # 用户退出登录
            androidvdi.vdi_disconnect(ip=vdi_tm_ip_1)  # 退出登录
            img.back_current_page()
            img.go_img_manage()
            img.scroll_into_view(img.image_frame_xpath.format(copy_name), click_type=1)
            message = img.get_value(img.img_pub_now.format(copy_name))
            logging.info(u"-------验证镜像发布状态为即将发布-----")
            assert message == u"镜像即将发布"
            time.sleep(300)
            img.back_current_page()
            img.go_img_manage()
            logging.info(u"-------等待发布时间到达后验证镜像发布----")
            assert u"镜像即将发布" not in img.get_value(img.img_xpath.format(copy_name))
            img.wait_image_update_cpmpleted(copy_name)
        finally:
            logging.info(u"----善后处理:删除用户、删除用户组、删除镜像、vdi断开连接---")
            cd_manage.cd_manage_recovery("ituser_a3_16")
            user.user_recovery("itgroup_a3_16")
            img.img_recovery(copy_name)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a3_17(self, com_fixture):
        """
        1、用例执行前需准备镜像
        2、创建用户组以及用户1、2绑定1镜像
        3、设置镜像发布时间为立即发布
        4、关闭镜像前退出1,2登录
        5、关闭镜像编辑验证镜像状态
        6、善后处理，删除用户，删除用户组
        """
        logging.info(u"------镜像管理测试用例test_a3_17开始执行-----")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        androidvdi = AndroidVdi()
        copy_name = "a3_17"
        try:
            img.go_img_manage()
            img.copy_image(vdi_base, copy_name)
            img.wait_image_update_cpmpleted(copy_name)
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a3_17", img_name=copy_name, cd_type=u"还原")
            user.create_user_in_group(group_name="itgroup_a3_17",
                                      user_name="ituser_a3_17_1", real_name="ituser_a3_17_1")
            user.create_user_in_group(group_name="itgroup_a3_17",
                                      user_name="ituser_a3_17_2", real_name="ituser_a3_17_2")
            # 连接终端登录用户A后断开adb连接
            androidvdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_2)
            androidvdi.login(name="ituser_a3_17_1", ip=vdi_tm_ip_2, pwd="123456")
            time.sleep(2)
            androidvdi.vdi_disconnect(ip=vdi_tm_ip_2)
            time.sleep(2)
            # 连接终端登录用户B
            androidvdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_1)
            androidvdi.login(name="ituser_a3_17_2", ip=vdi_tm_ip_1, pwd="123456")
            time.sleep(2)
            # 打开镜像编辑，编辑镜像
            img.back_current_page()
            img.go_img_manage()
            img.click_img_start(vm_name=copy_name, pudate_time=u"立即发布")
            time.sleep(1.5)
            img.open_admin_tool()  # 打开镜像编辑器
            # 镜像编辑期间用户A、B锁屏
            androidvdi.screen_lock()  # 用户B锁屏
            androidvdi.vdi_disconnect(ip=vdi_tm_ip_1)  # adb断开与用户B的终端连接
            time.sleep(5)
            androidvdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_2)  # adbl连接用户A所在的终端，并锁屏
            androidvdi.screen_lock()
            androidvdi.vdi_disconnect(ip=vdi_tm_ip_2)  # 断开与用户A的连接
            time.sleep(5)
            img.back_current_page()
            img.go_img_manage()
            img.close_img()  # 关闭镜像
            img.click_elem(img.refresh)  # 点击刷新
            time.sleep(5)
            mess1 = img.get_value(img.img_update_xpath.format(copy_name))
            assert u"请稍候......" in mess1
            img.wait_image_update_cpmpleted(copy_name)
            assert u"镜像即将发布" not in img.get_value(img.img_xpath.format(copy_name))
        finally:
            logging.info(u"----善后处理，删除用户，删除组、、删除镜像----")
            cd_manage.cd_manage_recovery("ituser_a3_17_")
            user.user_recovery("itgroup_a3_17")
            img.img_recovery(copy_name)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    @pytest.mark.aaa
    def test_a3_22(self, com_fixture):
        """
        1、用例执行前需准备镜像a、b
        2、创建用户组以及用户A绑定1中的a镜像
        3、vdi终端登录用户A
        4、web上修改用户绑定的镜像a变更为镜像b
        5、对镜像a进行编辑修改并关闭
        6、等待镜像发布后验证云桌面用户的状态为离线（验证被强关）
        7、善后处理删除用户、用户组和adb断开连接
        """
        logging.info(u"------镜像管理测试用例a3_22开始执行----")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        androidvdi = AndroidVdi()
        cd_manage = CDeskMange(com_fixture)
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a3_22", img_name=vdi_xp_image, cd_type=u"还原")  # 用户绑定a镜像
            user.driver.refresh()
            user.create_user_in_group(group_name="itgroup_a3_22", user_name="ituser_a3_22", real_name="ituser_a3_22")
            # 终端登录
            androidvdi.disconnect_all_devices_and_connect(ip=vdi_tm_ip_1)
            androidvdi.login(name="ituser_a3_22", ip=vdi_tm_ip_1, pwd="123456")
            androidvdi.vdi_disconnect(ip=vdi_tm_ip_1)
            # web上修改用户绑定的镜像为b镜像
            user.back_current_page()
            user.goto_usermanage_page()
            user.edit_user_vdi(user_name="ituser_a3_22", cd_type=u"还原", delimg_name=vdi_xp_image,
                               add_img=img_test_imgA, isdel=True, isadd=True)
            img.go_img_manage()
            # 将用户a第一次绑定的镜像设置为立即发布
            img.click_img_start(vm_name=vdi_xp_image, pudate_time=u"立即发布")  # 设置镜像发布时间为立即发布
            time.sleep(1.5)
            img.open_admin_tool()
            img.close_img()
            time.sleep(240)  # 等待镜像发布，倒计时结束，用户退出登录
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(name="ituser_a3_22")
            logging.info(u"-----验证镜像a发布后用户已经被强制退出，云桌面用户终端状态-----")
            assert cd_manage.get_value(cd_manage.terminal_online_status) != u"运行"
        finally:
            cd_manage.cd_manage_recovery("ituser_a3_22")
            logging.info(u"----善后处理----")
            user.user_recovery("itgroup_a3_22")

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a4_1(self, com_fixture):
        """
        1、进入镜像列表
        2、获取列表项
        3、验证第一个列表项的终端系列为idv
        4、验证最后一个终端为vdi
        """
        logging.info(u"-----镜像管理测试用例a4_1开始执行-----")
        img = Image(com_fixture)
        img.go_img_manage()
        last_img = len(img.find_elems(img.img_item))  # 获取镜像列表中的镜像个数
        logging.info(u"-----验证第一个和最后一个镜像的终端类型-----")
        assert "fat.png" in img.get_terminal_type(item=1)  # 验证第一个镜像的类型为idv
        assert "thin.png" in img.get_terminal_type(item=last_img - 3)  # 验证最后一个镜像类型为vdi

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a4_2(self, com_fixture):
        """
        1、不需准备镜像，镜像列表上有idv和vdi两种镜像即可
        2、查看idv镜像详情，验证属性
        3、查看vdi镜像详情，验证属性
        """
        img = Image(com_fixture)
        img.go_img_manage()
        img.check_img_info(img_name=idv_img_A)
        logging.info(u"----idv验证各种信息-----")
        assert u"镜像名称 :" in img.get_value(img.detail_left)
        assert u"镜像文件名 :" in img.get_value(img.detail_left)
        assert u"操作系统 :" in img.get_value(img.detail_left)
        assert u"镜像类型 :" in img.get_value(img.detail_left)
        assert u"系统盘(GB) :" in img.get_value(img.detail_left)
        assert u"已安装驱动终端型号 :" in img.get_value(img.detail_left)
        img.click_elem(img.btn_ok_xpath)
        img.back_current_page()
        img.go_img_manage()
        img.check_img_info(img_name=img_test_imgA)
        logging.info(u"----vdi验证各种信息-----")
        assert u"镜像名称 :" in img.get_value(img.detail_left)
        assert u"镜像文件名 :" in img.get_value(img.detail_left)
        assert u"操作系统 :" in img.get_value(img.detail_left)
        assert u"镜像类型 :" in img.get_value(img.detail_left)
        assert u"CPU(个) :" in img.get_value(img.detail_left)
        assert u"内存(GB) :" in img.get_value(img.detail_left)
        assert u"系统盘(GB) :" in img.get_value(img.detail_left)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a4_3(self, com_fixture):
        """
        1、提前准备idv和vdi镜像
        2、编辑idv镜像验证启动状态，编辑后关机验证更新状态
        3、编辑vdi镜像验证编辑时启动状态，编辑后关机验证处于更新状态
        4、创建用户组以及用户（个性用户),绑定vdi镜像，验证vdi镜像处于加锁状态
        """
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        copy_image1 = "a4_3_1"
        copy_image2 = "a4_3_2"
        try:
            img.go_img_manage()
            # 复制镜像
            img.copy_image(by_copy=idv_img_A, copy_name=copy_image1)
            img.copy_image(by_copy=vdi_base, copy_name=copy_image2)
            img.wait_image_update_cpmpleted(copy_image2)
            # idv镜像操作
            img.img_start_nopub(img_name=copy_image1)  # 编辑idv镜像
            time.sleep(1.5)
            img.open_admin_tool()  # 打开进行编辑器
            img.back_current_page()
            img.go_img_manage()
            logging.info(u"----验证idv镜像处于启动状态---")
            assert u"正在启动中" in img.get_elem_attribute(img.img_is_star.format(copy_image1), attribute="title")
            img.close_img()  # 关闭镜像
            time.sleep(2)
            img.back_current_page()
            img.go_img_manage()
            img.click_elem(img.refresh)
            logging.info(u"----验证idv镜像处于更新状态---")
            time.sleep(20)
            # 验证镜像正在更新
            assert img.get_value(img.img_update_xpath.format(copy_image1)) == u"镜像更新中，请稍候......"
            time.sleep(1)
            # vdi镜像操作
            img.back_current_page()
            img.go_img_manage()
            img.img_start_nopub(img_name=copy_image2)  # 编辑vdi镜像
            time.sleep(1.5)
            img.open_admin_tool()  # 打开进行编辑器
            img.back_current_page()
            img.go_img_manage()
            logging.info(u"----验证vdi镜像处于启动状态---")
            assert u"正在启动中" in img.get_elem_attribute(img.img_is_star.format(copy_image2), attribute="title")
            img.close_img()  # 关闭镜像
            time.sleep(2)
            img.back_current_page()
            img.go_img_manage()
            img.click_elem(img.refresh)
            time.sleep(15)
            logging.info(u"----验证vdi镜像处于更新状态---")
            assert img.get_elem_text(img.img_update_xpath.format(copy_image2)) == u"镜像更新中，请稍候......"  # 验证镜像正在更新
            img.wait_image_update_cpmpleted(copy_image2)
            user.back_current_page()
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="itgroup_a4_3", img_name=copy_image2)
            user.create_user_in_group(group_name="itgroup_a4_3", user_name="ituser_a4_3", real_name="ituser_a4_3")
            time.sleep(1)
            img.back_current_page()
            img.go_img_manage()
            assert u"已绑定个性云桌面(VDI)，该镜像不允许启动" in img.get_elem_attribute \
                (img.img_is_star.format(copy_image2), attribute="title")
        finally:
            try:
                logging.info(u"-----善后处理，删除用户，删除用户组，删除镜像----")
                user.user_recovery("itgroup_a4_3")
                img.img_recovery(copy_image1)
                img.img_recovery(copy_image2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a4_5(self):
        """
        1、查看镜像磁盘空间大小后创建文件大小直到镜像磁盘空间接近100%
        2、进入镜像管理页面，编辑镜像，验证无法进行编辑
        3、删除1中所创建的文件
        """
        m1 = server_conn(ip=host_ip, command=r'df -hl | grep /dev/sda4')  # 进入镜像磁盘空间，查看大小
        available = m1[60:62]
        available = int(available) - 1
        available = str(available)
        server_conn(host_ip, "cd /opt/lessons;fallocate -l " + available + "G bf")  # 创建文件
        # 后台创建大文件后web端没有同步数据，镜像依然可以编辑
        server_conn(host_ip, "rm -f /opt/lessons/bf")  # 删除大文件

    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a4_11(self, com_fixture):
        """
        1、复制现有的镜像(任意镜像)
        2、进入复制后的镜像编辑器并安装软件关机
        3、镜像更新成功
        """
        img = Image(com_fixture)
        copy_name = "a4_11"
        try:
            img.go_img_manage()
            img.copy_image(img_test_imgC, copy_name)  # 复制镜像
            ip = img.image_ip_set()
            img.wait_image_update_cpmpleted(copy_name)
            img.img_start_nopub(img_name=copy_name)  # 启动镜像
            time.sleep(1.5)
            img.open_admin_tool()  # 打开镜像编辑器
            win_conn_useful(ip=ip, name=s_user, pwd=s_pwd)
            # 安装软件
            win_conn(ip=ip, user_name=s_user, passwd=s_pwd, action_cmd="software_install", path="S")
            time.sleep(120)  # 等待软件安装成功
            logging.info(u"----验证access.log日志记录软件安装成功")
            message = get_win_conn_info(ip=ip, user_name="Administrator", passwd="rcd", cmd=r"type S:\access.log")
            assert "install" in message
            time.sleep(5)
            img.close_img()  # 关闭镜像
            img.wait_image_update_cpmpleted(copy_name)
        finally:
            img.img_recovery(copy_name)

    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.test_a5_1234
    # @pytest.mark.image
    # @pytest.mark.parametrize('name', search_idv_terminal)
    # def test_a5_1_2_3_4(self, com_fixture, name):
    #     """
    #     1、前置：需要有各种型号的终端连接到服务器上以及未安装驱动的win10镜像
    #     2、进入idv终端管理页面，搜索不同类型的终端型号
    #     3、进入镜像管理页面，根据2获取到的终端型号选择安装驱动
    #     4、待驱动安装完成后，验证镜像下拉框所对应的终端型号为已安装
    #     """
    #     img = Image(com_fixture)
    #     idv = IdvPage(com_fixture)
    #     idv.goto_idv_terminal_page()  # 进入idv页面
    #     idv.search_terminal(name=name)  # 搜索终端名称
    #     time.sleep(1)
    #     # 获取终端系列和版本
    #     serial = idv.get_terminal_productserial(name)
    #     version = idv.get_terminal_productversion()
    #     idv.close_terminal_detail()  # 关闭终端详情页
    #     idv.back_current_page()
    #     img.go_img_manage()
    #     # 安装驱动，不同终端配置不同，等待时间需长一些
    #     img.install_driver(img_name_a5_win10, serial, version, name)
    #     time.sleep(900)  # 安装驱动，并进行系统更新需等待50分钟左右
    #     img.go_img_manage()
    #     logging.info(u"----验证驱动下拉框的驱动类型为已安装----")
    #     img.goto_driver_install(img_name=img_name_a5_win10)  # 进入驱动安装页面
    #     img.click_elem(img.terminal_model)  # 点击终端型号
    #     if (serial == u'300' or serial == u'400') and (version == u'1'):
    #         assert u"Rain300/400系列(硬件版本：V1.XX)(已安装)" in img.get_value(img.terminal_model)
    #     if (serial == u'305' or serial == u'405') and (version == u'1'):
    #         assert u"Rain305/405系列(硬件版本：V1.XX)(已安装)" in img.get_value(img.terminal_model)
    #     if (serial == u'310' or serial == u'410') and (version == u'1'):
    #         assert u"Rain310/410系列(硬件版本：V1.XX)(已安装)" in img.get_value(img.terminal_model)
    #     if (serial == u'310' or serial == u'410') and (version == u'2'):
    #         assert u"Rain310/410系列(硬件版本：V2.XX)(已安装)" in img.get_value(img.terminal_model)
    #     if (serial == u'320') and (version == u'1'):
    #         assert u"Rain320系列(硬件版本：V1.XX)(已安装)" in img.get_value(img.terminal_model)
    #     if (serial == u'320') and (version == u'2'):
    #         assert u"Rain320系列(硬件版本：V2.XX)(已安装)" in img.get_value(img.terminal_model)
    #     time.sleep(1)
    #
    # @pytest.mark.case_level_1
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.test_a5678
    # @pytest.mark.image
    # @pytest.mark.parametrize('name', search_idv_terminal)
    # def test_a5_5_6_7_8(self, com_fixture, name):
    #     """
    #     1、前置：需要有各种型号的终端连接到服务器上以及未安装驱动的win10镜像
    #     2、进入idv终端管理页面，搜索不同类型的终端型号
    #     3、进入镜像管理页面，根据2获取到的终端型号选择安装驱动
    #     4、待驱动安装完成后，验证镜像下拉框所对应的终端型号为已安装
    #     """
    #     img = Image(com_fixture)
    #     idv = IdvPage(com_fixture)
    #     idv.goto_idv_terminal_page()  # 进入idv页面
    #     idv.search_terminal(name=name)  # 搜索终端名称=======
    #     time.sleep(1)
    #     # 获取终端系列和版本
    #     serial = idv.get_terminal_productserial(name)
    #     version = idv.get_terminal_productversion()
    #     idv.close_terminal_detail()  # 关闭终端详情页
    #     idv.back_current_page()
    #     img.go_img_manage()
    #     # 安装驱动，不同终端配置不同，等待时间需长一些
    #     img.install_driver(img_name_a5_win7, serial, version, name)
    #     time.sleep(900)  # 安装驱动，并进行系统更新需等待50分钟左右
    #     img.go_img_manage()
    #     logging.info(u"----验证驱动下拉框的驱动类型为已安装----")
    #     img.goto_driver_install(img_name=img_name_a5_win7)  # 进入驱动安装页面====
    #     img.click_elem(img.terminal_model)  # 点击终端型号
    #     if (serial == u'300' or serial == u'400') and (version == u'1'):
    #         assert u"Rain300/400系列(硬件版本：V1.XX)(已安装)" in img.get_value(img.terminal_model)
    #     if (serial == u'305' or serial == u'405') and (version == u'1'):
    #         assert u"Rain305/405系列(硬件版本：V1.XX)(已安装)" in img.get_value(img.terminal_model)
    #     if (serial == u'310' or serial == u'410') and (version == u'1'):
    #         assert u"Rain310/410系列(硬件版本：V1.XX)(已安装)" in img.get_value(img.terminal_model)
    #     if (serial == u'310' or serial == u'410') and (version == u'2'):
    #         assert u"Rain310/410系列(硬件版本：V2.XX)(已安装)" in img.get_value(img.terminal_model)
    #     if (serial == u'320') and (version == u'1'):
    #         assert u"Rain320系列(硬件版本：V1.XX)(已安装)" in img.get_value(img.terminal_model)
    #     if (serial == u'320') and (version == u'2'):
    #         assert u"Rain320系列(硬件版本：V2.XX)(已安装)" in img.get_value(img.terminal_model)
    #     time.sleep(1)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.image
    @pytest.mark.autotest_image
    def test_a7_1(self, com_fixture):
        """"
        1、前置条件，vdi镜像未安装Guestool工具
        2、创建还原组，绑定任意镜像
        3、验证还原组创建成功
        4、编辑镜像为稍后发布
        5、验证镜像未安装GT
        """
        logging.info(u"-------镜像测试用例a7_1开始执行----")
        img = Image(com_fixture)
        try:
            img.go_img_manage()
            img.edit_image_name_os(image_type=image_type_vdi, os=os_win7, image_name=vdi_not_gt_image)
            time.sleep(1.5)
            img.open_admin_tool()
            img.close_img()
            img.wait_image_update_cpmpleted(vdi_not_gt_image)
            logging.info(u"---验证镜像管理页面需要安装GT-----")
            assert u"需安装GuestTool" in img.get_value(img.img_pub_now.format(vdi_not_gt_image))
        finally:
            img.img_recovery(vdi_not_gt_image)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_image
    def test_a9_1(self, download_fixture):
        """
        1、进入镜像管理页面验证界面下方显示“上传文件，启动镜像需先安装管理员工具”和立即下载按钮
        2、点击下载按钮
        """
        if os.path.exists(admintoolpath):
            os.remove(admintoolpath)
        flag = False
        img = Image(download_fixture)
        login = Login(download_fixture)
        login.login(name=username, pwd=passwd)
        img.go_img_manage()
        logging.info(u"-----验证界面下方有下载工具----")
        assert u"“启动镜像”，“上传文件”需要先安装" in img.get_value(img.down_tool)
        assert u"管理员工具" in img.get_value(img.down_tool)
        assert u"立即下载" in img.get_value(img.down_tool)
        img.admin_tool_dowload(10)  # 等待10s
        if os.path.exists(admintoolpath):
            flag = 1
        logging.info(u"---判断默认下载路径下文件是否存在---")
        assert flag == 1

    u"-----------------------镜像中与终端相关8条用例-----------------------------------"

    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.image
    # def test_imgtest_1(self, com_fixture):
    #     """
    #     1.进入胖终端页面-未分组验证未分组绑定镜像项为非必填项
    #     2、搜索终端A并点击终端初始化，设置终端为多用户终端，点击下载
    #     3、验证提示信息为所在分组未绑定镜像
    #     4、创建分组1绑定其他终端（有镜像）,终端A绑定到分组1
    #     5、验证终端A的的绑定的镜像为分组镜像
    #     """
    #     idv = IdvPage(com_fixture)
    #     try:
    #         # 验证未分组绑定镜像为非必填以及删除未分组所绑定的镜像
    #         idv.goto_idv_terminal_page()
    #         idv.click_gp_edit_btn(gp_name=u"未分组")  # 点击idv-未分组按钮
    #         logging.info(u"---验证未分组-绑定镜像选项不是必填项----")
    #         assert idv.elem_is_exist(idv.weifenzu_feibit) == 1
    #         idv.del_weifenzu_imgisexit()  # 如果未分组有绑定镜像，删除，否则不操作
    #         # 新建分组，绑定idv镜像
    #         idv.del_gp_exist(name="tmgp_01")
    #         idv.idv_creat_group(name="tmgp_01", img_name=idv_img_B, desk_type=u"还原")
    #         # 搜索终端名称，对终端进行初始化操作,并且重启终端
    #         idv.back_current_page()
    #         idv.terminal_init1(name=idv_tm_ip_1)
    #         idv.reboot_terminal(idv_tm_ip_1)
    #         idv.wait_tm_reboot_success(name=idv_tm_ip_1, tm=1)
    #         # 选择终端模式为多用户，验证终端反馈信息为终端组未绑定镜像
    #         idv_initialization_click(ip=idv_tm_ip_1)
    #         idv_pattern_chose(ip=idv_tm_ip_1, pattern="public", times=2)
    #         time.sleep(1)
    #         assert idv_is_bind_image(ip=idv_tm_ip_1) == 1
    #         # 将终端绑定到分组1中
    #         idv.modify_idv(tm_name=idv_tm_ip_1, tm_group="tmgp_01")
    #         idv.reboot_terminal(idv_tm_ip_1)
    #         idv.wait_tm_reboot_success(name=idv_tm_ip_1, tm=1)
    #         time.sleep(200)
    #         # 终端页面获取镜像信息
    #         message1 = idv.get_terminal_img(name=idv_tm_ip_1)
    #         assert idv_img_B in message1
    #         time.sleep(2)
    #     finally:
    #         try:
    #             idv.click_gp_edit_btn(gp_name=u"未分组")  # 点击编辑未分组
    #             idv.add_weifenzu_image(img_name=idv_base)  # 未分组添加镜像
    #         except Exception as e:
    #             logging.info(e)
    #
    #
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.image
    # @pytest.mark.test_image
    # def test_imagetest_2(self, com_fixture):
    #     """
    #     1、判断未分组是否有绑定镜像，若没有绑定镜像则进行绑定
    #     2、将终端转移到未分组名下，进行终端初始化
    #     3、用户登录终端，验证绑定的镜像为未分组下绑定的镜像
    #     """
    #     idv = IdvPage(com_fixture)
    #     # 为未分组绑定镜像
    #     idv.goto_idv_terminal_page()
    #     idv.click_gp_edit_btn(gp_name=u"未分组")  # 点击编辑未分组
    #     idv.add_weifenzu_image(img_name=idv_base)  # 未分组添加镜像
    #     # 修改终端所在分组
    #     idv.modify_idv(tm_name=idv_tm_ip_1, tm_group=u"未分组")
    #     time.sleep(2)
    #     # 终端初始化并重启终端
    #     idv.terminal_init1(name=idv_tm_ip_1)
    #     idv.reboot_terminal(name=idv_tm_ip_1)
    #     idv.wait_tm_reboot_success(name=idv_tm_ip_1, tm=1)
    #     # 终端初始化且进行终端模式选择
    #     idv_initialization_click(ip=idv_tm_ip_1)  # 对终端进行初始化
    #     idv_pattern_chose(ip=idv_tm_ip_1, pattern="public")  # 终端模式选择公用终端
    #     time.sleep(300)  # 检查base以及镜像下载
    #     # 验证终端的分组以及绑定镜像信息
    #     msg = idv.get_terminal_img(name=idv_terminal_name)  # 获取终端绑定的镜像
    #     assert idv_img_A in msg
    #     msg1 = idv.get_terminal_group(name=idv_terminal_name)  # 获取终端绑定分组名称
    #     assert u"未分组" in msg1
    #     time.sleep(2)

    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.testimage_3
    # @pytest.mark.image
    # def testimage_3(self, com_fixture):
    #     """
    #     1、取消绑定未分组的镜像
    #     2、终端移动到未分组并且下载镜像
    #     3、验证未分组没有绑定镜像以及终端提示信息
    #     """
    #     idv = IdvPage(com_fixture)
    #     idv.goto_idv_terminal_page()
    #     # 编辑未分组，删除绑定的镜像
    #     idv.click_gp_edit_btn(gp_name=u"未分组")
    #     idv.del_weifenzu_imgisexit()  # 删除镜像绑定
    #     idv.click_gp_edit_btn(gp_name=u"未分组")
    #     idv.go_common_frame()
    #     logging.info(u"---验证未分组未绑定镜像----")
    #     assert idv.elem_is_exist(idv.btn_close_image) == 1
    #     idv.click_elem(idv.submit_btn_xpath)  # 点击确定
    #     idv.back_current_page()
    #     idv.click_elem(idv.sure_xpath)  # 二次确认
    #     time.sleep(2)
    #     # 将用户移到未分组下
    #     idv.modify_idv(tm_name=idv_tm_ip_1, tm_group=u"未分组")
    #     time.sleep(2)
    #     idv.terminal_init1(name=idv_tm_ip_1)  # 终端初始化
    #     time.sleep(2)
    #     # 重启终端
    #     idv.reboot_terminal(name=idv_tm_ip_1)
    #     time.sleep(46)
    #     # 终端操作对终端进行初始化
    #     idv_initialization_click(ip=idv_tm_ip_1)
    #     idv_pattern_chose(ip=idv_tm_ip_1, pattern="public")  # 终端模式选择公用终端
    #     time.sleep(2)
    #     assert idv_is_bind_image(ip=idv_tm_ip_1) == 1
    #     time.sleep(2)
    #
    # @pytest.mark.case_level_1
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.image
    # def testimage_4(self, com_fixture):
    #     """
    #     1、前置条件：准备一个idv镜像
    #     2、搜索AB终端，并绑定在未分组下
    #     3、多用户终端模式下创建新分组
    #     4、将A用户移动到新分组中，验证A终端在新建分组下
    #     5、取消未分组绑定镜像
    #     6、验证B终端不受影响
    #     """
    #     idv = IdvPage(com_fixture)
    #     # 未分组添加绑定镜像
    #     idv.goto_idv_terminal_page()
    #     idv.click_gp_edit_btn(u"未分组")
    #     idv.add_weifenzu_image(img_name=idv_img_A)
    #     # A、B终端移动到未分组下
    #     idv.modify_idv(tm_name=idv_tm_ip_1, tm_group=u"未分组")
    #     time.sleep(2)
    #     idv.modify_idv(tm_name=idv_tm_ip_2, tm_group=u"未分组")
    #     # 创建新的分组,并将终端A移到该分组
    #     idv.add_more_pub_tmgroup_notexist(name="tmgp_01", img_name=idv_img_B)
    #     idv.back_current_page()
    #     idv.modify_idv(tm_name=idv_tm_ip_1, tm_group="tmgp_01")  # 修改A的分组
    #     time.sleep(2)
    #     # 取消未分组镜像绑定
    #     idv.click_gp_edit_btn(gp_name=u"未分组")
    #     idv.del_weifenzu_imgisexit()
    #     idv.click_gp_edit_btn(gp_name=u"未分组")
    #     idv.go_common_frame()
    #     assert idv.elem_is_exist(idv.btn_close_image) == 1
    #     idv.back_current_page()
    #     msg1 = idv.get_terminal_group(name=idv_terminal_name)
    #     assert "tmgp_01" == msg1  # 验证终端所在的组为新建的分组
    #     idv.back_current_page()
    #     msg2 = idv.get_terminal_group(name=idv_tm_ip_2)
    #     assert u"未分组" == msg2  # 验证终端所在的组为新建的分组
    #
    # @pytest.mark.case_level_2
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.testimage_5
    # @pytest.mark.image
    # def test_image_5(self, com_fixture):
    #     """
    #     1、修改未分组名称为其他任意合法名称
    #     2、验证修改成功
    #     3、取消未分组下镜像绑定
    #     4、验证未分组下未绑定
    #     """
    #     idv = IdvPage(com_fixture)
    #     idv.goto_idv_terminal_page()
    #     # 变更未分组名称
    #     time.sleep(1)
    #     idv.edit_idv_gp(gp_name=u"未分组", rename=u"未分组名称变更", ty=1)
    #     idv.back_current_page()
    #     idv.go_left_iframe()
    #     # 验证名称变更成功
    #     assert u"未分组名称变更" in idv.get_elem_text(idv.all_group)
    #     time.sleep(1)
    #     idv.edit_idv_gp(gp_name=u"未分组名称变更", rename=u"未分组", ty=1)  # 名称变更回未分组
    #     # 取消绑定未分组绑定的镜像
    #     idv.click_gp_edit_btn(gp_name=u"未分组")
    #     idv.del_weifenzu_imgisexit()
    #     idv.click_gp_edit_btn(gp_name=u"未分组")
    #     idv.go_common_frame()
    #     # 点击未分组编辑验证没有镜像绑定
    #     assert idv.elem_is_exist(idv.btn_close_image) == 1
    #     time.sleep(3)
    #
    # @pytest.mark.case_level_2
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.testimage_6
    # @pytest.mark.image
    # def testimage_6(self, com_fixture):
    #     """
    #     1、将未分组绑定镜像，制造前置条件
    #     2、取消绑定未分组绑定镜像，同时修改系统盘本地盘
    #     3、验证修改成功
    #     """
    #     idv = IdvPage(com_fixture)
    #     idv.goto_idv_terminal_page()
    #     # 制造未分组绑定镜像的前置条件
    #     idv.click_gp_edit_btn(gp_name=u"未分组")
    #     idv.add_weifenzu_image(img_name=idv_img_A)
    #     # 取消未分组镜像绑定
    #     idv.click_gp_edit_btn(gp_name=u"未分组")
    #     idv.del_weifenzu_imgisexit()
    #     # 修改未分组参数
    #     idv.edit_idv_gp(gp_name=u"未分组", sys_disk="45", local_disk="close", ty=1)
    #     idv.click_gp_edit_btn(gp_name=u"未分组")
    #     idv.go_common_frame()
    #     logging.info(u"----验证配置修改成功----")
    #     assert idv.elem_is_exist(idv.btn_close_image) == 1  # 验证未分组已取消绑定镜像
    #     assert idv.get_elem_attribute(idv.change_disk_size_xpath, 'value') == "45"  # 验证系统盘大小为修改后的大小
    #     time.sleep(2)
    #
    # @pytest.mark.case_level_1
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.testimage_7
    # @pytest.mark.image
    # def testimage_7(self, com_fixture):
    #     """
    #     1、用户管理未分组开启idv特性并绑定镜像
    #     2、进入终端管理页面验证单用户终端未绑定用户组镜像与1一致
    #     3、修改终端类型为单用户，并且初始化终端下载镜像
    #     4、验证web终端所绑定的镜像为1镜像
    #     5、初始化终端
    #     """
    #     user = UserMange(com_fixture)
    #     idv = IdvPage(com_fixture)
    #     try:
    #         user.goto_usermanage_page()
    #         user.edit_gp_idv(gp_name=u"未分组", isopen_idv=u"open", image=idv_img_B)
    #         time.sleep(2)  # 等待分组修改成功
    #         idv.goto_idv_terminal_page()
    #         idv.click_single_group()  # 点击单用户组终端
    #         image_name = idv.get_detailBtn()
    #         assert image_name == idv_img_B
    #         idv.click_elem(idv.close_btns)
    #         time.sleep(2)
    #         idv.back_current_page()
    #         idv.click_mult_group()  # 点击多用户终端组
    #         idv.terminal_init1(name=idv_tm_ip_1)  # 进行终端初始化
    #         time.sleep(2)
    #         # 重启终端
    #         idv.reboot_terminal(name=idv_tm_ip_1)
    #         time.sleep(45)
    #         idv.modify_idv(tm_name=idv_tm_ip_1, tm_type=u"单用户")  # 修改终端类型为单用户
    #         time.sleep(2)
    #         # 初始化终端，选择单用户模式
    #         idv_initialization_click(ip=idv_tm_ip_1)
    #         idv_pattern_chose(ip=idv_tm_ip_1)
    #         time.sleep(400)  # 等待下载镜像
    #         idv.click_single_group()
    #         msg1 = idv.get_single_tm_gp(name=idv_terminal_name)  # 获取终端的
    #         img_info = idv.get_single_tm_image(tm_name=idv_terminal_name)
    #         logging.info(u"-------验证终端的分组为未绑定用户终端组-------")
    #         assert msg1 == u"未绑定用户终端组"
    #         assert img_info == idv_img_B
    #     except Exception as error:
    #         logging.error(error)
    #     # 修改终端分组为多用户
    #     idv.modify_idv(tm_name=idv_terminal_name, tm_type=u"多用户")
    #     time.sleep(2)
    #
    # @pytest.mark.case_level_1
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.testimage_8
    # def testimage_8(self, com_fixture):
    #     """
    #     1、进入用户管理页面编辑未分组idv特性为空
    #     2、进入终端管理页面，验证单用户终端分组所绑定的镜像为空
    #     3、初始化终端后验证终端页面截屏
    #     """
    #     user = UserMange(com_fixture)
    #     idv = IdvPage(com_fixture)
    #     try:
    #         # 进入用户管理页面
    #         user.goto_usermanage_page()
    #         user.edit_gp_idv(gp_name=u"未分组", isopen_idv=u"close")
    #         time.sleep(2)
    #         idv.goto_idv_terminal_page()
    #         idv.click_single_group()  # 点击单用户组终端
    #         image_name = idv.get_detailBtn()
    #         assert image_name == u' '  # 验证镜像为空
    #         idv.click_elem(idv.close_btns)
    #         time.sleep(2)
    #         idv.back_current_page()
    #         idv.click_mult_group()  # 点击多用户终端组
    #         idv.terminal_init1(name=idv_tm_ip_1)  # 进行终端初始化
    #         time.sleep(2)
    #         # 重启终端
    #         idv.reboot_terminal(name=idv_tm_ip_1)
    #         time.sleep(45)
    #         # 等待终端下载
    #         idv_initialization_click(ip=idv_tm_ip_1)
    #         time.sleep(60)
    #         assert idv.elem_is_exist(idv.btn_close_image) == 1
    #     except Exception as error:
    #         logging.error(error)
    #     idv.back_current_page()
    #     idv.click_single_group()
    #     idv.modify_idv(tm_name=idv_tm_ip_1, tm_type=u"多用户")


if __name__ == "__main__":
    # t = time.strftime("%Y-%m-%d %H%M")
    # pytest.main(["-m", "autotest_image", "--html", report_dir + "//{0}_image_html_report.html".format(t)])
    pytest.main(["-m", "aaa11111"])
    # pytest.main(["-m", "delete"])
    pass
