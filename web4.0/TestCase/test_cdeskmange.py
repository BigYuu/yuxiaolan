#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/10/11 16:50
"""
import datetime

import pytest
from WebPages.CdeskmangePage import CDeskMange
from TestData.Cdmdata import *
from Common.terminal_action import *
from WebPages.LoginPage import Login
from WebPages.Idvpage import IdvPage
from WebPages.adnroid_vdi_page import AndroidVdi
from WebPages.UserMangePage import UserMange


class Test_CDM:

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_idv_info_check(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.1，19用例开始执行--------------------------")
        p = CDeskMange(cmd_fixture)
        idv_login(idv_single_ip_list[0], 'idv1_02', '123')
        idv_login(idv_public_ip_list[1], 'idv1_03', '123')
        idv_guest_login(idv_guest_ip_list[0])
        if p.vm_login_success(idv_guest_ip_list[0], u'访客') == 0:
            for name in ["idv1_02", u'访客']:
                if name == u'访客':
                    name = idv_guest_ip_list[0]
                p.search_info(name)
                tip = p.get_terminal_ip(name)
                logging.info(u'{}终端连接后判断状态,用户名,终端状态等信息与实际相符'.format(name))
                terminal_info = get_terminal_info(tip)
                assert p.get_terminal_name(name) == terminal_info['terminal_name']
                if name == idv_guest_ip_list[0]:
                    assert p.get_user_name(name) == u'访客'
                else:
                    assert p.get_user_name(name) == name
                assert p.get_status(name) == u"运行"
                ip = p.get_cloud_desk_ip(name)
                if win_conn_useful(ip, s_user, s_pwd) == u'winrm可使用':
                    win_conn(ip, s_user, s_pwd, 'lock')
                    time.sleep(30)
                    logging.info(u'判断锁屏后的的状态是运行，锁屏后的状态为{}'.format(p.get_status(name)))
                    assert p.get_status(name) == u"运行"
                    logging.info('锁屏后重新登入')
                    win_conn(ip, suser, syspasswd, 'login')
                    time.sleep(5)
                    win_conn(ip, suser, syspasswd, 'logout')
                    time.sleep(30)
                    logging.info('判断退出登入后的状态为离线')
                    assert p.get_status(name) == u"离线"
        else:
            logging.error("云桌面管理A1.1，19用例未执行，终端登入出错")
            raise AssertionError
        logging.info("----------------------------------web云桌面管理A1.1，19用例结束------------------------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_user_vdi_idv_info_check(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.3用例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        v = AndroidVdi()
        try:
            p.search_info(vname)
            idv_login(idv_single_ip_list[0], vname, cpasswd)
            time.sleep(30)
            p.search_info(vname)
            assert p.get_terminal_type(idv_single_ip_list[0]) == u'IDV'
            assert p.get_status(idv_single_ip_list[0]) == u'运行'
            logging.info("用户用双重身份idv登入后再登入vdi判断页面显示的总孤单信息和终端的实际信息一致")
            v.vdi_connect(vdi_ip)
            v.login(vname, vdi_ip, cpasswd)
            p.search_info(vname)
            time.sleep(0.5)
            assert int(p.get_search_amount()) >= 2
            p.search_info(vdi_ip)
            assert p.get_terminal_type(vdi_ip) == u'VDI'
            assert p.get_status(vdi_ip) == u'运行'
            assert v.termianl_user_info() == vname
            assert v.termianl_name_info() == p.get_terminal_name(vdi_ip)
            dic = v.get_android_ip_mac()
            assert vdi_ip == p.get_terminal_ip(vdi_ip)
            assert dic['mac'] == p.get_terminal_mac(vdi_ip)
        finally:
            v.vdi_disconnect(vdi_ip)
        logging.info("----------------------------------web云桌面管理A1.3用例结束------------------------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_idv_info_check2(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.18用例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        v = AndroidVdi()
        try:
            v.vdi_connect(vdi_ip)
            client_login('vdi2_01', t_pwd)
            if p.vm_login_success(vdi_ip, 'vdi1_02', 1) == 1:
                v.login('vdi1_02', vdi_ip)
            logging.info("验证vdi终端正常用户信息正常")
            p.search_info('vdi1_02')
            assert p.get_terminal_type(vdi_ip) == u'VDI'
            assert p.get_vm_user_name(vdi_ip) == 'vdi1_02'
            logging.info("验证利旧客户端正常用户信息正常")
            p.search_info('vdi2_01')
            assert p.get_terminal_type('vdi2_01') == u'VDI'
            assert p.get_vm_user_name('vdi2_01') == 'vdi2_01'
            desk_ip = p.get_cloud_desk_ip('vdi2_01')
            logging.info("确认vdi2_01用户winrm可使用")
            logging.info("desk_ip:" + str(desk_ip))
            if win_conn_useful(desk_ip, s_user, s_pwd) == u'winrm可使用':
                logging.info("关闭利旧vdi2_01虚机")
                v.terminal_vm_close(desk_ip, s_user, s_pwd)
            v.terminal_close()
            logging.info("访客登录vdi1_03")
            v.guest_login_set('vdi1_03', t_pwd)
            v.click_guest_login(vdi_ip)
            client_guest_login('vdi2_02', t_pwd)
            logging.info("验证vdi终端访客用户信息正常")
            p.search_info('vdi1_03')
            assert p.get_terminal_type(vdi_ip) == u'VDI'
            assert p.get_vm_user_name(vdi_ip) == 'vdi1_03'
            logging.info("验证利旧客户端访客用户信息正常")
            p.search_info('vdi2_02')
            assert p.get_terminal_type('vdi2_02') == u'VDI'
            assert p.get_vm_user_name('vdi2_02') == 'vdi2_02'
        finally:
            v.vdi_disconnect(vdi_ip)
        logging.info("----------------------------------web云桌面管理A1.18用例结束------------------------------")

    # @pytest.mark.cdm
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_terminal_close(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.8,关机用例开始执行------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     for name in run_user:
    #         logging.info(u"{}用户进行关机操作".format(name))
    #         p.search_info(name)
    #         ip = p.get_terminal_ip(name)
    #         win_conn(ip, suser, syspasswd, 'close')
    #     time.sleep(35)
    #     for name1 in run_user:
    #         p.search_info(name1)
    #         logging.info(u"{}判断用户状态为离线".format(name1))
    #         assert p.get_status(name1) == u'离线'
    #     logging.info("----------------------------------web云桌面管理A1.8,关机用例结束------------------------------")

    @pytest.mark.cdm
    def test_vdi_info_check(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.2,用例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        v = AndroidVdi()
        v.vdi_connect(vdi_android_ip_list[1])
        for name in ['vdi2_01', 'vdi2_02', 'vdi2_03']:
            v.login(name, vdi_android_ip_list[1], '123')
            p.search_info(name)
            logging.info('{}终端连接后判断状态,用户名与实际相符'.format(name))
            assert p.get_user_name(name) == name
            assert p.get_status(name) == u"运行"
            ip = p.get_cloud_desk_ip(vdi_android_ip_list[1])
            if name == 'vdi2_01':
                if win_conn_useful(ip, s_user, s_pwd) == u'winrm可使用':
                    v.terminal_vm_close(ip, s_user, s_pwd)
            elif name == 'vdi2_02':
                v.screen_lock()
        logging.info("判端关机后状态为离线")
        time.sleep(30)
        assert p.get_status('vdi2_01') == u'离线'
        logging.info(u'判断状态是休眠，锁屏10分钟后的状态为{}'.format(p.get_status(name)))
        time.sleep(600)
        assert p.get_status('vdi2_02') == u"休眠"
        logging.info("----------------------------------web云桌面管理A1.2用例结束------------------------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_twouser_logoutone(self, cmd_fixture):
    #     logging.info("----------------------------web云桌面管理A1.4,52用例开始双属性用户退出其中一个30秒后会减少一条记录--------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     v = AndroidVdi()
    #     v.vdi_connect(vdi_android_ip_list[0])
    #     v.login('vdi1_01', vdi_android_ip_list[0], '123')
    #     idv_login(idv_ip_list[1], 'vdi1_01')
    #     p.search_info('vdi1_01')
    #     logging.info("判断初始用有IDv和vdi用户用双重生身份登入")
    #     first_amount = int(p.get_search_amount())
    #     assert first_amount >= 2
    #     p.search_info(idv_ip_list[1])
    #     assert p.get_terminal_type(idv_ip_list[1]) == u'IDV'
    #     assert p.get_status(idv_ip_list[1]) == u'运行'
    #     assert p.get_user_name(idv_ip_list[1]) == 'vdi1_01'
    #     assert get_idv_terminal_name(idv_ip_list[1]) == p.get_terminal_name(idv_ip_list[1])
    #     dic = get_ip_mac(idv_ip_list[1])
    #     assert dic['ip'] == p.get_terminal_ip(idv_ip_list[1])
    #     assert dic['mac'] == p.get_terminal_mac(idv_ip_list[1])
    #     p.search_info(vdi_android_ip_list[0])
    #     assert p.get_terminal_type(vdi_android_ip_list[0]) == u'VDI'
    #     assert p.get_status(vdi_android_ip_list[0]) == u'运行'
    #     assert v.termianl_user_info() == vname
    #     assert v.termianl_name_info() == p.get_terminal_name(vdi_android_ip_list[0])
    #     dic = v.get_android_ip_mac()
    #     assert dic['ip'] == p.get_terminal_ip(vdi_android_ip_list[0]).strip()
    #     assert dic['mac'] == p.get_terminal_mac(vdi_android_ip_list[0]).strip()
    #     ip = p.get_cloud_desk_ip(vdi_android_ip_list[0])
    #     if win_conn_useful(ip, s_user, s_pwd) == u'winrm可使用':
    #         v.terminal_vm_close(ip, s_user, s_pwd)
    #     time.sleep(35)
    #     logging.info("判断有一个用户退出后，查看云桌面用户信息减少一条")
    #     p.search_info('vdi1_01')
    #     assert p.get_status(vdi_android_ip_list[0]) == u'离线'
    #     logging.info("----------------------------------web云桌面管理A1.52用例结束------------------------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_other_manager_check(self, login_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.53/54例开始执行------------------------------")
    #     t = Login(login_fixture)
    #     p = CDeskMange(login_fixture)
    #     t.login(c_user, c_pwd)
    #     t.go_to_vdi_terminal_page()
    #     vd = IdvPage(login_fixture)
    #     vd.chang_vdi_group(vdi_ip, 'vdi1')
    #     vd.back_current_page()
    #     v = AndroidVdi()
    #     v.vdi_connect(vdi_ip)
    #     v.login('vdi1_03', vdi_ip, t_pwd)
    #     for name in admin_user:
    #         t.logout_user()
    #         t.login(name, '123456')
    #         t.goto_cloud_desk_manage()
    #         assert p.get_user_name(vdi_ip) == 'vdi1_03'
    #         assert p.get_terminal_name(vdi_ip) == v.termianl_name_info()
    #         assert p.get_user_group(vdi_ip) == 'vdi1'

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_net_off(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.6例开始执行------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     v = AndroidVdi()
    #     try:
    #         v.vdi_connect(vdi_android_ip_list[0])
    #         if p.get_status('vdi1_01') == u'离线':
    #             v.login('vdi1_01', vdi_android_ip_list[0], '123')
    #         logging.info("{}用户进行断网操作".format('vdi1_01'))
    #         ip = p.get_cloud_desk_ip('vdi1_01')
    #         if win_conn_useful(ip, s_user, s_pwd) == u'winrm可使用':
    #             win_conn(ip, s_user, s_pwd, 'networkoff')
    #         time.sleep(30)
    #         logging.info(u'判断断网，虚机的状态还是运行')
    #         assert p.get_status('vdi1_01') == u'运行'
    #     finally:
    #         v.vdi_disconnect(vdi_android_ip_list[0])
    #     logging.info("----------------------------------web云桌面管理A1.6用例结束------------------------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_ip_fill(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.10,11用例开始执行-----------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     u = UserMange(cmd_fixture)
    #     v = AndroidVdi()
    #     useful_ip = p.get_useful_ip()
    #     v.vdi_connect(vdi_ip)
    #     u.goto_usermanage_page()
    #     u.all_more_operate()
    #     u.click_fill_ip()
    #     logging.info("判断未选择用户信息提示是否正确")
    #     assert u.fill_ip_nouser_info() == u"请选择一条数据"
    #     i = 1
    #     for name in fill_ip_user:
    #         logging.info(u"{}用户进行ip填充操作".format(name))
    #         u.search_info(name)
    #         u.chose_user(name)
    #         if name == "idv2_01":
    #             u.fill_ip_allinfo(useful_ip[i], fmask, fgateway, dns='')
    #         else:
    #             u.fill_ip_allinfo(useful_ip[i], fmask, fgateway, fDNS)
    #         assert u.fill_ip_successinfo() == u"IP填充成功！"
    #         v.login(name, vdi_ip, t_pwd)
    #         logging.info("判断ip填充成功提示消息是否正确")
    #         p.goto_cloud_desk_manage()
    #         logging.info("判断ip填充后30秒ip信息和云桌面ip一致")
    #         p.search_info(name)
    #         assert p.get_cloud_desk_ip(name) == useful_ip[i]
    #         u.goto_usermanage_page()
    #         u.search_info(name)
    #         u.chose_user(name)
    #         u.clear_ip()
    #         time.sleep(30)
    #         v.login(name, vdi_ip, t_pwd)
    #         p.goto_cloud_desk_manage()
    #         logging.info("判断清空ip填充后30秒ip信息和云桌面ip不相同")
    #         assert p.get_cloud_desk_ip(name) != useful_ip[i]
    #         p.search_info(name)
    #         u.goto_usermanage_page()
    #         logging.info("----------------------------------web云桌面管理A1.10,11用例结束-----------------------------")
    #         i = i + 1

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_change_group(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.12-1vdi变更分组用例开始执行------------------")
    #     p = CDeskMange(cmd_fixture)
    #     a = AndroidVdi()
    #     v = IdvPage(cmd_fixture)
    #     v.goto_vdi_terminal_page()
    #     for ip in vdi_chage_user:
    #         v.goto_vdi_terminal_page()
    #         logging.info(u"{}用户进行变更分组操作".format(ip))
    #         v.search_terminal(ip)
    #         v.chang_vdi_group(ip, 'vdi3')
    #         p.goto_cloud_desk_manage()
    #         p.search_info(ip)
    #         if p.terminal_exist(ip) == 0:
    #             a.vdi_connect(ip)
    #             a.login('vdi2_01', ip, t_pwd)
    #         logging.info("判断变更分组后，云桌面管理显示的用户分组是变更后的")
    #         p.search_info(ip)
    #         assert p.get_user_group(ip) == 'vdi3'

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_change_group2(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.12-2idv变更分组用例开始执行------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     v = IdvPage(cmd_fixture)
    #     for ip in idv_chage_user:
    #         v.goto_idv_terminal_page()
    #         logging.info(u"{}用户进行变更分组操作".format(ip))
    #         v.idv_edit_change_group(ip, 'idv3')
    #         time.sleep(3)
    #         p.goto_cloud_desk_manage()
    #         p.search_info(ip)
    #         assert p.get_user_group(ip) == 'idv3'
    #     logging.info("----------------------------------web云桌面管理A1.12-2idv变更分组用例结束------------------------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('ip', [idv_single_ip_list[0], idv_public_ip_list[1], idv_common_ip_list[0]])
    def test_remote_assistance(self, cmd_fixture, ip):
        logging.info("----------------------------------web云桌面管理A1.25，26idv远程协助用例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        p.goto_cloud_desk_manage()
        try:
            # if ip == idv_common_ip_list[0]:
            #     logging.info("公共终端未开启")
            # elif p.vm_login_success(ip,a_25_user,1) == 1:
            #     idv_login(ip, a_25_user, '123')
            #     time.sleep(35)
            p.search_info(ip)
            cip = p.get_cloud_desk_ip(ip)
            p.click_remote_assistance(ip)
            time.sleep(6)
            if p.get_user_name(ip) == u"公用":
                logging.info("判断公用用户，无需虚机接受可自动连接远程协助")
                assert p.get_assistance_info() == u"对方接受了您的远程协助"
            else:
                logging.info("判断远程协助开启后，弹出正在请求对方接受的提示信息")
                assert re.match(u'正在发起远程协助，请稍等... 超时倒计时：\d+秒', p.get_assistance_info()) is not None
                p.back_current_page()
                logging.info("虚机接受远程协助")
                if win_conn_useful(cip, s_user, s_pwd) == u'winrm可使用':
                    win_conn(cip, s_user, s_pwd, u'assistance')
                time.sleep(10)
                logging.info("判断虚机接受远程协助后，返回信息给服务器")
                assert p.get_assistance_info() == u"对方接受了您的远程协助"
        except Exception as error:
            logging.error(error)
        finally:
            p.close_assistance_tool()
            p.click_close_assistion_button()

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_remote_assistance_reject(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.27，28,29远程协助用例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        p.goto_cloud_desk_manage()
        v = AndroidVdi()
        try:
            if p.vm_login_success(vdi_ip, reject_user, 1) == 1:
                v.vdi_connect(vdi_ip)
                v.login(reject_user, vdi_ip, t_pwd)
            p.search_info(reject_user)
            cip = p.get_cloud_desk_ip(reject_user)
            p.click_remote_assistance(reject_user)
            time.sleep(6)
            logging.info("判断远程协助发起")
            assert re.match(u'正在发起远程协助，请稍等... 超时倒计时：\d+秒', p.get_assistance_info()) != None
            if win_conn_useful(cip, s_user, s_pwd) == u'winrm可使用':
                win_conn(cip, s_user, s_pwd, 'reject')
            time.sleep(10)
            logging.info("判断web页面有拒绝提示")
            assert p.get_assistance_info() == u"对方拒绝了您的远程协助"
            p.click_close_assistion_button()
            p.back_current_page()
            p.click_remote_assistance(reject_user)
            time.sleep(185)
            logging.info("远程协助连接超时后判断web页面有超时提示")
            assert p.get_assistance_info() == u"对方无响应，或远程协助客户端工具未安装"
            p.click_close_assistion_button()
            p.back_current_page()
            logging.info("连接超时后再次发起远程协助")
            p.click_remote_assistance(reject_user)
            time.sleep(5)
            logging.info("超时后在次发起远程协助，对方可以接收到弹出窗口并接受")
            win_conn(cip, s_user, s_pwd, 'dialog')
            assert get_win_conn_info(cip, s_user, s_pwd, r"type C:\access.log") == u"exist"
            time.sleep(5)
            win_conn(cip, s_user, s_pwd, 'assistance')
            time.sleep(10)
            logging.info("超时后在次发起远程协助，可再次接受远程成协助，并有信息返回给web页面")
            assert p.get_assistance_info() == u"对方接受了您的远程协助"
        except Exception as error:
            logging.error(error)
        finally:
            p.close_assistance_tool()
            p.click_close_assistion_button()

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_vdi_remote_assistance_virshreboot(self, cmd_fixture):
    #     logging.info(
    #         "----------------------------------web云桌面管理A1.30发起远程协助后重启虚机再次发起用例开始执行------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     v = AndroidVdi()
    #     try:
    #         if p.vm_login_success(vdi_ip, reject_user, 1) == 1:
    #             v.vdi_connect(vdi_ip)
    #             v.login(reject_user, vdi_ip, t_pwd)
    #         p.search_info(reject_user)
    #         cip = p.get_cloud_desk_ip(reject_user)
    #         p.click_remote_assistance(reject_user)
    #         time.sleep(5)
    #         logging.info("开启远程协助后，重启虚机")
    #         if win_conn_useful(cip, s_user, s_pwd) == u'winrm可使用':
    #             win_conn(cip, s_user, s_pwd, "reboot")
    #         if win_conn_useful(cip, s_user, s_pwd) == u'winrm可使用':
    #             p.click_close_assistion_button()
    #             p.back_current_page()
    #             p.click_remote_assistance(reject_user)
    #             logging.info("重启后再次发起远程协助判断有弹出框，并可以正常接受")
    #             win_conn(cip, s_user, s_pwd, "dialog")
    #             time.sleep(5)
    #             assert str(get_win_conn_info(cip, suser, syspasswd, r"type C:\access.log")).strip() == "exist"
    #     except Exception as error:
    #         logging.error(error)
    #     finally:
    #         p.click_close_assistion_button()

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_vdi_remote_assistance_twice(self, cmd_fixture):
        logging.info("----------------------------web云桌面管理A1.31多个用户发起远程协助用例开始执行---------------------")
        p = CDeskMange(cmd_fixture)
        v = AndroidVdi()
        p.goto_cloud_desk_manage()
        try:
            if p.vm_login_success(vdi_ip, accept_user, 1) == 1:
                v.vdi_connect(vdi_ip)
                v.login(accept_user, vdi_ip, t_pwd)
            p.search_info(accept_user)
            ip = p.get_cloud_desk_ip(accept_user)
            p.click_remote_assistance(accept_user)
            if win_conn_useful(ip, s_user, s_pwd) == u'winrm可使用':
                win_conn(ip, s_user, s_pwd, 'assistance')
            time.sleep(15)
            p.open_assistance_tool()
            logging.info("判断成功发起远程协助")
            assert p.get_assistance_info() == u"对方接受了您的远程协助"
            driver = p.open_firefox()
            f = CDeskMange(driver)
            f.goto_cloud_desk_manage()
            f.click_remote_assistance(accept_user)
            time.sleep(5)
            logging.info("判断不能再次发起远程协助")
            assert f.get_assistance_info() == u"远程协助已存在，请稍后重试"
            f.click_close_assistion_button()
            t = Login(driver)
            t.logout_user()
            t.login(c_user2, c_pwd2)
            f.goto_cloud_desk_manage()
            f.click_remote_assistance(accept_user)
            logging.info("判断不能再次发起远程协助")
            time.sleep(5)
            assert f.get_assistance_info() == u"远程协助已存在，请稍后重试"
            driver.quit()
        except Exception as error:
            logging.error(error)
        finally:
            p.close_remot_assistance()
        logging.info("---------------------------web云桌面管理A1.31多个用户发起远程协助用例结束执行--------------------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.parametrize('name', guest_user)
    # def test_vdi_guest_assistance(self, cmd_fixture, name):
    #     logging.info(
    #         "----------------------------------web云桌面管理A1.32,33vdi终端访客登入远程协助测试用例开始------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     l = AndroidVdi()
    #     p.goto_cloud_desk_manage()
    #     if name == 'vdi2_01':
    #         l.vdi_connect(vdi_ip)
    #         l.guest_login_set(name, t_pwd)
    #         l.click_guest_login(vdi_ip)
    #         time.sleep(30)
    #     else:
    #         client_guest_login(name, t_pwd)
    #         time.sleep(30)
    #     p.search_info(name)
    #     p.click_remote_assistance(name)
    #     time.sleep(10)
    #     logging.info("终端{}用户发起远程协助判断可以直接登入不用等待同意".format(name))
    #     assert p.get_assistance_info() == u"对方接受了您的远程协助"
    #     p.close_assistance_tool()
    #     p.click_close_assistion_button()
    #     if name == 'vdi2_01':
    #         l.screen_lock()
    #         time.sleep(3)
    #         l.login(name, vdi_ip, cpasswd)
    #     else:
    #         client_logout()
    #         time.sleep(3)
    #         client_login(name, cpasswd)
    #         time.sleep(30)
    #     time.sleep(5)
    #     p.click_remote_assistance(name)
    #     time.sleep(6)
    #     assert p.get_assistance_info() == u"对方接受了您的远程协助"
    #     p.close_assistance_tool()
    #     p.click_close_assistion_button()
    #     logging.info("--------------------web云桌面管理A1.32,33vdi终端访客登入远程协助测试用例结束---------------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_vdi_guestsleep_assistance(self, cmd_fixture):
    #     logging.info("---------web云桌面管理A1.34vdi终端访客登入在云桌面中等10 分钟后发起远程协助测试用例开始--------")
    #     p = CDeskMange(cmd_fixture)
    #     l = AndroidVdi()
    #     for name in guest_user:
    #         if name == 'vdi2_01':
    #             l.vdi_connect(vdi_ip)
    #             l.set_sleep_time('10分钟')
    #             l.guest_login_set(name, cpasswd)
    #             l.click_guest_login(vdi_ip)
    #         else:
    #             client_sleep_time_set('10')
    #             client_guest_login(name, cpasswd)
    #     time.sleep(610)
    #     for name in guest_user:
    #         if name == 'vdi2_01':
    #             l.click_guest_login(vdi_ip)
    #         else:
    #             click_client_guest_login()
    #         time.sleep(10)
    #         p.click_remote_assistance(name)
    #         time.sleep(6)
    #         assert p.get_assistance_info() == u"对方接受了您的远程协助"
    #         p.close_assistance_tool()
    #         p.click_close_assistion_button()
    #     logging.info("------------web云桌面管理A1.34vdi终端访客登入在云桌面中等10 分钟后发起远程协助测试用例结束----------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_vdi_guestwait10_assistance(self, cmd_fixture):
    #     logging.info("---------------web云桌面管理A1.35vdi终端访客登入锁屏10分钟后发起远程协助测试用例开始----------")
    #     p = CDeskMange(cmd_fixture)
    #     l = AndroidVdi()
    #     for name in guest_user:
    #         if name == 'vdi2_01':
    #             l.vdi_connect(vdi_ip)
    #             l.set_sleep_time('10分钟')
    #             l.guest_login_set(name, cpasswd)
    #             l.click_guest_login(vdi_ip)
    #             time.sleep(10)
    #             l.screen_lock()
    #         else:
    #             client_sleep_time_set('10')
    #             client_guest_login(name, cpasswd)
    #             time.sleep(10)
    #             client_logout()
    #     time.sleep(610)
    #     for name in guest_user:
    #         if name == 'vdi2_01':
    #             l.click_guest_login(vdi_ip)
    #         else:
    #             click_client_guest_login()
    #         time.sleep(10)
    #         p.click_remote_assistance(name)
    #         time.sleep(6)
    #         assert p.get_assistance_info() == u"对方接受了您的远程协助"
    #         p.close_assistance_tool()
    #         p.click_close_assistion_button()
    #     logging.info("-------------web云桌面管理A1.35vdi终端访客登入锁屏10分钟后发起远程协助测试用例结束------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_vdi_guertoguest_assistance(self, cmd_fixture):
        logging.info("----------web云桌面管理A1.36,37vdi终端用户正常登入后再以访客登入发起远程协助测试用例开始-------")
        p = CDeskMange(cmd_fixture)
        v = AndroidVdi()
        v.vdi_connect(vdi_android_ip_list[0])
        if p.terminal_offline(access_user) == 1:
            p.close_chose_user(access_user)
        v.vdi_connect(vdi_android_ip_list[0])
        v.guest_login_set(access_user, t_pwd)
        time.sleep(2)
        v.login(access_user, vdi_android_ip_list[0], t_pwd)
        p.goto_cloud_desk_manage()
        p.search_info(access_user)
        cip = p.get_cloud_desk_ip(access_user)
        p.click_remote_assistance(access_user)
        time.sleep(10)
        logging.info("A1.37首次登入以普通用户登入，发起远程协助需要确认")
        assert re.match(u'正在发起远程协助，请稍等... 超时倒计时：\d+秒', p.get_assistance_info()) is not None
        if win_conn_useful(cip, s_user, s_pwd) == u'winrm可使用':
            win_conn(cip, s_user, s_pwd, "dialog")
            time.sleep(5)
            assert str(get_win_conn_info(cip, s_user, s_pwd, r"type C:\access.log")).strip() == "exist"
        p.click_close_assistion_button()
        p.search_info(access_user)
        cip = p.get_cloud_desk_ip(access_user)
        v.terminal_vm_close(cip, s_user, s_pwd)
        time.sleep(2)
        v.guest_login_set(access_user, t_pwd)
        v.click_guest_login(vdi_android_ip_list[0])
        time.sleep(10)
        p.click_remote_assistance(access_user)
        time.sleep(10)
        logging.info("A1.36首次登入以普通用户登入，关闭虚机在次登入以访客登入发起远程协助不需要确认")
        assert p.get_assistance_info() == u"对方接受了您的远程协助"
        p.close_assistance_tool()
        p.click_close_assistion_button()
        logging.info("-------web云桌面管理A1.36,37vdi终端用户正常登入后再以访客登入发起远程协助测试用例结束---------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_guestlogin_asuser(self, cmd_fixture):
    #     logging.info("----------web云桌面管理A1.38vdi终端访客登入后再关机再正常登入然后远程协助测试用例开始----------")
    #     p = CDeskMange(cmd_fixture)
    #     v = AndroidVdi()
    #     v.vdi_connect(vdi_ip)
    #     if p.terminal_offline(access_user) == 1:
    #         p.close_chose_user(access_user)
    #     v.vdi_connect(vdi_android_ip_list[0])
    #     v.guest_login_set(access_user, t_pwd)
    #     v.click_guest_login(vdi_ip)
    #     time.sleep(2)
    #     v.login(access_user, t_pwd)
    #     p.search_info(access_user)
    #     cip = p.get_cloud_desk_ip(access_user)
    #     p.click_remote_assistance(access_user)
    #     time.sleep(10)
    #     logging.info("终端访客登入后再关机再正常登入然后远程协助需要提示确认")
    #     assert re.match(u'正在发起远程协助，请稍等... 超时倒计时：\d+秒', p.get_assistance_info()) is not None
    #     if win_conn_useful(cip, s_user, s_pwd) == u'winrm可使用':
    #         win_conn(cip, s_user, s_pwd, "dialog")
    #         time.sleep(5)
    #         assert str(get_win_conn_info(cip, s_user, s_pwd, r"type C:\access.log")).strip() == "exist"
    #     logging.info("-------web云桌面管理A1.38vdi终端访客登入后再关机再正常登入然后远程协助测试用例结束------------")

    # @pytest.mark.cdm
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_guestlogin_asuser1(self, cmd_fixture):
    #     """用例需要未升级guesttool"""
    #     logging.info("-----------web云桌面管理A1.39更新后还原用户vdi终端访客登入然后远程协助测试用例开始-------------")
    #     p = CDeskMange(cmd_fixture)
    #     v = AndroidVdi()
    #     v.vdi_connect(vdi_android_ip_list[1])
    #     v.guest_login_set('vdi1_02', '123')
    #     v.click_guest_login(vdi_android_ip_list[1])
    #     p.click_remote_assistance(access_user)
    #     time.sleep(10)
    #     logging.info("终端{}用户发起远程协助判断等待同意".format(access_user))
    #     assert re.match(u'正在发起远程协助，请稍等... 超时倒计时：\d+秒', p.get_assistance_info()) is not None
    #     logging.info("------------web云桌面管理A1.39更新后还原用户vdi终端访客登入然后远程协助测试用例结束-----------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('name', close_user)
    def test_guestlogin_asuser2(self, cmd_fixture, name):
        logging.info("--------------web云桌面管理A1.40，41web更多操作关闭虚机测试用例开始---------------")
        p = CDeskMange(cmd_fixture)
        v = AndroidVdi()
        v.vdi_connect(vdi_ip)
        v.login(name, vdi_ip)
        if name == "vdi2_01":
            time.sleep(2)
            v.screen_lock()
            time.sleep(610)
        p.click_more_operate_close(name)
        logging.info("点击关闭虚机有确认提示")
        assert p.get_web_close_info() == u"确认关闭云桌面？"
        p.click_confirm_close()
        p.send_passwd_confirm(c_pwd)
        logging.info("关成功后有对应的信息提示")
        assert p.web_close_success_info() == u"成功执行关闭虚机1台！"
        flag = 0
        try:
            time.sleep(15)
            result = p.check_device_online(p.get_cloud_desk_ip(name))
            if result:
                # if win_conn_useful(p.get_cloud_desk_ip(name), s_user, s_pwd, 5) == '':
                flag = 1
        except:
            pass
        logging.info("判断终端虚机关闭")
        assert flag == 0
        time.sleep(30)
        assert p.get_status(name) == u'离线'
        p.click_more_operate(name)
        logging.info("判断离线用户的关机按钮不可点击")
        assert p.get_close_attribute() == 'true'
        logging.info("--------------web云桌面管理A1.40，41web更多操作关闭虚机测试用例结束---------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('name',restore_vdi_user)
    def test_vdi_Image_restore(self, cmd_fixture,name):
        p = CDeskMange(cmd_fixture)
        a = AndroidVdi()
        a.vdi_connect(vdi_android_ip_list[3])
        a.login(name, vdi_android_ip_list[3], t_pwd)
        a1 = server_sql_qurey(host_ip,
                              "select stu_name,vm_ip from lb_seat_info where vm_image_id "
                              "in (select id from lb_stu_image where user_name='{0}');".format(name))[0]
        inst_name = a1[0]
        vm_ip = a1[1]
        info = server_conn(host_ip, 'ls /opt/cache/cvm')
        name1 = re.findall(r'.*({}.inst).*'.format(inst_name), info)[0]
        init_size = server_conn(host_ip, "ls -l /opt/cache/cvm/|grep %s |awk '{print $5}'" % name1)
        p.click_more_operate(name)
        if name == 'vdi2_02':
            assert p.judge_cloud_desk_is_clickable() == u'不支持云桌面还原'
        else:
            assert p.judge_cloud_desk_is_clickable() == u'支持云桌面还原'
            if win_conn_useful(vm_ip, s_user, s_pwd) == u'winrm可使用':
                get_win_conn_info(vm_ip, s_user, s_pwd, "echo text>c:/a.text")
            p.click_restore2()
            time.sleep(2)
            assert server_conn(host_ip, "ls -l /opt/cache/cvm/|grep %s |awk '{print $5}'" % name1) != init_size
        logging.info("--------------web云桌面管理A1.42web更多操作vdi云桌面还原测试用例结束---------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('ip', A44_user)
    def test_vdi_Image_restore1(self, cmd_fixture,ip):
        logging.info("--------------web云桌面管理A1.43web更多操作idv云桌面还原测试用例开始---------------")
        p = CDeskMange(cmd_fixture)
        idv_login(ip, A44_bind_user[ip], t_pwd)
        time.sleep(30)
        p.click_more_operate(ip)
        if A44_bind_user[ip] == 'idv1_02':
            logging.info("个性用户支持云桌面还原")
            assert p.judge_cloud_desk_is_clickable() == u'支持云桌面还原'
        else:
            logging.info("还原用户不支持云桌面还原")
            assert p.judge_cloud_desk_is_clickable() == u'不支持云桌面还原'
        logging.info("--------------web云桌面管理A1.43web更多操作idv云桌面还原测试用例结束---------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('ip', A44_user)
    def test_idv_single_restore_cloud_desk(self, cmd_fixture, ip):
        logging.info("--------------web云桌面管理A1.44web更多操作idv云桌面还原测试用例开始---------------")
        p = CDeskMange(cmd_fixture)
        idv_guest_login(ip)
        time.sleep(30)
        p.goto_cloud_desk_manage()
        p.click_more_operate(ip)
        logging.info("单用户终端未绑定用户登入不支持镜像还原")
        assert p.judge_unbinduser_cloud_desk_is_clickable() == u'不支持云桌面还原'
        logging.info("--------------web云桌面管理A1.44web更多操作idv云桌面还原测试用例开始---------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('name', A45_user)
    def test_idv_public_restore_cloud_desk(self, cmd_fixture, name):
        logging.info("--------------web云桌面管理A1.45web更多操作idv云桌面还原测试用例开始---------------")
        p = CDeskMange(cmd_fixture)
        if name == 'idv2_02':
            ip = idv_single_ip_list[1]
        elif name == 'idv1_02':
            ip = idv_single_ip_list[0]
        if p.vm_login_success(ip, name, times=6) == 0:
            pass
        else:
            idv_login(ip, name, t_pwd)
            if p.vm_login_success(ip, name) == 0:
                pass
            else:
                logging.error("用户未登入")
        p.click_more_operate(name)
        if name == 'idv2_02':
            assert p.judge_cloud_desk_is_clickable() == u'不支持云桌面还原'
        elif name == 'idv1_02':
            assert p.judge_cloud_desk_is_clickable() == u'支持云桌面还原'
        logging.info("--------------web云桌面管理A1.45web更多操作idv云桌面还原测试用例开始---------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_idv_public_guest_restore_cloud_desk(self, cmd_fixture):
        logging.info("--------------web云桌面管理A1.46web更多操作idv云桌面还原测试用例开始---------------")
        p = CDeskMange(cmd_fixture)
        v = IdvPage(cmd_fixture)
        i = 1
        for ip in A46_user:
            v.goto_idv_terminal_page()
            v.idv_edit_change_group(ip, 'idv{}'.format(i))
            v.reboot_terminal(ip)
            i = i + 1
            time.sleep(90)
            idv_guest_login(ip)
            time.sleep(30)
            p.goto_cloud_desk_manage()
            p.click_more_operate(ip)
            if i == 2:
                assert p.judge_guest_cloud_desk_is_clickable() == u'不支持云桌面还原'
            else:
                assert p.judge_cloud_desk_is_clickable() == u'不支持云桌面还原'
        logging.info("--------------web云桌面管理A1.46web更多操作idv云桌面还原测试用例开始---------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_idv_common_restore_cloud_desk(self, cmd_fixture):
        logging.info("--------------web云桌面管理A1.47web更多操作idv云桌面还原测试用例开始---------------")
        p = CDeskMange(cmd_fixture)
        v = IdvPage(cmd_fixture)
        v.goto_idv_terminal_page()
        v.idv_edit_change_group(idv_common_ip_list[0], 'idv1')
        v.reboot_terminal(idv_common_ip_list[0])
        v.idv_edit_change_group(idv_common_ip_list[1], 'idv2')
        v.reboot_terminal(idv_common_ip_list[1])
        time.sleep(10)
        p.goto_cloud_desk_manage()
        for ip in A47_user:
            p.click_more_operate(ip)
            if ip == idv_common_ip_list[1]:
                assert p.judge_cloud_desk_is_clickable() == u'不支持云桌面还原'
            else:
                assert p.judge_cloud_desk_is_clickable() == u'支持云桌面还原'

        logging.info("--------------web云桌面管理A1.47web更多操作idv云桌面还原测试用例开始---------------")

    @pytest.mark.cdm1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('name', change_mirror_user)
    def test_mirror_change(self, cmd_fixture, name):
        logging.info("--------------web云桌面管理A1.48修改用户镜像用例开始---------------")
        p = CDeskMange(cmd_fixture)
        u = UserMange(cmd_fixture)
        a = AndroidVdi()
        a.vdi_connect(vdi_android_ip_list[3])
        a.login(name, vdi_android_ip_list[3], t_pwd)
        p.search_info(name)
        user_mirror_before = p.get_terminal_mirror(name)
        time.sleep(3)
        a.terminal_close()
        u.goto_usermanage_page()
        time.sleep(5)
        real_mirror = u.change_mirror(name)
        a.login(name, vdi_android_ip_list[3], t_pwd)
        time.sleep(5)
        p.goto_cloud_desk_manage()
        p.search_info(name)
        user_mirror_after = p.get_terminal_mirror(name)
        logging.info("判断修改镜像后，用户的终端的系统改变")
        logging.info("判断修改镜像后，用户云桌面管理页面的镜像信息改变")
        assert real_mirror == user_mirror_after
        assert user_mirror_before != user_mirror_after
        logging.info("--------------web云桌面管理A1.48修改用户镜像用例结束---------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_funa
    # def test_vdi_terminal_drift(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.50-1vdi终端桌面漂移测试用例开始------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     a = AndroidVdi()
    #     for ip in vdi_terminal:
    #         a.vdi_connect(ip)
    #         a.login(vdi_drift_name, ip, t_pwd)
    #         p.search_info(vdi_drift_name)
    #         logging.info("判断ip信息 是否一致")
    #         dic = a.get_android_ip_mac()
    #         assert p.get_terminal_ip(vdi_drift_name) == dic['ip']
    #         logging.info("判断mac信息 是否一致")
    #         assert p.get_terminal_mac(vdi_drift_name) == dic['mac']
    #         logging.info("判断终端名称信息 是否一致")
    #         assert p.get_terminal_name(vdi_drift_name) == a.termianl_name_info()
    #         a.vdi_disconnect(ip)
    #     logging.info("----------------------------------web云桌面管理A1.50-1vdi终端桌面漂移测试用例结束------------------------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_idv_terminal_drift(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.50-2idv终端桌面漂移测试用例开始------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     for ip in idv_terminal:
    #         idv_login(ip, idv_drif_name, t_pwd)
    #         time.sleep(30)
    #         p.search_info(idv_drif_name)
    #         logging.info("判断ip信息 是否一致")
    #         assert p.get_terminal_ip(idv_drif_name).__contains__(get_ip_mac(ip)["ip"])
    #         logging.info("判断mac信息 是否一致")
    #         assert p.get_terminal_mac(idv_drif_name).__contains__(get_ip_mac(ip)["mac"])
    #         logging.info("判断终端名称信息 是否一致")
    #         assert p.get_terminal_name(idv_drif_name).__contains__(get_idv_terminal_name(ip))
    #     logging.info("----------------------------------web云桌面管理A1.50-2idv终端桌面漂移测试用例结束------------------------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_custom_list(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.16例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        flag_list = p.custom_list()
        logging.info("判断取消勾选所有字段后的剩余选项")
        assert flag_list[0] == 1
        logging.info("判断全选所有字段后的所有选项")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_search_box(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.20例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        flag_list = p.search_box()
        logging.info("判断输入某ip后结果是否为完整记录")
        assert flag_list[0] == 1
        logging.info("判断输入部分用户名后返回结果是否为完整记录")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")
    #
    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_search_box_not_exist(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.21例开始执行------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     flag_list = p.search_box_not_exist()
    #     assert flag_list[0] == 1
    #     logging.info("判断输入特殊字符后的返回结果是否异常")
    #     logging.info("判断未输入任何字符后返回结果是否异常")
    #     assert flag_list[1] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_search_box_sql_injection(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.22例开始执行------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     flag_list = p.search_box_sql_injection()
    #     logging.info("判断输入sql注入语句后返回结果是否异常")
    #     assert flag_list[0] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_pagination_record(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.24例开始执行------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     flag_list = p.pagination_record()
    #     logging.info("判断信息记录是否以10条记录分页")
    #     assert flag_list[0] == 1
    #     logging.info("判断信息记录是否以20条记录分页")
    #     assert flag_list[1] == 1
    #     logging.info("判断信息记录是否以30条记录分页")
    #     assert flag_list[2] == 1
    #     logging.info("判断信息记录是否以50条记录分页")
    #     assert flag_list[3] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_custom_sort_settings(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.13例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        flag_list = p.custom_sort_settings()
        logging.info("判断退出后重新登录自定义列表是否保持不变")
        assert flag_list[0] == 1
        logging.info("判断浏览器清除cookies后再次登录自定义列表是否保持不变")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_custom_sort_rule(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.14例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        flag_list = p.custom_sort_rule()
        logging.info("判断用户名、姓名、用户组递增排序是否正确")
        assert flag_list[0] == 1
        logging.info("判断按IP排序是否正确")
        assert flag_list[1] == 1
        logging.info("判断按状态排序是否正确")
        assert flag_list[2] == 1
        logging.info("判断云桌面MAC、镜像、终端MAC是否无排序功能")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_custom_list_drag(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.15例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        flag_list = p.custom_list_drag()
        logging.info("判断勾选指定字段后列表数目正确")
        assert flag_list[0] == 1
        logging.info("判断可拖动元素有可拖动排序属性")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_list_info_display_1(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.17例开始执行------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     flag_list = p.list_info_display_1()
    #     logging.info("判断用户名元素是否含有tooltip属性")
    #     assert flag_list[0] == 1
    #     logging.info("判断用户名元素是否有width属性")
    #     assert flag_list[1] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.expecial_2
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # def test_search_performance(self, cmd_fixture):
    #     logging.info("----------------------------------web云桌面管理A1.23例开始执行------------------------------")
    #     p = CDeskMange(cmd_fixture)
    #     flag_list = p.search_performance()
    #     logging.info("判断搜索是否在1秒内完成")
    #     assert flag_list[0] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.cdm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_custom_sort_display1(self, cmd_fixture):
        logging.info("----------------------------------web云桌面管理A1.5例开始执行------------------------------")
        p = CDeskMange(cmd_fixture)
        flag_list = p.custom_sort_display1()
        logging.info("判断云主机管理页面是否按照默认排序")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束--------------------------------------------")


if __name__ == "__main__":
    t = time.strftime("%Y-%m-%d %H%M")
    pytest.main(['-m', 'webindex',"-k", "test_search"])
    # pytest.main(["-m", "cdm", "--html", report_dir + "//{0}_testcdm_htmlreport.html".format(t)])
