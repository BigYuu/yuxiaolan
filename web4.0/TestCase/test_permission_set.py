#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: LinMengYao
@contact: linmengyao@ruijie.com
@software: PyCharm
@time: 2018/12/10 14:17
"""
import pytest
import re
from Common.serverconn import *
from WebPages.LoginPage import Login
from TestData.Logindata import *
from WebPages.permission_setPage import PermissionSet
from TestData.permission_setdata import *
from WebPages.adnroid_vdi_page import AndroidVdi
from WebPages.CdeskmangePage import CDeskMange
from WebPages.UserMangePage import UserMange
from Common.terminal_action import *
from Common.file_dir import *


class TestPermissionSet:

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_create_new_account(self, com_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.1开始执行------------------------------")
        ps = PermissionSet(com_fixture)
        try:
            ps.go_admin_setting()
            ps.search_user(admin_name)
            ps.create_new_account()
            ps.add_user_group_account(keyword_search_user)
            ps.add_idv_group_account(keyword_search_idv)
            ps.add_vdi_group_account(keyword_search_vdi)
            ps.input_required_data(admin_name, name, password, assure_password)
            logging.info("新建管理员账号成功验证")
            ps.check_account(admin_name, status_normal, type_admin, keyword_search_user, keyword_search_idv,
                             keyword_search_vdi, user=1, idv=1, vdi=1)
        finally:
            logging.info("删除用户数据")
            ps.delete_manger_user(admin_name)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_warn_new_account(self, com_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.2开始执行------------------------------")
        ps = PermissionSet(com_fixture)
        ps.go_admin_setting()
        ps.create_new_account()
        ps.input_required_data(un_admin_name, name, password, assure_password)
        logging.info("用户名输入不合法比较提示信息是否正确")
        ps.check_warn_admin_name()
        ps.input_required_data(admin_name, name, un_password, un_password)
        logging.info("密码输入不合法比较提示信息是否正确")
        ps.check_warn_password()
        ps.input_required_data(admin_name, name, password, un_assure_password)
        logging.info("输入密码确认错误提示信息是否正确")
        ps.check_warn_assure_password()

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_add_ten_user_group(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.3开始执行------------------------------")
        user = Login(login_fixture)
        user.login(c_user, c_pwd)
        ps = PermissionSet(login_fixture)
        try:
            ps.go_admin_setting()
            ps.create_new_account()
            ps.add_ten_user_group(keyword_search_ten_user)
            ps.input_required_data(ten_admin_name, name, password, assure_password)
            ps.check_account(ten_admin_name, status_normal, type_admin, keyword_search_ten_user, keyword_search_idv,
                             keyword_search_vdi, user=1)
            ps.logout()
            user.login(ten_admin_name, password)
            ps.go_user_management()
            ps.check_ten_user_group()
        finally:
            ps.logout()
            user.login(c_user, c_pwd)
            logging.info("删除用户数据")
            ps.go_admin_setting()
            time.sleep(1)
            ps.delete_manger_user(ten_admin_name)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_add_no_resource_account(self, com_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.5开始执行------------------------------")
        ps = PermissionSet(com_fixture)
        try:
            ps.go_admin_setting()
            ps.create_new_account()
            ps.input_required_data(admin_name_no_resource, name, password, assure_password)
            ps.message_no_resource()
            ps.check_account(admin_name_no_resource, status_normal, type_admin)
        finally:
            logging.info("删除用户数据")
            ps.delete_manger_user(admin_name_no_resource)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_edit_user_group(self, com_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.6开始执行------------------------------")
        ps = PermissionSet(com_fixture)
        ps.go_admin_setting()
        try:
            ps.search_by_admin_name(common_admin)
            ps.edit_user_group(common_admin, keyword_search_user_A6)
            ps.check_account(common_admin, status_normal, type_admin, keyword_search_user_A6, user=1, idv=-1, vdi=-1,
                             action=1)
        finally:
            logging.info("数据恢复")
            ps.search_by_admin_name(common_admin)
            ps.chose_user_group(common_admin, ['vdi1', u'2级'])

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_edit_terminal_group(self, com_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.7开始执行------------------------------")
        ps = PermissionSet(com_fixture)
        ps.go_admin_setting()
        try:
            ps.search_by_admin_name(common_admin)
            ps.edit_idv_group(common_admin, keyword_search_idv_A7)
            ps.check_account(common_admin, status_normal, type_admin, keyword_search_idv=keyword_search_idv_A7,
                             user=-1, idv=1, vdi=-1, action=2)
            ps.edit_vdi_group(common_admin, keyword_search_vdi_A7)
            ps.check_account(common_admin, status_normal, type_admin, keyword_search_vdi=keyword_search_vdi_A7,
                             user=-1, idv=-1, vdi=1, action=3)
        finally:
            logging.info("数据恢复")
            ps.driver.refresh()
            ps.search_by_admin_name(common_admin)
            ps.edit_idv_group(common_admin, 'idv1')
            ps.edit_vdi_group(common_admin, 'vdi1')

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_edit_info(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.8开始执行------------------------------")
        user = Login(login_fixture)
        user.login(c_user, c_pwd)
        ps = PermissionSet(login_fixture)
        try:
            ps.go_admin_setting()
            ps.create_new_mannger(A_18_admin[0], A_18_admin[1], A_18_admin[2], A_18_admin[3], A_18_admin[4],
                                  A_18_admin[5],
                                  A_18_admin[6])
            ps.search_by_admin_name(A_18_admin[0])
            ps.edit_admin(A_18_admin[0], admin_name_A8, name_A8)
            ps.check_account(admin_name_A8, status_normal, type_admin, user=-1, idv=-1, vdi=-1, action=4)
            ps.reset_password(admin_name_A8, password_A8, password_A8)
            ps.logout()
            user.login(admin_name_A8, password)
            assert user.get_error_info() == u'用户名或密码错误'
            user.clear_info()
            user.login(admin_name_A8, password_A8)
            ps.welcome_user_logo(admin_name_A8)

        finally:
            logging.info("删除用户数据")
            ps.logout()
            user.login(c_user, c_pwd)
            ps.go_admin_setting()
            ps.delete_manger_user(admin_name_A8)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('ad_name', fuzzy_query_admin)
    def test_fuzzy_query_admin(self, com_fixture, ad_name):
        logging.info("------------------------------web管理员账号设置用例A1.11开始执行------------------------------")
        ps = PermissionSet(com_fixture)
        ps.go_admin_setting()
        ps.fuzzy_query_admin_check(ad_name)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_administrator_create_user_group(self, com_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.12开始执行------------------------------")
        ps = PermissionSet(com_fixture)
        ps.go_user_management()
        try:
            ps.add_user_group_check(user_group_name_A12)
            assert ps.click_user_group(user_group_name_A12) == u'用户组存在'
        finally:
            ps.driver.refresh()
            user = UserMange(com_fixture)
            user.del_group(user_group_name_A12, c_pwd)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_administrator_create_deepest_group(self, com_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.13开始执行------------------------------")
        ps = PermissionSet(com_fixture)
        ps.go_user_management()
        time.sleep(2)
        try:
            ps.create_user_group_round_check(user_group_template_A13, 10)
        except:
            raise AssertionError
        finally:
            user = UserMange(com_fixture)
            # for i in range(2,10):
            #     ps.click_group_unfold(user_group_template_A13+str(i))
            for i in range(10, 1, -1):
                user.del_group(user_group_template_A13 + str(i), c_pwd)
                time.sleep(0.5)

    @pytest.mark.permission12
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_admin_create_middle_user(self, login_fixture):
        logging.info("-----------------------------web管理员账号设置用例A1.14、16开始执行----------------------------")
        user = Login(login_fixture)
        user.login(common_admin, common_pwd)
        ps = PermissionSet(login_fixture)
        us = UserMange(login_fixture)
        vdi = AndroidVdi()
        try:
            ps.go_user_management()
            if int(us.search_num_info(user_name_A14))!= 0:
                us.del_chose_user(user_name_A14, common_pwd)
            group_name = ps.unfold_user_group(5)
            ps.create_user_check(user_name_A14, user_name_A14)
            ps.chk_usr_gp_attr(group_name, user_name_A14)
            vdi.vdi_connect(vdi_ip)
            vdi.login(user_name_A14.encode("utf-8"), vdi_ip, "123456")
            assert vdi.is_win_activity().__contains__('.RemoteCanvasActivity')
        finally:
            ps.go_user_management()
            vdi.terminal_close()
            vdi.vdi_disconnect(vdi_ip)
            us.del_chose_user(user_name_A14, common_pwd)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_admin_create_deepest_user(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.15开始执行------------------------------")
        user = Login(login_fixture)
        user.login(common_admin, common_pwd)
        ps = PermissionSet(login_fixture)
        us = UserMange(login_fixture)
        try:
            ps.go_user_management()
            group_name = ps.unfold_user_group(10)
            ps.create_user_check(user_name_A15, user_name_A15)
            ps.search_user(user_name_A15)
            ps.chk_usr_gp_attr(group_name, user_name_A15)
        finally:
            us.del_chose_user(user_name_A15, common_pwd)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_mv_terminal(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.17开始执行------------------------------")
        user = Login(login_fixture)
        user.login(c_user, c_pwd)
        ps = PermissionSet(login_fixture)
        try:
            ps.go_vdi()
            ps.terminal_group_click(u'未分组')
            count = ps.search_terminal(keyword_search_vdi_A17)
            ps.change_terminal_group(vdi_group_A17)
            ps.logout()
            user.login(common_admin, common_pwd)
            ps.go_vdi()
            ps.terminal_group_click(vdi_group_A17)
            ps.search_terminal(keyword_search_vdi_A17)
            ps.check_search_terminal(keyword_search_vdi_A17, count)
        finally:
            ps.logout()
            user.login(c_user, c_pwd)
            ps.go_vdi()
            ps.terminal_group_click(vdi_group_A17)
            ps.search_terminal(keyword_search_vdi_A17)
            ps.change_terminal_group(u'未分组')

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_admin_modify_pwd(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.18开始执行------------------------------")
        user = Login(login_fixture)
        user.login(common_admin, common_pwd)
        ps = PermissionSet(login_fixture)
        try:
            ps.go_modify_password(common_pwd, password_A8, password_A8)
            ps.logout()
            user.login(common_admin, password_A14)
            assert user.get_error_info() == u'用户名或密码错误'
            user.clear_info()
            user.login(common_admin, password_A8)
            ps.welcome_user_logo(common_admin)
        finally:
            ps.go_modify_password(password_A8, common_pwd, common_pwd)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_adm_modify_usr_gp(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.19开始执行------------------------------")
        user = Login(login_fixture)
        user.login(c_user, c_pwd)
        ps = PermissionSet(login_fixture)
        ps.go_admin_setting()
        ps.search_by_admin_name(common_admin)
        adm_usr_list = ps.get_adm_usr_gp()
        ps.logout()
        user.login(common_admin, common_pwd)
        ps.go_user_management()
        usr_manage_list = ps.get_usr_manage_gp()
        adm_usr_list.remove(u'未分组')
        usr_manage_list.remove(u'未分组')
        assert adm_usr_list == usr_manage_list
        ps.search_user(A1_19_user)
        usr_list = ps.edit_usr_check(A1_19_user)
        usr_list.remove(u'未分组')
        assert usr_manage_list == usr_list

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_adm_create_usr_gp(self, login_fixture):
        logging.info("-----------------------------web管理员账号设置用例A1.20、22开始执行----------------------------")
        user = Login(login_fixture)
        user.login(common_admin, common_pwd)
        ps = PermissionSet(login_fixture)
        try:
            ps.go_user_management()
            usr_gp_list = ps.get_usr_manage_gp()
            ps.click_user_group(usr_gp_list[0])
            ps.add_user_group_check(group_name_A20)
            ps.edit_usr_gp_base(group_name_A20)
            time.sleep(5)
            ps.logout()
            user.login(c_user, c_pwd)
            ps.go_user_management()
            ps.click_group_unfold(usr_gp_list[0])
            assert ps.click_user_group(group_name_A20) == u'用户组存在'
        finally:
            us = UserMange(login_fixture)
            us.del_group(group_name_A20, c_pwd)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_adm_create_deepest_gp(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.21开始执行------------------------------")
        user = Login(login_fixture)
        user.login(common_admin, common_pwd)
        ps = PermissionSet(login_fixture)
        try:
            ps.go_user_management()
            usr_gp_list = ps.get_usr_manage_gp()
            ps.click_user_group(usr_gp_list[0])
            ps.create_user_group_round_check(user_group_template_A21, 9, base=1)
            ps.logout()
            user.login(c_user, c_pwd)
            ps.go_user_management()
            ps.click_group_unfold(usr_gp_list[0])
            for i in range(2, 10):
                ps.click_group_unfold(user_group_template_A21 + str(i))
        finally:
            us = UserMange(login_fixture)
            for i in range(9, 1, -1):
                us.del_group(user_group_template_A21 + str(i), c_pwd)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_send_message(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.23开始执行------------------------------")
        user = Login(login_fixture)
        user.login(common_admin, common_pwd)
        ps = PermissionSet(login_fixture)
        ps.go_user_management()
        ps.unfold_user_group(10)
        ps.send_message_gp(u'10级', message_title_A23, message_content_A23)
        usr_list = ps.get_usr_list()
        ps.go_desk_manage()
        for usr in usr_list:
            vdi = AndroidVdi()
            vdi.vdi_connect(vdi_ip)
            vdi.login(usr, vdi_ip, "123")
            c_ip = ps.get_desk_ip(usr)
            assert vdi.is_win_activity() == "com.undatech.opaque.RemoteCanvasActivity"
            if win_conn_useful(c_ip, 'Administrator', 'rcd') == u'winrm可使用':
                win_conn(c_ip, 'Administrator', 'rcd', 'send_message')
                assert get_win_conn_info(c_ip, 'Administrator', 'rcd', r'type C:\access.log').__contains__('get_info')
                vdi.vdi_disconnect(vdi_ip)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_adm_view_message(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.24开始执行------------------------------")
        user = Login(login_fixture)
        user.login(c_user, c_pwd)
        ps = PermissionSet(login_fixture)
        ps.go_user_management()
        ps.send_message_gp(u'2级', message_title_A24, message_content_A24)
        time.sleep(5)
        ps.logout()
        user.login(common_admin, common_pwd)
        ps.go_user_management()
        ps.send_message_gp(u'2级', u'普通管理员信息', u'普通管理员信息测试')
        ps.open_message_log()
        ps.view_message_check(message_title_A24)
        ps.view_message_check(u'普通管理员信息')

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_adm_remote(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.25开始执行------------------------------")
        vdi = AndroidVdi()
        user = Login(login_fixture)
        cd = CDeskMange(login_fixture)
        try:
            vdi.vdi_connect(vdi_ip)
            vdi.login(A1_23_user, vdi_ip, '123')
            assert vdi.is_win_activity().__contains__('RemoteCanvasActivity')
            user.login(common_admin, common_pwd)
            ps = PermissionSet(login_fixture)
            ps.go_desk_manage()
            ip = ps.remote(A1_23_user)
            time.sleep(5)
            assert re.match(u'正在发起远程协助，请稍等... 超时倒计时：\d+秒', cd.get_assistance_info()) is not None
            cd.back_current_page()
            if win_conn_useful(ip, 'Administrator', 'rcd') == u'winrm可使用':
                win_conn(ip, 'Administrator', 'rcd', u'assistance')
                time.sleep(5)
                assert cd.get_assistance_info() == u'对方接受了您的远程协助'
        finally:
            cd.close_assistance_tool()
            time.sleep(1)
            cd.click_close_assistion_button()
            vdi.vdi_disconnect(vdi_ip)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_del_admin(self, com_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.9开始执行------------------------------")
        ps = PermissionSet(com_fixture)
        ps.go_admin_setting()
        ps.create_new_mannger(kwd_sch_uer_A9, kwd_sch_uer_A9, '123456', '123456')
        ps.search_by_admin_name(kwd_sch_uer_A9)
        ps.del_admin_check(kwd_sch_uer_A9)

    @pytest.mark.permission1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_del_lot_admin(self, login_fixture):
        logging.info("------------------------------web管理员账号设置用例A1.10开始执行------------------------------")
        user = Login(login_fixture)
        user.login(c_user, c_pwd)
        ps = PermissionSet(login_fixture)
        try:
            ps.go_admin_setting()
            ps.search_use_info('del_admin')
            ps.del_lot_admin_check()
            ps.logout()
            for u_name in A1_10_user:
                user.clear_info()
                user.login(u_name, '123456')
                assert user.get_error_info() == u'用户名或密码错误'
        finally:
            user.clear_info()
            user.login(c_user, c_pwd)
            ps.go_admin_setting()
            for u_name in A1_10_user:
                ps.create_new_mannger(u_name, u_name, '123456', '123456')


if __name__ == "__main__":
    pass
    t = time.strftime("%Y-%m-%d %H%M")
    pytest.main(['-v', "-m", "permission12"])
    # pytest.main(['-v','-s',"-m", "permission1", "--html", report_dir + "//{0}_permission_set_html_report.html".format(t)])
