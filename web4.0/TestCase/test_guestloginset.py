#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2019/3/12 14:30
"""
import pytest
import eventlet

from TestData.Terminalmangerdata import image_name1
from WebPages.Idvpage import IdvPage
from Common.terminal_action import *
from Common.file_dir import *
from TestData.basicdata import *

class Test_GuestLoginSet:

    @pytest.mark.webguest
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    # @pytest.mark.parametrize('name', idv_ip1)
    @pytest.mark.test_gust_login
    def test_web_guest_set_a1_1(self, idv_fixture):
        """
        执行步骤：
        1、在主控web上，进入IDV终端管理-多用户终端-未分组，选择在线终端A，点击修改，开启访客登录功能，查看终端登录页面变化
        2、在终端A上，点击访客登录，查看登录情况
        3、退出访客登录，使用用户名/密码登录成功
        1.6用例步骤
        1、终端列表下选择开启访客功能的终端，查看终端详情页面
        预期结果：
        1、终端增加访客登录入口
        2、访客登录成功
        3、使用用户名/密码登录成功
        1.6用例预期结果
        1、开启访客值为是
        """
        logging.info(u"=================web访客登入权限设置用例A1.1/6-1开始==============================")
        p = IdvPage(idv_fixture)
        idv_ip1 = idv_public_ip_list[0]
        get_dev_status = "cat /opt/lessons/RCC_Client/dev_status.ini "
        try:
            p.click_guest_login_set(idv_ip1)  # 启用终端访客登录
            # 重启终端
            p.reboot_terminal(idv_ip1)
            p.wait_tm_reboot_success(idv_ip1, 1)  # 等待终端重启成功
            idv_initialization_click(idv_ip1)
            idv_pattern_chose(idv_ip1)
            time.sleep(3)
            logging.info("判断开启访客登入权限，终端登入页面有访客登入按钮")
            assert idv_guest_login_open(idv_ip1) == u'访客登入按钮开启'
            idv_guest_login(idv_ip1)
            time.sleep(90)
            logging.info("判断后台终端不处于锁屏界面")
            info = terminal_conn(idv_ip1, get_dev_status)
            assert "locked                         = 0" in info
            # 重启终端，用户正常登录
            p.reboot_terminal(idv_ip1)
            p.wait_tm_reboot_success(idv_ip1, 1)  # 等待终端重启成功
            idv_login(idv_ip1, 'idv1_02', '123')
            time.sleep(90)
            logging.info("判断后台终端不处于锁屏界面")
            info = terminal_conn(idv_ip1, get_dev_status)
            assert "locked                         = 0" in info
            logging.info("A1.6用例验证")
            p.driver.refresh()
            p.search_terminal(idv_ip1)
            assert p.get_idv_guest_set_info(idv_ip1) == u'启用'
        finally:
            try:
                p.driver.refresh()
                p.reboot_terminal(idv_ip1)
                p.wait_tm_reboot_success(idv_ip1, 1)
            except Exception as e:
                logging.info(u"重启失败")
        # p.search_terminal(name)
        # tip = p.get_idv_ip(name)
        # dip = p.get_idv_desk_ip(name)
        # if judje_idv_vm_is_running(name) == 0:
        #     if win_conn_useful(dip, 'Administrator', 'rcd') == u'winrm可使用':
        #         win_conn(dip, 'Administrator', 'rcd', 'logout')
        #         if idv_in_login_page2(tip) == 1:
        #             pass
        # else:
        #     terminal_reboot(tip)
        #     time.sleep(5)
        # logging.info("判断开启访客登入权限，终端登入页面有访客登入按钮")
        # assert idv_guest_login_open(tip) == u'访客登入按钮开启'
        # idv_guest_login(tip)
        # logging.info("判断访客是否登入成功")
        # assert win_conn_useful(dip, 'Administrator', 'rcd') == u'winrm可使用'
        # win_conn(dip, 'Administrator', 'rcd', 'logout')
        # if idv_in_login_page2(tip) == 1:
        #     idv_login(tip, 'idv1_02', '123')
        #     logging.info("判断正常用户可正常登入")
        #     assert judge_ip_is_used(dip) == u'ip可用'
        # logging.info("A1.6用例验证")
        # assert p.get_idv_guest_set_info(name) == u'启用'
        logging.info(u"=================web访客登入权限设置用例A1.1/6-1开始==============================")

    @pytest.mark.webguest
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    # @pytest.mark.parametrize('name', idv_ip1)
    def test_web_guest_set_a1_2(self, idv_fixture):
        """
        执行步骤：
        1、在主控web上，进入IDV终端管理-多用户终端-未分组，选择离线终端A，点击修改，开启访客登录功能，查看终端登录页面变化
        2、终端A恢复在线，查看终端A变化，点击访客登录，查看登录情况
        预期结果：
        1、离线时开启访客登录，终端无访客登录入口。使用脱网登录成功
        2、终端恢复在线后，终端增加访客登录入口，访客登录成功
        """
        logging.info(u"=================web访客登入权限设置用例A1.2开始==============================")
        p = IdvPage(idv_fixture)
        idv_ip1 = idv_public_ip_list[0]
        get_dev_status = "cat /opt/lessons/RCC_Client/dev_status.ini "
        p.click_guest_login_set(idv_ip1)
        # 重启终端
        p.reboot_terminal(idv_ip1)
        p.wait_tm_reboot_success(idv_ip1, 1)  # 等待终端重启成功
        idv_initialization_click(idv_ip1)
        idv_pattern_chose(idv_ip1)
        time.sleep(3)
        logging.info(u"判断开启访客登入权限，终端登入页面有访客登入按钮")
        assert idv_guest_login_open(idv_ip1) == u'访客登入按钮开启'
        idv_guest_login(idv_ip1)
        time.sleep(90)
        logging.info(u"判断后台终端不处于锁屏界面")
        info = terminal_conn(idv_ip1, get_dev_status)
        assert "locked                         = 0" in info
        # p.go_main_iframe()
        # if judje_idv_vm_is_running(idv_ip1) == 0:
        #     if win_conn_useful(p.get_idv_desk_ip(idv_ip1), 'Administrator', 'rcd') == u'winrm可使用':
        #         win_conn(p.get_idv_ip(idv_ip1), 'Administrator', 'rcd', 'logout')
        #     if idv_in_login_page2(p.get_idv_ip(idv_ip1)) == 1:
        #         terminal_file_up(p.get_idv_ip(idv_ip1), parent_dir + '\offline.sh', r'Documents/offline.sh')
        #         eventlet.monkey_patch()
        #         with eventlet.Timeout(6, False):
        #             terminal_conn(p.get_idv_ip(idv_ip1), 'cd Documents/&&sh offline.sh')
        #         p.click_guest_login_set(idv_ip1, chose_type=u'启用')
        #         if judge_ip_is_used(p.get_idv_ip(idv_ip1)) == u'ip可用':
        #             assert idv_guest_login_open(p.get_idv_ip(idv_ip1)) == u'访客登入按钮开启'
        # else:
        #     logging.error("终端离线不可使用，请确认终端是否开启，网络是否连接")
        logging.info(u"=================web访客登入权限设置用例A1.2结束==============================")

    @pytest.mark.webguest
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    # @pytest.mark.parametrize('name', idv_ip1)
    def test_web_guest_set_a1_3(self, idv_fixture):  #, name)
        """
        执行步骤：
        1.3用例步骤
        1、在主控web上，进入IDV终端管理-多用户终端-未分组，选择在线终端A，点击修改，关闭访客登录功能，查看终端登录页面变化
        1.6用例步骤
        2、终端列表下选择关闭访客功能的终端，查看终端详情页面
        预期结果：
        1.3用例预期结果
        1、终端去掉访客登录入口
        1.6用例预期结果
        2、开启访客值为否
        """
        logging.info(u"=================web访客登入权限设置用例A1.3/6-2开始==============================")
        p = IdvPage(idv_fixture)
        idv_ip1 = idv_public_ip_list[0]
        p.click_guest_login_set(idv_ip1, chose_type=u'禁用')
        p.back_current_page()
        p.reboot_terminal(idv_ip1)
        p.wait_tm_reboot_success(idv_ip1, 1)
        if idv_in_login_page2(idv_ip1) == 1:
            logging.info("判断不开启访客登入权限，终端登入页面没有访客登入按钮")
            assert idv_guest_login_open(idv_ip1) == u'访客登入按钮未开启'
        logging.info("A1.6用例验证")
        assert p.get_idv_guest_set_info(idv_ip1) == u'禁用'
        logging.info(u"=================web访客登入权限设置用例A1.3/6-2结束==============================")

    @pytest.mark.webguest
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    # @pytest.mark.parametrize('name', idv_ip1)
    def test_web_guest_set_a1_4(self, idv_fixture):  # , name
        """
        执行步骤：
        1.4用例步骤
        1、在主控web上，进入IDV终端管理-多用户终端-未分组，选择离线终端A，点击修改，关闭访客登录功能，查看终端登录页面变化
        2、终端A恢复在线，查看终端A登录页面变化
        预期结果：
        1、离线时关闭访客登录，终端仍然有访客登录入口，且登录成功
        2、终端恢复在线后，终端去掉访客登录入口，且使用用户名/密码登录成功
        """
        logging.info(u"=================web访客登入权限设置用例A1.4开始==============================")
        p = IdvPage(idv_fixture)
        idv_ip1 = idv_public_ip_list[0]
        get_dev_status = "cat /opt/lessons/RCC_Client/dev_status.ini"
        # 重启终端，用户正常登录
        p.click_guest_login_set(name=idv_ip1, chose_type=u'禁用')
        p.reboot_terminal(idv_ip1)
        p.wait_tm_reboot_success(idv_ip1, 1)  # 等待终端重启成功
        if idv_in_login_page2(idv_ip1) == 1:
            logging.info(u"判断不开启访客登入权限，终端登入页面没有访客登入按钮")
            assert idv_guest_login_open(idv_ip1) == u'访客登入按钮未开启'
        idv_login(idv_ip1, 'idv1_02', '123')
        time.sleep(90)
        logging.info(u"判断后台终端不处于锁屏界面")
        info = terminal_conn(idv_ip1, get_dev_status)
        assert "locked                         = 0" in info
        # if p.get_idv_state(idv_ip1) == u'在线':
        #     if win_conn_useful(p.get_idv_desk_ip(idv_ip1), 'Administrator', 'rcd') == u'winrm可使用':
        #         win_conn(p.get_idv_ip(idv_ip1), 'Administrator', 'rcd', 'logout')
        #     if idv_in_login_page2(p.get_idv_ip(idv_ip1)) == 1:
        #         terminal_file_up(p.get_idv_ip(idv_ip1), parent_dir + '\offline.sh', r'Documents/offline.sh')
        #         eventlet.monkey_patch()
        #         with eventlet.Timeout(6, False):
        #             terminal_conn(p.get_idv_ip(idv_ip1), 'cd Documents/&&sh offline.sh')
        #         p.click_guest_login_set(idv_ip1, chose_type=u'禁用')
        #         if judge_ip_is_used(p.get_idv_ip(idv_ip1)) == u'ip可用':
        #             assert idv_guest_login_open(p.get_idv_ip(idv_ip1)) == u'访客登入按钮未开启'
        # else:
        #     logging.error("终端离线不可使用，请确认终端是否开启，网络是否连接")
        logging.info(u"=================web访客登入权限设置用例A1.4结束==============================")

    @pytest.mark.webguest
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    # @pytest.mark.parametrize('name', [u'未分组'])
    def test_web_guest_set_a1_7(self, idv_fixture):
        """
        执行步骤：
        1、进入主控web，管理胖终端
        2、选择在线、离线多个胖终端，在【更多-访客登录设置】下批量开启访客登录
        3、到终端查看是否有访客登录入口
        预期结果：
        1、不管原来是否开启访客登录，所选终端均被设置为开启访客登录
        2、在线终端上有访客登录入口，离线终端原来没有访客登录入口的则恢复在线后有访客登录入口
        3、各种终端的访客登录成功、使用账号密码登录成功
        """
        logging.info(u"=================web访客登入权限设置用例A1.7开始==============================")
        p = IdvPage(idv_fixture)
        idv_ip1 = idv_public_ip_list[0]
        idv_ip2 = idv_public_ip_list[1]
        try:
            # 创建分组，搜索终端，将终端移动该分组下并开启访客登录权限
            p.del_gp_exist("gust_login")
            p.idv_creat_group(name="gust_login", img_name=image_name1)
            p.modify_idv(tm_name=idv_ip1, tm_group="gust_login")
            p.modify_idv(tm_name=idv_ip2, tm_group="gust_login")
            p.click_guest_login_set("gust_login", chose_user=2, chose_type=u'开启')
            # 重启终端，回到登录页面
            p.reboot_terminal(idv_ip1)
            p.wait_tm_reboot_success(idv_ip1, 1)  # 待终端重启成功
            idv_initialization_click(idv_ip1)
            idv_pattern_chose(idv_ip1)  # 预留镜像变更后下载镜像时间，等待到登录页面
            p.reboot_terminal(idv_ip1)  # 再次重启分辨率正常
            p.wait_tm_reboot_success(idv_ip1, 1)  # 待终端重启成功
            if idv_in_login_page(idv_ip1) == 1:
                logging.info(u"判断开启访客登入权限，终端登入页面有访客登入按钮")
                assert idv_guest_login_open(idv_ip1) == u'访客登入按钮开启'
            # 重启终端，回到登录页面
            p.reboot_terminal(idv_ip2)
            p.wait_tm_reboot_success(idv_ip2, 1)  # 待终端重启成功
            idv_initialization_click(idv_ip2)
            idv_pattern_chose(idv_ip2)  # 预留镜像变更后下载镜像时间，等待到登录页面
            p.reboot_terminal(idv_ip2)  # 再次重启分辨率正常
            p.wait_tm_reboot_success(idv_ip2, 1)  # 待终端重启成功
            if idv_in_login_page(idv_ip2) == 1:
                logging.info(u"判断开启访客登入权限，终端登入页面有访客登入按钮")
                assert idv_guest_login_open(idv_ip2) == u'访客登入按钮开启'
        finally:
            p.driver.refresh()
            p.del_gp_exist("gust_login")
        # try:
        #     off_line = p.get_offline_tm()[0]  # 获取离线终端
        #     p.search_terminal(off_line)
        #     off_line_ip = p.get_idv_ip(off_line)
        #     p.reboot_terminal(off_line_ip)
        #     p.wait_tm_reboot_success(off_line_ip)

        # group_ip_dic = p.get_group_all_user(name)
        # p.click_guest_login_set(name, chose_user=2, chose_type=u'开启')
        # for key, vaule in group_ip_dic.items():
        #     win_conn(vaule, 'Administrator', 'rcd', 'logout')
        #     if idv_in_login_page(key) == 1:
        #         logging.info("判断不开启访客登入权限，终端登入页面没有访客登入按钮")
        #         assert idv_guest_login_open(key) == u'访客登入按钮开启'
        logging.info(u"=================web访客登入权限设置用例A1.7结束==============================")

    @pytest.mark.webguest
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    # @pytest.mark.parametrize('name', [u'未分组'])
    def test_web_guest_set_a1_8(self, idv_fixture):
        """
        执行步骤：
        1、进入主控web，管理胖终端
        2、选择在线、离线多个胖终端，在【更多-访客登录设置】下批量关闭访客登录
        3、到终端查看是否有访客登录入口
        预期结果：
        1、不管原来是否开启访客登录，所选终端均被设置为关闭访客登录
        2、在线终端上没有访客登录入口，离线终端没有访客登录入口，恢复在线后有访客登录入口
        3、各终端使用账号密码登录成功
        """
        logging.info(u"=================web访客登入权限设置用例A1.8开始==============================")
        p = IdvPage(idv_fixture)
        idv_ip1 = idv_public_ip_list[0]
        idv_ip2 = idv_public_ip_list[1]
        try:
            # 创建分组，搜索终端，将终端移动该分组下并开启访客登录权限
            p.del_gp_exist("gust_login")
            p.idv_creat_group(name="gust_login", img_name=image_name1)
            p.modify_idv(tm_name=idv_ip1, tm_group="gust_login")
            p.modify_idv(tm_name=idv_ip2, tm_group="gust_login")
            p.click_guest_login_set("gust_login", chose_user=2, chose_type=u'禁用')
            # 重启终端，回到登录页面
            p.reboot_terminal(idv_ip1)
            p.wait_tm_reboot_success(idv_ip1, 1)  # 待终端重启成功
            idv_initialization_click(idv_ip1)
            idv_pattern_chose(idv_ip1)  # 预留镜像变更后下载镜像时间，等待到登录页面
            p.reboot_terminal(idv_ip1)  # 再次重启分辨率正常
            p.wait_tm_reboot_success(idv_ip1, 1)  # 待终端重启成功
            if idv_in_login_page(idv_ip1) == 1:
                logging.info(u"判断不开启访客登入权限，终端登入页面没有访客登入按钮")
                assert idv_guest_login_open(idv_ip1) == u'访客登入按钮未开启'
            # 重启终端，回到登录页面
            p.reboot_terminal(idv_ip2)
            p.wait_tm_reboot_success(idv_ip2, 1)  # 待终端重启成功
            idv_initialization_click(idv_ip2)
            idv_pattern_chose(idv_ip2)  # 预留镜像变更后下载镜像时间，等待到登录页面
            p.reboot_terminal(idv_ip2)  # 再次重启分辨率正常
            p.wait_tm_reboot_success(idv_ip2, 1)  # 待终端重启成功
            if idv_in_login_page(idv_ip2) == 1:
                logging.info(u"判断不开启访客登入权限，终端登入页面没有访客登入按钮")
                assert idv_guest_login_open(idv_ip2) == u'访客登入按钮未开启'
        finally:
            p.driver.refresh()
            p.del_gp_exist("gust_login")
        # p = IdvPage(idv_fixture)
        # group_ip_dic = p.get_group_all_user(name)
        # p.click_guest_login_set(name, chose_user=2, chose_type=u'禁用')
        # for key, value in group_ip_dic.items():
        #     if idv_in_login_page(key) == 0:
        #         win_conn(value, 'Administrator', 'rcd', 'logout')
        #     if idv_in_login_page2(key) == 1:
        #         logging.info("判断不开启访客登入权限，终端登入页面没有访客登入按钮")
        #         assert idv_guest_login_open(key) == u'访客登入按钮未开启'
        logging.info(u"=================web访客登入权限设置用例A1.8结束==============================")

    @pytest.mark.webguest
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_web_guest_set_a1_9(self, vdi_fixture):
        """
        执行步骤：
        1、在主控web上，进入IDV终端管理-多用户终端-未分组，选择在线终端A，点击修改，关闭访客登录功能，查看终端登录页面变化
        预期结果：
        1、终端去掉访客登录入口
        """
        logging.info(u"=================web访客登入权限设置用例A1.9开始==============================")
        p = IdvPage(vdi_fixture)
        logging.info(u"瘦终端不存在访客登入权限设置按钮")
        assert p.vdi_page_exist_guest_set_button() == 1
        logging.info(u"=================web访客登入权限设置用例A1.9结束==============================")


if __name__ == "__main__":
    # pytest.main(["-m", "webguest1"])
    # pass
    # idv_guest_login_open('172.21.204.16')
    t = time.strftime("%Y-%m-%d %H%M")
    pytest.main(["-m", "webguest", "--html", report_dir + "//{0}_webguest_htmlreport.html".format(t)])
    # pytest.main(['-vv','-s', '-m', 'webguest1'])
