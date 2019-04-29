#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll && LinMengYao
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/12/29 14:32
"""
from string import strip

import pytest

from Common.serverconn import get_win_conn_info, terminal_conn
from Common.terminal_action import idv_initialization_click, idv_pattern_chose, idv_login, get_ip_mac, \
    get_idv_terminal_name, click_idv_set, idv_set_name_host_ip, idv_change_pwd, win_conn_useful
from TestData.Logindata import passwd, username
from TestData.Terminalmangerdata import *
from TestData.basicdata import *
from WebPages.Idvpage import IdvPage
from WebPages.LoginPage import Login
from WebPages.UserMangePage import UserMange
from WebPages.adnroid_vdi_page import AndroidVdi
import logging
import time
import re
import os


class Test_TerminalManger:

    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_new_vdi_group(self, vdi_fixture):
        logging.info("----------------------------------web终端管理A1.1，2用例开始执行------------------------------")
        tm = IdvPage(vdi_fixture)
        # 成功创建分组
        tm.vdi_new_group(vdi_new_group_name[0])
        assert tm.find_group(vdi_new_group_name[0]) == 1
        tm.delete_group(vdi_new_group_name[0])
        # 分组名称不能超过32位
        tm.click_new_group()
        tm.go_common_frame()
        assert tm.get_elem_attribute(tm.new_group_name_xpath, 'maxlength') == "32"
        tm.click_cancel()
        # 分组名称包含特殊字符
        tm.vdi_new_group(vdi_new_group_name[6])
        tm.click_confirm()
        assert re.match(".*?display: block;", tm.vdi_group_name_error_info()) is not None
        tm.click_cancel()
        # 创建已存在分组名称
        tm.vdi_new_group(name="repeat_test")
        tm.vdi_new_group(name="repeat_test")
        tm.back_current_page()
        time.sleep(2)
        assert tm.get_exist_info() == u"【repeat_test】终端组名已经存在"
        tm.click_sure()
        tm.go_common_frame()
        tm.click_cancel()
        time.sleep(2)
        logging.info("----------------------------------web终端管理A1.1，2用例结束------------------------------")

    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_new_vdi_login(self, vdi_fixture):
        """
        1、删除终端，登录终端，验证终端所在分组为未分组
        """
        logging.info("----------------------------------web终端管理A1.3用例开始执行------------------------------")
        a = AndroidVdi()
        tm = IdvPage(vdi_fixture)
        # 搜索中终端并删除
        tm.search_terminal(vdi_terminal_ip)
        tm.vdi_select_all()
        tm.vdi_terminal_delete()
        time.sleep(20)
        a.disconnect_all_devices_and_connect(vdi_terminal_ip)
        a.login(vdi_user, vdi_terminal_ip)
        logging.info("判断新连接的vdi终端是否在未分组中")
        assert tm.get_vdi_group_name(vdi_user) == u'未分组'
        a.screen_lock()  # 锁屏
        a.vdi_disconnect(vdi_terminal_ip)  # 断开连接
        logging.info("----------------------------------web终端管理A1.3用例结束------------------------------")

    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_vdi_bach_delete(self, vdi_fixture):
        """
        1、搜索终端，并批量进行删除
        2、待终端删除后搜索该终端，验证搜索不到该终端
        """
        logging.info("----------------------------------web终端管理A1.6用例开始执行------------------------------")
        tm = IdvPage(vdi_fixture)
        a = AndroidVdi()
        try:
            # 搜索中终端并删除
            tm.search_terminal(vdi_terminal_ip)
            tm.vdi_select_all()
            tm.vdi_terminal_delete()
            # 验证搜索不到被删除的终端
            tm.search_terminal(vdi_terminal_ip)
            logging.info("批量删除终端后终端分组的终端数量为0")
            assert int(tm.total_count()) == 0
        finally:
            # 环境恢复
            a.disconnect_all_devices_and_connect(vdi_terminal_ip)
            a.login(name=vdi_user, ip=vdi_terminal_ip)
            time.sleep(30)
            a.screen_lock()  # 锁屏
            a.vdi_disconnect(vdi_terminal_ip)  # 断开连接
            logging.info("----------------------------------web终端管理A1.6用例开始执行------------------------------")

    # @pytest.mark.terminal
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.autotest
    # def test_vdi_bach_close(self, vdi_fixture):
    #     """
    #     1、搜索终端，选中搜索的终端，点击批量关闭终端
    #     2、使用ping命令
    #     """
    #     logging.info("----------------------------------web终端管理A1.5用例开始执行------------------------------")
    #     tm = IdvPage(vdi_fixture)
    #     tm.search_terminal(vdi_shutdown_ip)
    #     tm.vdi_select_all()
    #     tm.vdi_terminal_bach_close()
    #     assert tm.vdi_close_success_info() == u'终端关机成功'
    #     info = os.popen("ping {}".format(vdi_shutdown_ip))
    #     time.sleep(3)
    #     s1 = info.read().decode('gb2312')
    #     assert u"请求超时" in s1

    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_vdi_bach_group_change(self, com_fixture):
        """
        1、创建分组，将终端移至该分组下
        2、搜索终端，验证终端分组信息
        """
        logging.info("----------------------------------web终端管理A1.4用例开始执行------------------------------")
        idv = IdvPage(com_fixture)
        try:
            idv.goto_idv_terminal_page()
            # 创建分组
            idv.del_gp_exist(name="tm_gp04")
            idv.idv_creat_group(name="tm_gp04", img_name=image_name1)
            # 搜索终端移至分组下
            idv.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp04")
            # 搜索终端
            idv.search_terminal(idv_ip_1)
            tm_gp = idv.get_idv_gp(idv_ip_1)
            assert "tm_gp04" in tm_gp
        finally:
            # 善后，删除终端组
            idv.del_gp_exist(name="tm_gp04")
            time.sleep(2)
            logging.info("----------------web终端管理A1.4用例开始结束-------------")

    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('name', search_info)
    @pytest.mark.autotest_tm
    def test_vdi_search(self, vdi_fixture, name):
        logging.info("----------------------------------web终端管理A1.9,10用例开始执行-----------------------------")
        tm = IdvPage(vdi_fixture)
        vdi_android = AndroidVdi()
        tm.search_terminal(name)
        if name == 'vdi2_01':
            vdi_android.disconnect_all_devices_and_connect(ip=vdi_terminal_ip)
            vdi_android.login(name="vdi2_01", ip=vdi_terminal_ip)
            time.sleep(20)
            tm.search_terminal(name)
            logging.info("判断存在的用户可以搜索到唯一的信息")
            assert tm.total_count() == 1
            vdi_android.screen_lock()
            vdi_android.vdi_disconnect(ip=vdi_terminal_ip)
        elif name == 'vdi':
            logging.info("判断模糊搜素可以搜索到对应的信息")
            assert tm.total_count() != 0
        elif name.__contains__('172.21'):
            logging.info("判断ip搜索可以搜索到唯一的信息")
            assert tm.total_count() == 1
        elif name.__contains__("!"):
            logging.info("判断特殊字符串不能搜索到信息")
            assert tm.total_count() == 0
        else:
            logging.info("判断不存在的用户不能搜索到信息")
            assert tm.total_count() == 0
        logging.info("----------------------------------web终端管理A1.9,10用例开始结束------------------------------")

    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_vdi_info(self, vdi_fixture):
        logging.info("----------------------------------web终端管理A1.8用例开始执行------------------------------")
        tm = IdvPage(vdi_fixture)
        tm.search_terminal(vdi_terminal_ip)
        dic_info = tm.click_vdi_info(vdi_terminal_ip)
        tm.close_terminal_detail()
        tm_name = tm.get_vdi_name(vdi_terminal_ip)
        tm_sn = tm.get_vdi_sn(vdi_terminal_ip)
        logging.info("判断终端详情页面显示的信息和实际的一致")
        assert dic_info['name'] == tm_name
        # assert dic_info['cpu'] == cpu
        # assert dic_info['sys'] == sys
        assert dic_info['sn'] == tm_sn
        # assert dic_info['version'] == version
        # assert dic_info['mac'] == mac
        # assert dic_info['men'] == men
        # assert dic_info['mainboard'] == mainboard
        # assert dic_info['bios'] == bios
        # assert dic_info['storage'] == storage
        logging.info("----------------------------------web终端管理A1.8用例开结束------------------------------")

    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_vdi_check(self, vdi_fixture):
        logging.info("----------------------------------web终端管理A1.7用例开始执行------------------------------")
        tm = IdvPage(vdi_fixture)
        tm.click_terminal_check()
        tm.go_common_frame()
        tm.get_check_state_info(vdi_terminal_ip)
        time.sleep(2)
        logging.info(u"验证终端检测全部结果不为0")
        tm.go_common_frame()
        assert tm.get_value(tm.allCount_xpath) != 0

    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_new_idv_group(self, idv_fixture):
        logging.info("----------------------------------web终端管理A1.11,12用例开始执行------------------------------")
        tm = IdvPage(idv_fixture)
        # 创建分组成功
        tm.idv_new_group(idv_new_group_name[3])
        assert tm.find_group(idv_new_group_name[3]) == 1
        tm.delete_group(idv_new_group_name[3])
        tm.send_passwd_confirm()
        # 验证最大字符为32个字符
        tm.click_new_group()
        tm.go_common_frame()
        assert tm.get_elem_attribute(tm.new_group_name_xpath, "maxlength") == '32'
        tm.click_cancel()
        # 创建特殊字符分组
        tm.idv_new_group(idv_new_group_name[6])
        tm.click_confirm()
        tm.click_confirm()
        assert re.match(".*?display: block;", tm.vdi_group_name_error_info()) is not None
        tm.click_cancel()
        # 创建同名分组
        tm.idv_new_group(idv_new_group_name[0])
        tm.idv_new_group(idv_new_group_name[0])
        tm.back_current_page()
        time.sleep(2)
        assert tm.get_exist_info() == u"【test】终端组名已经存在"
        tm.click_sure()
        tm.go_common_frame()
        tm.click_cancel()
        tm.delete_group(idv_new_group_name[0])
        tm.send_passwd_confirm()
        time.sleep(2)
        logging.info("----------------------------------web终端管理A1.11,12用例开结束------------------------------")

    # ----------------------LinMengYao----------------------
    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm1
    def test_binding_image(self, com_fixture):
        """
        1、创建分组1，对终端进行初始化和重启操作后，将终端移至分组1下，
        2、创建用户，并登录终端，web上验证该终端绑定为分组镜像
        3、连接到终端服务器，验证终端的桌面类型为还原
        4、修改终端桌面类型为个性，连接终端服务器验证终端桌面类型为还原
        5、善后处理：删除终端组、用户以及用户组
        """
        logging.info("--------------------------------web终端管理用例A1.13、14开始执行--------------------------------")
        tm = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            # 创建用户组和用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="tm_testgp_134", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_testgp_134", user_name="tm_user_13", real_name="tm_user_13")
            tm.goto_idv_terminal_page()
            # 创建终端组,绑定镜像
            tm.del_gp_exist(name="tm_gp13")
            tm.idv_creat_group(name="tm_gp13", img_name=image_name1)
            # 搜索终端，将终端移至该分组下,并重启
            tm.search_terminal_anayway(idv_ip_1)
            tm.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp13")
            # 选择终端模式,用户登录终端
            tm.reboot_terminal(idv_ip_1)
            tm.wait_tm_reboot_success(idv_ip_1, 1)
            idv_initialization_click(idv_ip_1)
            idv_pattern_chose(ip=idv_ip_1, pattern="public")
            idv_login(ip=idv_ip_1, user_name="tm_user_13")
            idv_change_pwd(ip=idv_ip_1, name="tm_user_13", pwd="123")
            idv_login(ip=idv_ip_1, user_name="tm_user_13")
            time.sleep(60)
            # web上验证该终端的镜像为终端组绑定的镜像
            logging.info(u"验证终端后台绑定的镜像信息与分组信息一致")
            image_info = terminal_conn(idv_ip_1, cat_vm_image_info)
            assert image_name1 in image_info
            # 连接到终端服务器验证桌面类型为还原
            res = terminal_conn(idv_ip_1, cat_default_info)
            assert "allow_recovery                 = 1" in res
            # 修改终端桌面模式为个性
            tm.driver.refresh()
            tm.edit_idv_gp(gp_name="tm_gp13", desk_type=u"个性", ty=1)
            time.sleep(6)
            # 重启终端后，用户再次登录
            tm.reboot_terminal(idv_ip_1)
            tm.wait_tm_reboot_success(idv_ip_1, 1)
            idv_initialization_click(idv_ip_1)
            idv_login(ip=idv_ip_1, user_name="tm_user_13")
            time.sleep(60)
            # 连接到终端服务器，验证此时终端的桌面类型为个性
            res = terminal_conn(idv_ip_1, cat_default_info)
            assert "allow_recovery                 = 0" in res
        finally:
            try:
                # 删除终端组
                tm.del_gp_exist("tm_gp13")
                # 删除用户组和用户
                user.user_recovery("tm_testgp_134")
            except Exception as e:
                logging.info(e)

    @pytest.mark.terminal
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    @pytest.mark.terminal
    def test_set_gp_sys_disk(self, com_fixture):
        """
        1、创建分组，将终端移值该分组
        2、用户登录，验证系统盘大小为为40G，用户退出
        3、修改终端系统盘大小为50G，用户登录，验证系统盘大小为设置的值，用户退出
        4、修改终端组系统盘大小大于100G，验证配置不生效，用户退出
        5、善后处理，删除终端组，删除用户和用户组
        """
        logging.info("----------------------------------web终端管理用例A1.15开始执行----------------------------------")
        tm = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            # 创建用户组和用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="tm_testgp_15", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_testgp_15", user_name="tm_user_15", real_name="tm_user_15")
            # 创建终端组以及将终端移至该分组
            tm.goto_idv_terminal_page()
            tm.del_gp_exist(name="tm_gp15")
            tm.idv_creat_group(name="tm_gp15", img_name=image_name1)
            tm.search_terminal_anayway(idv_ip_1)
            tm.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp15")
            # 重启终端,
            tm.reboot_terminal(idv_ip_1)
            tm.wait_tm_reboot_success(idv_ip_1, 1)
            # 获取云桌面ip
            tm.search_terminal(idv_ip_1)
            desk_ip = tm.get_idv_desk_ip(idv_ip_1)
            # 用户登录终端
            idv_initialization_click(idv_ip_1)
            idv_pattern_chose(ip=idv_ip_1, pattern="public")
            idv_login(ip=idv_ip_1, user_name="tm_user_15")
            idv_change_pwd(ip=idv_ip_1, name="tm_user_15", pwd="123")
            idv_login(ip=idv_ip_1, user_name="tm_user_15")
            logging.info(u"查询虚机的系统盘大小")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            info = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd=cmd_c_size)
            assert tm.convert_size(info) == 40
            # 重启终端，修改终端组系统盘大小为50G
            tm.edit_idv_gp(gp_name="tm_gp15", sys_disk="50", ty=1)
            tm.back_current_page()
            tm.reboot_terminal(idv_ip_1)
            tm.wait_tm_reboot_success(idv_ip_1, 1)
            idv_login(ip=idv_ip_1, user_name="tm_user_15")
            logging.info(u"查询系统盘大小")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            info = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd=cmd_c_size)
            assert tm.convert_size(info) == 50
            # 修改终端组系统盘大小超过100G，验证不生效
            tm.edit_idv_gp(gp_name="tm_gp15", sys_disk="120", ty=1)
            tm.click_gp_edit_btn("tm_gp15")
            tm.go_common_frame()
            assert tm.get_elem_attribute(tm.change_disk_size_xpath, 'value') == '100'
            tm.click_cancel()
        finally:
            try:
                # 善后处理，删除终端组、用户以及用户组
                tm.del_gp_exist(name="tm_gp15")
                user.user_recovery("tm_testgp_15")
            except Exception as e:
                logging.info(e)

    @pytest.mark.terminal
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_enable_local_disk(self, com_fixture):
        """
        1、用户管理创建用户组和用户
        2、终端管理创建终端组（默认开启D盘），连接移至终端组，
        3、用户登录该终端，验证D盘存在，重启终端，用户退出
        4、修改终端组D盘属性关闭，用户再次登录终端
        5、验证用户无D盘可使用，重启终端
        6、善后处理：删除终端组、用户和用户组
        """
        logging.info("----------------------------------web终端管理用例A1.16开始执行----------------------------------")
        tm = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            # 创建用户组和用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="tm_testgp_16", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_testgp_16", user_name="tm_user_16", real_name="tm_user_16")
            # 创建终端组以及将终端移至该分组
            tm.goto_idv_terminal_page()
            tm.del_gp_exist(name="tm_gp16")
            tm.idv_creat_group(name="tm_gp16", img_name=image_name1)
            tm.search_terminal_anayway(idv_ip_1)
            tm.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp16")
            # 获得云桌面ip
            tm.search_terminal(idv_ip_1)
            desk_ip = tm.get_idv_desk_ip(idv_ip_1)
            tm.back_current_page()
            # 重启终端，用户登录终端
            tm.reboot_terminal(idv_ip_1)
            tm.wait_tm_reboot_success(idv_ip_1, 1)
            idv_initialization_click(idv_ip_1)
            idv_pattern_chose(ip=idv_ip_1, pattern="public")
            idv_login(ip=idv_ip_1, user_name="tm_user_16")
            idv_change_pwd(ip=idv_ip_1, name="tm_user_16", pwd="123")
            idv_login(ip=idv_ip_1, user_name="tm_user_16")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            info = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd=cmd_d_exist)
            assert info_disk_exist in info
            # 重启终端,修改终端组本地盘策略为关闭
            tm.edit_idv_gp(gp_name="tm_gp16", local_disk="close", ty=1)
            tm.back_current_page()
            tm.reboot_terminal(idv_ip_1)
            tm.wait_tm_reboot_success(idv_ip_1, 1)
            # 用户再次登录终端，验证无D盘可使用
            idv_initialization_click(idv_ip_1)
            idv_login(ip=idv_ip_1, user_name="tm_user_16")
            time.sleep(60)
            disk_info = terminal_conn(idv_ip_1, cat_default_info)
            assert "allow_userdisk                 = 0" in disk_info
            # win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            # info = get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd=cmd_d_exist)
            # assert info_disk_exist not in info
        finally:
            try:
                # 重启终端，删除终端组、用户组和用户
                tm.del_gp_exist(name="tm_gp16")
                user.user_recovery("tm_testgp_16")
            except Exception as e:
                logging.info(e)

    @pytest.mark.terminal
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    # @pytest.mark.test_tm
    def test_group_note(self, com_fixture):
        logging.info("----------------------------------web终端管理用例A1.17开始执行----------------------------------")
        tm = IdvPage(com_fixture)
        try:
            tm.goto_idv_terminal_page()
            tm.del_gp_exist(name="tm_gp_17")
            tm.idv_creat_group(name="tm_gp_17", img_name=image_name1)
            tm.edit_idv_gp(gp_name='tm_gp_17', note=u"描述测试测试测试", ty=1)
            # 查看分组详情，验证分组描述信息
            tm.click_gp_edit_btn(gp_name="tm_gp_17")
            tm.go_common_frame()
            # 验证maxlength值为60
            assert tm.get_elem_attribute(tm.tm_note_xpath, 'maxlength') == '60'
            tm.click_cancel()
        finally:
            try:
                # 善后处理：删除新增终端
                tm.del_gp_exist(name="tm_gp_17")
            except Exception as e:
                logging.info(e)

    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest
    @pytest.mark.autotest_tm
    def test_idv_set_host_ip(self, com_fixture):
        """初始化终端，选择该终端模式为多用户，验证是否在未分组终端组下"""
        logging.info("----------------------------------web终端管理用例A1.18开始执行----------------------------------")
        tm = IdvPage(com_fixture)
        tm.goto_idv_terminal_page()
        tm.terminal_init1(idv_ip_2)
        tm.reboot_terminal(idv_ip_2)
        tm.wait_tm_reboot_success(idv_ip_2, 1)
        idv_initialization_click(idv_ip_2)
        idv_pattern_chose(ip=idv_ip_2, pattern="public", times=15)
        tm.back_current_page()
        tm.search_terminal(idv_ip_2)
        gp_name = tm.get_idv_gp(idv_ip_2)
        logging.info("验证初次连接云主机的胖终端是否在未分组下")
        assert gp_name == u'未分组'

    @pytest.mark.terminal
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_modify_gp_name(self, com_fixture):
        logging.info("----------------------------------web终端管理用例A1.19开始执行----------------------------------")
        tm = IdvPage(com_fixture)
        tm.goto_idv_terminal_page()
        tm.idv_creat_group(name="tm_gp_19", img_name=image_name1)
        tm.edit_idv_gp(gp_name="tm_gp_19", rename="tm_rename_gp_19", ty=1)
        logging.info("验证修改胖终端组名后能否通过组名找到该组")
        tm.back_current_page()
        time.sleep(0.5)
        tm.get_ciframe(tm.all_page_iframe_id)
        assert "tm_rename_gp_19" in tm.get_value(tm.all_group)
        tm.del_gp_exist(name="tm_rename_gp_19")
        time.sleep(2)

    @pytest.mark.terminal
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_terminal_20(self, com_fixture):
        """
        1、创建用户组和用户
        2、创建终端分组，将终端移动到该分组上，用户登录，同时在C盘创建数据，用户退出登录
        4、修改终端分组绑定的镜像，重启终端，验证存在差分的终端镜像不会被改变
        5、删除终端组用户用户组以及重启终端
        """
        idv = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            # 创建用户组和用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="tm_ugp20", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_ugp20", user_name="tm_user20", real_name="tm_user20")
            # # 创建终端分组,修改终端所在分组
            idv.goto_idv_terminal_page()
            idv.del_gp_exist(name="tm_gp20")
            idv.idv_creat_group(name="tm_gp20", img_name=image_name1, desk_type=u"个性")
            # 修改终端分组，重启终端
            idv.search_terminal_anayway(idv_ip_1)
            idv.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp20")
            # 验证在线终端不受影响
            img_status = idv.get_terminal_status(idv_ip_1)
            assert u"在线" in img_status
            # 获取终端云桌面ip以及终端的镜像
            idv.search_terminal(idv_ip_1)
            desk_ip = idv.get_idv_desk_ip(idv_ip_1)
            idv.back_current_page()
            tm_image = idv.get_terminal_img(idv_ip_1)
            # 用户登录终端,并在终端写入数据
            idv.reboot_terminal(idv_ip_1)
            idv.wait_tm_reboot_success(idv_ip_1, 1)
            idv_initialization_click(idv_ip_1)
            idv_pattern_chose(ip=idv_ip_1, pattern="public")
            idv_login(ip=idv_ip_1, user_name="tm_user20")
            idv_change_pwd(ip=idv_ip_1, name="tm_user20", pwd="123")
            idv_login(ip=idv_ip_1, user_name="tm_user20")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            time.sleep(2)
            get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd="ipconfig > C:\yxltm_test.txt")
            time.sleep(2)
            # 修改分组绑定镜像
            idv.back_current_page()
            idv.edit_idv_gp(gp_name="tm_gp20", img=image_name2, ty=1)
            # 重启终端
            idv.back_current_page()
            idv.reboot_terminal(idv_ip_1)
            idv.wait_tm_reboot_success(idv_ip_1, 1)
            idv_initialization_click(idv_ip_1)
            idv_pattern_chose(idv_ip_1, "public")
            tm_image1 = idv.get_terminal_img(idv_ip_1)
            assert tm_image in tm_image1
        finally:
            try:
                # 善后处理
                idv.del_gp_exist(name="tm_gp20")
                user.user_recovery("tm_ugp20")
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    @pytest.mark.test_tm
    def test_terminal_21(self, com_fixture):
        """
        2、终端管理创建终端（默认为还原），将终端移动到该终端组下
        3、连接服务器查看修改是否生效
        4、修改终端模式为个性，连接服务器验证终端模式为个性，验证终端为在线状态，不受影响
        5、修改终端模式为还原，验证需要二次密码确认
        6、删除终端组
        """
        idv = IdvPage(com_fixture)
        try:
            idv.goto_idv_terminal_page()
            # 创建终端组桌面类型为还原，并将终端移动到该分组下
            idv.del_gp_exist("tm_gp21")
            idv.idv_creat_group(name="tm_gp21", img_name=image_name1)
            idv.modify_idv(tm_name=idv_ip_2, tm_group="tm_gp21")
            idv.back_current_page()
            idv.reboot_terminal(name=idv_ip_2)
            idv.wait_tm_reboot_success(idv_ip_2, 1)
            idv_initialization_click(idv_ip_2)
            idv_pattern_chose(idv_ip_2, "public")
            # 连接服务器，验证终端桌面类型为还原
            res = terminal_conn(ip=idv_ip_2, command=cat_default_info)
            assert u"allow_recovery                 = 1" in res
            # 修改分组桌面类型还原->个性
            idv.edit_idv_gp(gp_name="tm_gp21", desk_type=u"个性", ty=1)
            desk_type = idv.get_terminal_desk_type(idv_ip_2)
            assert u"个性" in desk_type
            time.sleep(3)
            # 验证在线终端不受影响
            res = terminal_conn(ip=idv_ip_2, command=cat_default_info)
            assert u"allow_recovery                 = 1" in res
        finally:
            try:
                # 删除终端
                idv.del_gp_exist("tm_gp21")
                time.sleep(2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_22(self, com_fixture):
        """
        1、创建公用户&多用户分组
        2、分组进行扩容
        3、验证扩容成功
        4、裁剪系统盘，验证裁剪不成功
        5、善后处理，删除分组
        """
        idv = IdvPage(com_fixture)
        try:
            idv.goto_idv_terminal_page()
            # 创建分组1
            idv.del_gp_exist(name="tm_gp22")  # 删除已存在分组
            time.sleep(1)
            idv.idv_creat_group(name="tm_gp22", img_name=image_name1, desk_type=u"个性")
            # 修改分组的系统盘为60
            idv.edit_idv_gp(gp_name="tm_gp22", sys_disk="60", ty=1)
            idv.back_current_page()
            idv.click_gp_edit_btn(gp_name="tm_gp22")
            idv.go_common_frame()
            sys_disk = idv.get_elem_attribute(idv.change_disk_size_xpath, 'aria-valuenow')  # 获取系统盘大小
            logging.info(u"验证系统盘扩容成功")
            assert sys_disk == "60"
            idv.click_confirm()
            idv.click_sure()
            # 裁剪系统盘为40G
            idv.back_current_page()
            idv.edit_idv_gp(gp_name="tm_gp22", sys_disk="40", ty=1)
            idv.back_current_page()
            idv.click_gp_edit_btn(gp_name="tm_gp22")
            idv.go_common_frame()
            sys_disk = idv.get_elem_attribute(idv.change_disk_size_xpath, 'aria-valuenow')  # 获取系统盘大小
            logging.info(u"验证系统盘裁剪失效")
            assert sys_disk == "60"
            idv.click_elem(idv.cancel_button_xpath)
        finally:
            try:
                idv.del_gp_exist(name="tm_gp22")
                time.sleep(2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.code
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_24(self, com_fixture):
        """
        1、创建分组修改分组的本地属性为关闭
        2、用户登录验证无本地盘使用，并且验证需要输入二次密码
        3、修改分组的本地属性为开启
        4、验证web上本地盘状态是开启的
        """
        idv = IdvPage(com_fixture)
        try:
            idv.goto_idv_terminal_page()
            # 创建分组，默认本地盘为开启
            idv.del_gp_exist("tm_gp24")
            idv.idv_creat_group(name="tm_gp24", img_name=image_name1)
            # 将终端移动该分组下，修改分组关闭本地盘使用
            idv.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp24")
            time.sleep(5)
            idv.edit_idv_gp(gp_name="tm_gp24", local_disk="close", ty=1)
            idv.back_current_page()
            idv.search_terminal(idv_ip_1)
            idv.click_idv_more_operate(idv_ip_1)
            idv.click_idv_edit(idv_ip_1)
            idv.go_common_frame()
            # 验证终端的本地盘是非启用状态
            assert "_unselect" in idv.get_elem_attribute(idv.other_set_xpath, "class")
            idv.click_cancel()
            # 修改分组1的本地盘为开启
            idv.edit_idv_gp(gp_name="tm_gp24", local_disk="open", ty=1)
            idv.back_current_page()
            idv.search_terminal(idv_ip_1)
            idv.click_idv_more_operate(idv_ip_1)
            idv.click_idv_edit(idv_ip_1)
            idv.go_common_frame()
            # 验证终端的本地盘是启用状态
            assert "_select" in idv.get_elem_attribute(idv.other_set_xpath, "class")
            idv.click_cancel()
            # info = terminal_conn(ip=idv_ip_1, command=cat_default_info)
            # assert "allow_userdisk                 = 1" in info
        finally:
            try:
                # 善后，删除终端组
                idv.del_gp_exist("tm_gp24")
                time.sleep(2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.code
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_25(self, com_fixture):
        """
        1、创建分组，搜索终端将，将终端移至该分组下
        2、修改终端的信息，与分组不一致
        3、修改分组信息后验证终端的信息不会随分组改变而改变
        """
        idv = IdvPage(com_fixture)
        try:
            idv.goto_idv_terminal_page()
            idv.del_gp_exist(name="tm_gp25")  # 删除已存在分组
            time.sleep(1)
            # 创建分组：桌面类型为还原，系统盘为40G，本地盘为开启
            idv.idv_creat_group(name="tm_gp25", img_name=image_name1)
            # 移动终端到分组1下,开启本地盘,个性桌面，系统盘为45G
            idv.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp25", desk_type=u"个性", sys_disk="45",
                           enable_d_disk="open")
            time.sleep(2)
            idv.back_current_page()
            # 查看终端信息
            idv.search_tm_click_edit(idv_ip_1)
            time.sleep(1)
            # 修改终端分组属性前获取终端的信息
            dis_size = idv.get_elem_attribute(idv.change_disk_size_xpath, "value")  # 获取系统盘大小
            local_disk = idv.get_elem_attribute(idv.enableUseLocalDiskId, 'class')  # 获取本地盘的状态
            idv.click_cancel()
            # 修改分组的属性:系统盘大小为50G，本地盘策略为关闭
            idv.back_current_page()
            idv.edit_idv_gp(tm_name="tm_gp25", sys_disk="50", local_disk="close")
            idv.back_current_page()
            # 验证终端的属性不跟随终端组改变
            idv.search_tm_click_edit(idv_ip_1)
            time.sleep(1)
            # 修改终端分组属性前获取终端的信息
            dis_size1 = idv.get_elem_attribute(idv.change_disk_size_xpath, "value")  # 获取系统盘大小
            local_disk1 = idv.get_elem_attribute(idv.enableUseLocalDiskId, 'class')  # 获取本地盘的状态
            logging.info(u"---验证修改分组的信息不影响终端的信息---")
            assert dis_size == dis_size1
            assert local_disk == local_disk1
            idv.click_elem(idv.cancel_button_xpath)  # 点击关闭
        finally:
            try:
                idv.del_gp_exist(name="tm_gp25")
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_26(self, com_fixture):
        """
        1、创建终端组
        2、将终端移动到分组下
        4、删除分组，验证需要进行二次确认、验证终端的分组信息为未分组，验证终端为在线，不受影响
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        # 创建分组1
        idv.del_gp_exist(name="tm_gp26")  # 删除已存在分组
        time.sleep(1)
        idv.idv_creat_group(name="tm_gp26", img_name=image_name1)
        # 搜索终端移动终端到分组1
        idv.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp26")  # 移动终端分组到分组1
        time.sleep(3)
        # 删除该终端分组
        flag = idv.del_gp_exist("tm_gp26")
        # 删除分组验证需要二次确认
        logging.info(u"---验证需要进行二次确认---")
        assert flag == 1
        idv.back_current_page()
        gp_name = idv.get_terminal_group(name=idv_ip_1)
        logging.info(u"---验证该终端所在的分组为未分组----")
        assert u"未分组" in gp_name
        status = idv.get_terminal_status(name=idv_ip_1)
        assert u"在线" in status
        time.sleep(2)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_27(self, com_fixture):
        """
        1、创建分组1，并将终端移动到该分组下
        2、搜索终端从多用户切换到公共，验证需要进行二次确认
        3、搜索终端从公共切换到多用户，验证需要二次确认
        4、搜索终端从多用户切换到单用户，验证需要进行二次确认，验证其分组信息为未绑定用户终端组
        5、善后：删除分组，并将终端进行初始化
        """
        idv = IdvPage(com_fixture)
        try:
            idv.goto_idv_terminal_page()
            # 创建分组1,将终端移动到分组下
            idv.del_gp_exist(name="tm_gp27")  # 删除已存在分组
            time.sleep(1)
            idv.idv_creat_group(name="tm_gp27", img_name=image_name1)
            idv.search_terminal_anayway(idv_ip_2)
            idv.modify_idv(tm_name=idv_ip_2, tm_group="tm_gp27")
            time.sleep(3)
            # 搜索终端，修改终端模式为公共
            flag = idv.modify_idv(tm_name=idv_ip_2, tm_type=u"公用")
            logging.info(u"---验证从多用户->公用需要进行二次密码确认---")
            assert flag == 1
            time.sleep(2)
            # 搜索终端，修改终端模式为多用户
            logging.info(u"---验证从公用->多用户需要进行二次密码确认---")
            flag = idv.modify_idv(tm_name=idv_ip_2, tm_type=u"多用户")
            assert flag == 1
            time.sleep(2)
            # 搜索终端，修改终端模式为单用户
            logging.info(u"----验证从多用户->单用户需要进行二次密码确认----")
            flag = idv.modify_idv(tm_name=idv_ip_2, tm_type=u"单用户")
            assert flag == 1
            time.sleep(2)
            # 进入单用户终端组，搜索终端
            logging.info(u"---获取终端组的信息，验证信息为未绑定终端组----")
            idv.goto_idv_terminal_single_terminal_group_page()
            gp_name = idv.get_single_tm_gp(name=idv_ip_2)
            assert u"未绑定用户终端组" in gp_name
        finally:
            try:
                # 善后处理
                logging.info(u"善后处理")
                idv.driver.refresh()
                idv.goto_idv_terminal_single_terminal_group_page()
                idv.modify_idv(tm_name=idv_ip_2, tm_type=u"多用户")
                time.sleep(3)
                idv.goto_idv_terminal_moreandpub_terminal_group_page()  # 进入多用户&公用终端组
                idv.del_gp_exist(name="tm_gp27")
                time.sleep(2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_28(self, com_fixture):
        """
        1、搜索终端，修改终端名称
        2、用修改后的终端名称搜索
        3、验证终端存在
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        idv.modify_idv(tm_name=idv_ip_1, tm_rename="Rename_idv")
        tm_ip = idv.get_terminal_idv_ip("Rename_idv")
        assert tm_ip == idv_ip_1

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_29(self, com_fixture):
        """
        1、创建分组1、2，将终端移动到1下
        2、等待文件检查结束，镜像开始下载（此时终端不存在差分），移动该终端到分组2下
        3、重启终端，验证该终端镜像为分组2的镜像
        4、善后处理，删除分组
        """
        idv = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            # 用户管理创建用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="tm_test29", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_test29", user_name="tm_user29", real_name="tm_user29")
            # 创建分组1、2
            idv.goto_idv_terminal_page()
            idv.del_gp_exist(name="tm_gp29_1")  # 删除已存在分组
            idv.del_gp_exist(name="tm_gp29_2")  # 删除已存在分组
            idv.idv_creat_group(name="tm_gp29_1", img_name=image_name1, desk_type=u"个性")
            idv.idv_creat_group(name="tm_gp29_2", img_name=image_name2)
            # 修改终端所在的分组为分组1
            idv.search_terminal_anayway(idv_ip_1)
            idv.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp29_1")
            time.sleep(2)
            idv.reboot_terminal(idv_ip_1)
            idv.wait_tm_reboot_success(idv_ip_1, 1)
            idv_initialization_click(ip=idv_ip_1)
            idv_pattern_chose(ip=idv_ip_1, pattern=u"public")
            # 对终端进行初始化操作后，验证该镜像绑定的镜像与组一致
            logging.info(u"对终端进行初始化验证镜像跟随终端组")
            image_info = terminal_conn(idv_ip_1, cat_vm_image_info)
            assert image_name1 in image_info
            # tm_img = idv.get_terminal_img(name=idv_ip_1)
            # assert image_name1 in tm_img
            idv.back_current_page()
            idv.search_terminal(idv_ip_1)
            desk_ip = idv.get_idv_desk_ip(idv_ip_1)
            # 用户登录终端，并在C盘写入文件
            idv_initialization_click(ip=idv_ip_1)
            # 有些终端不大稳定，在修改用户名和密码之前需要先做登录（输入错误的用户名和密码)
            idv_login(ip=idv_ip_1, user_name="tm_user29")
            idv_change_pwd(ip=idv_ip_1, name="tm_user29", pwd="123")
            idv_login(ip=idv_ip_1, user_name="tm_user29")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            get_win_conn_info(ip=desk_ip, user_name=s_user, passwd=s_pwd, cmd="ipconfig > C:\yxltm_test.txt")
            # 移动该终端到分组2，重启终端，验证镜像未改变
            flag = idv.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp29_2")
            logging.info(u"验证二次密码确认")
            assert flag == 1  # 验证二次确认密码
            time.sleep(4)
            # 重启终端，验证镜像未改变
            idv.reboot_terminal(idv_ip_1)
            idv.wait_tm_reboot_success(idv_ip_1, 1)
            img = idv.get_terminal_img(idv_ip_1)
            logging.info(u"验证存在差分的镜像未被改变")
            assert img == image_name1
            idv_initialization_click(idv_ip_1)
            idv_pattern_chose(idv_ip_1, "public")
        finally:
            try:
                # 善后处理
                idv.del_gp_exist("tm_gp29_1")
                idv.del_gp_exist("tm_gp29_2")
                user.user_recovery("tm_test29")
                # user.back_current_page()
                # user.goto_usermanage_page()
                # user.del_user_in_group(group_name="tm_test29")
                # time.sleep(2)
                # user.del_group(name="tm_test29", password=passwd)
                # time.sleep(2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_30(self, com_fixture):
        """
        1、创建终端分组为类型为个性，将终端移动该分组下重启终端
        2、更改终端的桌面类型个性->还原，验证需要进行二次确认
        3、验证终端状态为在线，在线用户不受影响
        4、终端退出登录后再次登录，验证c盘数据1消失，同时在终端c盘创建数据2,
        5、修改终端桌面类型还原->个性
        6、退出登录，验证数据2存在
        """
        idv = IdvPage(com_fixture)
        try:
            idv.goto_idv_terminal_page()
            idv.idv_creat_group(name="tm_gp_30", img_name=image_name1, desk_type=u"个性")
            idv.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp_30")
            time.sleep(2)
            # 重启终端，连接服务器验证终端类型为个性
            idv.reboot_terminal(name=idv_ip_1)
            idv.wait_tm_reboot_success(idv_ip_1, 1)
            time.sleep(60)
            info = terminal_conn(ip=idv_ip_1, command=cat_default_info)
            assert "allow_recovery                 = 0" in info
            # 修改终端类型为还原,验证需要二次密码确认
            idv.back_current_page()
            flag = idv.modify_idv(tm_name=idv_ip_1, desk_type=u"还原")
            assert flag == 1
            time.sleep(3)
            # 重启终端，连接终端服务器，验证此时桌面类型为还原
            idv.reboot_terminal(idv_ip_1)
            idv.wait_tm_reboot_success(idv_ip_1, 1)
            time.sleep(60)
            info = terminal_conn(ip=idv_ip_1, command=cat_default_info)
            assert "allow_recovery                 = 1" in info
            # 修改终端组所的系统盘大小
            idv.edit_idv_gp(gp_name="tm_gp_30", sys_disk="60", ty=1)
            time.sleep(5)
            # 此时终端为自定义终端，属性不跟随分组
            idv.search_terminal(idv_ip_1)
            idv.click_idv_more_operate(idv_ip_1)
            idv.click_idv_edit(idv_ip_1)
            idv.go_common_frame()
            sys_size = idv.get_elem_attribute(idv.change_disk_size_xpath, 'value')
            assert '60' != sys_size
            idv.click_cancel()
        finally:
            try:
                # 善后处理，删除终端组
                idv.del_gp_exist("tm_gp_30")
                time.sleep(2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_31(self, com_fixture):
        """
        1、创建分组，将终端移动到该分组下
        2、扩容系统盘大小，验证扩容成功
        3、裁剪系统盘大小，验证裁剪不生效
        4、修改终端组系统盘大小，验证该终端的系统盘不跟随终端组大小改变而改变
        5、删除分组
        """
        idv = IdvPage(com_fixture)
        try:
            idv.goto_idv_terminal_page()
            idv.del_gp_exist(name="tm_gp31")  # 删除已存在分组
            time.sleep(1)
            # 创建分组：桌面类型为还原，系统盘为40G，本地盘为开启
            idv.idv_creat_group(name="tm_gp31", img_name=image_name1)
            # 移动终端到分组下
            idv.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp31", sys_disk="45")
            idv.back_current_page()
            time.sleep(1)
            # 查看终端信息，获取终端系统盘大小
            idv.search_tm_click_edit(idv_ip_1)
            time.sleep(1)
            dis_size1 = idv.get_elem_attribute(idv.change_disk_size_xpath, "value")  # 获取系统盘大小45G
            assert "45" in dis_size1
            idv.click_cancel()
            idv.back_current_page()
            # 裁剪：裁剪系统盘大小为40
            idv.modify_idv(tm_name=idv_ip_1, sys_disk="40")
            idv.back_current_page()
            # 查看终端信息，获取终端系统盘大小
            idv.search_tm_click_edit(idv_ip_1)
            time.sleep(1)
            dis_size1 = idv.get_elem_attribute(idv.change_disk_size_xpath, "value")  # 获取系统盘大小45G
            # 验证系统盘裁剪不生效
            assert "45" in dis_size1
            idv.click_cancel()
            idv.back_current_page()
            # 修改终端组的系统盘大小为50G
            idv.edit_idv_gp(gp_name="tm_gp31", sys_disk="50", ty=1)
            time.sleep(3)
            # 搜索终端，验证其属性不会跟随终端走
            idv.search_tm_click_edit(idv_ip_1)
            time.sleep(1)
            dis_size1 = idv.get_elem_attribute(idv.change_disk_size_xpath, "value")  # 获取系统盘大小45G
            # 验证该终端为自定义终端
            assert "45" in dis_size1
            idv.click_cancel()
        finally:
            try:
                idv.del_gp_exist(name="tm_gp31")
                time.sleep(2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_32(self, com_fixture):
        """
        1、修改终端关闭本地盘策略
        2、web上验证修改成功，验证需要进行二次确认同时验证终端状态为在线
        3、修改分组磁盘为50G，验证终端的磁盘大小不跟随分组改变而改变
        4、修改终端开启本地盘策略，web上验证修改成功
        """
        idv = IdvPage(com_fixture)
        try:
            idv.goto_idv_terminal_page()
            # 创建分组，本地盘默认为开启
            idv.del_gp_exist(name="tm_gp32")  # 删除已存在分组
            time.sleep(1)
            idv.idv_creat_group(name="tm_gp32", img_name=image_name1)
            # 移动终端到分组下
            idv.modify_idv(tm_name=idv_ip_1, tm_group="tm_gp32")
            idv.back_current_page()
            # 修改分组，关闭本地盘
            flag = idv.modify_idv(tm_name=idv_ip_1, enable_d_disk="close")
            assert flag == 1
            idv.back_current_page()
            # 验证终端的本地磁盘属性为关闭
            idv.search_terminal(idv_ip_1)
            idv.click_idv_more_operate(idv_ip_1)
            idv.click_idv_edit(idv_ip_1)
            idv.go_common_frame()
            # 验证终端的本地盘是关闭状态
            assert "_unselect" in idv.get_elem_attribute(idv.other_set_xpath, "class")
            idv.click_cancel_button()
            # 验证终端状态为在线
            status = idv.get_terminal_status(name=idv_ip_1)
            assert u"在线" in status
            # 修改终端的分组系统盘为50G
            idv.back_current_page()
            idv.edit_idv_gp(tm_name="tm_gp32", sys_disk="50")
            # 搜索终端，验证其属性不会跟随终端走
            idv.search_tm_click_edit(idv_ip_1)
            time.sleep(1)
            dis_size1 = idv.get_elem_attribute(idv.change_disk_size_xpath, "value")  # 获取系统盘大小45G
            # 验证该终端为自定义终端
            assert "50" not in dis_size1
            idv.click_cancel_button()
            # 修改终端为开启本地盘
            idv.modify_idv(tm_name=idv_ip_1, enable_d_disk="open")
            # 验证终端的本地磁盘属性为关闭
            idv.search_terminal(idv_ip_1)
            idv.click_idv_more_operate(idv_ip_1)
            idv.click_idv_edit(idv_ip_1)
            idv.go_common_frame()
            # 验证终端的本地盘是关闭状态
            assert "_select" in idv.get_elem_attribute(idv.other_set_xpath, "class")
            idv.click_elem(idv.cancel_button_xpath)
        finally:
            try:
                idv.back_current_page()
                idv.del_gp_exist(name="tm_gp32")
                time.sleep(2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_33(self, com_fixture):
        """
        -1、用户管理创建用户，用户登录
        1、还原镜像之前在C盘创建数据
        2、点击镜像还原，验证需要进行二次确认
        3、用户登录终端，验证C盘数据被还原
        """
        idv = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            # 创建用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="tm_ugp33", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_ugp33", user_name="tm_user33", real_name="tm_user33")
            time.sleep(2)
            idv.goto_idv_terminal_page()
            idv.search_terminal(idv_ip_1)
            desk_ip = idv.get_idv_desk_ip(idv_ip_1)
            # 终端用户登录
            idv.reboot_terminal(idv_ip_1)
            idv.wait_tm_reboot_success(idv_ip_1, 1)
            idv_initialization_click(idv_ip_1)
            idv_login(ip=idv_ip_1, user_name="tm_user33")
            idv_change_pwd(ip=idv_ip_1, name="tm_user33", pwd="123")
            idv_login(ip=idv_ip_1, user_name="tm_user33")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            # 向C盘写入数据
            time.sleep(2)
            get_win_conn_info(desk_ip, s_user, s_pwd, "ipconfig > C:\yyy01.txt")
            # 还原镜像验证，需要进行二次确认
            idv.back_current_page()
            flag = idv.restore_img(idv_ip_1)
            assert flag == 1
            # 还原终端，终端自动重启，用户登录终端，验证C盘的数据被删除
            idv.wait_tm_reboot_success(idv_ip_1, 1)
            idv_initialization_click(idv_ip_1)
            idv_login(ip=idv_ip_1, user_name="tm_user33")
            win_conn_useful(ip=desk_ip, name=s_user, pwd=s_pwd)
            # 验证c盘数据被还原
            msg1 = get_win_conn_info(ip=desk_ip, user_name=Administrator, passwd=rcd, cmd="dir")
            assert "yyy01.txt" not in msg1
        finally:
            try:
                # 重启终端，删除用户
                idv.back_current_page()
                idv.reboot_terminal(idv_ip_1)
                idv.wait_tm_reboot_success(idv_ip_1, 1)
                user.user_recovery("tm_ugp33")
                # user.back_current_page()
                # user.goto_usermanage_page()
                # user.del_user_in_group(group_name="tm_ugp33")
                # user.del_group(name="tm_ugp33")
                # time.sleep(30)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_a1_34(self, com_fixture):
        """
        1、搜索单用户终端，并将终端进行初始化操作
        2、连接终端，设置服务器ip，并设置终端为单用户终端
        3、进入单用户终端页面，搜索终端，验证该终端所在的组为未绑定用户终端组
        """
        logging.info("----------------------------------终端管理A1.34用例开始执行------------------------------")
        idv = IdvPage(com_fixture)
        # 进入单用户终端页面
        idv.goto_idv_terminal_page()
        idv.goto_idv_terminal_single_terminal_group_page()
        # 初始化终端，并修改终端的模式为单用户终端
        idv.search_terminal_anayway(idv_ip_3, 1)
        idv.terminal_init1(idv_ip_3)
        # 进入多用户终端组重启终端
        idv.goto_idv_terminal_moreandpub_terminal_group_page()
        idv.reboot_terminal(idv_ip_3)
        idv.wait_tm_reboot_success(idv_ip_3, 1)
        idv_initialization_click(idv_ip_3)
        time.sleep(60)
        # 将终端设置为单用终端（默认模式为单用户终端）
        idv.back_current_page()
        idv.goto_idv_terminal_single_terminal_group_page()
        tm_gp = idv.get_single_tm_gp(idv_ip_3)
        assert u"未绑定用户终端组" in tm_gp
        logging.info("----------------------------------终端管理A1.34用例结束------------------------------")

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_a1_35(self, idv_fixture):
        logging.info("----------------------------------终端管理A1.35用例开始执行------------------------------")
        idv_page = IdvPage(idv_fixture)
        idv_page.goto_idv_terminal_single_terminal_group_page()
        arr1 = idv_page.get_all_single_terminal_group_name()
        del arr1[len(arr1) - 1]
        str1 = "".join(arr1)
        idv_page.goto_user_manage_page()
        arr2 = idv_page.get_all_user_group_name()
        str2 = "".join(arr2)
        assert str1 == str2
        logging.info("----------------------------------终端管理A1.35用例结束------------------------------")

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_36(self, com_fixture):
        """
        1、创建分组以及用户，开启idv特性
        2、在单用户终端组绑定1中创建的用户
        3、用户登录终端
        4、验证绑定的镜像类型为1用户中所绑定镜像
        5、验证该终端位置自动移动到用户对应单用户终端组，即所在分组为1中所创建的分组
        6、善后：删除用户，删除用户组，重启终端
        """
        idv = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            user.goto_usermanage_page()
            # 创建开启idv特性分组以及用户
            user.create_group_openidv(group_name="tm_ugp36", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_ugp36", user_name="tm_user36", real_name="tm_user36")
            time.sleep(1)
            # 进入单用户终端页面搜索终端，并绑定用户
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=idv_ip_3, user_name="tm_user36")
            time.sleep(2)
            # 用户登录终端
            idv.reboot_terminal(idv_ip_3)
            idv.wait_tm_reboot_success(idv_ip_3)
            idv_initialization_click(ip=idv_ip_3)
            idv_pattern_chose(idv_ip_3)
            idv_login(ip=idv_ip_3, user_name="tm_user36")
            idv_change_pwd(ip=idv_ip_3, name="tm_user36", pwd="123")
            idv_login(ip=idv_ip_3, user_name="tm_user36")
            time.sleep(60)
            logging.info(u"---验证终端分组信息---")
            idv.back_current_page()
            tm_gp = idv.get_single_tm_gp(idv_ip_3)
            assert u"tm_ugp36" in tm_gp
            logging.info(u"---验证终端镜像---")
            image_info = terminal_conn(idv_ip_3, cat_vm_image_info)
            assert image_name1 in image_info
            time.sleep(3)
        finally:
            try:
                # 善后处理，解绑用户，重启终端
                idv.remove_bingding_user(idv_ip_3)
                idv.reboot_terminal(idv_ip_3)
                idv.wait_tm_reboot_success(idv_ip_3)
                user.user_recovery("tm_ugp36")
                # user.back_current_page()
                # user.goto_usermanage_page()
                # user.del_user_in_group(group_name="tm_ugp36")
                # user.del_group(name="tm_ugp36")
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_37(self, com_fixture):
        """
        1、用户管理创建分组与用户
        2、搜索某个终端移动，修改终端类型为单用户
        4、到单用户页面搜索该终端，绑定1所创建的用户
        5、验证此时单用户所在的分组为单用户终端分组
        6、解绑该终端所绑定的用户，验证该终端此时所在的分组为未绑定用户终端组
        7、善后处理
        """
        idv = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            # 创建开启idv特性分组以及用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="tm_ugp37", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_ugp37", user_name="tm_user37", real_name="tm_user37")
            time.sleep(1)
            # 进入单用户终端页面搜索终端，并绑定用户
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=idv_ip_3, user_name="tm_user37")
            time.sleep(2)
            idv.back_current_page()
            tm_gp = idv.get_single_tm_gp(idv_ip_3)
            assert u"tm_ugp37" in tm_gp
            # 搜索终端并解绑用户
            idv.search_terminal(idv_ip_3)
            idv.click_elem(idv.remove_bingding_xpath)
            idv.go_common_frame()
            idv.click_elem(idv.confirm_xpath)
            logging.info(u"--验证解绑将删除数据--")
            assert u"解绑会清空终端上保存的用户数据" in idv.get_value(idv.unbing_info)
            idv.send_passwd_confirm(passwd)
            tm_gp = idv.get_single_tm_gp(idv_ip_3)
            assert u"未绑定用户终端组" in tm_gp
        finally:
            try:
                # 重启终端，删除用户和用户组
                idv.back_current_page()
                idv.reboot_terminal(idv_ip_3)
                idv.wait_tm_reboot_success(idv_ip_3)
                user.user_recovery("tm_ugp37")
                # user.back_current_page()
                # user.goto_usermanage_page()
                # user.del_user_in_group(group_name="tm_ugp37")
                # user.del_group(name="tm_ugp37")
                # time.sleep(30)  # 待终端环境恢复
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_38(self, com_fixture):
        """
        1、创建开启idv特性的用户组和用户
        2、进入终端管理-单用户终端组
        3、在单用户终端组搜索终端绑定1中创建的用户
        4、编辑该终端，验证其只可修改终端名称，其他属性为disable
        6、解绑该终端，验证终端模式和终端名称两者属性是可修改
        """
        idv = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            # 创建开启idv特性分组以及用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="tm_ugp38", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_ugp38", user_name="tm_user38", real_name="tm_user38")
            time.sleep(1)
            # 进入单用户终端页面搜索终端，并绑定用户
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=idv_ip_3, user_name="tm_user38")
            time.sleep(2)
            idv.back_current_page()
            logging.info(u"---验证绑定用户的终端可修改属性,修改终端名称---")
            idv.search_terminal(idv_ip_3)
            idv.click_idv_more_operate(idv_ip_3)
            idv.click_idv_edit(idv_ip_3)
            idv.go_common_frame()
            time.sleep(1)
            assert "true" == idv.get_elem_attribute(idv.idv_tm_type, "disabled")
            assert "true" == idv.get_elem_attribute(idv.idv_tm_group, 'disabled')
            assert "true" == idv.get_elem_attribute(idv.idv_tm_desk_type, 'disabled')
            assert "true" == idv.get_elem_attribute(idv.system_disk_size, 'disabled')
            assert "true" == idv.get_elem_attribute(idv.enableUseLocalDiskId, 'disabled')
            idv.click_cancel()
            # 解绑终端所绑定的用户
            idv.back_current_page()
            idv.remove_bingding_user(idv_ip_3)
            time.sleep(2)
            idv.back_current_page()
            logging.info(u"---验证解绑后终端参数--")
            idv.search_terminal(idv_ip_3)
            idv.click_idv_more_operate(idv_ip_3)
            idv.click_idv_edit(idv_ip_3)
            idv.go_common_frame()
            assert "true" == idv.get_elem_attribute(idv.idv_tm_group, 'disabled')
            assert "true" == idv.get_elem_attribute(idv.idv_tm_desk_type, 'disabled')
            assert "true" == idv.get_elem_attribute(idv.system_disk_size, 'disabled')
            assert "true" == idv.get_elem_attribute(idv.enableUseLocalDiskId, 'disabled')
            idv.click_cancel()
            time.sleep(1)
        finally:
            try:
                # 善后处理
                user.back_current_page()
                user.goto_usermanage_page()
                user.del_user_in_group(group_name="tm_ugp38")
                user.del_group(name="tm_ugp38")
                time.sleep(2)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_39(self, com_fixture):
        """
        1、搜索终端单用户终端，点击编辑终端，验证该终端分组属性不可修改
        """
        # 搜索终端，变更其类型为单用户终端
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        idv.goto_idv_terminal_single_terminal_group_page()
        idv.search_terminal_anayway(idv_ip_3, 1)
        logging.info(u"---验证单用户终端分组属性不可修改---")
        idv.search_terminal(idv_ip_3)
        idv.click_idv_more_operate(idv_ip_3)
        idv.click_idv_edit(idv_ip_3)
        assert "true" == idv.get_terminal_attribute(idv.idv_tm_group, "disabled")
        idv.click_cancel()

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_40(self, com_fixture):
        """
        1、创建开启idv特性的用户组和用户
        2、搜索终端绑定用户，修改终端模式修改为多用户
        3、验证不允许修改
        5、解绑终端，修改终端模式为多用户或公用
        6、验证此时终端的分组为多用户&公用终端组组中的未分组
        7、环境恢复，还原终端类型为单用户终端
        """
        idv = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            # 创建开启idv特性分组以及用户
            user.goto_usermanage_page()
            user.create_group_openidv(group_name="tm_ugp40", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_ugp40", user_name="tm_user40", real_name="tm_user40")
            time.sleep(2)
            # 进入单用户终端页面搜索终端，并绑定用户
            idv.goto_idv_terminal_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=idv_ip_3, user_name="tm_user40")
            idv.back_current_page()
            # 验证绑定单用户的终端模式不可修改
            logging.info(u"---验证绑定用户的终端模式不可修改---")
            idv.search_terminal(idv_ip_3)
            idv.click_idv_more_operate(idv_ip_3)
            idv.click_idv_edit(idv_ip_3)
            idv.go_common_frame()
            time.sleep(1)
            assert u"true" == idv.get_elem_attribute(idv.idv_tm_type, "disabled")
            idv.click_cancel()
            idv.back_current_page()
            # 解绑用户，修改该终端为多用户终端
            idv.remove_bingding_user(idv_ip_3)
            time.sleep(2)
            idv.back_current_page()
            idv.modify_idv(tm_name=idv_ip_3, tm_type=u"多用户")
            # 进入多用户&公共用户页面
            idv.back_current_page()
            idv.goto_idv_terminal_moreandpub_terminal_group_page()
            tm_gp = idv.get_terminal_group(name=idv_ip_3)
            assert u"未分组" == tm_gp
            idv.back_current_page()
        finally:
            try:
                # 善后，恢复终端为单用户终端
                idv.modify_idv(tm_name=idv_ip_3, tm_type=u"单用户")
                idv.back_current_page()
                idv.goto_idv_terminal_single_terminal_group_page()  # 进入单用户终端页面
                idv.reboot_terminal(idv_ip_3)
                time.sleep(1)
                user.back_current_page()
                user.goto_usermanage_page()
                user.del_user_in_group(group_name="tm_ugp40")
                time.sleep(1)
                user.del_group(name="tm_ugp40")
                time.sleep(45)  # 待终端环境恢复
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_41(self, com_fixture):
        """
        1、搜索多用户终端验证终端mac和web上显示的一致
        2、搜索公用终端mac和web上显示一致
        3、搜索单用户终端终端的mac和web上显示一致
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        logging.info(u"-------------多用户终端验证------------")
        idv.search_terminal_anayway(idv_ip_1)
        tm_mac = idv.get_idv_mac(idv_ip_1)
        dic = get_ip_mac(ip=idv_ip_1)
        assert tm_mac == dic['mac']
        assert idv_ip_1 == dic['ip']
        idv.back_current_page()
        logging.info(u"---------------公用户验证--------------")
        idv.search_terminal_anayway(idv_ip_4)
        tm_mac = idv.get_idv_mac(idv_ip_4)
        dic = get_ip_mac(ip=idv_ip_4)
        assert tm_mac == dic['mac']
        assert idv_ip_4 == dic['ip']
        idv.back_current_page()
        logging.info(u"---------------单用户验证--------------")
        idv.goto_idv_terminal_single_terminal_group_page()
        idv.search_terminal_anayway(idv_ip_3, 1)
        tm_mac = idv.get_idv_mac_single(idv_ip_3)
        dic = get_ip_mac(ip=idv_ip_3)
        assert tm_mac == dic['mac']
        assert idv_ip_3 == dic['ip']
        idv.back_current_page()

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.parametrize('diff_terminal', mac_diff)
    @pytest.mark.autotest_tm
    def test_terminal_42(self, com_fixture, diff_terminal):
        """
        1、搜索不同类型的终端，查看mac
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        tm_mac = idv.get_idv_mac(diff_terminal)
        dic = get_ip_mac(ip=diff_terminal)
        assert tm_mac == dic['mac']
        assert diff_terminal == dic['ip']
        idv.back_current_page()

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.parametrize('name1', search_terminal)
    @pytest.mark.autotest_tm
    def test_a1_42(self, com_fixture, name1):
        """
        1、分别搜索多、公、单用户终端的终端，并将终端进行初始化操作
        2、验证需要进行二次密码确认
        3、验证ip，终端名称不变
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        idv.search_terminal(name1)
        if name1 not in idv.get_value(idv.tableContent_xpath):
            idv.back_current_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.search_terminal(name1)
        flag = idv.terminal_init1(name=name1)  # 初始化终端
        logging.info(u"---验证需要二次确认----")
        assert flag == 1
        info = terminal_conn(ip=name1, command=r"cd /opt/lessons & ll")  # 进入终端后台查看是否存在差分
        logging.info(u"---验证终端不存在差分文件----")
        assert ".image" not in info
        logging.info(u"---查看ip和mac等信息未被删除---")
        dic = get_ip_mac(ip=name1)
        assert name1 == dic['ip']
        logging.info(u"--验证终端名称未被删除---")
        tm_name = get_idv_terminal_name(ip=name1)
        assert tm_name != ' '
        idv.back_current_page()
        idv.reboot_terminal(name1)
        time.sleep(45)  # 待终端重启

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.parametrize('info', tm_mode)
    @pytest.mark.autotest_tm
    def test_terminal_43(self, com_fixture, info):
        """
        1、搜索多、公、单用户终端，将终端进行还原
        2、验证需要进行二次密码确认
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        # 搜索多用户进行终端还原
        idv.search_terminal_anayway(info)
        idv.modify_idv(tm_name=info, desk_type=u"个性")  # 修改终端为个性终端
        idv.reboot_terminal(info)
        idv.wait_tm_reboot_success(info, 1)
        idv.search_terminal(info)
        idv.click_idv_more_operate(info)
        idv.click_elem(idv.restore_cd_xpath)  # 点击还原云桌面
        idv.back_current_page()
        idv.click_elem(idv.confirm_reboot_xpath)
        # 验证二次确认密码输入框存在
        assert idv.elem_is_exist(idv.confirm_passwd_xpath) == 0

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest
    @pytest.mark.parametrize('info', tm_mode)
    @pytest.mark.autotest_tm
    def test_terminal_44(self, com_fixture, info):
        """
        1、搜索多、公、单用户终端，将终端进行D盘清空
        2、验证需要进行二次密码确认
        3、备注：验证终端用户D盘数据是否被清空未做校验，
           等待时间过长从更换终端模式到下载镜像到删除D盘数据再到重启验证
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        # 修改终端的本地盘为开启状态
        idv.search_terminal(info)
        if info not in idv.get_value(idv.tableContent_xpath):
            idv.back_current_page()
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.search_terminal(info)
        idv.modify_idv(tm_name=info, enable_d_disk="open")
        time.sleep(3)
        flag = idv.clear_Ddisk(info)
        assert flag == 1
        idv.back_current_page()
        # # 重启终端
        # idv.reboot_terminal(info)
        # time.sleep(45)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_45(self, com_fixture):
        """
        1、搜索在线终端，点击日志搜集
        2、搜索离线终端，点击搜集日志，验证离线终端无法搜集日志
        3、完成部分，下载的压缩包无法解压查看验证内容
        """
        idv = IdvPage(com_fixture)
        # login = Login(download_fixture)
        # login.login(name=username, pwd=passwd)
        idv.goto_idv_terminal_page()
        # 搜索离线终端
        off_line_name = idv.get_offline_tm()
        idv.search_terminal(off_line_name[0])
        idv.click_idv_more_operate(off_line_name[0])
        # 验证搜集日志是不可点击
        assert u"终端离线，不支持收集终端日志" in idv.get_elem_attribute(idv.terminal_log, 'title')

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_terminal_46(self):  # , com_fixture
        """
        1、搜索终端，点击ip设置，修改终端ip和云桌面ip
        2、重启终端，等待终端起机后搜索终端，验证终端的ip和云桌面是修改后的ip
        3、注：该过程不可逆，一旦修改ip终端会处于离线状态，未写
        """
        pass
        # idv = IdvPage()
        # idv.goto_idv_terminal_page()
        # # 设置终端ip
        # idv.back_current_page()
        # idv.terminal_ip_set(tm_name=tm_online3, terminal_ip="172.21.3.122", cd_ip="172.21.3.222")
        # time.sleep(5)
        # idv.back_current_page()
        # tm_ip = idv.get_terminal_idv_ip(name=tm_online3)
        # assert "172.21.3.122" in tm_ip
        # cd_ip = idv.get_idv_desk_ip(tm_name=tm_online3)
        # assert "172.21.3.222" in cd_ip
        # time.sleep(2)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_47(self, com_fixture):
        """
        1、事先需准备一个未连接到本服务器的在线终端
        2、此时查看idv终端管理页面没有出现该终端
        3、连接该终端到本服务器上
        4、刷新页面，搜索终端名称，验证页面出现该终端名称
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        # 搜索未连接到本服务器的在线终端，验证终端不存在
        idv.search_terminal(name="rcd_yxl")
        search_text = idv.getinfo_by_search_after()
        assert u"无记录信息" in search_text
        # 连接到测试终端（未连接到服务器，但终端在线的终端ip）
        idv_initialization_click(idv_ip_1)
        idv_pattern_chose(idv_ip_1, "public")
        click_idv_set(ip=idv_ip_1)
        idv_set_name_host_ip(ip=idv_ip_1, name="rcd_yxl", h_ip=host_ip)  # 设置终端名称，以及连接到本服务器上
        time.sleep(5)  # 等待5s
        # 点击刷新，搜索刚连上的终端名称，验证终端存在
        idv.back_current_page()
        idv.click_refresh()
        idv.search_terminal_anayway(name="rcd_yxl")
        idv.search_terminal(name="rcd_yxl")
        search_text = idv.getinfo_by_search_after()
        assert "rcd_yxl" in search_text
        time.sleep(2)
        logging.info(u"---善后：修改终端名称，以便用例可反复执行---")
        idv_initialization_click(idv_ip_1)
        click_idv_set(ip=idv_ip_1)
        idv_set_name_host_ip(ip=idv_ip_1, name="rcd", h_ip=host_ip)  # 设置终端名称，以及连接到本服务器上
        idv.back_current_page()
        idv.click_refresh()
        idv.back_current_page()
        idv.reboot_terminal(idv_ip_1)
        idv.wait_tm_reboot_success(idv_ip_1, 1)

    # @pytest.mark.case_level_1
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.terminal
    # @pytest.mark.autotest
    # def test_terminal_48(self, com_fixture):
    #     """
    #     1、创建多用户分组，搜索1在线终端，分别验证关机操作前状态为在线
    #     2、终端做关机操作，等待几秒，验证1终端的状态为离线
    #     """
    #     idv = IdvPage(com_fixture)
    #     idv.goto_idv_terminal_page()
    #     # 创建分组1
    #     idv.del_gp_exist(name="idv_tmgp48")  # 删除已存在分组
    #     time.sleep(1)
    #     idv.idv_creat_group(name="idv_tmgp48", img_name=image_name1, desk_type=u"个性")
    #     # 搜索在线终端，验证状态为在线
    #     idv.back_current_page()
    #     tm_status = idv.get_terminal_status(name=shut_down_tm)
    #     assert u"在线" in tm_status
    #     # 将两个终端移动到分组1下
    #     idv.modify_idv(tm_name=shut_down_tm, tm_group="idv_tmgp48")
    #     time.sleep(2)
    #     # 终端关机
    #     idv.back_current_page()
    #     idv.click_tm_gp_and_close_tm(group_name="idv_tmgp48")
    #     time.sleep(10)
    #     # 关机后，搜索连个终端，验证均为离线
    #     idv.back_current_page()
    #     tm_status = idv.get_terminal_status(name=shut_down_tm)
    #     assert u"离线" in tm_status
    #     idv.driver.refresh()
    #     time.sleep(2)
    #     # 删除创建的终端
    #     idv.del_gp_exist(name="idv_tmgp48")
    #     time.sleep(2)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_49(self, com_fixture):
        """
        1、创建多用户分组，搜索两个在线终端，分别验证重启前状态为在线
        2、终端做重启操作，验证两个终端的状态为重启中
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        # 创建分组1
        idv.del_gp_exist(name="idv_tmgp49")  # 删除已存在分组
        time.sleep(1)
        idv.idv_creat_group(name="idv_tmgp49", img_name=image_name1, desk_type=u"个性")
        # 搜索终端，验证状态为在线
        idv.search_terminal_anayway(idv_ip_1)
        tm_status = idv.get_terminal_status(name=idv_ip_1)
        assert u"在线" in tm_status
        # 将两个终端移动到分组1下
        idv.modify_idv(tm_name=idv_ip_1, tm_group="idv_tmgp49")
        time.sleep(2)
        # 终端重启
        idv.back_current_page()
        idv.click_tm_gp_and_reboot_tm(group_name="idv_tmgp49")
        # 验证终端的状态
        tm_status = idv.get_terminal_status(name=idv_ip_1)
        assert u"重启中" in tm_status
        idv.wait_tm_reboot_success(idv_ip_1, 1)
        idv_initialization_click(idv_ip_1)
        idv_pattern_chose(idv_ip_1, "public")
        # 删除创建的分组
        idv.driver.refresh()
        idv.del_gp_exist(name="idv_tmgp49")
        time.sleep(20)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_50(self, com_fixture):
        """
        1、创建多用户分组，搜索一个在线终端和一个离线终端分别移动到1分组下
        2、删除该分组下的所有终端，验证一个终端删除失败，原因为在线终端不可删除
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        # 创建终端组
        idv.del_gp_exist(name="idv_tmgp50")  # 删除已存在分组
        idv.idv_creat_group(name="idv_tmgp50", img_name=image_name1)
        # 获取离线终端，并将其移动到创建的终端组
        offline_name = idv.get_offline_tm()
        try:
            idv.modify_idv(tm_name=offline_name[0], tm_group="idv_tmgp50")
        except Exception as error:
            print(u"搜索的离线终端超过最大终端数,或离线终端不存在")
        # 搜索在线终端，将其移动到创建的终端组
        idv.search_terminal_anayway(idv_ip_1)
        idv.modify_idv(tm_name=idv_ip_1, tm_group="idv_tmgp50")
        # 终端删除
        idv.back_current_page()
        idv.click_tm_gp_and_del_tm(group_name="idv_tmgp50")
        time.sleep(3)
        # 验证在线终端无法删除
        idv.back_current_page()
        assert u"在线终端不能删除" in idv.get_elem_text(idv.tips_text)
        time.sleep(1)
        idv.click_elem(idv.sure_xpath)  # 点击确定
        # 善后处理，删除离线终端
        idv.driver.refresh()
        idv.del_gp_exist(name="idv_tmgp50")
        time.sleep(2)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_52(self, com_fixture):
        """
        1、创建用户组和用户
        2、在多用户-公用终端组创建终端组
        3、进入单用户终端组，搜索终端
        4、绑定1创建的用户后，修改绑定的终端组为多用户
        5、验证需解绑才可移动终端
        6、解绑终端，将其移动到多用户终端组，重启终端，查看终端模式
        7、将该终端移动到单用户终端组，验证需要二次密码确认
        8、重启终端
        """
        idv = IdvPage(com_fixture)
        user = UserMange(com_fixture)
        try:
            user.goto_usermanage_page()
            # 创建开启idv特性分组以及用户
            user.create_group_openidv(group_name="tm_ugp52", cd_type=u"个性", img_name=image_name1)
            user.create_user_in_group(group_name="tm_ugp52", user_name="tm_user52", real_name="tm_user52")
            time.sleep(1)
            # 创建终端组
            idv.goto_idv_terminal_page()
            idv.del_gp_exist(name="tm_gp52")  # 删除已存在分组
            time.sleep(1)
            idv.idv_creat_group(name="tm_gp52", img_name=image_name1, desk_type=u"个性")
            idv.back_current_page()
            # 进入单用户终端组页面，搜索终端绑定用户
            idv.goto_idv_terminal_single_terminal_group_page()
            idv.single_bingding_user(tm_name=idv_ip_3, user_name="tm_user52")
            idv.back_current_page()
            time.sleep(2)
            # 搜索用户变更终端模式
            idv.click_gp_modify_tmtype(group_name="tm_ugp52")
            idv.back_current_page()
            tips_info = idv.get_tips_text()
            assert u"已经绑定用户，无法变更终端模式，请先解除绑定后在执行变更操作" in tips_info
            idv.click_elem(idv.sure_xpath)  # 点击确定
            # 解绑终端移动到多用户分组
            idv.remove_bingding_user(idv_ip_3)
            idv.modify_idv(tm_name=idv_ip_3, tm_type=u"多用户")
            # 进入多用户终端组,搜索终端，并重启
            idv.goto_idv_terminal_moreandpub_terminal_group_page()
            idv.reboot_terminal(idv_ip_3)
            idv.wait_tm_reboot_success(idv_ip_3, 1)
            idv_initialization_click(idv_ip_3)
            idv_pattern_chose(idv_ip_3)
            # 连接到服务器，查看终端模式为多用户
            info = terminal_conn(ip=idv_ip_3, command=cat_logic_ini)
            assert "mode                           = 1" in info
            # 将终端移动到创建的分组下
            idv.modify_idv(tm_name=idv_ip_3, tm_group="tm_gp52")
            idv.back_current_page()
            # 变更分组模式为单用户
            flag = idv.click_tm_gp_and_change_tm_type(group_name="tm_gp52", terminal_type=u"单用户")
            logging.info(u"----验证需要进行二次确认------")
            assert flag == 1
            # 删除创建的终端组
            idv.driver.refresh()
            idv.del_gp_exist(name="tm_gp52")
            time.sleep(3)
        finally:
            try:
                # 善后：进入单用户终端组页面
                idv.goto_idv_terminal_single_terminal_group_page()
                idv.reboot_terminal(idv_ip_3)
                user.goto_usermanage_page()
                user.del_user_in_group(group_name="tm_ugp52")
                time.sleep(2)
                user.del_group(name="tm_ugp52")
                time.sleep(45)
            except Exception as e:
                logging.info(e)

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.autotest_tm
    def test_terminal_53(self, com_fixture):
        """
        1、搜索idv进行，模糊查询，验证查询结果正确
        2、终端ip查找，查询结果正确
        3、搜索终端，移至单用户终端组，进入单用户终端组搜索终端，验证搜索终端存在
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        # 搜索终端，模糊查询
        idv.search_terminal(name="172.21")
        search_info = idv.getinfo_by_search_after()
        logging.info(u"---验证模糊查询搜索终端存在---")
        assert "172.21" in search_info
        # 根据终端ip搜索
        idv.search_terminal(name=idv_ip_4)
        search_info = idv.getinfo_by_search_after()
        logging.info(u"---ip查询搜索终端存在----")
        assert idv_ip_4 in search_info
        idv.back_current_page()
        # 进入单用户页面，搜索终端
        idv.goto_idv_terminal_single_terminal_group_page()
        idv.search_terminal_anayway(idv_ip_3, ty=1)
        idv.search_terminal(name=idv_ip_3)
        search_info = idv.getinfo_by_search_after()
        assert idv_ip_3 in search_info

    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.terminal
    @pytest.mark.autotest_tm
    def test_terminal_54(self, com_fixture):
        """
        1、输入不存在用户，终端名以及ip和特殊字符查询终端
        2、验证插叙终端不存在
        """
        idv = IdvPage(com_fixture)
        idv.goto_idv_terminal_page()
        idv.search_terminal(name="bucunzaiyonghu_yuxiaolan")
        info = idv.getinfo_by_search_after()
        assert u"无记录信息" in info
        idv.search_terminal(name="bucunzaizhognduan")
        info = idv.getinfo_by_search_after()
        assert u"无记录信息" in info
        idv.search_terminal(name="1.1.1.1")
        info = idv.getinfo_by_search_after()
        assert u"无记录信息" in info
        idv.search_terminal(name="@#$$%%^")
        info = idv.getinfo_by_search_after()
        assert u"无记录信息" in info


if __name__ == "__main__":
    t = time.strftime("%Y-%m-%d %H%M")
    pytest.main(["-m", "autotest_tm1", "--html", report_dir + "//{0}_terminal_html_report.html".format(t)])
    # pytest.main(["-m", "terminal11"])
