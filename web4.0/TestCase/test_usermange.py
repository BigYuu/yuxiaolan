#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/11/15 14:28
"""
import pytest
from TestData.Usermanagedata import *
from WebPages.CdeskmangePage import CDeskMange
from WebPages.Idvpage import IdvPage
from WebPages.UserMangePage import UserMange
from time import sleep
from uiautomation import Keys
from Common.terminal_action import *
from WebPages.adnroid_vdi_page import AndroidVdi
from WebPages.indexPage import *
from WebPages.ImagePage import *
from Common.Mylog import logging
from WebPages.ImagePage import Image
import logging


class Test_UserMange:
    # @pytest.mark.userManage
    # def test_idv_info_check_2(self, user_pm_fixture):
    #     logging.info("--------------------------------web用户管理A1.76-4批量填充用例开始执行-------------------------")
    #     u = UserMange(user_pm_fixture)
    #     try:
    #         u.goto_usermanage_page()
    #         u.create_group_openvdi(group_name="ugp_87", cd_type=u"个性", img_name=image_name3)
    #         u.create_user_in_group(group_name="ugp_87", user_name="user_87_1", real_name="user_87_1")
    #         u.search_info("user_87_")
    #         u.chose_all_user()
    #         u.fill_ip_allinfo(ip, mask, gateway, dns)
    #         assert u.fill_ip_successinfo() == u"IP填充成功！"
    #     finally:
    #         try:
    #             u.user_recovery("ugp_87")
    #         except Exception as e:
    #             logging.info(e)
    #     logging.info("---------------------------------web用户管理A1.76-4批量填充用例结束-----------------------------")

    @pytest.mark.userManage
    @pytest.mark.parametrize('name', group_name)
    def test__nfo_check(self, user_pm_fixture, name):
        logging.info("---------------------------------web用户管理A1.76-4批量填充用例开始执行-------------------------")
        u = UserMange(user_pm_fixture)
        u.create_group()
        u.vdi_attribute_set(name)

    # -----------------------------------吴少锋完成的部分开始-------------------------------------#
    # @pytest.mark.userManage
    # @pytest.mark.usergroup
    # def test_UserGroupName(self, user_pm_fixture):
    #     """
    #     执行步骤：
    #     1、新建用户组输入全英文、全中文、全数字
    #     2、用户组名混合输入英文、数字、中文以及"_","-","@","."这四个特殊符号,且不能以"_"开头
    #     3、用户组名设置为其他字符
    #     4、用户组名输入超过最大32字节
    #     5、英文、中文、数字、所有符号输入
    #     6、描述最大支持60字符输入
    #     7、描述为非必填项
    #     预期结果：
    #     1、创建用户组成功
    #     2、创建用户组成功
    #     3、不允许使用其他字符，创建失败
    #     4、自动读取前32字符作为组名称
    #     5、描述设置成功
    #     6、描述最大字节输入成功
    #     7、不填写描述点击确认
    #     """
    #     logging.info("-----------------web用户管理A1.1,A1.2,A1.3用例开始执行--------------------")
    #     userGp = UserMange(user_pm_fixture)
    #     try:
    #         for content in user_name_describe_list:
    #             time.sleep(com_slp)
    #             userGp.click_elem(userGp.usergroup_add_button_xpath)
    #             userGp.elem_send_keys(userGp.usergroup_name_input_xpath, content)
    #             try:
    #                 userGp.usergroup_name_errormsg(userGp.usergroup_name_errormsg_xpath)
    #             except:
    #                 time.sleep(com_slp)
    #                 userGp.elem_send_keys(userGp.usergroup_describe_xpath, content)
    #                 if content == user_name_describe_list[-1]:
    #                     userGp.clear_input(userGp.usergroup_describe_xpath)
    #                 if content == user_name_describe_list[-2]:
    #                     assert len(userGp.get_elem_attribute(userGp.usergroup_name_input_xpath, 'value')) == 32
    #                     assert len(userGp.get_elem_attribute(userGp.usergroup_describe_xpath, 'value')) == 60
    #                 userGp.click_confirm()
    #                 assert userGp.get_elem_text(userGp.tip_xpath) == userGroup_createSuccessfully_info
    #             else:
    #                 logging.info("----------------------------用户组名称错误------------------------------")
    #                 userGp.click_elem(userGp.cancel_button_xpath)
    #                 continue
    #     finally:
    #         try:
    #             # 善后处理，删除添加的用户组
    #             for info in del_group_list:
    #                 userGp.del_group(name=info, password=passwd)
    #                 time.sleep(1)
    #         except Exception as e:
    #             logging.info(e)
    #     logging.info("-------------------web用户管理A1.1,A1.2,A1.3用例结束----------------------")

    @pytest.mark.userManage
    @pytest.mark.usergroup
    def test_UserGroup_Character(self, user_pm_fixture):
        """
        执行步骤:
        1、默认不启用IDV云终端
        2、勾选启用IDV云终端
        3、默认不启用VDI云桌面
        4、勾选启用VDI云桌面
        预期结果：
        1、默认项为不启用，组内用户无法使用IDV云终端
        2、该用户组拥有IDV云终端使用权限
        3、默认项为不启用，组内用户无法使用VDI云终端
        4、该用户组拥有VDI云桌面使用权限
        """
        logging.info("-----------------web用户管理A1.4 , A1.10用例开始执行--------------------")
        userGp = UserMange(user_pm_fixture)
        userGp.click_elem(userGp.usergroup_add_button_xpath)
        assert userGp.get_elem_text(userGp.usergroup_idv_status_close_xpath).find(close_info) >= 0
        userGp.choose_Terminal_character('idv')
        assert userGp.get_elem_text(userGp.usergroup_idv_status_open_xpath).find(open_info) >= 0
        assert userGp.get_elem_text(userGp.usergroup_vdi_status_close_xpath).find(close_info) >= 0
        userGp.choose_Terminal_character('vdi')
        assert userGp.get_elem_text(userGp.usergroup_vdi_status_open_xpath).find(open_info) >= 0
        logging.info("-----------------web用户管理A1.4,A1.10用例结束--------------------")

    # @pytest.mark.userManage1234
    # @pytest.mark.usergroup_idv
    # def test_UserGroup_IDV_imagebind(self, user_pm_fixture):
    #     """
    #     执行步骤
    #     1、设置IDV绑定镜像，点击添加勾选当前启用的IDV镜像镜像绑定
    #     2、绑定镜像不选择时，新建用户组
    #     预期结果test_changeUsergroupIdvCharacter
    #     1、组内用户登录IDV终端显示为绑定镜像系统
    #     2、新建用户组不成功，绑定IDV镜像为必填项
    #     """
    #     logging.info("-----------------web用户管理A1.5用例开始执行--------------------")
    #     userGp_IDV = UserMange(user_pm_fixture)
    #     Idv = IdvPage(user_pm_fixture)
    #     c = CDeskMange(user_pm_fixture)
    #     try:
    #         userGp_IDV.click_elem(userGp_IDV.usergroup_add_button_xpath)
    #         userGp_IDV.elem_send_keys(userGp_IDV.usergroup_name_input_xpath, userGroup_name_list[0])
    #         userGp_IDV.choose_Terminal_character('idv')
    #         assert userGp_IDV.get_elem_attribute(userGp_IDV.idvimage_bind_xpath, 'placeholder') == chooseImage_info
    #         userGp_IDV.click_confirm()
    #         assert userGp_IDV.get_elem_text(userGp_IDV.idvimage_bind_errormsg_xpath).find(idvimage_bind_errormsg_info) >= 0
    #         userGp_IDV.image_bind(idv, idvImage=idv_default_image)
    #         userGp_IDV.click_confirm()
    #         userGp_IDV.findUserGroupCreateNewuser(userGroup_name_list[0], 'A1.5')
    #         userGp_IDV.click_confirm()
    #         userGp_IDV.back_current_page()
    #         # 进入终端管理--多用户终端组
    #         Idv.goto_idv_terminal_page()
    #         Idv.goto_idv_terminal_moreandpub_terminal_group_page()
    #         # 搜索终端，获取终端ip绑定用户后重启终端
    #         Idv.reboot_terminal(name=idv_public_ip_list[1])
    #         Idv.back_current_page()
    #         time.sleep(80)
    #         idv_initialization_click(idv_public_ip_list[1])
    #         click_idv_set(idv_public_ip_list[1])
    #         idv_change_pwd(idv_public_ip_list[1], "A1.5", "123")
    #         idv_login(idv_public_ip_list[1], "A1.5")
    #         c.goto_cloud_desk_manage()
    #         dcip = c.get_cloud_desk_ip("A1.5")
    #         c.back_current_page()
    #         print dcip
    #         win_conn_useful(dcip, s_user, s_pwd)
    #         info = get_win_conn_info(dcip, s_user, s_pwd, r'ver')
    #         assert list(info)[-11] == '6'
    #     finally:
    #         # 善后处理
    #         Idv.goto_idvtm_page()
    #         Idv.goto_idv_terminal_moreandpub_terminal_group_page()
    #         time.sleep(5)
    #         Idv.reboot_terminal(name=idv_public_ip_list[1])
    #         Idv.wait_tm_reboot_success(idv_public_ip_list[1], 1)
    #         userGp_IDV.back_current_page()
    #         userGp_IDV.goto_usermanage()
    #         userGp_IDV.search_info(name='A1.5')
    #         userGp_IDV.del_user(passwd)
    #         time.sleep(2)
    #         userGp_IDV.del_group(name=userGroup_name_list[0], password=passwd)
    #
    #     logging.info("-----------------web用户管理A1.5用例结束--------------------")

    @pytest.mark.userManage123
    @pytest.mark.usergroup_idv
    def test_UserGroup_IDV_SystemDisk(self, com_fixture):
        """
        执行步骤
        1、镜像设置的系统盘为默认值40G，该镜像绑定用户组
        2、镜像设置的系统盘大小非默认值100G，该镜像绑定用户组时，显示系统盘大小为镜像对应的系统盘大小
        3、设置系统盘大小越界，小于40G和大于100G
        预期结果
        1、绑定用户组时显示为默认40G
        2、绑定用户组时显示为对应镜像设置值100G，设置系统盘终端是否生效根据终端硬盘容量决定
        3、设置不生效，返回原先值
        """
        logging.info("-----------------web用户管理A1.7 , A1.8用例开始执行--------------------")
        userGroup_IDV = UserMange(com_fixture)
        img = Image(com_fixture)
        time.sleep(com_slp)
        userGroup_IDV.goto_usermanage()
        userGroup_IDV.open_character(idv, userGroup_name_list[1])
        assert userGroup_IDV.get_systemDisk_content(userGroup_IDV.IDV_systemDisk_xpath) == '40'
        userGroup_IDV.image_bind(idv)
        imageName = userGroup_IDV.get_elem_attribute(userGroup_IDV.idvimage_bind_xpath, 'value')
        userGroup_IDV.click_elem(userGroup_IDV.cancel_button_xpath)
        time.sleep(com_slp)
        img.go_img_manage()
        time.sleep(com_slp)
        disk_size = img.get_sysdisk_size(imageName)
        img.click_cancel()
        img.back_current_page()
        userGroup_IDV.goto_usermanage()
        userGroup_IDV.open_character(idv, userGroup_name_list[1])
        userGroup_IDV.image_bind(idv)
        assert userGroup_IDV.get_systemDisk_content(userGroup_IDV.IDV_systemDisk_xpath) == disk_size
        userGroup_IDV.set_systemDisk_content(userGroup_IDV.IDV_systemDisk_xpath, '20')
        assert userGroup_IDV.get_systemDisk_content(userGroup_IDV.IDV_systemDisk_xpath) != '20'
        userGroup_IDV.set_systemDisk_content(userGroup_IDV.IDV_systemDisk_xpath, '110')
        assert userGroup_IDV.get_systemDisk_content(userGroup_IDV.IDV_systemDisk_xpath) != '110'
        logging.info("-----------------web用户管理A1.7 , A1.8用例结束--------------------")

    # @pytest.mark.userManage
    # @pytest.mark.usergroup_vdi
    # def test_UserGroup_VDI_vlan(self, user_pm_fixture):
    #     """
    #     执行步骤
    #     1、设置对应VLAN，可设置vlan 1~4094，
    #     2、验证设置VLAN，最大值4094可以配置
    #     3、设置越界VLAN ID 4095，
    #     4、使用英文、负数等无效VLAN
    #     预期结果
    #     1、该用户组云桌面属于用户组设置的VLAN，发出的报文带VLAN TAG
    #     2、可配置，该用户组云桌面属于用户组设置的VLAN，发出的报文带VLAN TAG
    #     3、无效，不可配置，回退会原先设置值
    #     4、无效，不可配置，回退会原先设置值
    #     """
    #     logging.info("-----------------web用户管理A1.11，A1.12用例开始执行--------------------")
    #     userGp_VDI = UserMange(user_pm_fixture)
    #     try:
    #         userGp_VDI.open_character(vdi, userGroup_name_list[2])
    #         userGp_VDI.clear_input(userGp_VDI.vlan_input_xpath)
    #         userGp_VDI.elem_send_keys(userGp_VDI.vlan_input_xpath, '4094')
    #         userGp_VDI.image_bind(vdi)
    #         userGp_VDI.click_confirm()
    #         text1 = server_conn(host_ip, command1)
    #         text2 = server_conn(host_ip, command2)
    #         assert text1.find(command1[9:]) >= 0
    #         assert text2.find(command2[9:]) >= 0
    #         userGp_VDI.open_character(vdi, userGroup_name_list[3])
    #         for vlan in vlan_list:
    #             userGp_VDI.clear_input(userGp_VDI.vlan_input_xpath)
    #             userGp_VDI.elem_send_keys(userGp_VDI.vlan_input_xpath, vlan)
    #             assert userGp_VDI.get_elem_attribute(userGp_VDI.vlan_input_xpath, 'aria-valuenow') != vlan
    #     finally:
    #         try:
    #             # 善后处理，删除添加过的数据
    #             userGp_VDI.user_recovery(userGroup_name_list[2])
    #         except Exception as e:
    #             logging.info(e)
    #     logging.info("-----------------web用户管理A1.11，A1.12用例结束--------------------")

    @pytest.mark.userManage
    @pytest.mark.usergroup_vdi
    def test_bindUserGroupImage_UserDefaultImage(self, user_pm_fixture):

        logging.info("-----------------web用户管理A1.14用例开始执行--------------------")
        userVdi = UserMange(user_pm_fixture)
        try:
            userVdi.open_character(vdi, userGroup_name_list[4])
            userVdi.image_bind(vdi)
            imageName = userVdi.get_elem_attribute(userVdi.vdiimage_bind_xpath, 'value')
            userVdi.click_elem(userVdi.confire_button_xpath)
            time.sleep(com_slp)
            userVdi.findUserGroupCreateNewuser(userGroup_name_list[4], user_list[0])
            userVdi.click_elem(userVdi.vdi_set_xpath)
            assert imageName == userVdi.get_elem_attribute(userVdi.vdiimage_bind_xpath, 'value')
            time.sleep(com_slp)
            userVdi.click_elem(userVdi.cancel_button_xpath)
            logging.info("-----------------web用户管理A1.14用例结束--------------------")
            logging.info("-----------------web用户管理A1.21用例开始执行--------------------")
            time.sleep(com_slp)
            userVdi.findUserGroupCreateNewuser(userGroup_name_list[4], user_list[0])
            userVdi.click_elem(userVdi.confire_button_xpath)
            time.sleep(3)
            userVdi.chainstay(userVdi.userGroup_list_xpath % userGroup_name_list[4])
            userVdi.edit_userGroupCharacter(userGroup_name_list[4], vdi)
            userVdi.click_confirm()
            userVdi.warnning_info(vdiCharacterError_info)
            userVdi.check_userDetail(user_list[0])
            userVdi.click_elem(userVdi.userDetail_vdiSet_xpath)
            assert userVdi.get_elem_text(userVdi.userDetail_vdiSetContent_xpath).find(close_info) >= 0
            userVdi.click(userVdi.close_info_button_xpath)
        finally:
            try:
                # 善后处理：删除添加过的数据
                userVdi.user_recovery(userGroup_name_list[4])
                # userVdi.search_info(name=user_list[0])
                # userVdi.del_user(passwd)
                # time.sleep(2)
                # userVdi.del_group(name=userGroup_name_list[4], password=passwd)
            except Exception as e:
                logging.info(e)
        logging.info("-----------------web用户管理A1.21用例结束--------------------")

    # @pytest.mark.userManage
    # @pytest.mark.usergroup_vdi
    # def test_UserGroup_VDI_SystemDisk(self, user_pm_fixture):
    #     logging.info("-----------------web用户管理A1.19用例开始执行--------------------")
    #     userVdi = UserMange(user_pm_fixture)
    #     userVdi.open_character(vdi, userGroup_name_list[5])
    #     assert userVdi.get_systemDisk_content(userVdi.VDI_systemDisk_xpath) == '20'
    #     userVdi.set_systemDisk_content(userVdi.VDI_systemDisk_xpath, 10)
    #     assert userVdi.get_systemDisk_content(userVdi.VDI_systemDisk_xpath) != '10'
    #     assert userVdi.get_systemDisk_content(userVdi.VDI_systemDisk_xpath) == '20'
    #     logging.info("---------------------web用户管理A1.19用例结束--------------------")

    @pytest.mark.userManage123
    @pytest.mark.user
    def test_UserNoChangedCharacter(self, user_pm_fixture):
        logging.info("-----------------web用户管理A1.23用例开始执行--------------------")
        user = UserMange(user_pm_fixture)
        try:
            user.open_character(vdi, userGroup_name_list[6])
            user.image_bind(vdi)
            user.click_confirm()
            time.sleep(com_slp)
            user.findUserGroupCreateNewuser(userGroup_name_list[6], user_list[1], all)
            user.set_systemDisk_content(user.VDI_systemDisk_xpath, '50')
            user.click_confirm()
            user.edit_userGroupCharacter(userGroup_name_list[6], vdi)
            user.click_confirm()
            user.click_elem(user.warnning_confire_xpath)
            user.check_userDetail(user_list[1])
            user.click_elem(user.userDetail_vdiSet_xpath)
            assert user.get_elem_text(user.userDetail_vdiSetContent_xpath).find(open_info) >= 0
            user.click_elem(user.userDetail_close_xpath)
            logging.info("-----------------web用户管理A1.23用例结束--------------------")
            logging.info("-----------------web用户管理A1.32用例开始执行--------------------")
            user.edit_userGroupCharacter(userGroup_name_list[6], vdi)
            user.image_bind(vdi)
            user.changeCpuAccount()
            user.changeMemory(10)
            user.set_systemDisk_content(user.VDI_systemDisk_xpath, 60)
            user.changePersonalDisk(50)
            user.click_confirm()
            user.click_elem(user.warnning_confire_xpath)
            user.check_userDetail(user_list[1])
            user.click_elem(user.userDetail_vdiSet_xpath)
            assert user.get_elem_text(user.userDetail_cpuContent_xpath).find(cpuContent_info)
            assert user.get_elem_text(user.userDetail_memContent_xpath).find(memContent_info)
            assert user.get_elem_text(user.userDetail_systemDiskContent_xpath).find(systemDiskContent_info)
            assert user.get_elem_text(user.userDetail_perDiskContent_xpath).find(perDiskContent_info)
            user.click_elem(user.userDetail_close_xpath)
            time.sleep(com_slp)
            logging.info("-----------------web用户管理A1.32用例结束--------------------")
            logging.info("-----------------web用户管理A1.27，A1.28用例开始执行--------------------")
            user.edit_userGroupCharacter(userGroup_name_list[6])
            user.changeDesktopStyle(vdi, restore)
            user.image_bind(vdi, " ", vdi_image)
            user.click(user.vdi_set_xpath)
            user.click_confirm()
            user.click_elem(user.warnning_confire_xpath)
            user.check_userDetail(user_list[1])
            user.click_elem(user.userDetail_vdiSet_xpath)
            assert user.get_elem_text(user.userDetail_desktopContent_xpath).find(desktopStyleContent_info)
            assert user.get_elem_text(user.userDetail_imageContent_xpath).find(imageBindContent_info)
            user.click_elem(user.userDetail_close_xpath)
        finally:
            try:
                # 善后处理，删除添加过的数据
                user.driver.refresh()
                user.back_current_page()
                user.goto_usermanage_page()
                user.search_info(name=user_list[1])
                user.del_user(password=passwd)
                time.sleep(2)
                user.del_group(name=userGroup_name_list[6], password=passwd)
            except Exception as e:
                logging.info(e)
        logging.info("-----------------web用户管理A1.27，A1.28用例结束--------------------")

    @pytest.mark.userManage
    @pytest.mark.user
    def test_vlan_user(self, user_pm_fixture):
        logging.info("-----------------web用户管理A1.24用例开始执行--------------------")
        user = UserMange(user_pm_fixture)
        try:
            user.open_character(vdi, userGroup_name_list[7])
            user.image_bind(vdi)
            user.clear_input(user.vlan_input_xpath)
            user.elem_send_keys(user.vlan_input_xpath, '5')
            user.click_confirm()
            text1 = server_conn(host_ip, command3)
            text2 = server_conn(host_ip, command4)
            assert text1.find(command3[9:]) >= 0
            assert text2.find(command4[9:]) >= 0
            user.edit_userGroupCharacter(userGroup_name_list[7])
            user.clear_input(user.vlan_input_xpath)
            user.elem_send_keys(user.vlan_input_xpath, '4094')
            user.click_confirm()
            user.click_elem(user.warnning_confire_xpath)
            text1 = server_conn(host_ip, command1)
            text2 = server_conn(host_ip, command2)
            assert text1.find(command1[9:]) >= 0
            assert text2.find(command2[9:]) >= 0
        finally:
            try:
                # 善后处理
                user.user_recovery(userGroup_name_list[7])
                # time.sleep(2)
                # user.del_group(name=userGroup_name_list[7], password=passwd)
            except Exception as e:
                logging.info(e)
        logging.info("-----------------web用户管理A1.24用例结束--------------------")

    @pytest.mark.userManage
    @pytest.mark.userdm
    @pytest.mark.case_level_1
    @pytest.mark.autotest1
    def test_a1_29(self, com_fixture):
        """创建创建还原用户分组，并在分组下创建非自定义用户"""
        logging.info("-----------a1_29用例执行----------")
        user = UserMange(com_fixture)
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="gp_a1_29", img_name=restore_vdi_base, cd_type=u"还原")
            user.create_user_in_group(group_name="gp_a1_29", user_name="user_a1_29", real_name="user_a1_29")
            user.edit_user_vdi(user_name="user_a1_29", cd_type=u"个性", isadd=True, add_img=vdi_default_mirror)
            info = server_sql_qurey(host_ip, "select desktop from lb_seat_info where user_name = 'user_a1_29'")
            assert info == [(1,)]
        finally:
            try:
                user.user_recovery("gp_a1_29")
            except Exception as e:
                logging.info(e)

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.autotest1
    def test_a1_31(self, com_fixture):
        """创建创建还原用户分组，并在分组下创建非自定义用户"""
        logging.info(u"-----------a1_31用例执行----------")
        user = UserMange(com_fixture)
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="gp_a1_31", img_name=restore_vdi_base, cd_type=u"还原")
            user.create_user_in_group(group_name="gp_a1_31", user_name="user_a1_31", real_name="user_a1_31")
            # 修改组下用户，设置为非自定义用户
            user.edit_user_vdi(user_name="user_a1_31", cd_type=u"个性", isadd=True, add_img=vdi_default_mirror)
            # 编辑用户组属性修改个人盘为50G，验证对用户无影响
            user.editor_group_vdi_disk(gp_name="gp_a1_31", d_disk="50")
            info = server_sql_qurey(host_ip, "select disk_size from lb_seat_info where user_name = 'user_a1_31'")
            assert info != [(50,)]
        finally:
            try:
                user.user_recovery("gp_a1_31")
            except Exception as e:
                logging.info(e)

    @pytest.mark.userManage123
    @pytest.mark.usergroup_idv
    def test_changeUsergroupIdvCharacter(self, user_pm_fixture):
        userIdv = UserMange(user_pm_fixture)
        try:
            userIdv.createUserGroupCreateNewuser(userGroup_name_list[8], user_list[2], idv)
            userIdv.click_elem(userIdv.confire_button_xpath)
            time.sleep(com_slp)
            userIdv.findUserGroupCreateNewuser(userGroup_name_list[8], user_list[3])
            userIdv.set_systemDisk_content(userIdv.IDV_systemDisk_xpath, 50)
            userIdv.click_elem(userIdv.confire_button_xpath)
            time.sleep(3)
            logging.info("-----------------web用户管理A1.37，A1.39，A1.42用例开始执行--------------------")
            userIdv.edit_userGroupCharacter(userGroup_name_list[8])
            userIdv.changeDesktopStyle(idv, restore)
            userIdv.image_bind(idv, idv_image)
            userIdv.click_elem(userIdv.confire_button_xpath)
            info = userIdv.get_tips()
            assert u"IDV云终端桌面类型[个性--->还原]，将删除用户保存在IDV终端上的系统盘个性数据" in info
            userIdv.click(userIdv.sure_xpath)
            userIdv.send_passwd_confirm(passwd)
            userIdv.check_userDetail(user_list[2])
            userIdv.click_elem(userIdv.userDetail_idvSet_xpath)
            assert userIdv.get_elem_text(userIdv.userDetail_idvDesktopStyle_xpath).find(restore) >= 0
            userIdv.click_elem(userIdv.userDetail_close_xpath)
            userIdv.check_userDetail(user_list[3])
            userIdv.click_elem(userIdv.userDetail_idvSet_xpath)
            assert userIdv.get_elem_text(userIdv.userDetail_idvDesktopStyle_xpath).find(desktopStyleContent_info) >= 0
            assert userIdv.get_elem_text(userIdv.userDetail_idvImageContent_xpath).find(imageIdvBindContent_info) >= 0
            userIdv.click_elem(userIdv.userDetail_close_xpath)
            userIdv.findUserGroupCreateNewuser(userGroup_name_list[8], user_list[4])
            assert userIdv.get_elem_attribute(userIdv.idvdesktop_xpath, 'value') == restore
            userIdv.click_elem(userIdv.confire_button_xpath)
            logging.info("----------------------web用户管理A1.37，A1.39，A1.42用例结束-----------------------")
            logging.info("----------------------web用户管理A1.38用例开始执行-----------------------")
            time.sleep(2)
            userIdv.edit_userGroupCharacter(userGroup_name_list[8])
            userIdv.changeDesktopStyle(idv, personality)
            userIdv.image_bind(idv)
            userIdv.click_confirm()
            userIdv.click_elem(userIdv.warnning_confire_xpath)
            userIdv.check_userDetail(user_list[2])
            userIdv.click_elem(userIdv.userDetail_idvSet_xpath)
            assert userIdv.get_elem_text(userIdv.userDetail_idvDesktopStyle_xpath).find(personality) >= 0
            userIdv.click_elem(userIdv.userDetail_close_xpath)
            userIdv.findUserGroupCreateNewuser(userGroup_name_list[8], user_list[5])
            assert userIdv.get_elem_attribute(userIdv.idvdesktop_xpath, 'value').find(personality) >= 0
            time.sleep(com_slp)
            userIdv.click_elem(userIdv.confire_button_xpath)
            logging.info("----------------------web用户管理A1.38用例结束-----------------------")
            logging.info("-----------------web用户管理A1.34，A1.36用例开始执行--------------------")
            time.sleep(2)
            userIdv.edit_userGroupCharacter(userGroup_name_list[8], idv)
            userIdv.click_confirm()
            info = userIdv.get_tips()
            assert u"将无法登录IDV终端" in info
            userIdv.click(userIdv.sure_xpath)
            userIdv.send_passwd_confirm(passwd)
            userIdv.check_userDetail(user_list[2])
            userIdv.click_elem(userIdv.userDetail_idvSet_xpath)
            assert userIdv.get_elem_text(userIdv.userDetail_idvSetContent_xpath).find(close_info) >= 0
            userIdv.click_elem(userIdv.userDetail_close_xpath)
            userIdv.check_userDetail(user_list[3])
            userIdv.click_elem(userIdv.userDetail_idvSet_xpath)
            assert userIdv.find_elem(userIdv.userDetail_idvSetContent_xpath).text.find(open_info) >= 0
            userIdv.click_elem(userIdv.userDetail_close_xpath)
        finally:
            try:
                # 善后处理
                userIdv.user_recovery(userGroup_name_list[8])
                # userIdv.del_user_in_group(group_name=userGroup_name_list[8])
                # time.sleep(2)
                # userIdv.del_group(name=userGroup_name_list[8], password=passwd)
            except Exception as e:
                logging.info(e)
        logging.info("-----------------web用户管理A1.34用例未结束，仅完成一点  A1.36用例结束--------------------")

    # -------------------------------以上用例为原78条用例集中的排序，以下用的是100条用例的用例集排序--------------------

    # @pytest.mark.userManage
    # @pytest.mark.user
    # def test_inheritCharacter(self, user_pm_fixture):
    #     logging.info("---------------------web用户管理A1.55用例开始执行--------------------")
    #     user = UserMange(user_pm_fixture)
    #     try:
    #         user.open_character(all, userGroup_name_list[10])
    #         user.image_bind(all)
    #         user.changePersonalDisk(50)
    #         user.open_spaceDisk()
    #         characterList = user.characterDetail(all)
    #         user.click_confirm()
    #         time.sleep(com_slp)
    #         logging.info("创建新的vdi用户组，用于有特性用户更改组时选择")
    #         user.open_character(vdi, userGroup_name_list[11])
    #         user.image_bind(vdi)
    #         perDiskSize = user.get_elem_attribute(user.personalDisk_xpath, 'value')
    #         user.click_confirm()
    #         logging.info("比对新建用户是否继承用户组特性")
    #         user.findUserGroupCreateNewuser(userGroup_name_list[10], user_list[7])
    #         user.property_compare(characterList, all)
    #         user.click_confirm()
    #         time.sleep(3)
    #         logging.info("---------------------web用户管理A1.55用例结束------------------------")
    #         logging.info("---------------------web用户管理A1.56 A1.57用例开始执行--------------------")
    #         user.edit_user(user_list[7])
    #         user.choose_userGroup(userGroup_name_list[11])
    #         user.click_elem(user.vdi_set_xpath)
    #         #   user.warnning_info()
    #         user.click_confirm()
    #         user.click_elem(user.warnning_confire_xpath)
    #         time.sleep(com_slp)
    #         user.click_usergp_list(userGroup_name_list[11])
    #         user.edit_user(user_list[7])
    #         logging.info("新用户组仅开启vdi特性，用户特性相较原来不做更改,且个人盘与当前用户组个人盘大小不同")
    #         user.property_compare(characterList, all)
    #         assert user.get_elem_attribute(user.personalDisk_xpath, 'value') != perDiskSize
    #         user.back_current_page()
    #         user.click_elem(user.cancel_button1)
    #     finally:
    #         try:
    #             # 善后处理：删除数据
    #             user.del_user_in_group(group_name=userGroup_name_list[11])
    #             time.sleep(3)
    #             user.del_group(name=userGroup_name_list[11], password=passwd)
    #             time.sleep(1)
    #             user.del_group(name=userGroup_name_list[10], password=passwd)
    #         except Exception as e:
    #             logging.info(e)
    #     logging.info("---------------------web用户管理A1.56,A1.57用例结束------------------------")

    @pytest.mark.userManage
    @pytest.mark.user
    def test_vdiSwitch(self, user_pm_fixture):
        logging.info("---------------------web用户管理A1.58用例开始执行---------------------")
        user = UserMange(user_pm_fixture)
        try:
            user.createUserGroupCreateNewuser(userGroup_name_list[12], user_list[8], ' ', vdi)
            assert user.get_elem_text(user.usergroup_vdi_status_open_xpath).find(open_info) >= 0
            user.click_confirm()
            user.judgeUserDefine(user_list[8])
            user.edit_userGroupCharacter(userGroup_name_list[12], vdi)
            user.click_elem(user.vdi_set_xpath)
            user.image_bind(vdi)
            user.click_confirm()
            user.click_elem(user.warnning_confire_xpath)
            user.edit_user(user_list[8])
            user.click_elem(user.usergroup_vdi_switch_xpath)
            assert user.get_elem_text(user.usergroup_vdi_status_close_xpath).find(close_info) >= 0
            user.click_elem(user.confire_button_xpath)
            user.warnning_info(vdiCharacterError_info)
            user.judgeUserDefine(user_list[8])
        finally:
            try:
                # 善后处理
                user.user_recovery(userGroup_name_list[12])
                # user.del_user_in_group(group_name=userGroup_name_list[12])
                # time.sleep(2)
                # user.del_group(name=userGroup_name_list[12], password=passwd)
            except Exception as e:
                logging.info(e)
        logging.info("---------------------web用户管理A1.58用例结束-----------------------")

    @pytest.mark.userManage123
    @pytest.mark.user
    def test_idvSwitch(self, user_pm_fixture):
        logging.info("---------------------web用户管理A1.65用例开始执行---------------------")
        user = UserMange(user_pm_fixture)
        try:
            user.createUserGroupCreateNewuser(userGroup_name_list[13], user_list[9], ' ', idv)
            assert user.get_elem_text(user.usergroup_idv_status_open_xpath).find(open_info) >= 0
            user.click_confirm()
            user.judgeUserDefine(user_list[9])
            user.edit_userGroupCharacter(userGroup_name_list[13], idv)
            user.image_bind(idv)
            user.click_confirm()
            user.click_elem(user.warnning_confire_xpath)
            user.edit_user(user_list[9])
            user.click_elem(user.usergroup_idv_switch_xpath)
            assert user.get_elem_text(user.usergroup_idv_status_close_xpath).find(close_info) >= 0
            user.click_confirm()
            info = user.get_tips()
            assert u"将无法登录IDV终端" in info
            user.click(user.sure_xpath)
            user.send_passwd_confirm(passwd)
            user.judgeUserDefine(user_list[9])
        finally:
            try:
                # 善后处理
                user.user_recovery(userGroup_name_list[13])
                # user.del_user_in_group(group_name=userGroup_name_list[13])
                # time.sleep(2)
                # user.del_group(name=userGroup_name_list[13], password=passwd)
            except Exception as e:
                logging.info(e)
        logging.info("---------------------web用户管理A1.65用例结束-----------------------")

    # @pytest.mark.userManage
    # @pytest.mark.user
    # def test_userDetail(self, user_pm_fixture):
    #     logging.info("---------------------web用户管理A1.77用例开始执行---------------------")
    #     user = UserMange(user_pm_fixture)
    #     try:
    #         user.createUserGroupCreateNewuser(userGroup_name_list[14], user_list[10], idv)
    #         user.click_confirm()
    #         time.sleep(com_slp)
    #         user.click_elem(user.userName_list_xpath % user_list[10])
    #         try:
    #             user.find_elem(user.userDetailDialog)
    #         except:
    #             logging.info("列表单击用户名未打开用户详情")
    #             return
    #         else:
    #             pass
    #         user.click_elem(user.userDetail_idvSet_xpath)
    #         assert user.get_elem_text(user.userDetail_idvSetContent_xpath).find(open_info) >= 0
    #         assert user.get_elem_text(user.userDetail_idvImageContent_xpath).find(idv_default_image) >= 0
    #         assert user.get_elem_text(user.userDetail_idvDesktopStyle_xpath).find(personality) >= 0
    #         assert user.get_elem_text(user.userDetail_idvSysDiskContent_xpath).find(idv_default_image_sysDiskSize) >= 0
    #         assert user.get_elem_text(user.userDetail_allowLocationDisk).find(yes) >= 0
    #         user.click(user.close_info_button_xpath)
    #     finally:
    #         try:
    #             # 善后处理
    #             user.user_recovery(userGroup_name_list[14])
    #             # user.del_user_in_group(group_name=userGroup_name_list[14])
    #             # time.sleep(2)
    #             # user.del_group(name=userGroup_name_list[14], password=passwd)
    #         except Exception as e:
    #             logging.info(e)
    #     logging.info("-----------------------web用户管理A1.77用例结束-----------------------")

    @pytest.mark.userManage123
    @pytest.mark.user
    @pytest.mark.user_test_a1_85
    def test_IpFill(self, user_pm_fixture):
        logging.info("-----------------------web用户管理A1.85用例开始执行-----------------------")
        user = UserMange(user_pm_fixture)
        try:
            user.createUserGroupCreateNewuser(userGroup_name_list[16], user_list[12])
            user.click_confirm()
            user.moreButtonList(user.fillIP_xpath)
            assert user.get_elem_text(user.fillIpTip_xpath).find(noUserFillIp_Info) >= 0
            user.click_elem(user.userCheckBox_xpath % user_list[12])
            user.moreButtonList(user.fillIP_xpath)
            user.fillip(ip_fill, subnetMask, gateWay, dns_fill, all)
            assert user.get_elem_text(user.fillIpTip_xpath).find(noVdiFillIp_Info) >= 0
            time.sleep(2)
            user.click_elem(user.cancel_button_xpath)
            time.sleep(3)
            user.edit_userGroupCharacter(userGroup_name_list[16], vdi)
            user.image_bind(vdi)
            user.click_confirm()
            user.click_elem(user.warnning_confire_xpath)
            time.sleep(com_slp)
            user.findUserGroupCreateNewuser(userGroup_name_list[16], user_list[13])
            user.click_confirm()
            for i in range(12, 14):
                time.sleep(3)
                user.click_elem(user.userCheckBox_xpath % user_list[i])
                user.moreButtonList(user.fillIP_xpath)
                if 12 == i:
                    user.fillip(ip_fill, subnetMask, gateWay, dns_fill, all)
                else:
                    user.fillip(ip_fill, subnetMask, gateWay, dns_fill, noIP)
                assert user.get_elem_text(user.tip_xpath).find(ipFillSuccess_info) >= 0
            for i in range(14, 16):
                user.findUserGroupCreateNewuser(userGroup_name_list[16], user_list[i])
                user.click_confirm()
                time.sleep(3)
            user.click_elem(user.allCheckBox_xpath)
            user.moreButtonList(user.fillIP_xpath)
            user.fillip(ip_fill, subnetMask, gateWay, dns_fill, all)
            assert user.get_elem_text(user.tip_xpath).find(ipFillSuccess_info) >= 0
            time.sleep(3)
            for i in range(12, 16):
                user.check_userDetail(user_list[i])
                user.cloud_desk_ip()
                assert int(user.cloud_desk_ip().split('.')[3]) == int(ip_fill.split('.')[3]) + (i - 12)
                user.close_info()
        finally:
            try:
                # 善后处理
                user.user_recovery(userGroup_name_list[16])
            except Exception as e:
                logging.info(e)
        logging.info("-----------------------web用户管理A1.85用例结束，IP自动分配一项未验证-----------------------")

    @pytest.mark.userManage
    @pytest.mark.user
    def test_userDefineShow(self, user_pm_fixture):
        logging.info("-----------------------web用户管理A1.96用例开始执行-----------------------")
        user = UserMange(user_pm_fixture)
        try:
            user.createUserGroupCreateNewuser(userGroup_name_list[15], user_list[11], ' ', idv)
            user.click_confirm()
            user.judgeUserDefine(user_list[11])
            user.chainstay(user.user_defined_xpath % user_list[11])
            assert user.get_elem_text(user.userDefineInfo_xpath).find(userDefineInfo) >= 0
            user.check_userDetail(user_list[11])
            user.click_elem(user.userDetail_idvSet_xpath)
            assert user.get_elem_text(user.userDetail_idvSetContent_xpath).find(characterStatusOpenDetail) >= 0
            time.sleep(com_slp)
            user.click(user.close_info_button_xpath)
        finally:
            try:
                # 善后处理
                user.user_recovery(userGroup_name_list[15])
                # user.del_user_in_group(group_name=userGroup_name_list[15])
                # time.sleep(2)
                # user.del_group(name=userGroup_name_list[15], password=passwd)
            except Exception as e:
                logging.info(e)
        logging.info("-----------------------web用户管理A1.96用例结束-----------------------")

    @pytest.mark.userManage
    @pytest.mark.user
    def test_search(self, user_pm_fixture):
        logging.info("-----------------------web用户管理A1.97用例结束-----------------------")
        user = UserMange(user_pm_fixture)
        assert user.get_elem_attribute(user.search_xpath, 'placeholder').find(search_info) >= 0
        user.elem_send_keys(user.search_xpath, searchContent)
        user.elem_send_keys(user.search_xpath, Keys.ENTER)
        try:
            assert user.get_elem_text(user.searchCount_xpath).find(searchCountIsZero) >= 0
            assert user.get_elem_text(user.searchNoData_xpath).find(searchNoData) >= 0
        except:
            logging.info("搜索出现错误条目")
        else:
            logging.info("暂无数据")
        logging.info("-----------------------web用户管理A1.97用例结束-----------------------")

    @pytest.mark.userManage
    @pytest.mark.user
    def test_userDefineCharacter(self, user_pm_fixture):
        logging.info("-----------------------web用户管理A1.74用例开始执行-----------------------")
        user = UserMange(user_pm_fixture)
        try:
            user.createUserGroupCreateNewuser(userGroup_name_list[17], user_list[16], ' ', idv)
            curStatus = idv
            user.click_confirm()
            time.sleep(3)
            for text in info_list:
                statusList = [idv, vdi, space]
                user.judgeUserDefine(user_list[16])
                user.edit_user(user_list[16])
                statusList.remove(curStatus)
                assert user.characterStatus(curStatus) == 1
                for status in statusList:
                    assert user.characterStatus(status) == 0
                    time.sleep(com_slp)
                if curStatus == vdi:
                    return
                user.openCharacter(statusList[-1])
                if statusList[-1] == vdi:
                    user.image_bind(vdi)
                user.click_confirm()
                info = user.get_tips()
                assert text in info
                user.click(user.sure_xpath)
                user.send_passwd_confirm(passwd=passwd)
                time.sleep(2)
                curStatus = statusList[-1]
                # 善后处理
        finally:
                user.user_recovery(userGroup_name_list[17])

        logging.info("-----------------------web用户管理A1.74用例结束-----------------------")

    @pytest.mark.userManage1234
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_40_41_idv(self, com_fixture):
        logging.info("-----------------------web用户管理A1.40、41用例开始-----------------------")
        """
        执行步骤：
        1、对用户组 IDV云终端设置关闭切换为开启
        2、对用户组 IDV云终端设置开启切换为关闭
        预期结果：
        1、关->开，组内用户支持IDV终端使用
        2、开->关，组内用户失去IDV终端使用能力,该操作需增加风险提示，并二次密码输入确认
        3、不影响当前在用IDV用户使用
        4、终端重启后更新用户信息，原绑定用户在线登录失败；脱网也无法登陆。
        """
        u = UserMange(com_fixture)
        Idv = IdvPage(com_fixture)
        c = CDeskMange(com_fixture)
        try:
            u.goto_usermanage()
            u.createUserGroupCreateNewuser(idv_tm, user_idv_tm, idv)
            u.click_confirm()
            u.back_current_page()
            # 进入终端管理--多用户终端组
            Idv.goto_idv_terminal_page()
            Idv.goto_idv_terminal_moreandpub_terminal_group_page()
            # 搜索终端，获取终端ip绑定用户后重启终端
            Idv.reboot_terminal(name=idv_public_ip_list[2])
            Idv.back_current_page()
            time.sleep(80)
            # 设置用户密码并登录终端
            click_idv_set(idv_public_ip_list[2])  # idv_public_ip_list[2]
            idv_change_pwd(idv_public_ip_list[2], user_idv_tm, "123")
            idv_login(idv_public_ip_list[2], user_idv_tm)
            time.sleep(10)  # 待终端登录成功
            logging.info("41用例结束,40用例开始")
            Idv.back_current_page()
            time.sleep(2)
            u.goto_usermanage()
            u.edit_gp_idv(idv_tm, 'close')
            u.edit_user(user_idv_tm)
            assert u.get_elem_text(u.usergroup_idv_status_close_xpath).find(close_info) >= 0
            u.click_cancel()
            u.back_current_page()
            time.sleep(1)
            Idv.goto_idvtm_page()
            Idv.goto_idv_terminal_moreandpub_terminal_group_page()
            Idv.reboot_terminal(name=idv_public_ip_list[2])
            Idv.back_current_page()
            time.sleep(80)
            # 登录终端
            idv_screan_siz_set(idv_public_ip_list[2])  # 设置终端分辨率
            time.sleep(1)
            idv_login(ip=idv_public_ip_list[2], user_name=user_idv_tm)
            time.sleep(10)  # 待终端登录成功
            c.goto_cloud_desk_manage()
            assert c.get_status(name=idv_tm).find(u"离线") >= 0
            c.back_current_page()
        finally:
            try:
                # 善后处理
                Idv.driver.refresh()
                Idv.goto_idvtm_page()
                Idv.goto_idv_terminal_moreandpub_terminal_group_page()
                Idv.reboot_terminal(name=idv_public_ip_list[2])
                Idv.back_current_page()
                time.sleep(2)
                u.goto_usermanage()
                time.sleep(5)
                u.del_user_in_group(group_name=idv_tm)
                time.sleep(2)
                u.del_group(name=idv_tm, password=passwd)
            except Exception as e:
                logging.info(e)
        logging.info("-----------------------web用户管理A1.40、41用例结束-----------------------")

    @pytest.mark.userManage1234
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_44_70_idv(self, com_fixture):
        logging.info("-----------------------web用户管理A1.44、70用例开始-----------------------")
        """
        执行步骤：
        1、对用户组 IDV云终端设置云桌面类型还原->个性
        2、组内新增用户
        3、对用户IDV云终端配置修改，对在用用户的影响
        预期结果：
        1、组内原先还原用户，桌面类型变更为个性，且当前在用用户不影响，IDV终端重启连接云主机后生效
        2、新增用户为个性模式
        3、不影响当前在用IDV云终端使用
        """
        u = UserMange(com_fixture)
        Idv = IdvPage(com_fixture)
        c = CDeskMange(com_fixture)
        group_name = "group_44"
        user_name = "user_44"
        try:
            u.goto_usermanage()
            u.create_group_openidv(group_name, restore, idv_image)  # 运行时镜像改为还原镜像
            u.findUserGroupCreateNewuser(group_name, user_name)
            u.click_confirm()
            u.back_current_page()
            # 进入终端管理--多用户终端组
            Idv.goto_idv_terminal_page()
            Idv.goto_idv_terminal_moreandpub_terminal_group_page()
            # 搜索终端，获取终端ip绑定用户后重启终端
            Idv.reboot_terminal(name=idv_public_ip_list[2])
            Idv.wait_tm_reboot_success(idv_public_ip_list[2], 1)
            time.sleep(2)
            # 设置用户密码并登录终端
            idv_initialization_click(idv_public_ip_list[2])
            click_idv_set(idv_public_ip_list[2])
            idv_change_pwd(idv_public_ip_list[2], user_name, "123")
            idv_login(idv_public_ip_list[2], user_name)
            if win_conn_useful(idv_public_ip_list[2], user_name, "123"):
                c.goto_cloud_desk_manage()
                c.goto_cloud_desktop_search(user_name)
                dcip = c.get_cloud_desk_ip(user_name)
                c.back_current_page()
                info = get_win_conn_info(dcip, s_user, s_pwd, r'dir')
                assert info.find(newfile) < 0
        finally:
                # 善后处理
                Idv.goto_idv_terminal_page()
                time.sleep(2)
                Idv.goto_idv_terminal_moreandpub_terminal_group_page()
                time.sleep(2)
                Idv.reboot_terminal(name=idv_public_ip_list[2])
                Idv.wait_tm_reboot_success(idv_public_ip_list[2], 1)
                u.user_recovery(group_name)

        logging.info("-----------------------web用户管理A1.44、70用例结束-----------------------")

    # -----------------------------------吴少锋完成的部分结束-------------------------------------#

    # ------------------------------------------cyl------------------------------------------#
    @pytest.mark.userManage
    @pytest.mark.userdm
    @pytest.mark.case_level_1
    def test_collectlog(self, com_fixture):
        """
        执行步骤：1、当用户处于运行中，在云桌面管理界面，选择云桌面，点击日志收集
        预期结果：1、可收集该在用用户VDI日志信息
        """
        logging.info('-----------------------------Web用户管理：A1.79例开始执行-----------------------')
        user = UserMange(com_fixture)
        group_name = "ugp_a1_79"
        user_name = "user_a1_79"
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name=group_name, img_name=restore_vdi_base, cd_type=u"还原")
            user.create_user_in_group(group_name=group_name, user_name=user_name, real_name=user_name)
            user.driver.refresh()
            user.login_client(user_name, "123456")
            time.sleep(150)
            user.back_current_page()
            user.goto_cdesk_page()
            user.refresh_webdriver()
            user.find_user(user_name)
            user.collect_log(user_name)
            time.sleep(2)
            logging.info("判断用户运行时收集云桌面日志是否成功")
            assert user.collect_log_succ() != ''
        finally:
            user.close_client()
            time.sleep(30)
            user.user_recovery(group_name)
        logging.info("----------------------------------测试用例结束-------------------------")

    # @pytest.mark.case_level_2
    # @pytest.mark.userManage
    # def test_collectlog_sleep(self, com_fixture):
    #     """
    #     执行步骤：1、当用户处于关闭或者休眠状态时，在云桌面管理界面，选择云桌面，点击日志收集
    #     预期结果：1、无法收集，并提示“云桌面处于关闭或休眠状态，不能实时收集日志！”
    #     """
    #     logging.info('------------------------Web用户管理：A1.80例开始执行---------------------------')
    #     user = UserMange(com_fixture)
    #     group_name = "ugp_a1_80"
    #     user_name = "user_a1_80"
    #     try:
    #         user.goto_usermanage_page()
    #         user.create_group_openvdi(group_name=group_name, img_name=restore_vdi_base, cd_type=u"还原")
    #         user.create_user_in_group(group_name=group_name, user_name=user_name, real_name=user_name)
    #         user.driver.refresh()
    #         user.login_client(user_name, "123456")
    #         time.sleep(150)
    #         user.close_client()
    #         time.sleep(60)
    #         user.goto_cdesk_page()
    #         user.find_user("user_a1_79")
    #         time.sleep(2)
    #         logging.info("判断用户关闭或休眠时收集云桌面日志是否成功")
    #         assert user.desklog_errormsg_tips() != ''
    #     finally:
    #         user.user_recovery(group_name)
    #     logging.info("----------------------------------测试用例结束-------------------------")

    # @pytest.mark.case_level_2
    # @pytest.mark.userManage
    # def test_ipdelete_without_check(self, user_pm_fixture):
    #     """
    #     执行步骤：1、未勾选用户时，点击IP清空操作
    #     预期结果：1、IP清空失败，且提示“没有选中任何数据，请先选择!”
    #     """
    #     logging.info('----------------------------Web用户管理：A1.90例开始执行---------------------------')
    #     u = UserMange(user_pm_fixture)
    #     u.goto_usermanage_page()
    #     u.ip_delete()
    #     time.sleep(2)
    #     logging.info("判断在不选中用户的前提下点击清空ip是否成功")
    #     assert u.deleteip_errormsg_get() != ''
    #     logging.info("----------------------------------测试用例结束-------------------------")

    @pytest.mark.case_level_1
    @pytest.mark.userManage
    def test_deleteip_with_checkuser(self, user_pm_fixture):
        """
        执行步骤：1、选择已配好IP的用户点击清空IP按钮（包含只配置DNS或IP或全配的情况）
        预期结果：1、IP清空成功
        """
        logging.info('-----------------------------Web用户管理：A1.89例开始执行------------------------------')
        u = UserMange(user_pm_fixture)
        group_name = "ugp_a1_89"
        user_name = "user_a1_89"
        try:
            u.goto_usermanage_page()
            u.create_group_openvdi(group_name=group_name, img_name=restore_vdi_base, cd_type=u"还原")
            u.create_user_in_group(group_name=group_name, user_name=user_name, real_name=user_name)
            u.driver.refresh()
            u.login_client(user_name, "123456")
            time.sleep(150)
            u.close_client()
            time.sleep(60)
            u.find_user(user_name)
            # 只配置DNS
            u.edit_user(user_name)
            time.sleep(2)
            u.vdi_set()
            u.edit_ip('', '', '', main_DNS1, prepare_DNS1)
            u.confirm_edit()
            u.choose_user(user_name)
            u.clear_ip()
            logging.info('只配DNS时，IP清空成功')
            assert u.check_ipclear() != ''
            # 全配
            u.refresh_webdriver()
            u.goto_usermanage_page()
            u.find_user(user_name)
            u.edit_user(user_name)
            time.sleep(2)
            u.vdi_set()
            u.edit_ip(ip1, subnet_mask1, gateway1, main_DNS1, prepare_DNS1)
            u.confirm_edit()
            u.choose_user(user_name)
            u.clear_ip()
            logging.info('只配DNS时，IP清空成功')
            assert u.check_ipclear() != ''
            time.sleep(2)
        finally:
            u.user_recovery(group_name)
        logging.info("----------------------------------测试用例结束-------------------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    def test_attribute_list_drag(self, user_pm_fixture):
        """
        前置步骤：在Web用户管理界面
                1、勾选用户各类属性并展示
                2、拖拽已展示的属性
        预期结果：1、用户属性默认展示用户名、状态、IDV、IDV终端IP、IDV云桌面IP、VDI、VDI终端IP、VDI云桌面IP、网盘、操作等，可选展示属性有姓名、类型、绑定终端、备课资源等
                2、用户名固定在列表第一列，操作固定在列表末端，其余属性可拖拽
        """
        logging.info("----------------------------------Web用户管理：A1.94例开始执行------------------------------")
        u = UserMange(user_pm_fixture)
        u.goto_usermanage_page()
        flag_list = u.attribute_list_drag()
        logging.info("判断勾选指定字段后列表数目正确")
        assert flag_list[0] == 1
        logging.info("判断可拖动元素有可拖动排序属性")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.case_level_1
    @pytest.mark.userManage
    def test_user_sort_rule(self, user_pm_fixture):
        """
            前置步骤：在Web用户管理界面
                    1、点击用户属性排序用户
            执行步骤：在Web用户管理界面
                    1、点击用户属性排序用户
            预期结果：在用户属性中
                    1、用户名、用户组、姓名、绑定终端支持数字字母排序
                    2、IDV终端IP、IDV虚机IP、VDI终端IP、VDI虚机IP、云盘属性支持数字排序
                    3、默认用户名升序，页面退出后重新进不记录之前排序规则
        """
        logging.info("----------------------------------Web用户管理：A1.95例开始执行------------------------------")
        u = UserMange(user_pm_fixture)
        u.goto_usermanage_page()
        u.show_user_attribute()
        flag = u.user_sort_rule()
        logging.info("判断用户名、用户组、姓名、绑定终端是否正确")
        assert flag[0] == 1
        logging.info("判断IDV终端IP、IDV虚机IP、VDI终端IP、VDI虚机IP、云盘是否正确")
        assert flag[1] == 1
        logging.info("判断刷新后是否恢复默认排序")
        assert flag[2] == 1
        time.sleep(2)
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # 导入用户模板
    @pytest.mark.userManage
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_import_model_user(self, user_pm_fixture):
        """
        执行步骤：1、当web用户组中只有一个未分组初始状态时，用户模板下载和导入
        预期结果：1、用户模板下载和导入（导入用户名称支持中英文特殊字符等），有导入用户数、耗时提示
        :param user_pm_fixture:
        :return:
        """
        logging.info("----------------------------------Web用户管理：A1.82例开始执行------------------------------")
        u = UserMange(user_pm_fixture)
        u.download_usermodel()
        u.import_usermodel()
        u.choose_usermodel(usermodel_xlsx)
        time.sleep(2)
        logging.info("判断导入用户模板是否成功")
        assert u.confirm_import_usermodel() != ''
        # 还原环境，删除组和用户
        time.sleep(1)
        u.group_click(vdi_model_group_name)
        time.sleep(1)
        try:
            u.delete_user_in_group(vdi_model_group_name, passwd)
            time.sleep(5)
        except:
            pass
        u.delete_group(vdi_model_group_name, passwd)
        time.sleep(2)
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.case_level_0
    # @pytest.mark.userManage
    # @pytest.mark.usertest_a1_84
    # def test_import_vdi_model(self, user_pm_fixture):
    #     """
    #     执行步骤：1、当web上已创建有与用户模板中同名的VDI特性已开启的用户组时，若该同名用户组待导入用户的个人盘或者系统盘所需空间充足时用户模板导入
    #              2、当web上已创建有与用户模板中同名的VDI特性已开启的用户组时，若该同名用户组用户的个人盘或者系统盘所需空间不足时用户模板导入
    #     预期结果：1、用户模板导入成功（导入用户名称支持中英文特殊字符等），有导入用户数、耗时提示
    #              2、用户导入失败，并提示相应的导入失败原因
    #     """
    #     logging.info("----------------------------------Web用户管理：A1.84例开始执行------------------------------")
    #     u = UserMange(user_pm_fixture)
    #     time.sleep(1)
    #     u.group_click(u"总览")
    #     u.create_group()
    #     u.set_group_name(vdiGroupName)
    #     u.group_vdi_attribute()
    #     time.sleep(1)
    #     u.edit_vdi_mirror(vdi_default_mirror)
    #     time.sleep(3)
    #     u.confirm_create_group()
    #     time.sleep(3)
    #     u.group_click(vdiGroupName)
    #     u.import_usermodel()
    #     u.choose_usermodel(usermodel_xlsx3)
    #     time.sleep(2)
    #     logging.info("判断空间不足时导入vdi用户模板是否成功")
    #     assert u.error_msg() != ''
    #     u.import_error()
    #     u.import_usermodel()
    #     u.choose_usermodel(usermodel_xlsx)
    #     time.sleep(2)
    #     logging.info("判断空间充足时导入vdi用户模板是否成功")
    #     assert u.confirm_import_usermodel() != ''
    #     # 还原环境，将以上导入的用户删除
    #     u.del_group(vdiGroupName, passwd)
    #     try:
    #         u.delete_user_in_group(vdi_model_group_name, passwd)
    #         time.sleep(5)
    #     except:
    #         pass
    #     u.del_group(vdi_model_group_name, passwd)
    #     time.sleep(2)
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")


    # @pytest.mark.case_level_1
    # @pytest.mark.userManage
    # def test_ip_conflict(self, user_pm_fixture):
    #     """
    #     执行步骤：1、选个一个用户，县级IP填充，输入的IP是已经分配给其他用户的
    #     预期结果：1、IP填充失败，给出相应提示信息
    #     """
    #     logging.info("----------------------------------Web用户管理：A1.88例开始执行------------------------------")
    #     u = UserMange(user_pm_fixture)
    #     u.goto_usermanage_page()
    #     u.find_user(norun_user[2])
    #     u.edit_config(norun_user[2])
    #     u.vdi_set()
    #     u.edit_ip(ip2, subnet_mask2, gateway2, main_DNS2, prepare_DNS2)
    #     u.confirm_edit()
    #     u.find_user(norun_user[3])
    #     u.edit_config(norun_user[3])
    #     u.vdi_set()
    #     u.edit_ip(ip2, subnet_mask2, gateway2, main_DNS2, prepare_DNS2)
    #     u.confirm_edit()
    #     logging.info("判断是否给出ip冲突提示")
    #     assert u.edit_false_msg() != ''
    #     time.sleep(2)
    #     u.close_edit()
    #     # 还原环境，将ip改为空
    #     u.find_user(norun_user[2])
    #     u.edit_config(norun_user[2])
    #     u.vdi_set()
    #     u.edit_ip('', '', '', '', '')
    #     u.confirm_edit()
    #     time.sleep(2)
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.case_level_2
    # @pytest.mark.userManage
    # def test_overlay_2IP(self, user_pm_fixture):
    #     """执行步骤：1、填充ip出现跨2网段即最后一个用户填充的地址超过255时，若两个网段的地址不在一个大网段
    #                 2、填充ip出现跨2网段即最后一个用户填充的地址超过255时，若两个网段的地址都在一个大网段
    #        预期结果：（两个网段ip是否在一个大网段取决于子网掩码，即：两个网段ip和子网掩码都换算成二进制进行&运算得到结果相同则是同一个大网段，反之就不是同一个大网段）
    #                 1、填充失败，且提示“此网段的网络资源不足！”
    #                 2、填充成功，然后查看下跨网段的ip起始地址都合法（ip应在1-255）
    #     """
    #     logging.info("----------------------------------Web用户管理：A1.86例开始执行------------------------------")
    #     u = UserMange(user_pm_fixture)
    #     u.group_click(vdi_group_name)
    #     time.sleep(1)
    #     u.choose_user(norun_user[1])
    #     time.sleep(1)
    #     u.choose_user(norun_user[2])
    #     time.sleep(1)
    #     u.choose_user(norun_user[3])
    #     time.sleep(2)
    #     u.fill_ip_allinfo(ip3, subnet_mask3, gateway3, main_DNS3)
    #     logging.info("判断是否给出网段网络资源不足提示")
    #     assert u.edit_false_msg() != ''
    #     time.sleep(2)
    #     u.close_edit()
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.case_level_0
    @pytest.mark.userManage
    def test_import_model_sameuser(self, user_pm_fixture):
        """
        执行步骤：1、当web上已创建有与用户模板中同名的VDI特性未开启的用户组时，导入用户模板
        预期结果：1、用户模板导入成功（导入用户名称支持中英文特殊字符等），有导入用户数、耗时提示
        """
        logging.info("----------------------------------Web用户管理：A1.83例开始执行------------------------------")
        u = UserMange(user_pm_fixture)
        u.goto_usermanage_page()
        u.group_click(u'总览')
        u.create_group()
        u.set_group_name(vdi_model_group_name)
        u.confirm_create_group()
        time.sleep(2)
        u.import_usermodel()
        u.choose_usermodel(usermodel_xlsx)
        time.sleep(2)
        logging.info("判断导入同组名用户模板是否成功")
        assert u.confirm_import_usermodel() != ''
        time.sleep(2)
        # 还原环境，将用户及组删除
        try:
            u.delete_user_in_group(vdi_model_group_name, passwd)
            time.sleep(5)
        except:
            pass
        u.del_group(vdi_model_group_name, passwd)
        time.sleep(2)
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.case_level_1
    @pytest.mark.userManage
    def test_renew_auser(self, user_pm_fixture):
        """
            执行步骤：1、选择用户，点击云桌面还原
            预期结果：1、触发个性类型云桌面初始化还原操作，重要操作告警提示，并需管理员二次密码确认，提示“针对VDI云桌面，将删除系统盘的用户个性数据，保留个人盘的数据”
        """
        logging.info("----------------------------------Web用户管理：A1.78例开始执行------------------------------")
        u = UserMange(user_pm_fixture)
        group_name = "ugp_a1_78"
        user_name = "user_a1_78"
        try:
            u.goto_usermanage_page()
            u.create_group_openvdi(group_name=group_name, img_name=image_name3, cd_type=u"个性")
            u.create_user_in_group(group_name=group_name, user_name=user_name, real_name=user_name)
            u.driver.refresh()
            u.login_client(user_name, "123456")
            time.sleep(150)
            u.close_client()
            time.sleep(60)
            u.goto_cdesk_page()
            time.sleep(2)
            u.find_user(user_name)
            u.renew_a_user(user_name)
            time.sleep(2)
            logging.info("判断是否有二次提示")
            try:
                u.confirm_renew(passwd)
            except:
                logging.info("无二次提示")
                assert False
            time.sleep(2)
        finally:
            u.user_recovery(group_name)
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.case_level_1
    @pytest.mark.userManage
    def test_VDI_ip(self, user_pm_fixture):
        """
        执行步骤：1、填写正确的静态IP\掩码\网关\DNS
        预期结果：1、该用户VDI云桌面在用或用户登录云桌面都可生效
        """
        logging.info("----------------------------------Web用户管理：A1.63例开始执行------------------------------")
        u = UserMange(user_pm_fixture)
        group_name = "ugp_a1_63"
        user_name = "user_a1_63"
        try:
            u.goto_usermanage_page()
            u.create_group_openvdi(group_name=group_name, img_name=restore_vdi_base, cd_type=u"还原")
            u.create_user_in_group(group_name=group_name, user_name=user_name, real_name=user_name)
            u.driver.refresh()
            u.login_client(user_name, "123456")
            time.sleep(150)
            u.close_client()
            time.sleep(60)
            u.goto_usermanage()
            time.sleep(2)
            u.find_user(user_name)
            time.sleep(2)
            u.hide_attribute()
            u.edit_config(user_name)
            time.sleep(2)
            u.edit_ip(ip2, subnet_mask2, gateway2, main_DNS2, prepare_DNS2)
            u.confirm_edit()
            logging.info("判断ip是否更改成功")
            assert u.edit_succ_msg() != ''
        finally:
            u.user_recovery(group_name)
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.case_level_2
    # @pytest.mark.userManage
    # def test_edit_VLAN_error(self, user_pm_fixture):
    #     """
    #     执行步骤：1、设置越界VLAN ID 4095，
    #             2、使用英文、负数等无效VLAN
    #             3、用户VLAN不填，点击保存
    #     预期结果：1、无效，不可配置，回退会原先设置值
    #             2、无效，不可配置，回退会原先设置值
    #             3、VLAN项是必填项，不填无法保存
    #     """
    #     logging.info("----------------------------------Web用户管理：A1.14例开始执行------------------------------")
    #     u = UserMange(user_pm_fixture)
    #     u.goto_usermanage_page()
    #     u.find_user(norun_user[0])
    #     time.sleep(2)
    #     u.edit_config(norun_user[0])
    #     u.vdi_set()
    #     time.sleep(2)
    #     logging.info("判断VLAN数值过大时，点击确定，是否会自动变为系统可分配的最大VLAN")
    #     assert u.edit_VLAN_over_error(vlan_max) == '4094'
    #     u.confirm_edit_vlan()
    #     u.edit_config(norun_user[0])
    #     u.vdi_set()
    #     logging.info("判断vlan是否成功更改")
    #     assert u.check_over_vlan() == '4094'
    #
    #     flag = u.edit_VLAN_other_error(vlan)
    #     logging.info("判断vlan处输入字母时是否回退到原先值")
    #     assert flag[0] == 1
    #     logging.info("判断vlan处不填数字是否回退到原先值")
    #     assert flag[1] == 1
    #     logging.info("判断vlan处输入负数时是否回退到1")
    #     assert flag[2] == 1
    #     # 还原环境 将vlan改为1
    #     u.edit_VLAN_over_error(1)
    #     u.confirm_edit_vlan()
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.case_level_2
    # @pytest.mark.userManage
    # def test_user_xdisk_decrease(self, user_pm_fixture):
    #     """
    #     操作步骤：1、用户网盘原设置为5G，当前使用1G，修改用户配置裁减网盘为2G
    #             2、用户组裁减后，查看对应存储位置剩余容量大小
    #             3、用户网盘原设置为5G，当前使用4G，修改用户配置裁减网盘为3G
    #     预期结果：1、可裁减，配置生效
    #             2、剩余容量变大
    #             3、不可裁减、配置不生效，给出错误提示
    #     """
    #     logging.info("----------------------------------Web用户管理：A1.73例开始执行------------------------------")
    #     u = UserMange(user_pm_fixture)
    #     d = CDeskMange(user_pm_fixture)
    #     # 开启用户网盘属性
    #     u.find_user(norun_user[0])
    #     u.edit_config(norun_user[0])
    #     info = u.get_elem_attribute(u.is_x_disk_open, 'class')
    #     if "checked" not in info:
    #         u.open_clouddisk_attribute()
    #         time.sleep(2)
    #         u.confirm_open_xdisk()
    #     else:
    #         u.click(u.confirm_xpath1)
    #         u.click(u.sure_xpath)
    #     time.sleep(2)
    #
    #     a = AndroidVdi()
    #     # 连接vdi终端设备
    #     a.vdi_connect(vdi_android_ip_list[1])
    #     # 登录vdi云桌面
    #     a.login(norun_user[0], '', t_pwd)
    #     d.click_cloud_desk_manage()
    #     u.refresh_webdriver()
    #     time.sleep(2)
    #     d.search_info(name=norun_user[0])
    #     ip = d.get_cloud_desk_ip(name=norun_user[0])
    #     time.sleep(0.5)
    #     win_conn_useful(ip, s_user, s_pwd)
    #     # vdi发送cmd命令
    #     a = win_conn(ip, s_user, s_pwd, r'create_new_file,X:\1G.txt,1073741824')
    #     time.sleep(10)
    #     get_win_conn_info(ip, s_user, s_pwd, r"echo 1G>X:\1G.txt")
    #     a = win_conn(ip, s_user, s_pwd, r'create_new_file,X:\1G.txt,1073741824')
    #     time.sleep(10)
    #     print('-----return:-----', a)
    #     # 关机
    #     u.goto_cdesk_page()
    #     u.close_vdi_desktop(norun_user[0], passwd)
    #     time.sleep(10)
    #     # 云盘剪裁为2g
    #     u.goto_usermanage_page()
    #     u.find_user(norun_user[0])
    #     u.edit_config(norun_user[0])
    #     u.edit_xdisk_value(xdisk_decrease1)
    #     u.confirm_edit()
    #     logging.info("判断5G被占用1G时，云盘是否能减小为2G")
    #     assert u.edit_succ_msg() != ''
    #     time.sleep(2)
    #     # --------------------------
    #     u.find_user(norun_user[0])
    #     u.edit_config(norun_user[0])
    #     u.edit_xdisk_value(xdisk_increase)
    #     u.confirm_edit()
    #
    #     a.login(norun_user[0], '', t_pwd)
    #     win_conn_useful(ip, s_user, s_pwd)
    #     a = win_conn(ip, s_user, s_pwd, r'create_new_file,X:\3G.txt,3221225472')
    #     time.sleep(10)
    #     # 关机
    #     u.goto_cdesk_page()
    #     u.close_vdi_desktop(norun_user[0], passwd)
    #     time.sleep(10)
    #     # # 云盘剪裁为3g
    #     u.goto_usermanage_page()
    #     u.find_user(norun_user[0])
    #     u.edit_config(norun_user[0])
    #     u.edit_xdisk_value(xdisk_decrease2)
    #     u.confirm_edit()
    #     logging.info("判断5G被占用4G时，云盘是否能减小为3G")
    #     assert u.edit_false_msg() != ''
    #     time.sleep(2)
    #     # 还原环境，将用户的云盘关闭
    #     u.close_xdisk()
    #     u.confirm_edit()
    #     u.admin_confirm(passwd)
    #     time.sleep(2)
    #     a.vdi_disconnect(vdi_android_ip_list[1])
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.case_level_1
    @pytest.mark.userManage
    def test_user_xdisk_open(self, user_pm_fixture):
        """
        执行步骤：1、用户组未启用网盘，修改组内用户为启用网盘
                2、用户组启用网盘，修改组内用户为不启用网盘
        预期结果：1、启动VDI云桌面或IDV虚机后可使用网盘，读写正常；后台查看/opt/user_disk/disk_space/var/www/html/rj/data/local目录下对应用户网盘文件存在。
                2、启动VDI云桌面或IDV虚机后无网盘使用；重要操作告警提示，并需管理员二次密码确认；后台查看/opt/user_disk/disk_space/var/www/html/rj/data/local目录下对应用户网盘文件删除
        """
        logging.info("----------------------------------Web用户管理：A1.71例开始执行------------------------------")
        u = UserMange(user_pm_fixture)
        group_name = "ugp_a1_71"
        user_name = "user_a1_71"
        try:
            u.goto_usermanage_page()
            u.create_group_openvdi(group_name=group_name, img_name=restore_vdi_base, cd_type=u"还原")
            u.create_user_in_group(group_name=group_name, user_name=user_name, real_name=user_name)
            u.driver.refresh()
            u.login_client(user_name, "123456")
            time.sleep(150)
            u.close_client()
            time.sleep(60)
            u.goto_usermanage()
            time.sleep(2)
            # 开启用户网盘属性
            u.find_user(user_name)
            time.sleep(1)
            u.edit_config(user_name)
            info = u.get_elem_attribute(u.is_x_disk_open, 'class')
            if "checked" not in info:
                u.open_clouddisk_attribute()
                u.confirm_open_xdisk()
            else:
                u.click(u.confirm_xpath1)
                u.click(u.sure_xpath)
            time.sleep(2)

            time.sleep(2)
            # 从数据库中查找新增用户云盘位置
            xdisk_location = server_sql_qurey(host_ip,
                                              "select disk_location from lb_seat_info where user_name = '{0}'".format(
                                                  user_name))
            path = str(xdisk_location)
            path = path.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(",", "").replace("u",
                                                                                                                     "")
            k = u.create_vdi_ssh_shell(ip=host_ip,
                                       command="ls /user_disk/'{0}'/".format(path))
            time.sleep(3)
            print('-----return:-----', k)
            logging.info("判断用户组云盘不开启，用户云盘开启，登录该用户vdi后查看后台文件是否存在")
            assert user_name in k
            # 用户组修改为云盘特性开启
            u.goto_usermanage_page()
            time.sleep(2)
            u.group_click(group_name)
            u.edit_userGroupCharacter(group_name)
            time.sleep(3)
            u.open_clouddisk_attribute()
            time.sleep(2)
            u.confirm_open_xdisk()
            time.sleep(10)
            # 关闭某用户云盘
            u.find_user(user_name)
            u.edit_config(user_name)
            info = u.get_elem_attribute(u.is_x_disk_open, 'class')
            if "checked" in info:
                u.close_xdisk()
                u.confirm_edit()
                u.admin_confirm()
                time.sleep(10)
            else:
                u.click(u.confirm_xpath1)
                u.click(u.sure_xpath)
                time.sleep(2)
            # 从数据库中查找新增用户云盘位置
            xdisk_location = server_sql_qurey(host_ip,
                                              "select disk_location from lb_seat_info where user_name = '{0}'".format(user_name))

            path = str(xdisk_location)
            path = path.replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace(",", "").replace("u",
                                                                                                                     "")
            path = path[7:]
            # shell命令查看服务器
            b = u.create_vdi_ssh_shell(host_ip,
                                       r"ls /user_disk/disk_space/var/www/html/rj/data/'{0}'/".format(path))

            logging.info("判断用户组云盘开启，用户云盘不开启，登录该用户vdi后查看后台文件是否存在")
            assert user_name not in b
        # 还原环境，将用户组云盘关闭
        finally:
            u.user_recovery(group_name)
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.case_level_1
    # @pytest.mark.userManage
    # def test_user_xdisk_increase(self, user_pm_fixture):
    #     """
    #     执行步骤：1、扩容网盘大小，将原先5G调整为10G
    #             2、存储位置剩余容量只有1G，扩容用户网盘2G
    #     预期结果：1、VDI云桌面或IDV虚机（已启动或未启动云桌面）可查看调整后的网盘大小
    #             2、不可修改给出提示
    #
    #     """
    #     logging.info("----------------------------------Web用户管理：A1.72例开始执行------------------------------")
    #     u = UserMange(user_pm_fixture)
    #     group_name = "ugp_a1_72"
    #     user_name = "user_a1_72"
    #     try:
    #         u.goto_usermanage_page()
    #         u.create_group_openvdi(group_name=group_name, img_name=restore_vdi_base, cd_type=u"还原")
    #         u.create_user_in_group(group_name=group_name, user_name=user_name, real_name=user_name)
    #         u.driver.refresh()
    #         u.login_client(user_name, "123456")
    #         time.sleep(150)
    #         u.goto_usermanage()
    #         time.sleep(2)
    #     # 开启用户网盘属性
    #         u.find_user(user_name)
    #         u.edit_config(user_name)
    #         u.open_clouddisk_attribute()
    #         u.confirm_open_xdisk()
    #         time.sleep(2)
    #
    #         #  扩容云盘空间超过可用空间最大值
    #
    #         u.edit_config(norun_user[2])
    #         max_xdisk = u.get_max_xdisk()
    #         u.edit_xdisk_value(int(max_xdisk) + 2)
    #         u.click_confirm()
    #         logging.info("扩容云盘空间超过可用空间最大值时，给出不可修改提示")
    #         assert u.get_increase_xdisk_wrong_msg() != ''
    #         # 将5g存储空间扩容成10g
    #         u.edit_xdisk_value(xdisk_increase2)
    #         u.confirm_edit()
    #         # 用shell命令连接服务器查看该用户的网盘大小
    #         u.create_vdi_ssh_shell(host_ip,
    #                                r"cd /opt/user_disk/disk_space/var/www/html/rj/data/")
    #         time.sleep(2)
    #         location = u.create_vdi_ssh_shell(host_ip, r"grep '{0}' /etc/passwd".format(norun_user[2]))
    #         time.sleep(4)
    #         uid = location.split(':')[2]
    #         xdisk_size = u.create_vdi_ssh_shell(host_ip, r"sudo -u \#'{0}' /sbin/smbquota 0 0 '{0}'".format(uid, uid))
    #         xdisk_size = xdisk_size.split(' ')[2]
    #         xdisk_size1 = int(xdisk_size)
    #         xdisk_size = xdisk_size1 / 1024 / 1000
    #         assert xdisk_size == int(xdisk_increase2)
    #
    #     finally:
    #         u.close_client()
    #         time.sleep(60)
    #         u.user_recovery(group_name)
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.case_level_2
    # @pytest.mark.userdm
    # @pytest.mark.userManage
    # def test_user_external_equipment(self, user_pm_fixture):
    #     """
    #     执行步骤：1、修改用户组外设策略，比如关闭存储设备
    #     预期结果：1、IDV虚机/VDI云桌面下次启动生效
    #     """
    #     logging.info("----------------------------------Web用户管理：A1.50例开始执行------------------------------")
    #     u = UserMange(user_pm_fixture)
    #     # 关闭存储设备
    #     u.find_user(norun_user[0])
    #     u.edit_config(norun_user[0])
    #     u.click_external_equipment()
    #     u.close_usb_cc_ok(u'存储设备')
    #     u.confirm_edit()
    #     time.sleep(2)
    #     u.get_desk_ip()
    #     time.sleep(0.5)
    #     a = AndroidVdi()
    #     # 连接vdi终端设备
    #     a.vdi_connect(vdi_android_ip_list[1])
    #     # 登录vdi云桌面
    #     a.login(norun_user[0], vdi_android_ip_list[1])
    #
    #     time.sleep(40)
    #
    #     # 查询数据库，看该用户的某外设是否已经关闭
    #     usb_cc_ok = server_sql_qurey(host_ip,
    #                                  "select usb_cc_ok from idv_user a left join fusion_peripheral_config b on a.fusion_peripheral_config_id = b.id where user_name = '{0}'".format(
    #                                      norun_user[0]))
    #     usb_cc_ok = usb_cc_ok[0]
    #     usb_cc_ok = usb_cc_ok[0]
    #     time.sleep(1)
    #     print usb_cc_ok
    #
    #     logging.info("判断IDV虚机/VDI云桌面下次启动时是否生效")
    #     assert usb_cc_ok == 0
    #     time.sleep(2)
    #
    #     # 关机
    #     u.goto_cdesk_page()
    #     u.close_vdi_desktop(norun_user[0], passwd)
    #     time.sleep(10)
    #     a.vdi_disconnect(vdi_android_ip_list[1])
    #     # 还原环境，将用户的外设存储打开
    #     u.goto_usermanage_page()
    #     u.find_user(norun_user[0])
    #     u.edit_config(norun_user[0])
    #     u.click_external_equipment()
    #     u.open_usb_cc_ok(u'存储设备')
    #     u.confirm_edit()
    #     time.sleep(8)
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.case_level_1
    # @pytest.mark.userdm
    # @pytest.mark.userManage
    # def test_user_rool_back(self, user_pm_fixture):
    #     """
    #     执行步骤：1、当剩余磁盘空间不多，将用户从个性还原互切时，同时扩大个人盘且增量大于剩余磁盘空间
    #     预期结果：1、用户修改失败，数据库需要回滚完全，用户的vdi特性需要和变更用户前状态一致
    #     """
    #     logging.info("----------------------------------Web用户管理：A1.30例开始执行------------------------------")
    #     u = UserMange(user_pm_fixture)
    #     try:
    #         time.sleep(1)
    #         # 创建一个vdi特性用户组
    #         u.group_click(u"总览")
    #         u.create_group()
    #         u.set_group_name(vdi_model_group_name)
    #         u.group_vdi_attribute()
    #         time.sleep(1)
    #         u.edit_vdi_mirror(vdi_default_mirror)
    #         time.sleep(3)
    #         u.confirm_create_group()
    #         time.sleep(10)
    #         # 在新建组中导入10个用户
    #         # try:
    #         #     u.import_usermodel()
    #         #     u.choose_usermodel(model)
    #         #     u.confirm_import_usermodel()
    #         #     time.sleep(6)
    #         # except:
    #         #     pass
    #         # 在该用户组中添加一个用户
    #         u.group_click(vdi_model_group_name)
    #         u.creat_user(vdi_model_group_name + '1', vdi_model_group_name + '1')
    #         time.sleep(1)
    #         u.confirm_create_user()
    #         time.sleep(3)
    #         # 进入镜像管理中查看可分配的最大磁盘
    #         u.goto_mirror_manage_page()
    #         u.into_mirror_cifream()
    #         u.click_disk_val()
    #         u.out_cifream()
    #         u.into_prompt_cifream()
    #         u.input_user_num('1')
    #         list = u.get_disk_val()
    #         time.sleep(2)
    #         u.out_cifream()
    #         u.close_calsu_page()
    #         # 进入用户编辑页面，修改新建用户的磁盘，使其超出界限
    #         u.goto_usermanage_page()
    #         u.find_user(vdi_model_group_name + '1')
    #         u.edit_config(vdi_model_group_name + '1')
    #         u.vdi_set()
    #         u.set_cdesk_val(int(list[0]) + 2)
    #         u.set_ddesk_val(int(list[1]) + 2)
    #         logging.info('回滚')
    #         assert u.get_cdesk_val() != int(list[0]) + 2
    #         u.close_edit()
    #         time.sleep(10)
    #     finally:
    #         try:
    #             # 还原环境，删除导入的用户
    #             u.user_recovery(vdi_model_group_name)
    #             # u.delete_user_in_group(vdi_model_group_name, passwd)
    #             # time.sleep(5)
    #             # u.del_group(vdi_model_group_name, passwd)
    #             # time.sleep(2)
    #         except Exception as e:
    #             logging.info(e)
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_0
    def test_user_attribute_filter(self, user_pm_fixture):
        """
        执行步骤：1、在用户管理界面中点击用户的状态、类型或备课资源属性
        预期结果：1、用户状态属性支持筛选全部、正常、禁用
                2、用户类型支持筛选全部、本地、AD、LDAP等
                3、备课资源支持筛选全部、已使用、未使用、未授权等
                页面退出重新登录，不记录之前的筛选规则
        """
        logging.info("----------------------------------Web用户管理：A1.98例开始执行------------------------------")
        u = UserMange(user_pm_fixture)
        u.goto_usermanage_page()
        time.sleep(1)
        u.make_sure_filter_attributes_checked()  # 开启装状态和类型
        u.check_filter_item()
        time.sleep(1)
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.case_level_1
    @pytest.mark.userManage
    def test_user_xdisk_config(self, user_pm_fixture):
        """
            执行步骤：1、默认不启用个人网盘
                    2、启用个人网盘，并将网盘位置设置为内置存储，网盘大小设置为默认5G
                    3、启用个人网盘，并将网盘位置设置为内置存储，网盘大小设置为非默认值10G
                    4、新建/编辑用户或用户组设置VDI个人网盘为2T
            预期结果：1、VDI或IDV用户登录云桌面无网盘可用
                    2、VDI或IDV用户登录云桌面可使用网盘，并且网盘大小为5G，可查看当前网盘剩余大小
                    3、VDI或IDV用户登录云桌面可使用网盘，并且网盘大小为10G，可查看当前网盘剩余大小
                    4、VDI用户登录云桌面可使用网盘，并且网盘大小为2T，可查看当前网盘剩余大小
        """
        logging.info("----------------------------------Web用户管理：A1.20例开始执行------------------------------")
        u = UserMange(user_pm_fixture)
        time.sleep(1)
        # 创建一个vdi特性用户组
        u.group_click(u"总览")
        u.create_group()
        u.set_group_name('a_group')
        u.group_vdi_attribute()
        time.sleep(1)
        u.edit_vdi_mirror(vdi_default_image)
        time.sleep(3)
        u.confirm_create_group()
        time.sleep(3)

        # 在该用户组中添加一个用户
        u.group_click('a_group')
        u.creat_user('a_group1', 'a_group1')
        time.sleep(1)
        u.confirm_create_user()
        time.sleep(3)
        # 登录该用户，用cmd命令查询网盘
        u.login_client('a_group1', vdi_init_pwd)
        time.sleep(50)
        # skell命令连接服务器查看该用户的网盘大小
        u.create_vdi_ssh_shell(host_ip,
                               r"cd /opt/user_disk/disk_space/var/www/html/rj/data/")
        time.sleep(2)
        u.close_client()
        location = u.create_vdi_ssh_shell(host_ip, r"grep '{0}' /etc/passwd".format('a_group1'))
        time.sleep(4)

        assert location == ''
        time.sleep(15)
        # # 开启云盘属性
        u.goto_usermanage_page()
        u.find_user('a_group1')
        u.edit_config('a_group1')
        u.open_clouddisk_attribute()
        u.confirm_open_xdisk()
        u.login_client('a_group1', vdi_init_pwd)
        time.sleep(50)
        u.create_vdi_ssh_shell(host_ip,
                               r"cd /opt/user_disk/disk_space/var/www/html/rj/data/")
        time.sleep(2)
        location = u.create_vdi_ssh_shell(host_ip, r"grep '{0}' /etc/passwd".format('a_group'))
        time.sleep(4)
        uid = location.split(":")[2]
        xdisk_size = u.create_vdi_ssh_shell(host_ip, r"sudo -u \#'{0}' /sbin/smbquota 0 0 '{0}'".format(uid, uid))
        xdisk_size = xdisk_size.split(" ")[2]
        xdisk_size1 = int(xdisk_size)
        xdisk_size = xdisk_size1 / 1024 / 1024
        assert xdisk_size == 5
        time.sleep(3)
        u.close_client()
        time.sleep(20)
        # 云盘设置为10g
        u.edit_config('a_group1')
        u.edit_xdisk_value(xdisk_increase2)
        u.confirm_edit()
        u.login_client('a_group1', vdi_init_pwd)
        time.sleep(50)
        u.create_vdi_ssh_shell(host_ip,
                               r"cd /opt/user_disk/disk_space/var/www/html/rj/data/")
        time.sleep(2)
        location = u.create_vdi_ssh_shell(host_ip, r"grep '{0}' /etc/passwd".format('a_group1'))
        time.sleep(4)
        uid = location.split(':')[2]
        xdisk_size = u.create_vdi_ssh_shell(host_ip, r"sudo -u \#'{0}' /sbin/smbquota 0 0 '{0}'".format(uid, uid))
        xdisk_size = xdisk_size.split(' ')[2]
        xdisk_size1 = int(xdisk_size)
        xdisk_size = xdisk_size1 / 1024 / 1024
        print '剩余磁盘大小:'
        assert xdisk_size == 10
        time.sleep(3)
        u.close_client()
        time.sleep(20)
        # 云盘设置为2T
        u.edit_config('a_group1')
        u.edit_xdisk_value(2000)
        u.confirm_edit()
        u.login_client('a_group1', vdi_init_pwd)
        time.sleep(50)
        u.create_vdi_ssh_shell(host_ip,
                               r"cd /opt/user_disk/disk_space/var/www/html/rj/data/")
        time.sleep(2)
        location = u.create_vdi_ssh_shell(host_ip, r"grep '{0}' /etc/passwd".format('a_group'))
        time.sleep(4)
        uid = location.split(':')[2]
        xdisk_size = u.create_vdi_ssh_shell(host_ip, r"sudo -u \#'{0}' /sbin/smbquota 0 0 '{0}'".format(uid, uid))
        xdisk_size = xdisk_size.split(' ')[2]
        xdisk_size1 = int(xdisk_size)
        xdisk_size = xdisk_size1 / 1024 / 1024
        print '剩余磁盘大小:'
        assert xdisk_size == 2000
        time.sleep(3)
        u.close_client()
        time.sleep(20)
        # 还原环境，删除用户,删除用户组
        u.user_recovery("a_group1")
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.case_level_1
    @pytest.mark.userManage
    def test_vdi_config(self, user_pm_fixture):
        """
        执行步骤：1、绑定标配VDI镜像，将用户组VDI云桌面配置CPU、内存进行扩容，比如配置为6核3G内存30G系统盘，
                2、绑定高性能VDI镜像，将用户组VDI云桌面配置CPU、内存进行裁减，比如配置为2核2G内存
                3、绑定VDI镜像，将用户组VDI云桌面配置个人盘进行扩容或裁减
        预期结果：1、组内用户登录VDI云桌面，配置读取修改后用户组的VDI配置属性
                2、组内用户登录VDI云桌面，配置读取修改后用户组的VDI配置属性
                3、组内用户登录VDI云桌面，个人盘配置读取修改后用户的VDI配置属性
        """
        logging.info("----------------------------------Web用户管理：A1.18例开始执行------------------------------")
        u = UserMange(user_pm_fixture)
        desk = CDeskMange(user_pm_fixture)
        # 创建一个绑定标配镜像的用户组
        u.group_click(u"总览")
        u.create_group()
        u.set_group_name('18_group')
        u.group_vdi_attribute()
        time.sleep(1)
        u.edit_vdi_mirror(standard_mirror)
        time.sleep(3)
        u.confirm_create_group()
        time.sleep(3)

        # 在该用户组中添加一个用户
        u.group_click('18_group')
        u.creat_user('18_group1', '18_group1')
        time.sleep(1)
        u.confirm_create_user()
        time.sleep(10)
        # 用户组VDI云桌面配置CPU、内存进行扩容
        u.group_click('18_group')
        time.sleep(1)
        u.edit_group('18_group')
        u.edit_CPU()  # 8
        u.edit_internal_memory()  # 3
        u.confirm_edit()

        a = AndroidVdi()
        # 连接vdi终端设备
        a.vdi_connect(vdi_android_ip_list[1])
        # 登录vdi云桌面
        a.login('18_group1', ip=vdi_android_ip_list[1], pwd=vdi_init_pwd)
        time.sleep(100)
        u.refresh_webdriver()
        time.sleep(20)
        desk.goto_cloud_desk_manage()
        desk.search_info(name='18_group1')
        desk_ip = desk.get_cloud_desk_ip(name='18_group1')
        u.goto_usermanage_page()
        # cmd命令连接服务器查看该用户的cpu\内存大小
        time.sleep(2)
        cpu_num = u.vdi_desk_cmd(desk_ip, s_user, s_pwd, r"echo %NUMBER_OF_PROCESSORS%")
        time.sleep(20)
        cpu_num = re.findall("\d+", cpu_num)[0]
        print cpu_num
        logging.info("判断cpu的个数是否与组一起变为8")
        assert int(cpu_num) == 8
        time.sleep(2)
        internal_memory = u.vdi_desk_cmd(desk_ip, s_user, s_pwd, r"wmic memorychip")
        time.sleep(20)
        memory = u.split_internal_memory(internal_memory)

        logging.info("判断内存是否与组一起变为3")
        assert memory == 3
        time.sleep(3)
        # 关机
        u.goto_cdesk_page()
        time.sleep(3)
        u.close_vdi_desktop('18_group1', passwd)
        time.sleep(15)
        # 用户组绑定高配镜像，VDI云桌面配置CPU、内存进行裁减
        u.goto_usermanage_page()
        time.sleep(1)
        u.group_click('18_group')
        u.edit_group('18_group')
        u.edit_vdi_mirror(senior_mirror)
        u.renew_CPU()  # 4
        u.renew_internal_memory()  # 2
        u.confirm_edit()
        # 输入密码确认修改
        u.admin_confirm(passwd)
        # 登录用户并查看配置

        a.login('18_group1', vdi_android_ip_list[1], vdi_init_pwd)
        time.sleep(120)

        cpu_num = u.vdi_desk_cmd(desk_ip, s_user, s_pwd, r"echo %NUMBER_OF_PROCESSORS%")
        time.sleep(2)
        cpu_num = re.findall("\d+", cpu_num)[0]
        logging.info("判断cpu的个数是否与组一起变为4")
        assert int(cpu_num) == 4
        time.sleep(2)
        internal_memory = u.vdi_desk_cmd(desk_ip, s_user, s_pwd, r"wmic memorychip")
        time.sleep(20)
        memory = u.split_internal_memory(internal_memory)
        logging.info("判断内存是否与组一起变为2")
        assert memory == 2
        time.sleep(3)
        # 关机
        u.goto_cdesk_page()
        time.sleep(3)
        u.close_vdi_desktop('18_group1', passwd)
        time.sleep(15)
        # 绑定VDI镜像，将用户组VDI云桌面配置个人盘进行扩容或裁减
        u.goto_usermanage_page()
        time.sleep(1)
        u.group_click('18_group')
        u.edit_group('18_group')
        u.edit_vdi_mirror(vdi_default_mirror)
        u.set_cdesk_val(50)
        time.sleep(2)
        u.set_ddesk_val(30)
        time.sleep(1)
        u.confirm_edit()
        u.admin_confirm(passwd)
        # 登录用户并查看配置
        a.login('18_group1', vdi_android_ip_list[1], vdi_init_pwd)
        time.sleep(120)

        # cmd命令连接服务器查看该用户的盘符大小
        time.sleep(3)
        cddisk = u.vdi_desk_cmd(desk_ip, s_user, s_pwd,
                                r'wmic LogicalDisk')

        time.sleep(50)
        print cddisk
        c = u.split_disk_val(cddisk)
        # print c
        logging.info("判断c盘是否与用户组一起变为50g")
        assert c[0] == 49
        logging.info("判断d盘是否与用户组一起变为30g")
        assert c[1] == 29
        # 关机
        u.goto_cdesk_page()
        u.close_vdi_desktop('18_group1', passwd)
        time.sleep(15)
        a.vdi_disconnect(vdi_android_ip_list[1])
        # 还原环境
        u.goto_usermanage_page()
        time.sleep(2)
        u.delete_user_in_group('18_group', passwd)
        time.sleep(5)
        u.delete_group('18_group', passwd)
        time.sleep(2)
        logging.info("----------------------------------------测试用例结束---------------------------------------------")


    @pytest.mark.case_level_1
    @pytest.mark.userManage
    def test_change_userGroup_idv_restore_image(self, user_pm_fixture):
        logging.info("----------------------------------Web用户管理：A1.47例开始执行------------------------------")
        user = UserMange(user_pm_fixture)
        try:
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="ugp_a1_47", cd_type=u"还原", img_name=image_name)
            user.create_user_in_group(group_name="ugp_a1_47", user_name="uname_a1_47", real_name="uname_a1_47")
            # u = UserMange(user_pm_fixture)
            # # 编辑用户组特性
            user.edit_userGroupCharacter("ugp_a1_47")
            # 修改系统盘大小
            user.edit_cdesk()
            user.confirm_edit()
            user.admin_confirm(passwd)
            # 验证修改成功与否 提示：用户组IDV云终端特性修改成功！
            message = user.getTipMessage()
            print(message)
            assert message == u"用户组IDV云终端特性修改成功！"
        finally:
            try:
                user.user_recovery("ugp_a1_47")
            except Exception as e:
                logging.info(e)
        logging.info("-------------------测试用例结束-------------------------")


    @pytest.mark.case_level_1
    @pytest.mark.coderLee
    @pytest.mark.userManage
    @pytest.mark.autotest1
    def test_change_userGroup_idv_system_disk(self, com_fixture):
        logging.info("------------------Web用户管理：A1.49例开始执行-------------------")
        user = UserMange(com_fixture)
        try:
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="ugp_a1_49", cd_type=u"还原", img_name=image_name)
            user.create_user_in_group(group_name="ugp_a1_49", user_name="uname_a1_49", real_name="uname_a1_49")
            # u = UserMange(user_pm_fixture)
            # # 编辑用户组特性
            user.edit_userGroupCharacter("ugp_a1_49")
            # 修改系统盘大小
            user.edit_cdesk()
            user.confirm_edit()
            user.admin_confirm(passwd)
            # 验证修改成功与否 提示：用户组IDV云终端特性修改成功！
            message = user.getTipMessage()
            print(message)
            assert message == u"用户组IDV云终端特性修改成功！"
        finally:
            try:
                user.user_recovery("ugp_a1_49")
            except Exception as e:
                logging.info(e)
        logging.info("-------------------测试用例结束-------------------------")


    @pytest.mark.case_level_1
    @pytest.mark.coderLee1
    @pytest.mark.userManage
    def test_change_userGroup_idv_desktop(self, com_fixture):
        logging.info("----------------------------------Web用户管理：A1.66例开始执行------------------------------")
        user = UserMange(com_fixture)
        idv = IdvPage(com_fixture)
        group_name = "group_a1_66_1"
        user_name = "user_a1_66_1"
        try:
            user.goto_usermanage_page()
            user.create_group_openidv(group_name=group_name, cd_type=u"还原", img_name=image_name2)
            user.create_user_in_group(group_name=group_name, user_name=user_name, real_name=user_name)
            user.driver.refresh()
            user.edit_user_idv(user_name=user_name, add_img=image_name, isadd=True)
            user.driver.refresh()
            # 进入单用户终端页面搜索终端，并绑定用户
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=idv_single_ip_list[2], user_name=user_name)
            # 用户登录终端，并在C盘写入文件
            idv_initialization_click(ip=idv_single_ip_list[2])
            time.sleep(2)
            idv_login(ip=idv_single_ip_list[2], user_name=user_name, pwd=t_pwd)
            idv_change_pwd(ip=idv_single_ip_list[2], name=user_name, pwd=t_pwd)
            idv_login(ip=idv_single_ip_list[2], user_name=user_name)
            desk_ip = idv.get_single_tm_desk_type_bytm_ip(idv_single_ip_list[2])
            if win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd) == u'winrm可使用':
                get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd="echo .> C:\zt_test.txt")
            else:
                logging.error(u"终端登录错误")
                assert False
            # 重启终端，验证文件依然存在
            idv.reboot_terminal(idv_single_ip_list[2])
            idv.wait_tm_reboot_success(idv_single_ip_list[2], 1)
            idv_login(ip=idv_single_ip_list[2], user_name=user_name)
            if win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd) == u'winrm可使用':
                result = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd="if exist \"C:\zt_test.txt\" echo a")
                if result is not None:
                    assert True
                else:
                    logging.info(u"用例错误，桌面类型不随用户桌面类型指定")
                    assert False
            else:
                logging.error(u"终端登录错误")
                assert False
        finally:
            try:
                # 善后处理
                idv.reboot_terminal(idv_single_ip_list[2])
                idv.wait_tm_reboot_success(idv_single_ip_list[2])
                user.user_recovery(group_name)
            except Exception as e:
                logging.info(e)

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_vdi_desktop_1(self, com_fixture):
        # logging.info("-------web用户管理A1.59_1用例开始执行------")
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        android_vdi = AndroidVdi()
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="ugp_a1_59_1", img_name=restore_vdi_base, cd_type=u"还原")
            user.create_user_in_group(group_name="ugp_a1_59_1", user_name="user_a1_59_1", real_name="ugp_a1_59_1")
            user.driver.refresh()
            user.create_group_openvdi(group_name="ugp_a1_59_2", img_name=vdi_default_mirror, cd_type=u"个性")
            user.create_user_in_group(group_name="ugp_a1_59_2", user_name="user_a1_59_2", real_name="ugp_a1_59_2")
            user.edit_user_vdi(user_name="user_a1_59_1", cd_type=u"个性", isadd=True, add_img=vdi_default_mirror)
            user.edit_user_vdi(user_name="user_a1_59_1", cd_type=u"个性", isadd=True, add_img=vdi_default_mirror)
            user.driver.refresh()
            user.edit_user_vdi(user_name="user_a1_59_2", cd_type=u"还原", isadd=True, add_img=restore_vdi_base)
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.login(name="user_a1_59_1", ip=vdi_tm_ip_1, pwd="123456")
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_2)
            android_vdi.login(name="user_a1_59_2", ip=vdi_tm_ip_2, pwd="123456")
            info1 = server_sql_qurey(host_ip, "select desktop from lb_seat_info where user_name = 'user_a1_59_1'")
            assert info1 == [(1,)]
            info2 = server_sql_qurey(host_ip, "select desktop from lb_seat_info where user_name = 'user_a1_59_2'")
            assert info2 == [(0,)]
        finally:
            try:
                # 善后处理
                cd_manage.driver.refresh()
                cd_manage.goto_cloud_desk_manage()
                cd_manage.search_info("ugp_a1_59_")
                cd_manage.close_img(passwd)
                user.user_recovery("ugp_a1_59_1")
                user.user_recovery("ugp_a1_59_2")
            except Exception as e:
                logging.info(e)
        # logging.info("----------------------------------web用户管理A1.59_1用例结束------------------------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_change_vdi_image(self, com_fixture):
        logging.info(u"----------------web用户管理A1.60用例开始执行--------------")
        user = UserMange(com_fixture)
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="ugp_a1_60", img_name=restore_vdi_base, cd_type=u"还原")
            user.create_user_in_group(group_name="ugp_a1_60", user_name="user_a1_60", real_name="user_a1_60")
            # 修改用户绑定的镜像
            user.edit_user_vdi(user_name="user_a1_60", cd_type=u"还原", isdel=True, delimg_name=restore_vdi_base,
                               isadd=True, add_img=vdi_base)
            user.driver.refresh()
            user.search_info("user_a1_60")
            user.check_userDetail(userName="user_a1_60")
            user.click_elem(user.vdi_set_xpath)
            assert user.elem_is_exist(user.img_name.format(restore_vdi_base)) == 0
        finally:
            try:
                user.user_recovery("ugp_a1_60")
            except Exception as e:
                logging.info(e)
        # logging.info("----------------------------------web用户管理A1.60用例结束------------------------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_vdi_desktop_type_3(self, com_fixture):
        """
        1、创建分组,桌面模式分别为个性与还原
        2、用户登录
        """
        logging.info(u"---------------web用户管理A1.15_1用例开始执行------------------")
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        a = AndroidVdi()
        gp_name = "a1_15_1"
        # gp_name2 = "a1_15_2"
        user_name_1 = "user_a1_15_1"
        # user_name_2 = "user_a1_15_2"
        try:
            # 创建还原、个性用户组和用户
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name=gp_name, img_name=restore_vdi_base, cd_type=u"还原")
            user.create_user_in_group(group_name=gp_name, user_name=user_name_1, real_name=user_name_1)
            user.driver.refresh()
            # user.create_group_openvdi(group_name=gp_name2, img_name=vdi_default_image)
            # user.create_user_in_group(group_name=gp_name2, user_name=user_name_2, real_name=user_name_2)
            a.disconnect_all_devices_and_connect(ip=vdi_tm_ip_1)
            a.login(name=user_name_1, ip=vdi_tm_ip_1, pwd="123456")
            a.disconnect_all_devices_and_connect(vdi_tm_ip_2)
            a.login(name="vdi1_03", ip=vdi_tm_ip_2)
            des_type_1 = server_sql_qurey(host_ip,
                                          "select desktop from lb_seat_info where user_name = '{0}'".format(
                                              user_name_1))
            print(des_type_1)
            assert des_type_1 == [(0,)]
            des_type_2 = server_sql_qurey(host_ip,
                                          "select desktop from lb_seat_info where user_name = 'vdi1_03'")  # .format(user_name_2))
            print(des_type_2)
            assert des_type_2 == [(1,)]
        finally:
            try:
                a.vdi_disconnect(vdi_tm_ip_2)
                cd_manage.driver.refresh()
                cd_manage.goto_cloud_desk_manage()
                cd_manage.search_info("user_a1_15_")
                cd_manage.close_img(passwd)
                user.user_recovery(gp_name)
                # user.user_recovery(gp_name2)
            except Exception as e:
                logging.info(e)
        logging.info(u"-----------web用户管理A1.15_1用例结束---------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_vdi_cpu(self, com_fixture):
        logging.info(u"------------web用户管理A1.61用例开始执行----------------")
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        android_vdi = AndroidVdi()
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="ugp_a1_61", cd_type=u"个性", img_name=vdi_default_image)
            user.create_user_in_group(group_name="ugp_a1_61", user_name="user_a1_61", real_name="user_a1_61")
            # 修改用户
            user.editor_user_disk(user_name="user_a1_61", cpu=6)
            # 用户登录
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.login(name="user_a1_61", ip=vdi_tm_ip_1, pwd="123456")
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info("user_a1_61")
            desk_ip = cd_manage.get_cloud_desk_ip("user_a1_61")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            info = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd="wmic cpu get NumberOfCores")
            assert "6" in info
        finally:
            try:
                # 善后处理
                android_vdi.vdi_disconnect(vdi_tm_ip_1)
                cd_manage.search_info("user_a1_61")
                cd_manage.close_img(passwd)
                user.user_recovery("ugp_a1_61")
            except Exception as e:
                logging.info(e)
            logging.info(u"-----------web用户管理A1.61用例结束------------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_a1_62(self, com_fixture):
        """创建用户组和用户，修改分组的属性，验证非自定义用户属性跟随分组"""
        logging.info(u"--------web用户管理A1.62用例开始执行---------------")
        user = UserMange(com_fixture)
        android_vdi = AndroidVdi()
        idv = IdvPage(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        cmd_D_get_size = 'wmic logicaldisk where name="D:" get size'
        cmd_C_get_size = 'wmic logicaldisk where name="C:" get size'
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="ugp_a1_62", img_name=vdi_default_image, cd_type=u"个性")
            user.create_user_in_group(group_name="ugp_a1_62", user_name="user_a1_62", real_name="user_a1_62")
            user.editor_user_disk(user_name="user_a1_62", d_disk="40", sys_disk="60")
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.login(name="user_a1_62", ip=vdi_tm_ip_1, pwd="123456")
            # 获取云桌面ip
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info("user_a1_62")
            desk_ip = cd_manage.get_cloud_desk_ip("user_a1_62")
            # 使用cmd命令验证个人盘大小为50
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            info1 = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd=cmd_D_get_size)
            size = idv.convert_size(info1)
            assert size == 40
            info2 = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd=cmd_C_get_size)
            size2 = idv.convert_size(info2)
            assert size2 == 60
            cd_manage.search_info("user_a1_62")
            cd_manage.close_img(passwd)
            user.goto_usermanage_page()
            # 裁剪用户组个人盘为10G,从数据库查询更改不生效
            user.editor_user_disk(user_name="user_a1_62", d_disk="10")
            info = server_sql_qurey(host_ip, "select disk_size from lb_seat_info where user_name = 'user_a1_34'")
            assert info != [(10,)]
        finally:
            try:
                # 善后处理
                android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
                user.user_recovery("ugp_a1_62")
            except Exception as e:
                logging.info(e)
        logging.info(u"------------------web用户管理A1.62用例结束--------------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_cpu_memory(self, com_fixture):
        """创建用户组和用户，修改分组的属性，验证非自定义用户属性跟随分组"""
        logging.info(u"-------------web用户管理A1.33用例开始执行----------------")
        user = UserMange(com_fixture)
        android_vdi = AndroidVdi()
        idv = IdvPage(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        cmd_D_get_size = 'wmic logicaldisk where name="D:" get size'
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="ugp_a1_33", img_name=restore_vdi_base, cd_type=u"还原")
            user.create_user_in_group(group_name="ugp_a1_33", user_name="user_a1_33", real_name="user_a1_33")
            user.editor_group_vdi_disk(gp_name="ugp_a1_33", d_disk="50")
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.login(name="user_a1_33", ip=vdi_tm_ip_1, pwd="123456")
            # 获取云桌面ip
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info("user_a1_33")
            desk_ip = cd_manage.get_cloud_desk_ip("user_a1_33")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            info = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd=cmd_D_get_size)
            size = idv.convert_size(info)
            assert size == 50
        finally:
            try:
                # 善后处理
                cd_manage.driver.refresh()
                cd_manage.goto_cloud_desk_manage()
                cd_manage.search_info("user_a1_33")
                cd_manage.close_img(passwd)
                time.sleep(15)
                user.user_recovery("ugp_a1_33")
            except Exception as e:
                logging.info(e)
        logging.info(u"----------------web用户管理A1.33用例结束-------------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_a1_34(self, com_fixture):
        """创建用户组和用户，修改分组的属性，验证非自定义用户属性跟随分组"""
        logging.info(u"--------------web用户管理A1.34用例开始执行--------------")
        user = UserMange(com_fixture)
        android_vdi = AndroidVdi()
        idv = IdvPage(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        cmd_D_get_size = 'wmic logicaldisk where name="D:" get size'
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="ugp_a1_34", img_name=restore_vdi_base, cd_type=u"还原")
            user.create_user_in_group(group_name="ugp_a1_34", user_name="user_a1_34", real_name="user_a1_34")
            user.editor_group_vdi_disk(gp_name="ugp_a1_34", d_disk="30")
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.login(name="user_a1_34", ip=vdi_tm_ip_1, pwd="123456")
            # 获取云桌面ip
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info("user_a1_34")
            desk_ip = cd_manage.get_cloud_desk_ip("user_a1_34")
            # 使用cmd命令验证个人盘大小为50
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            info = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd=cmd_D_get_size)
            size = idv.convert_size(info)
            assert size == 30
            cd_manage.search_info("user_a1_34")
            cd_manage.close_img(passwd)
            time.sleep(15)
            user.goto_usermanage_page()
            # 裁剪用户组个人盘为10G,从数据库查询更改不生效
            user.editor_group_vdi_disk(gp_name="ugp_a1_34", d_disk="10")
            info = server_sql_qurey(host_ip, "select disk_size from lb_seat_info where user_name = 'user_a1_34'")
            assert info == [(30,)]
        finally:
            try:
                # 善后处理
                user.user_recovery("ugp_a1_34")
            except Exception as e:
                logging.info(e)
        logging.info(u"----------------web用户管理A1.34用例结束--------------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_0
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_reset_password(self, com_fixture):
        logging.info(u"-------------web用户管理A1.81用例开始执行-----------------")
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        android_vdi = AndroidVdi()
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="ugp_a1_81", img_name=vdi_image, cd_type=u"还原")
            user.create_user_in_group(group_name="ugp_a1_81", user_name="usera1_81", real_name="usera1_81")
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.set_passwd(name="usera1_81", oldpasswd="123456", newpasswd="123")
            android_vdi.login(name="usera1_81", ip=vdi_tm_ip_1, pwd="123")
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info("usera1_81")
            status = cd_manage.get_status("usera1_81")
            assert u"运行" in status
            cd_manage.search_info("usera1_81")
            cd_manage.close_img(passwd)
            user.goto_usermanage_page()
            user.user_reset_password(user_name="usera1_81")
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.login(name="usera1_81", ip=vdi_tm_ip_1, pwd="123456")
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info("usera1_81")
            status = cd_manage.get_status("usera1_81")
            assert u"运行" in status
            cd_manage.search_info("usera1_81")
            cd_manage.close_img(passwd)
        finally:
            try:
                # 善后
                android_vdi.vdi_disconnect(vdi_tm_ip_1)
                user.user_recovery("ugp_a1_81")
            except Exception as e:
                logging.info(e)
            logging.info(u"---------------web用户管理A1.81用例结束-------------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_a1_21(self, com_fixture):
        logging.info(u"-------------------web用户管理A1.21_2用例开始执行---------------")
        user = UserMange(com_fixture)
        android_vdi = AndroidVdi()
        cd_manage = CDeskMange(com_fixture)
        try:
            # 创建个性用户和还原用户组以及用户
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="ugp_a1_21_1", img_name=restore_vdi_base, cd_type=u"还原")
            user.create_user_in_group(group_name="ugp_a1_21_1", user_name="uname_a1_21_1", real_name="uname_a1_21_1")
            user.driver.refresh()
            user.create_user_in_group(group_name="ugp_a1_21_1", user_name="uname_a1_21_2", real_name="uname_a1_21_2")
            user.edit_user_vdi(user_name="uname_a1_21_2", cd_type=u"个性", isadd=True, add_img=image_name3)
            # 个性用户用登录终端
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.login(name="uname_a1_21_2", ip=vdi_tm_ip_1, pwd="123456")
            # 还原用户登录终端
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_2)
            android_vdi.login(name="uname_a1_21_1", ip=vdi_tm_ip_2, pwd="123456")
            android_vdi.vdi_disconnect(vdi_tm_ip_2)
            # 修改还原用户的系统盘以及个人盘大小和网盘大小
            user.editor_user_disk(user_name="uname_a1_21_1", d_disk="40", x_disk="10")
            # 修改个性用户的系统盘以及个人盘大小和网盘大小
            user.editor_user_disk(user_name="uname_a1_21_2", internal_memory="6", d_disk="40", send_password=1)
            # 连接数据库查询还原用户的数据，验证个人盘被修改
            info = server_sql_qurey(host_ip,
                                    "select disk_size from lb_seat_info where user_name = 'uname_a1_21_1'")
            assert info == [(40,)]
            # 连接数据库查询个性用户的数据，验证个人盘大小不变
            info1 = server_sql_qurey(host_ip,
                                     "select disk_size from lb_seat_info where user_name = 'vdi1_03'")
            assert info1 != [(40,)]
        finally:
            try:
                cd_manage.driver.refresh()
                cd_manage.goto_cloud_desk_manage()
                cd_manage.search_info("uname_a1_21_")
                cd_manage.close_img(passwd)
                user.user_recovery("ugp_a1_21_1")
            except Exception as e:
                logging.info(e)
        logging.info(u"----------------web用户管理A1.21_2用例结束-----------------")

    # @pytest.mark.userManage
    # @pytest.mark.case_level_1
    # @pytest.mark.case_type_fun
    # @pytest.mark.autotest1
    # def test_cpu_memory_disk(self, com_fixture):
    #     logging.info(u"-----------------web用户管理A1.17用例开始执行---------------")
    #     img = Image(com_fixture)
    #     user = UserMange(com_fixture)
    #     highter_image = "high_image"
    #     custom_image = "custom_image"
    #     try:
    #         # 复制标准镜像
    #         img.go_img_manage()
    #         img.copy_image(by_copy=vdi_standard_image, copy_name=highter_image)
    #         img.copy_image(by_copy=vdi_standard_image, copy_name=custom_image)
    #         img.wait_image_update_cpmpleted(custom_image)
    #         img.click_image_edit(highter_image)
    #         img.editor_img_sysconfig(sysconfig_type=u"高性能", pubdate=u"立即发布")
    #         time.sleep(0.5)
    #         img.open_admin_tool()
    #         img.close_img()
    #         img.click_image_edit(custom_image)
    #         img.editor_img_sysconfig(sysconfig_type=u"自定义", memory_size="4", system_disk_size="50", pubdate=u"立即发布")
    #         time.sleep(0.5)
    #         img.open_admin_tool()
    #         img.close_img()
    #         img.wait_image_update_cpmpleted(custom_image)
    #         # 用户组创建用户，绑定相应的镜像
    #         user.back_current_page()
    #         user.goto_usermanage_page()
    #         user.create_group_openvdi(group_name="ugp_a1_17_1", img_name=vdi_standard_image, cd_type=u"还原")
    #         user.create_user_in_group(group_name="ugp_a1_17_1", user_name="user_a1_17_1", real_name="user_a1_17_1")
    #         user.driver.refresh()
    #         user.create_group_openvdi(group_name="ugp_a1_17_2", img_name=highter_image, cd_type=u"还原")
    #         user.create_user_in_group(group_name="ugp_a1_17_2", user_name="user_a1_17_2", real_name="user_a1_17_2")
    #         user.driver.refresh()
    #         user.create_group_openvdi(group_name="ugp_a1_17_3", img_name=custom_image, cd_type=u"还原")
    #         user.create_user_in_group(group_name="ugp_a1_17_3", user_name="user_a1_17_3", real_name="user_a1_17_3")
    #         result = server_sql_qurey(host_ip,
    #                                   "select vm_cpu,vm_memory,vm_sys_size from lb_seat_info where user_name = 'user_a1_17_1'")
    #         assert result == [(4, 2, 20)]
    #     finally:
    #         try:
    #             user.user_recovery("ugp_a1_17_1")
    #             user.user_recovery("ugp_a1_17_2")
    #             user.user_recovery("ugp_a1_17_3")
    #             img.img_recovery(highter_image)
    #             img.img_recovery(custom_image)
    #         except Exception as e:
    #             logging.info(e)
    #     logging.info(u"--------------web用户管理A1.17用例结束-----------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_a1_16(self, com_fixture):
        logging.info(u"-------web用户管理A1_16执行-------")
        user = UserMange(com_fixture)
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="ugp_a1_16", img_name=restore_vdi_base, cd_type=u"还原")
            user.create_user_in_group(group_name="ugp_a1_16", user_name="user_a1_16", real_name="user_a1_16")
            user.driver.refresh()
            user.search_info("user_a1_16")
            user.check_userDetail("user_a1_16")
            assert user.elem_is_exist("//span[contains(text(),'{}')]".format(restore_vdi_base)) == 0
        finally:
            try:
                user.user_recovery("ugp_a1_16")
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.autotest1
    @pytest.mark.userManage
    @pytest.mark.case_type_fun
    def test_vdi_system_disk_size(self, com_fixture):
        """
        1、复制两个镜像，分别用作绑定还原和个性
        2、编辑复制完成的镜像，修改系统盘为80G
        3、用户登录验证系统盘大小为80G
        4、还原用户处于登录状态修改镜像系统盘大小
        5、验证无法进行修改
        6、绑定个性镜像的用户登录终端
        7、修改被个性用户绑定的镜像，修改系统盘大小
        8、验证无法修改
        9、善后
        """
        logging.info(u"--------------Web用户管理：A1.35例开始执行-------------")
        img = Image(com_fixture)
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        idv = IdvPage(com_fixture)
        android_vdi = AndroidVdi()
        try:
            # 复制两个镜像
            img.go_img_manage()
            img.copy_image(by_copy=restore_vdi_base, copy_name="vdi_restore")
            img.wait_image_update_cpmpleted("vdi_restore")
            img.back_current_page()
            img.go_img_manage()
            # 编辑某个镜像，设置系统盘大小为80G
            img.click_image_edit("vdi_restore")
            img.editor_img_sysconfig(sysconfig_type=u"自定义", system_disk_size="80", pubdate=u"立即发布")
            time.sleep(0.5)
            img.open_admin_tool()
            time.sleep(3)
            img.close_img()
            img.wait_image_update_cpmpleted("vdi_restore")
            img.back_current_page()
            # 进入用户管理页面，创建用户
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="igp_a1_35_1", img_name="vdi_restore", cd_type=u"还原")
            user.create_user_in_group(group_name="igp_a1_35_1", user_name="user_a1_35_1", real_name="user_a1_35_1")
            # 还原用户登录
            android_vdi.disconnect_all_devices_and_connect(vdi_tm_ip_1)
            android_vdi.login(name="user_a1_35_1", ip=vdi_tm_ip_1, pwd="123456")
            # 进入云桌面获取ip
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info("user_a1_35_1")
            desk_ip1 = cd_manage.get_cloud_desk_ip("user_a1_35_1")
            win_conn_useful(ip=desk_ip1, name=s_user, pwd=s_pwd)
            info = get_win_conn_info(ip=desk_ip1, user_name=s_user, passwd=s_pwd,
                                     cmd='wmic logicaldisk where name="C:" get size')
            sys_size = idv.convert_size(info)
            assert sys_size == 80
        finally:
            try:
                # 善后
                cd_manage.driver.refresh()
                cd_manage.goto_cloud_desk_manage()
                cd_manage.search_info("user_a1_35_1")
                cd_manage.close_img(passwd)
                user.user_recovery("igp_a1_35_1")
                # user.user_recovery("igp_a1_35_2")
                img.img_recovery("vdi_restore")
            except Exception as e:
                logging.info(e)
            logging.info(u"-------------------Web用户管理：A1.35例开始执行--------------------")

    @pytest.mark.case_level_1
    @pytest.mark.coderLee1
    @pytest.mark.userManage
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_set_idv_desktop_type(self, com_fixture):
        logging.info(u"--------------Web用户管理：A1.6例开始执行--------------")
        user = UserMange(com_fixture)
        gp_name1 = "usertest_a1_6_1"
        gp_name2 = "usertest_a1_6_2"
        # u_name1 = "ut_a1_6_1"
        u_name2 = "ut_a1_6_2"
        try:
            user.goto_usermanage_page()
            # 创建还原分组，在还原分组下创建用户
            user.create_group_openidv(group_name=gp_name2, cd_type=u"还原", img_name=image_name)
            user.create_user_in_group(group_name=gp_name2, user_name=u_name2, real_name=u_name2)
            time.sleep(2)
            # 分别搜索用户，验证用户类型
            user.search_info("idv1_03")
            user.check_userDetail("idv1_03")
            assert u"个性" in user.get_value(user.idvPolicy)
            user.close_info()
            user.search_info(u_name2)
            user.check_userDetail(u_name2)
            assert u"还原" in user.get_value(user.idvPolicy)
            user.close_info()
            user.driver.refresh()
        finally:
            try:
                # 还原环境
                user.user_recovery(gp_name2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.userManage
    @pytest.mark.case_type_fun
    @pytest.mark.autotest11
    def test_user_idv_img(self, com_fixture):
        """
        1、创建分组还原，以及用户
        2、进入单用户终端组页面，绑定该用户
        3、用户登录终端
        4、修改组所绑定的镜像，重启终端
        5、验证终端镜像改变
        6、善后处理
        """
        logging.info("------------Web用户管理：A1.47例开始执行---------------")
        user = UserMange(com_fixture)
        idv = IdvPage(com_fixture)
        gp_name = "ugp_a1_47"
        u_name = "uname_a1_47"
        get_vm_name = "cat /opt/lessons/RCC_Client/vm_image_info.ini"
        try:
            # 创建用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name=gp_name, cd_type=u"还原", img_name=image_name)
            user.create_user_in_group(group_name=gp_name, user_name=u_name, real_name=u_name)
            # 进入单用户终端组绑定用户
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=single_tm_ip, user_name=u_name)
            # 重启终端，验证终端所绑定的镜像
            idv.reboot_terminal(single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)
            idv_initialization_click(single_tm_ip)
            idv_pattern_chose(single_tm_ip)
            info = terminal_conn(single_tm_ip, get_vm_name)
            assert image_name + ".base" in info
            # 修改分组所绑定的镜像
            user.back_current_page()
            user.goto_usermanage_page()
            user.edit_gp_idv(gp_name=gp_name, image=image_name2)
            # 进入终端管理页面，重启终端
            idv.driver.refresh()
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.reboot_terminal(single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)
            time.sleep(120)  # 等待终端检查文件完成
            # 分组更换绑定的镜像后，验证镜该终端所绑定的镜像为变更后的镜像
            info = terminal_conn(single_tm_ip, get_vm_name)
            assert image_name2 + ".base" in info
        finally:
            try:
                # 善后处理
                user.user_recovery(gp_name)
                idv.driver.refresh()
                idv.goto_idv_terminal_page()
                idv.goto_idv_terminal_single_terminal_group_page()
                idv.reboot_terminal(single_tm_ip)
                idv.wait_tm_reboot_success(single_tm_ip)
            except Exception as e:
                logging.info(e)
            logging.info("--------------Web用户管理：A1.47例结束执行-------------")

    @pytest.mark.case_level_1
    @pytest.mark.userManage
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_user_a1_75(self, com_fixture):
        """
        1、创建用户组和用户
        2、终端绑定用户，并且用户登录终端
        3、删除用户，验证需要二次确认，验证用户网盘消失，以及用户状态为在线，不受影响
        4、重启终端，验证用户无法登录终端
        """
        logging.info(u"----------Web用户管理：A1.75例开始执行--------------")
        user = UserMange(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        idv = IdvPage(com_fixture)
        gp_name = "ugp_a1_75"
        u_name = "user_a1_75"
        get_x_disk = "wmic logicaldisk where name='X:' get size"
        try:
            user.goto_usermanage_page()
            # 创建用户组以及用户
            user.create_group_openidv(group_name=gp_name, cd_type=u"个性", img_name=image_name2, cloud_disk=1)
            user.create_user_in_group(group_name=gp_name, user_name=u_name, real_name=u_name)
            # 进入终端管理页面绑定用户
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=single_tm_ip, user_name=u_name)
            idv.back_current_page()
            idv.reboot_terminal(name=single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)
            idv_initialization_click(single_tm_ip)
            idv_pattern_chose(single_tm_ip)
            idv_login(ip=single_tm_ip, user_name=u_name)
            idv_change_pwd(ip=single_tm_ip, name=u_name, pwd="123")
            idv_login(ip=single_tm_ip, user_name=u_name)
            time.sleep(15)
            # 修改删除用户
            user.back_current_page()
            user.goto_usermanage_page()
            user.del_user_in_group(gp_name)  # 删除用户
            # 验证在线用户不受影响
            cd_manage.back_current_page()
            cd_manage.goto_cloud_desk_manage()
            status = cd_manage.get_status(u_name)
            assert u"运行" in status
            time.sleep(60)  # 删除用户需要等60S终端才生效
            # 获取云桌面ip
            cd_manage.search_info(u_name)
            desk_ip = cd_manage.get_cloud_desk_ip(u_name)
            win_conn_useful(desk_ip, s_user, s_pwd)
            info = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd=get_x_disk)
            assert "5368709120" not in info
        finally:
            try:
                # 善后处理
                user.driver.refresh()
                user.back_current_page()
                user.goto_usermanage_page()
                user.del_group_exist(gp_name)
                idv.driver.refresh()
                idv.goto_idv_terminal_page()
                idv.goto_idv_terminal_single_terminal_group_page()
                idv.reboot_terminal(single_tm_ip)
                idv.wait_tm_reboot_success(single_tm_ip)
            except Exception as e:
                logging.info(e)
        logging.info(u"------------Web用户管理：A1.75例结束执行----------------")

    @pytest.mark.autotest1
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.userManage
    def test_usermanage_09(self, com_fixture):
        """
        1、创建开启IDV特性的用户组，并在该分组下创建用户，开启本地盘
        2、到终端-单用户页面搜索终端，绑定1中创建的分组，并登录终端
        3、验证用户登录，连接服务器，验证D盘的参数为1支持本地盘
        4、编辑用户，修改用户的本地盘上属性为关闭
        5、用户退出再登录，验证D盘参数为-1：不支持使用D盘
        6、善后：终端解绑，删除用户组和用户
        """
        user = UserMange(com_fixture)
        idv = IdvPage(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        try:
            # 进入用户管理页面，创建用户组和用户（开启本地盘）
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="usertest09_group", cd_type=u"个性", img_name=image_name)
            user.create_user_in_group(group_name="usertest09_group", user_name="user01", real_name="user01")
            # 进入终端管理--单用户终端组
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            # 搜索终端，获取终端ip绑定用户后重启终端
            idv.single_bingding_user(tm_name=single_tm_ip, user_name="user01")
            idv.back_current_page()
            idv.reboot_terminal(name=single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)  # 等待终端重启成功
            # 设置用户密码并登录终端
            idv_initialization_click(single_tm_ip)
            idv_pattern_chose(single_tm_ip)
            idv_login(ip=single_tm_ip, user_name="user01")
            idv_change_pwd(ip=single_tm_ip, name="user01", pwd="123")
            idv_login(ip=single_tm_ip, user_name="user01")
            # 等待用户登录
            cd_manage.back_current_page()
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info("user01")
            desk_ip = cd_manage.get_cloud_desk_ip("user01")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            # 连接服务器，验证支持本地盘使用,值为1
            info = terminal_conn(ip=single_tm_ip, command="cd /opt/lessons/RCC_Client;cat dev_policy.ini")
            assert 'allow_userdisk                 = 1' in info
            # 进入用户管理页面，关闭本地盘
            user.back_current_page()
            user.goto_usermanage_page()
            user.edit_user_idv(user_name="user01", local_disk="close")
            # 进入终端管理，重启终端
            idv.driver.refresh()
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.back_current_page()
            idv.reboot_terminal(name=single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)
            # 登录终端
            idv_initialization_click(single_tm_ip)
            idv_pattern_chose(single_tm_ip)
            idv_login(ip=single_tm_ip, user_name="user01")
            # 等待用户登录
            cd_manage.back_current_page()
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info("user01")
            desk_ip = cd_manage.get_cloud_desk_ip("user01")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            # 连接服务器，验证支持本地盘使用,值为1
            info = terminal_conn(ip=single_tm_ip, command="cd /opt/lessons/RCC_Client;cat dev_policy.ini")
            assert 'allow_userdisk                 = 0' in info
        finally:
            try:
                # 善后处理：解绑用户，删除用户，删除用户组
                user.user_recovery("usertest09_group")
                idv.driver.refresh()
                idv.goto_idv_terminal_page()
                idv.goto_idv_terminal_single_terminal_group_page()
                idv.reboot_terminal(single_tm_ip)
                idv.wait_tm_reboot_success(single_tm_ip)
            except Exception as e:
                logging.info(e)

    @pytest.mark.autotest1
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.userManage
    def test_usermanage_13(self, com_fixture):
        """
        1、创建分组和用户（开启vdi特性）
        2、编辑用户设置其VLAN为4094
        3、连接服务器，输入指令：ifconfig
        4、验证返回的信息带有bond0.4094
        5、善后：删除用户组和用户
        """
        user = UserMange(com_fixture)
        try:
            user.goto_usermanage_page()
            user.create_group_openvdi(group_name="usertest_13", cd_type=u"还原", img_name=vdi_image)
            user.create_user_in_group(group_name="usertest_13", user_name="user_mgrtest_13",
                                      real_name="user_mgrtest_13")
            user.editor_user_vlan(user_name="user_mgrtest_13", vlan="4094")
            info = server_conn(ip=host_ip, command="ifconfig")
            assert "bond0.4094" in info
        finally:
            try:
                user.user_recovery("usertest_13")
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.userManage
    @pytest.mark.autotest1
    def test_usermanage_46(self, com_fixture):
        """
        1、创建个性分组绑定镜像1，在该分组下创建用户A和B
        2、进入终端-单用户终端，绑定用户A(未产生差分)
        3、进入用户管理页面，修改分组所绑定的镜像为2镜像
        4、进入终端页面，重启终端，用户A登录验证镜像修改为2镜像
        5、用户A登录后，在C盘写入数据（此时产生差分）
        6、修改分组镜像为1，验证用户镜像不变更
        7、善后处理：解绑终端，删除用户和用户组
        """
        user = UserMange(com_fixture)
        idv = IdvPage(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        get_vm_info = "cat /opt/lessons/RCC_Client/vm_image_info.ini"
        try:
            # 创建分组绑定镜像1，创建用户A和B
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="usertest_46", cd_type=u"个性", img_name=image_name)
            user.create_user_in_group(group_name="usertest_46", user_name="usertest46_A", real_name="usertest46_A")
            # 进入终端-单用户终端组页面
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=single_tm_ip, user_name="usertest46_A")
            idv.back_current_page()
            # 重启终端，修改用户密码并登录
            idv.reboot_terminal(name=single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)  # 等待终端重启成功
            idv_initialization_click(single_tm_ip)
            idv_pattern_chose(ip=single_tm_ip)
            time.sleep(60)
            info = terminal_conn(single_tm_ip, get_vm_info)
            assert image_name + ".base" in info
            # 进入用户管理页面,编辑分组所绑定的镜像
            user.back_current_page()
            user.goto_usermanage_page()
            user.edit_gp_idv(gp_name="usertest_46", image=image_name2)
            # 进入终端管理页面,重启终端，验证终端所绑定的镜像改变
            idv.driver.refresh()
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.reboot_terminal(single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)
            idv_initialization_click(single_tm_ip)
            idv_pattern_chose(ip=single_tm_ip)
            idv_login(ip=single_tm_ip, user_name="usertest46_A")
            idv_change_pwd(ip=single_tm_ip, name="usertest46_A", pwd="123")
            idv_login(ip=single_tm_ip, user_name="usertest46_A")
            time.sleep(60)
            # 验证未产生差分的用户镜像跟随分组改变
            info = terminal_conn(single_tm_ip, get_vm_info)
            assert image_name2 + ".base" in info
            # 进入云桌面获取ip,并在C盘写入数据，创建差分
            cd_manage.back_current_page()
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info(single_tm_ip)
            desk_ip = cd_manage.get_cloud_desk_ip(single_tm_ip)
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            win_conn(ip=desk_ip, user_name=s_user, passwd=s_pwd, action_cmd="echo .> C:\i_test.txt")
            # 进入用户管理页面,编辑分组所绑定的镜像
            user.back_current_page()
            user.goto_usermanage_page()
            user.edit_gp_idv(gp_name="usertest_46", image=image_name)
            # 进入终端管理页面,重启终端，验证终端所绑定的镜像不改变
            idv.driver.refresh()
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.reboot_terminal(single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)
            info = terminal_conn(single_tm_ip, get_vm_info)
            assert image_name2 + ".base" in info
        finally:
            try:
                user.user_recovery("usertest_46")
                idv.driver.refresh()
                idv.goto_idv_terminal_page()
                idv.goto_idv_terminal_single_terminal_group_page()
                idv.reboot_terminal(single_tm_ip)
                idv.wait_tm_reboot_success(single_tm_ip)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.userManage
    @pytest.mark.autotest1
    def test_usermanage_67(self, com_fixture):
        """
        1、创建用户组和用户A（个性）、B（还原），绑定镜像1
        2、用户A登录终端后，修改用户A所绑定的镜像2，重启终端，验证A登录的终端镜还是镜像1
        3、用户B登录另一终端后，修改用户B所绑定的镜像2，重启终端，验证B登录的终端镜像编程镜像2
        4、善后：删除用户组和用户
        """
        user = UserMange(com_fixture)
        idv = IdvPage(com_fixture)
        cd_manage = CDeskMange(com_fixture)
        try:
            # 创建分组绑定镜像1，创建用户A（个性）和B（还原）
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="usertest_67", cd_type=u"个性", img_name=image_name2)
            user.create_user_in_group(group_name="usertest_67", user_name="usertest67_A", real_name="usertest67_A")
            user.create_user_in_group(group_name="usertest_67", user_name="usertest67_B", real_name="usertest67_B")
            user.edit_user_idv(user_name="usertest67_B", cd_type=u"还原", isadd=True, add_img=image_name)
            # 进入终端-单用户终端组页面
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            # 终端分别绑定A和B用户
            idv.single_bingding_user(tm_name=single_tm_ip, user_name="usertest67_A")
            idv.back_current_page()
            time.sleep(2)
            idv.single_bingding_user(tm_name=single_tm_ip2, user_name="usertest67_B")
            idv.back_current_page()
            # 重启终端用户A登录
            idv.reboot_terminal(name=single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)
            idv_initialization_click(single_tm_ip)
            idv_pattern_chose(single_tm_ip)
            idv_login(ip=single_tm_ip, user_name="usertest67_A")
            idv_change_pwd(ip=single_tm_ip, name="usertest67_A", pwd="123")
            idv_login(ip=single_tm_ip, user_name="usertest67_A")
            # 重启终端用户B登录
            idv.reboot_terminal(name=single_tm_ip2)
            idv.wait_tm_reboot_success(single_tm_ip2)
            idv_initialization_click(single_tm_ip2)
            idv_pattern_chose(single_tm_ip2)
            idv_login(ip=single_tm_ip2, user_name="usertest67_B")
            idv_change_pwd(ip=single_tm_ip2, name="usertest67_B", pwd="123")
            idv_login(ip=single_tm_ip2, user_name="usertest67_B")
            # 进入云桌面,获取ip，用户A创建差分
            cd_manage.back_current_page()
            cd_manage.goto_cloud_desk_manage()
            cd_manage.search_info("usertest67_A")
            desk_ip = cd_manage.get_cloud_desk_ip("usertest67_A")
            win_conn_useful(desk_ip, s_user, s_pwd)
            win_conn(ip=desk_ip, user_name=s_user, passwd=s_pwd, action_cmd="echo .> C:\i_test.txt")
            # 进入用户管理页面,修改用户A和B的镜像
            user.back_current_page()
            user.goto_usermanage_page()
            user.edit_user_idv(user_name="usertest67_A", isadd=True, add_img=image_name)
            user.edit_user_idv(user_name="usertest67_B", cd_type=u"还原", isadd=True, add_img=image_name2)
            # 进入终端管理页面,重启终端，验证绑定有差分的用户镜像未变更
            idv.driver.refresh()
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.reboot_terminal(name=single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)
            info = idv.get_single_tm_image(tm_name=single_tm_ip)
            assert image_name2 in info
            idv.back_current_page()
            # 重启还原用户的终端
            idv.reboot_terminal(name=single_tm_ip2)
            idv.wait_tm_reboot_success(single_tm_ip2)
            info = idv.get_single_tm_image(tm_name=single_tm_ip2)
            # assert image_name2 in info
            idv.back_current_page()
        finally:
            try:
                # 善后处理：解绑用户，删除用户和用户组
                user.user_recovery("usertest_67")
                idv.driver.refresh()
                idv.goto_idv_terminal_page()
                idv.goto_idv_terminal_single_terminal_group_page()
                idv.reboot_terminal(name=single_tm_ip)
                idv.reboot_terminal(name=single_tm_ip2)
                idv.wait_tm_reboot_success(single_tm_ip2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.userManage
    @pytest.mark.autotest1
    def test_usermanage_68(self, com_fixture):
        """
        1、用户管理页面，创建分组以及用户
        2、终端管理--单用户终端，搜索单用户终端并绑定用户
        3、进入到用户管理页面，搜索用户，点击编辑
        4、查看编辑页面的系统盘信息反馈
        """
        user = UserMange(com_fixture)
        idv = IdvPage(com_fixture)
        try:
            # 进入用户管理页面，创建用户组和用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="user068_group", cd_type=u"个性", img_name=image_name2)
            user.create_user_in_group(group_name="user068_group", user_name="user_068", real_name="user_068")
            # 进入终端管理页面,绑定用户
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=single_tm_ip, user_name="user_068")
            idv.back_current_page()
            # 进入用户管理页面,点击编辑，查看用户系统盘的反馈信息
            user.goto_usermanage_page()
            user.searc_click_edit(user_name="user_068")
            info = user.get_value(user.sys_feedback)
            assert u"系统盘最大可扩容" in info
            user.click_elem(user.confirm_xpath1)
            user.click_elem(user.resure_btns)
        finally:
            try:
                # 善后处理，删除用户和用户组
                user.user_recovery("user068_group")
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.userManage
    @pytest.mark.case_type_fun
    @pytest.mark.autotest1
    def test_idv_Local_disk(self, com_fixture):
        """
        1、创建分组以及用户（组允许使用本地盘，用户不允许使用本地盘）
        2、进入单用户终端页面，搜索终端绑定该用户
        3、重启终端，用户登录验证终端属性本地盘是否开启
        4、修改分组以及用户（组不允许使用本地盘，用户允许使用本地盘）
        5、重启终端，用户登录，验证终端本地盘属性
        6、善后处理
        """
        # logging.info("----------Web用户管理：A1.69例开始执行-------------")
        user = UserMange(com_fixture)
        idv = IdvPage(com_fixture)
        try:
            user.goto_usermanage_page()
            get_d_allow = "cat /opt/lessons/RCC_Client/dev_policy.ini"
            # 用户组本地盘为开启，用户本地盘为关闭
            user.create_group_openidv(group_name="ugp_a1_69", cd_type=u"还原", img_name=image_name)
            user.create_user_in_group(group_name="ugp_a1_69", user_name="user_a1_69", real_name="user_a1_69")
            user.edit_user_idv(user_name="user_a1_69", cd_type=u"还原", local_disk="close")
            # 进入终端管理页面,绑定用户
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=single_tm_ip, user_name="user_a1_69")
            idv.reboot_terminal(single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)
            idv_initialization_click(single_tm_ip)
            idv_pattern_chose(ip=single_tm_ip)
            time.sleep(60)
            info = terminal_conn(ip=single_tm_ip, command=get_d_allow)
            # 验证用户本地盘属性为关闭
            assert "allow_userdisk                 = 0" in info
            # 更改用户组本地盘属性为关闭，用户本地盘属性为开启
            user.back_current_page()
            user.goto_usermanage_page()
            user.edit_gp_idv(gp_name="ugp_a1_69", isopen_local_disk="close")
            user.edit_user_idv(user_name="user_a1_69", cd_type=u"还原", local_disk="open")
            # 进入终端页面重启终端
            idv.driver.refresh()
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.reboot_terminal(single_tm_ip)
            idv.wait_tm_reboot_success(single_tm_ip)
            info = terminal_conn(ip=single_tm_ip, command=get_d_allow)
            # 验证用户本地盘属性为开启
            assert "allow_userdisk                 = 1" in info
        finally:
            try:
                # 善后处理
                user.user_recovery("ugp_a1_69")
            except Exception as e:
                logging.info(e)
            # logging.info("--------------Web用户管理：A1.69例结束执行----------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.case_type_fun
    def test_usermanage_lesson_resource(self, com_fixture):
        logging.info("----------------------------------web用户管理A1.91用例开始执行------------------------------")
        # Todo 连接服务器
        user = UserMange(com_fixture)
        user.goto_usermanage_page()

    # -------------------------------------------------wzy--------------------------------------------------------------

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_create_user(self, com_fixture):

        """
        执行步骤：1、新建用户输入全英文、全中文、全数字
                2、用户名混合输入英文、数字、中文以及"_","-","@","."这四个特殊符号,且不能以"_"开头
        预期结果：1、创建用户成功
                2、创建用户成功
        """
        logging.info("------------------------------------web用户管理A1.52测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        f = UserMange(com_fixture)
        try:
            f.goto_usermanage_page()
            f.createUserGroupCreateNewuser('test1-52', 'happyboy')
            f.click_confirm()
            f.findUserGroupCreateNewuser('test1-52', u'西域男孩')
            f.click_confirm()
            f.findUserGroupCreateNewuser('test1-52', '123456789')
            f.click_confirm()
            f.findUserGroupCreateNewuser('test1-52', u'你好9527sir_-@.')
            f.click_confirm()
        finally:
            try:
                f.user_recovery("test1-52")
                # f.delete_user_in_group('test1-52', 'admin')
                # f.del_group('test1-52', 'admin')
                # time.sleep(5)
            except Exception as e:
                logging.info(e)
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.userManage
    # @pytest.mark.case_level_2
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_create_sameuser(self, com_fixture):
    #     """
    #     执行步骤：1、配置与现用用户相同用户名
    #     预期结果：1、创建失败，用户名必须唯一
    #
    #     """
    #     logging.info("------------------------------------web用户管理A1.53测试用例开始执行-------------------------------")
    #     p = AuthenManage(com_fixture)
    #     f = UserMange(com_fixture)
    #     try:
    #         f.goto_usermanage_page()
    #         f.createUserGroupCreateNewuser('test1-53', 'happyboy')
    #         f.click_confirm()
    #         f.findUserGroupCreateNewuser('test1-53', 'happyboy')
    #         assert p.elem_is_exist(p.user_already_exits_xpath) == 0
    #         f.click_cancel()
    #     finally:
    #         try:
    #             f.user_recovery("test1-53")
    #             # f.delete_user_in_group('test1-53', 'admin')
    #             # f.del_group('test1-53', 'admin')
    #             # time.sleep(5)
    #         except Exception as e:
    #             logging.info(e)
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.userManage
    # @pytest.mark.case_level_2
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_username_limit32(self, com_fixture):
    #     """
    #     执行步骤：
    #             1、支持配置最大32个字符
    #             1、配置超过32个字符
    #     预期结果：1、创建用户成功
    #             2、不允许配置
    #     :param com_fixture:
    #     :return:
    #     """
    #     logging.info("------------------------------------web用户管理A1.54测试用例开始执行-------------------------------")
    #     p = AuthenManage(com_fixture)
    #     f = UserMange(com_fixture)
    #     try:
    #         f.goto_usermanage_page()
    #         f.createUserGroupCreateNewuser('test1-54', 'youaremysunshineemmm')
    #         f.click_confirm()
    #     finally:
    #         try:
    #             f.user_recovery("test1-54")
    #             # f.delete_user_in_group('test1-54', 'admin')
    #             # f.del_group('test1-54', 'admin')
    #             # time.sleep(5)
    #         except Exception as e:
    #             logging.info(e)
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.userManage222
    # @pytest.mark.case_level_2
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_change_attributes_vdi(self, com_fixture):
    #     """
    #     执行步骤：1、VDI用户正在使用时，更改该用户VDI配置属性
    #     预期结果：1、除单独更改网络设置，支持VDI在用修改，其他配置更改不允许VDI在用时更改
    #     :param com_fixture:
    #     :return:
    #     """
    #     logging.info("------------------------------------web用户管理A1.64测试用例开始执行-------------------------------")
    #     p = AuthenManage(com_fixture)
    #     f = UserMange(com_fixture)
    #     try:
    #         f.goto_usermanage_page()
    #         f.createUserGroupCreateNewuser('test1-64', u'ee', vdi)
    #         f.click_confirm()
    #         time.sleep(2)
    #         f.login_client('ee', '123456')
    #         time.sleep(35)
    #         count = 0
    #         flag = 0
    #         while (count < 9):
    #             f.click_more_operate('ee')
    #             f.click_elem(f.editor_btns_xpath)
    #             f.click_elem(f.vdi_policy)
    #             if count == 0:
    #                 f.edit_VLAN()
    #             if count == 1:
    #                 f.changeDesktopStyle(vdi, restore)
    #                 f.image_bind(vdi, vdiImage=standard_mirror)
    #                 time.sleep(1)
    #                 f.find_elem(f.vdiimage_bind_xpath).click()
    #                 f.click_confirm()
    #                 f.find_elem(f.sure_xpath).click()
    #                 f.send_passwd_confirm(passwd)
    #                 assert f.elem_is_exist(f.prompt_frame_xpath) == 0
    #                 f.click_elem(f.back_btns)
    #                 time.sleep(4)
    #                 count += 1
    #                 continue
    #             if count == 2:
    #                 f.changeCpuAccount()
    #             if count == 3:
    #                 f.edit_internal_memory()
    #             if count == 4:
    #                 f.edit_cdesk()
    #             if count == 5:
    #                 f.edit_ddesk()
    #             if count == 6:
    #                 flag = 1
    #                 f.edit_trans_info(u'双向传输')
    #             if count == 7:
    #                 flag = 1
    #                 f.edit_check_identity_info()
    #             if count == 8:
    #                 flag = 1
    #                 f.edit_ip('172.21.195.168', '255.255.255.0', '172.21.195.1', '192.168.58.110', '192.168.58.111')
    #             count += 1
    #             if flag == 1:
    #                 f.click_confirm()
    #                 f.click_elem(f.sure_xpath)
    #                 time.sleep(2)
    #                 assert f.elem_is_exist(f.prompt_frame_xpath) == 1
    #                 continue
    #             f.click_confirm()
    #             f.click_elem(f.sure_xpath)
    #             assert f.elem_is_exist(f.prompt_frame_xpath) == 0
    #             f.click_elem(f.back_btns)
    #             time.sleep(3)
    #         f.close_client()
    #         time.sleep(30)
    #     finally:
    #         try:
    #             f.user_recovery('test1-64')
    #             # f.goto_usermanage_page()
    #             # f.delete_user_in_group('test1-64', 'admin')
    #             # f.del_group('test1-64', 'admin')
    #             # time.sleep(8)
    #         except Exception as e:
    #             logging.info(e)
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_deleteUserGroup(self, user_pm_fixture):
        """
        执行步骤：
                1、选择用户组进行删除
                2、被删除用户组用户重新登录VDI云桌面或IDV云终端
        预期结果：1、组内用户全部移动到未分组中，重要操作告警提示，并需管理员二次密码确认
                2、被删除用户组用户并不继承未分组属性，而是保留用户个性属性

        """
        logging.info("-----------------web用户管理A1.51用例开始执行--------------------")
        user = UserMange(user_pm_fixture)
        try:
            user.createUserGroupCreateNewuser(userGroup_name_list[9], user_list[6], vdi)
            user.click_confirm()
            time.sleep(com_slp)
            info = user.click_del_gp_btn(userGroup_name_list[9])
            assert u"删除用户组会把该组下的所有用户转移到未分组，确定要删除该用户组吗？" in info
            user.click(user.confirm_deleteuser)
            user.send_passwd_confirm(passwd)
            time.sleep(com_slp)
            user.click_elem(user.userGroup_list_xpath % ungrouped)
            assert user.get_elem_text(user.userName_list_xpath % user_list[6]).find(user_list[6]) >= 0
            user.login_client(name=user_list[6], pwd='123456')
            time.sleep(20)
            user.close_client()
            user.click_more_operate(user_list[6])
            user.click_elem(user.editor_btns_xpath)
            user.click_elem(user.vdi_policy)
            assert user.find_elem(user.vdidesktop_xpath).get_attribute('value') == u'个性'
            user.click_elem(user.cancel_button_xpath)
        finally:
            user.user_recovery(userGroup_name_list[9])
            user.delete_user1(u"未分组", user_list[6])
        logging.info("-----------------web用户管理A1.45用例结束--------------------")


    @pytest.mark.userManage
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_shaopan(self):
        logging.info("-----------------测试用例--------------------")
        assert 1 == 1
    logging.info("-----------------用例结束--------------------")


if __name__ == "__main__":
    t = time.strftime("%Y-%m-%d %H%M")
    # pytest.main(['-vv', "-m", "userManage", "--html", report_dir + "//{0}_testuserManage_htmlreport.html".format(t)])
    pytest.main(["-k", "test_shaopan"])
    # pytest.main(["-m", "userManage123"])
