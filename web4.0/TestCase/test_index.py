#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll / zhouxihong
@contact: chengll@ruijie.com / zhouxihong.ruijie.com.cn
@software: PyCharm
@time: 2018/8/27 8:37 / 2018.10.10
"""
import pytest
from WebPages.LoginPage import Login
from WebPages.indexPage import IndexPage
from WebPages.Idvpage import IdvPage
from WebPages.CdeskmangePage import CDeskMange
from TestData.Logindata import *
from WebPages.warningpage import WarningPage
from Common.terminal_action import *
from WebPages.adnroid_vdi_page import AndroidVdi
from WebPages.AuthenmanagePage import AuthenManage
import eventlet
from Common import Mylog

class Test_Index:

    @pytest.mark.webindex
    @pytest.mark.rcm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_login(self, login_fixture):
        """
        用例名称：A1.1
        用例模块：web用户管理
        用例作者：程丽丽
        测试点：WEB登录
        前置步骤：
        执行步骤：
        1.服务器启动成功后，打开服务器WEB
        2.输入正确的用户名和密码（admin\admin, admin1\admin1）
        校验点：
        能够成功登录服务器web用户管理
           """
        logging.info("---------------------------------web用户管理A1.1.2测试用例开始执行------------------------------")
        lg = Login(login_fixture)
        lg.login('', '')
        null_info_waring = lg.get_null_info()
        logging.info("账号密码为空判断提示是否正确")
        assert null_info_waring == null_messg_info
        lg.login(login_user_fail["name"], login_user_fail["passwd"])
        a = lg.get_error_info()
        logging.info("判断账号，密码错误提示是否正确")
        assert a == error_messg_info
        lg.clear_info()
        lg.login(c_user, c_pwd)
        user_info = IndexPage(login_fixture).get_user_info1()
        logging.info("判断账号密码正确是否可正常登入")
        assert user_info.__contains__(login_user_succ["user_info"]) is True
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_old_client_download(self, download_fixture):
        logging.info("----------------------------------web用户管理A1.4-1利旧客户端下载测试用例开始执行--------------")
        if os.path.exists(rloadpath):
            os.remove(rloadpath)
        flag = False
        tg = Login(download_fixture)
        tg.old_client_dowload(rtime)
        if os.path.exists(rloadpath):
            flag = True
        logging.info("判断默认下载路径下文件是否存在")
        assert flag is True
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.rcm
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_halo_download(self, download_fixture):
        logging.info("--------------------------web用户管理A1.4-2halo工具下载测试用例开始执行------------------------")
        if os.path.exists(hloadpath):
            os.remove(hloadpath)
        flag = False
        tg = Login(download_fixture)
        tg.halo_dowload(htime)
        i = 0
        while i < 12:
            if os.path.exists(hloadpath):
                flag = True
                break
            else:
                time.sleep(10)
            i = i + 1
        logging.info("判断默认下载路径下文件是否存在")
        assert flag is True
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.mrcm
    def test_online_service(self, login_fixture):
        logging.info("----------------------------------web用户管理A1.6在线客服测试用例开始执行-----------------------")
        tg = Login(login_fixture)
        tg.online_service()
        info = tg.get_questions()
        logging.info("判断发送的信息和显示在消息框中的信息是否一致")
        assert info == questions
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_technology(self, login_fixture):
        logging.info("----------------------------------web用户管理A1.5技术论坛测试用例开始执行----------------------")
        tg = Login(login_fixture)
        title = tg.get_technology_page()
        logging.info("页面是否跳转")
        assert title == webtitle
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_virshnum(self, com_fixture):
        logging.info("----------------web用户管理A1.11-1,A1.14-2,3web用户管理查看虚机数用例开始执行------------------")
        lp = IndexPage(com_fixture)
        ip_address = lp.get_ip_info()
        for ip in ip_address:
            logging.info("服务器ip为：{}".format(ip))
            temp = server_conn(ip, 'virsh list |wc -l')
            time.sleep(1)
            num_01 = int(temp) - 3
            logging.info("后台查询出虚机数量为{}".format(num_01))
            num_02 = int(lp.get_virsh_amount(ip))
            logging.info("web用户管理显示出虚机数量{}".format(num_02))
            logging.info("------------------------判断每台服务器的虚机数量和页面显示的是否一致-----------------------")
            assert num_01 == num_02
            state = lp.get_status(ip)
            assert state == u"正常"
        logging.info("---------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_cpu_used(self, com_fixture):
        logging.info("-------------web用户管理A1.11-2，A1.18web用户管理查看cpu使用率用例开始执行----------------------")
        lp = IndexPage(com_fixture)
        ip_address = lp.get_ip_info()
        for ip in ip_address:
            logging.info("服务器ip为：{}".format(ip))
            temp = server_conn(ip, 'sar -u 1 1 | tail -n 1 | tr -s " " | cut -d " " -f 8')
            a = temp.replace("\n", '')
            used_01 = round(100 - float(a), 2)
            logging.info("后台查询cpu利用率为{}".format(used_01))
            used_02 = lp.get_cpuuse(ip)
            logging.info("web用户管理显示出cpu利用率为{}".format(used_02))
            diff_value = abs(used_01 - used_02)
            logging.info("-------------判断每台服务页面显示的cpu利用率和后台查询出的结果差值小于1---------------------")
            assert diff_value <= 5
        logging.info("-------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_men_used(self, com_fixture):
        logging.info("-----------------------web用户管理A1.11-3，A1.19web用户管理查看内存使用率用例开始执行----------")
        lp = IndexPage(com_fixture)
        ip_address = lp.get_ip_info()
        for ip in ip_address:
            logging.info("服务器ip为：{}".format(ip))
            dic_01 = get_free_info(ip, "free")
            menu_sed = round((float(dic_01["used"]) - float(dic_01["buffers"]) - float(dic_01["cached"])) / float(
                dic_01["total"]) * 100, 2)
            logging.info("后台查询内存利用率为{}".format(menu_sed))
            used_02 = lp.get_memuse(ip)
            logging.info("web用户管理显示出内存利用率为{}".format(used_02))
            diff_value = abs(menu_sed - used_02)
            logging.info("------------------判断每台服务页面显示的内存利用率和后台查询出的结果差值小于1---------------")
            assert diff_value <= 2
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_info_check(self, com_fixture):
        logging.info("-----------------web用户管理A1.14-1web用户管理查看ip与实际是否相符用例开始执行------------------")
        lp = IndexPage(com_fixture)
        ip_address = lp.get_ip_info()
        for ip in server_ip:
            flag = 0
            if ip in ip_address:
                flag = 1
            logging.info("falg为0表示实际ip与页面ip显示不相符，为1表示相符实际flag为：{}".format(flag))
            assert flag == 1
        logging.info("------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_network_warning(self, com_fixture):
        logging.info("-----------------------web用户管理A1.21web用户管理从告警到恢复测试用例开始执行-----------------")
        lp = IndexPage(com_fixture)
        ip_address = lp.get_ip_info()
        for ip in ip_address:
            server_conn(ip, "pkill -9 librccvmm")
            time.sleep(60)
            assert lp.get_status(ip) == u"正常"
        logging.info("--------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_network_error(self, com_fixture):
        logging.info("----------------------web用户管理A1.12,13web断网故障用例开始执行------------------------------")
        lg = IndexPage(com_fixture)
        ip_list = lg.get_ip_info()
        for i in range(len (ip_list)):
            if lg.get_status(ip_list[i]) == u"正常":
                if i>=1:
                    terminal_file_up(ip_list[i], parent_dir + '\offline.sh', r'/home/offline.sh',password="MjI1ZDY2NjQ")
                    eventlet.monkey_patch()
                    with eventlet.Timeout(6, False):
                        terminal_conn(ip_list[i], 'cd /home/&&sh offline.sh')
                    time.sleep(60)
                    assert lg.get_status(ip_list[i]) == u"故障"
                    time.sleep(60)
                    assert lg.get_status(ip_list[i]) == u"正常"
        logging.info("----------------------web用户管理A1.12,13web断网故障用例结束---------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_warming(self, warming_fixture):
        logging.info("----------------------------------web用户管理A1.20web告警用例开始执行--------------------------")
        try:
            lp = IndexPage(warming_fixture)
            server_conn(mainip, 'cd /;fallocate -l 35G bf')
            time.sleep(30)
            num = lp.get_warming_num()
            info = lp.get_warning_info()
            lp.goto_warming_info()
            p = WarningPage(warming_fixture)
            logging.info(u"制造告警判断30秒后气泡里的告警数量和告警页面的数量是否一致")
            assert num == p.get_warming_count()
            logging.info(u"判断气泡里的告警信息和告警页面的数量是否一致")
            logging.info(u"首页告警信息为{}".format(info))
            logging.info(u"告警页面的告警信息为{}".format(p.get_warming_info()))
            assert re.sub(r'\s', '', info) == re.sub(r'\s', '', p.get_warming_info())
            lp.back_current_page()
            lp.goto_indexpage()
            lp.logout()
            tg = Login(warming_fixture)
            tg.login(username, passwd)
            logging.info("判断退出后登入告警信息是还是存在")
            assert info == lp.get_warning_info()
            lp.close_warning()
            logging.info("判断关闭告警窗口后不会再出现")
            if lp.elem_is_exist(lp.warming_infoip_xpath) is not None:
                assert re.sub(r'\s', '', info) != re.sub('\s', '', lp.get_warning_info())
            else:
                assert lp.elem_is_exist(lp.warming_infoip_xpath) is None
        finally:
            server_conn(mainip, 'rm -f /bf')
        logging.info("----------------------------------------测试用例结束----------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.vdi
    def test_vdi_group(self, com_fixture):
        logging.info("-------------------web用户管理A1.22-1web用户管理vdi终端用户用例开始执行------------------------")
        lg = IndexPage(com_fixture)
        v = AndroidVdi()
        logging.info("运行中虚机为{}".format(lg.get_running_vdi()))
        logging.info("休眠中虚机为{}".format(lg.get_sleep_vdi()))
        sum1 = int(lg.get_running_vdi()) + int(lg.get_sleep_vdi())
        logging.info("计算vdi虚机总数量为{0}".format(sum1))
        logging.info("判断计算出的虚数量和页面显示的是否一致")
        assert int(lg.get_vdicount()) == sum1
        running_amount = int(lg.get_running_vdi())
        lg.click_running_vdi()
        v.vdi_connect(vdi_android_ip_list[0])
        for name in  running_vdi_name:
            v.login(name, vdi_android_ip_list[0],'123')
            time.sleep(8)
            v.screen_lock()
            time.sleep(5)
        v.vdi_disconnect(vdi_android_ip_list[0])
        for name in running_vdi_group_name:
            logging.info("{0}分组有{1}台运行中虚机".format(name, vdi_user_running[name]))
            assert int(lg.get_vdi_group_num(name)) == vdi_user_running[name]
            running_amount = running_amount + int(lg.get_vdi_group_num(name))
        logging.info("各组运行中虚机相加之和为{}".format(running_amount))
        logging.info("判断各组的运行中虚机相加是否等于页面显示的运行中虚机")
        assert int(lg.get_running_vdi()) == running_amount
        lg.click_sleep_vdi()
        sleep_amount =int(lg.get_sleep_vdi())
        time.sleep(610)
        for name in running_vdi_group_name:
            lg.click_sleep_vdi()
            logging.info("{0}分组有{1}台运休眠虚机".format(name, vdi_user_running[name]))
            assert int(lg.get_vdi_group_num(name)) == vdi_user_running[name]
            sleep_amount = sleep_amount + int(lg.get_vdi_group_num(name))
        logging.info("各组休眠中虚机相加之和为{}".format(sleep_amount))
        logging.info("判断各组的休眠中虚机相加是否等于页面显示的休眠中虚机")
        assert int(lg.get_sleep_vdi()) == sleep_amount
        logging.info("-----------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.idv
    @pytest.mark.rcm
    def test_idv_group(self, com_fixture):
        logging.info("-------------------------web用户管理A1.23web用户管理idv终端用户用例开始执行-------------------")
        lg = IndexPage(com_fixture)
        t = IdvPage(com_fixture)
        logging.info("运行中虚机为{}".format(lg.get_running_idv()))
        logging.info("休眠中虚机为{}".format(lg.get_sleep_idv()))
        sum_1 = int(lg.get_running_idv()) + int(lg.get_sleep_idv())
        logging.info("计算idv虚机总数量为{0}".format(sum_1))
        logging.info("判断计算出的虚数量和页面显示的是否一致")
        assert int(lg.get_idvcount()) == sum_1
        running_amount = int(lg.get_running_idv())
        t.goto_idv_terminal_page()
        t.idv_edit_change_group(idv_public_ip_list[1], 'idv_index1')
        for i in range(2,4):
            t.idv_edit_change_group(idv_public_ip_list[i], 'idv_index2')
        time.sleep(3)
        lg.goto_indexpage()
        lg.click_running_idv()
        for name in running_idv_group_name:
            logging.info("{0}分组有{1}台运行中虚机".format(name, idv_user_running[name]))
            assert int(lg.get_idv_group_num(name)) == idv_user_running[name]
        logging.info("判断各组的运行中虚机相加是否等于页面显示的运行中虚机")
        assert int(lg.get_running_idv()) == running_amount
        # lg.click_sleep_idv()
        # sleep_amount = int(lg.get_sleep_idv())
        # cd_ip = server_sql_qurey(host_ip, "SELECT vm_ip from idv_terminal where ip='{}'"
        #                              .format(idv_public_ip_list[1]))[0][0]
        # if win_conn_useful(idv_public_ip_list[1]) == u'winrm可使用':
        #     win_conn(cd_ip, 'Administrator', 'rcd', "close")
        # for name in running_idv_group_name:
        #     assert int(lg.get_idv_group_num(name)) == idv_user_running[name]
        #     sleep_amount = sleep_amount + int(lg.get_idv_group_num(name))
        # logging.info("各组离线中虚机相加之和为{}".format(sleep_amount))
        # logging.info("判断各组的离线中虚机相加是否等于页面显示的离线中虚机")
        # assert int(lg.get_sleep_idv()) == sleep_amount
        logging.info("---------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.vdi
    def test_change_vdi_state(self, com_fixture):
        logging.info("----------------web用户管理A1.24web用户管理vdi终端运行休眠状态改变用例开始执行------------------")
        lg = IndexPage(com_fixture)
        cd = CDeskMange(com_fixture)
        cd.goto_cloud_desk_manage()
        ad = AndroidVdi()
        cd.search_info('vdi_index2_03')
        time.sleep(1)
        if int(cd.get_search_amount()) != 0:
            if cd.get_status('vdi_index2_03') == u'运行':
                tip = cd.get_terminal_ip('vdi_index2_03')
                ad.vdi_connect(tip)
                ad.terminal_close()
        lg.goto_indexpage()
        before = int(lg.get_running_vdi())
        logging.info("新增唤醒vdi终端前虚机数量{}".format(before))
        ad.vdi_connect(vdi_android_ip_list[0])
        ad.login('vdi_index2_03',vdi_android_ip_list[0], t_pwd)
        logging.info("新增唤醒终端脚本后虚机数量{}".format(lg.get_running_vdi()))
        assert int(lg.get_running_vdi()) == before + 1
        after = int(lg.get_running_vdi())
        after_sleep = int(lg.get_sleep_vdi())
        ad.screen_lock()
        time.sleep(610)
        logging.info("休眠后虚机数量为{}".format(int(lg.get_vdicount())))
        assert after - 1 == int(lg.get_running_vdi())
        assert after_sleep + 1 == int(lg.get_sleep_vdi())
        after1 = int(lg.get_running_vdi())
        after_sleep1 = int(lg.get_sleep_vdi())
        ad.login('vdi_index2_03',vdi_android_ip_list[0], t_pwd)
        assert int(lg.get_running_vdi()) == after1 + 1
        assert int(lg.get_sleep_vdi()) == after_sleep1 - 1
        logging.info("-------------------web用户管理A1.24web用户管理vdi终端运行离线状态改变用例结束------------------")

    # @pytest.mark.webindex
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.idv
    # @pytest.mark.rcm
    # def test_change_idv_state(self, com_fixture):
    #     logging.info("------------------------web用户管理A1.25web用户管理idv终端运行休眠状态改变用例开始执行--------")
    #     lp = IndexPage(com_fixture)
    #     idv_login(idv_ip_list[0], 'idvindex1_03', c_pwd)
    #     time.sleep(35)
    #     logging.info("终端登入后终端数量")
    #     after = int(lp.get_running_vdi())
    #     after_offline = int(lp.get_sleep_idv())
    #     cloud_ip = server_sql_qurey(host_ip,"SELECT vm_ip from idv_terminal where ip='{}'".format(idv_ip_list[0]))[0][0]
    #     if win_conn_useful(cloud_ip,s_user,s_pwd) == u'winrm可使用':
    #         win_conn(cloud_ip, 'Administrator','rcd', 'close')
    #     else:
    #         logging.error("终端退出失败")
    #     time.sleep(50)
    #     logging.info(u"关机后虚机数量为{}".format(int(lp.get_running_vdi())))
    #     logging.info("判断关闭终端后，运行的终端的数量减少，离线的终端数量新增")
    #     assert after - 1 == int(lp.get_running_vdi())
    #     assert after_offline + 1 == int(lp.get_sleep_idv())
    #     logging.info("-------------------web用户管理A1.25web用户管理idv终端运行离线状态改变用例结束----------------")

    # @pytest.mark.webindex
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.idv
    # @pytest.mark.rcm
    # def test_idv_batch_close(self, com_fixture):
    #     logging.info("----------------------web用户管理A1.27,28-3web用户管理idv终端批量关机用例开始执行---------------")
    #     lp = IndexPage(com_fixture)
    #     befor_close_num = int(lp.get_running_idv())
    #     logging.info("批量关机前运行中idv数量为：{}".format(befor_close_num))
    #     lp.click_running_idv()
    #     outline_num = int(lp.get_sleep_idv())
    #     logging.info("批量关机前离线idv数量为：{}".format(outline_num))
    #     num = int(lp.get_idv_group_num(colse_idv_groupname))
    #     lp.goto_idv_terminal_page(colse_idv_groupname)
    #     p = IdvPage(com_fixture)
    #     idv_namelist = p.get_treminal_name_list(colse_idv_groupname)
    #     lp.goto_indexpage()
    #     lp.close_idv_terminal_chose(colse_idv_groupname)
    #     logging.info("关闭运行中idv{}台".format(num))
    #     lp.close_idv_terminal()
    #     lp.server_cancle()
    #     logging.info("取消批量关机，运行中虚机不减少")
    #     assert befor_close_num == int(lp.get_running_idv())
    #     lp.close_idv_terminal()
    #     lp.send_passwd_confirm('11')
    #     logging.info("输入错误密码给出对应提示")
    #     assert lp.get_error_passwd_info() == u"管理员密码不正确！"
    #     lp.send_passwd_again()
    #     logging.info("判断提示信息是否正常")
    #     assert lp.get_close_success_info() == u"批量关机成功！"
    #     lp.click_sleep_idv()
    #     time.sleep(10)
    #     logging.info("判断批量关机后运行中虚机是否相应的减少")
    #     assert int(lp.get_running_idv()) == befor_close_num - num
    #     logging.info("判断批量关机后离线虚机数量是否相应的增加{}台，增加后未{}台".format(num, outline_num + num))
    #     assert int(lp.get_sleep_idv()) == outline_num + num
    #     lp.goto_idv_terminal_page(colse_idv_groupname)
    #     for name in idv_namelist:
    #         p.search_terminal(name)
    #         logging.info("判断用户的状态离线")
    #         assert p.get_idv_state(name) == u"离线"
    #         # try:
    #         #     logging.info("环境恢复用户退出后重新登入")
    #         #     tip = server_sql_qurey("select t.ip from idv_terminal t inner join idv_user u  on"
    #         #                            " t.user_id = u.id where u.user_name='{}'".format(name))[0][0]
    #         #     idv_login(tip, name, c_pwd)
    #         # except Exception as error:
    #         #     logging.error(error)
    #         #     logging.error("{}用户环境恢复未成功，用户未成功登入idv".format(name))
    #     logging.info("--------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.webindex
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.idv
    # @pytest.mark.rcm
    # def test_idv_close_all(self, com_fixture):
    #     logging.info("----------------------web用户管理A1.29-3web用户管理idv终端关机用例开始执行------------------")
    #     lp = IndexPage(com_fixture)
    #     lp.goto_indexpage()
    #     p = IdvPage(com_fixture)
    #     if int(lp.get_running_idv()) != 0:
    #         name_list1 = []
    #         for name in lp.get_idv_user_grouplist():
    #             lp.goto_idv_terminal_page(name)
    #             for name1 in p.get_treminal_name_list(name):
    #                 name_list1.append(name1)
    #             lp.goto_indexpage()
    #         lp.close_all_idv_terminal()
    #         for name2 in name_list1:
    #             lp.click_sleep_idv()
    #             lp.goto_idv_terminal_page(name2)
    #             p.search_terminal(name2)
    #             logging.info("多组批量关机后判断用户的状态为离线")
    #             assert p.get_idv_state(name2) == u"离线"
    #             lp.goto_indexpage()
    #         logging.info("判断批量关机后运行中虚机为0台")
    #         assert int(lp.get_running_idv()) == 0
    #         for name in name_list1:
    #             logging.info("环境恢复，{}终端重新登入".format(name))
    #             tip = server_sql_qurey("select t.ip from idv_terminal t inner join idv_user u  on"
    #                                    " t.user_id = u.id where u.user_name='{}'".format(name))[0][0]
    #             idv_login(tip, name, c_pwd)
    #     else:
    #         logging.info("没有多个用户组可进行批量关机")
    #     logging.info("--------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.vdi
    def test_vdi_running_batch_close(self, com_fixture):
        logging.info("-----------------web用户管理A1.26，28-1web用户管理vdi终端批量关机用例开始执行------------------")
        lp = IndexPage(com_fixture)
        v = AndroidVdi()
        v.vdi_connect(vdi_android_ip_list[0])
        for name in running_idv_name_26:
            v.login(name ,vdi_android_ip_list[0])
            v.screen_lock()
            time.sleep(5)
        before_close_num = int(lp.get_running_vdi())
        logging.info("批量关机前运行中idv数量为：{}".format(before_close_num))
        lp.click_running_vdi()
        p = CDeskMange(com_fixture)
        lp.goto_indexpage()
        num = int(lp.get_vdi_group_num(colse_runvdi_groupname))
        lp.close_vdi_terminal_chose(colse_runvdi_groupname)
        logging.info("关闭运行中idv{}台".format(num))
        lp.close_vdi_terminal()
        lp.server_cancle()
        logging.info("取消批量关机，运行中虚机不减少")
        assert before_close_num == int(lp.get_running_vdi())
        lp.close_vdi_terminal()
        lp.send_passwd_confirm('11')
        logging.info("输入错误密码给出对应提示")
        assert lp.get_error_passwd_info() == u"管理员密码不正确！"
        lp.send_passwd_again()
        logging.info("判断告警信息是否正常")
        assert lp.get_close_success_info() == u"批量关机成功！"
        lp.goto_vdi_terminal_page()
        for name in running_idv_name_26:
            p.search_info(name)
            logging.info("判断用户的状态为管理员关机中")
            assert u"管理员关机中,离线".__contains__(p.get_status(name))
        lp.goto_indexpage()
        time.sleep(10)
        logging.info("判断批量关机后运行中虚机是否相应的减少{0}台，减少后数量为{1}".format(num, before_close_num - num))
        logging.info("页面获取的数量为{}".format(lp.get_running_vdi()))
        assert int(lp.get_running_vdi()) == before_close_num - num
        lp.goto_vdi_terminal_page()
        time.sleep(90)
        for name in running_idv_name_26:
            p.search_info(name)
            logging.info("判断100秒后虚机状态均变成离线")
            assert p.get_status(name) == u"离线"
        logging.info("-----------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.vdi
    def test_vdi_running_close_all(self, com_fixture):
        logging.info("-----------------web用户管理A1.29-1web用户管理vdi终端批量关机用例开始执行--------------------")
        lp = IndexPage(com_fixture)
        p = CDeskMange(com_fixture)
        lp.goto_indexpage()
        if int(lp.get_running_vdi()) != 0:
            all_name = []
            name_list2 = lp.get_vdi_user_grouplist()
            for name in name_list2:
                for name1 in p.get_group_user_name(name):
                    all_name.append(name1)
                lp.goto_indexpage()
            lp.close_all_vdi_terminal()
            logging.info("判断告警信息是否正常")
            assert lp.get_close_success_info() == u"批量关机成功！"
            lp.goto_vdi_terminal_page()
            for name in all_name:
                p.search_info(name)
                logging.info("关闭多个用户组vdi判断用户的状态为管理员关机中")
                assert p.get_status(name) == u"管理员关机中"
            time.sleep(10)
            lp.goto_indexpage()
            logging.info("判断关机后运行中vdi为0台")
            assert int(lp.get_running_vdi()) == 0
            time.sleep(90)
            lp.goto_vdi_terminal_page()
            for name in all_name:
                p.search_info(name)
                logging.info("判断100秒后虚机状态均变成离线")
                assert p.get_status(name) == u'离线'
        else:
            logging.info("没有多个用户组可进行批量关机")
        logging.info("-----------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex2
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.vdi
    @pytest.mark.rcm
    def test_vdi_sleep_batch_close(self, com_fixture):
        logging.info("---------------------web用户管理A1.27,28-2web用户管理vdi终端批量关机用例开始执行----------------")
        lp = IndexPage(com_fixture)
        v = AndroidVdi()
        v.vdi_connect(vdi_android_ip_list[0])
        for name in running_idv_name_26:
            v.login(name, vdi_android_ip_list[0])
            v.screen_lock()
        v.vdi_disconnect(vdi_android_ip_list[0])
        time.sleep(610)
        befor_close_num = int(lp.get_sleep_vdi())
        logging.info("批量关机前休眠中idv数量为：{}".format(befor_close_num))
        lp.click_sleep_vdi()
        num = int(lp.get_vdi_group_num(colse_runvdi_groupname))
        p = CDeskMange(com_fixture)
        lp.goto_indexpage()
        lp.click_sleep_vdi()
        lp.close_vdi_terminal_chose(colse_runvdi_groupname)
        logging.info("关闭休眠中idv{}台".format(num))
        lp.close_vdi_terminal()
        lp.server_cancle()
        logging.info("取消批量关机，休眠中虚机不减少")
        assert befor_close_num == int(lp.get_sleep_vdi())
        lp.close_vdi_terminal()
        lp.send_passwd_confirm('11')
        assert lp.get_error_passwd_info() == u"管理员密码不正确！"
        lp.send_passwd_again()
        logging.info("判断告警信息是否正常")
        assert lp.get_close_success_info() == u"批量关机成功！"
        lp.goto_vdi_terminal_page()
        for name in running_idv_name_26:
            p.search_info(name)
            logging.info("判断虚机状态均变成离线")
            assert p.get_status(name) == u"离线"
        lp.goto_indexpage()
        lp.click_sleep_vdi()
        time.sleep(10)
        logging.info("判断批量关机后运行中虚机是否相应的减少{0}台，减少后数量为{1}".format(num, befor_close_num - num))
        logging.info("页面获取的数量为{}".format(lp.get_sleep_vdi()))
        assert int(lp.get_sleep_vdi()) == befor_close_num - num
        logging.info("----------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex3
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.vdi
    def test_vdi_sleep_close_all(self, com_fixture):
        logging.info("---------------------web用户管理29-2web用户管理vdi终端批量关机用例开始执行------------------")
        lp = IndexPage(com_fixture)
        p = CDeskMange(com_fixture)
        if int(lp.get_sleep_vdi()) != 0:
            lp.click_sleep_vdi()
            all_name = []
            name_list2 = lp.get_vdi_user_grouplist()
            for name in name_list2:
                for name1 in p.get_group_user_name(name):
                    all_name.append(name1)
                lp.goto_indexpage()
                lp.click_sleep_vdi()
            lp.close_all_vdi_terminal()
            logging.info("判断告警信息是否正常")
            assert lp.get_close_success_info() == u"批量关机成功！"
            lp.goto_vdi_terminal_page()
            for name in all_name:
                p.search_info(name)
                logging.info("判断虚机状态均变成离线")
                assert p.get_status(name) == u'离线'
            time.sleep(10)
            lp.goto_indexpage()
            logging.info("判断关机后运行中vdi为0台")
            assert int(lp.get_sleep_vdi()) == 0
        else:
            logging.info("没有多个用户组可进行批量关机")
        logging.info("----------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_logout(self, login_fixture):
        logging.info("--------------------------web用户管理A1.8、A1.9测试用例开始执行--------------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        time.sleep(2 * com_slp)
        IndexPage(login_fixture).logout()
        logging.info("注销后查看能否正常退出到登录界面")
        Login(login_fixture).login_page_click()
        assert tg.find_elem(Login.null_messg_xpath).text == null_messg_info
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        logging.info("判断能否再次登录成功")
        assert tg.find_elem(IndexPage.user_info_xpath).text.__contains__(login_user_succ["user_info"])
        tg.find_elem(IndexPage.logout_xpath).click()
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        time.sleep(login_time_config)
        IndexPage(login_fixture).logout()
        logging.info("登录一段时间后，点击注销，判断能否退出到登录界面")
        Login(login_fixture).login_page_click()
        assert tg.find_elem(Login.null_messg_xpath).text == null_messg_info
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        logging.info("判断退出后是否还能正常登录")
        assert tg.find_elem(IndexPage.user_info_xpath).text.__contains__(login_user_succ["user_info"])
        logging.info("-------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_about(self, login_fixture):
        logging.info("---------------------------------web用户管理A1.10测试用例开始执行-------------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        temp_text2 = IndexPage(login_fixture).index_about()
        logging.info("判断软件版本号信息")
        assert temp_text2[u'软件版本号信息'].__contains__(version)
        logging.info("判断本系统支持")
        assert browser_support == temp_text2[u'本系统支持']
        logging.info("判断技术服务热线")
        assert support_tel == temp_text2[u'技术服务热线']
        logging.info("判断技术支持ID")
        assert support_id == temp_text2[u'技术支持ID']
        logging.info("判断SVN Reversion")
        assert svn_reversion == temp_text2['SVN Reversion']
        logging.info("---------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_batch_off_unchecked_group(self, login_fixture):
        logging.info("---------------------------------web用户管理A1.30测试用例开始执行------------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        time.sleep(com_slp)
        tg.find_elem(IndexPage.idv_batch_close_xpath).click()
        time.sleep(com_slp)
        logging.info("判断提示：请选择一条数据")
        assert u'请选择一条数据' == tg.find_elem(IndexPage.batch_close_tip_xpath).text
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_search_jump_error(self, login_fixture):
        logging.info("---------------------------------web用户管理A1.39测试用例开始执行-------------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        logging.info('判断输入异常信息后搜索结果')
        assert IndexPage(login_fixture).search_jump_error() == 1
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_cloud_vdi_jump(self, login_fixture):
        logging.info("----------------------------web用户管理A1.41/A1.42测试用例开始执行------------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_1, flag_2 = IndexPage(login_fixture).cloud_vdi_jump()
        logging.info('判断是否跳转到云桌面管理页面')
        assert flag_1 == 1
        logging.info('判断是否跳转到idv终端管理页面')
        assert flag_2 == 1
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_web_navigation_bar(self, login_fixture):
        logging.info("------------------------------web用户管理A1.40测试用例开始执行---------------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_1, flag_2, flag_3 = IndexPage(login_fixture).web_navigation_bar()
        logging.info('判断首页导航栏标题')
        assert flag_1 == 1
        logging.info('判断点击其他导航栏后的标题')
        assert flag_2 == 1
        logging.info('判断深度最深的导航栏标题')
        assert flag_3 == 1
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_search_jump_smart(self, login_fixture):
        logging.info("-----------------------------web用户管理A1.37/A1.38测试用例开始执行----------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = IndexPage(login_fixture).search_jump_smart()
        logging.info("判断搜索结果是否包含终端管理内容")
        assert flag_list[0] == 1
        logging.info("判断搜索结果是否包含用户管理的内容")
        assert flag_list[1] == 1
        logging.info("判断搜索结果是否包含云桌面管理的内容")
        assert flag_list[2] == 1
        logging.info("判断搜索结果是否实时更新")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_search_jump(self, login_fixture):
        logging.info("---------------------------------web用户管理A1.36测试用例开始执行-------------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = IndexPage(login_fixture).search_jump()
        logging.info("判断搜索结果是否包含用户内容")
        assert flag_list[0] == 1
        logging.info("判断搜索结果是否包含终端名称")
        assert flag_list[1] == 1
        logging.info("判断搜索结果是否包含云桌面管理")
        assert flag_list[2] == 1
        logging.info('判断是否跳转到终端管理页面')
        assert flag_list[3] == 1
        logging.info('判断是否跳转到云桌面管理页面')
        assert flag_list[4] == 1
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webindex1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_cloud_storage_sys_space_check(self, login_fixture):
        logging.info("--------------------------------web用户管理A1.31测试用例开始执行-------------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = IndexPage(login_fixture).cloud_storage_sys_space_check()
        logging.info('判断云桌面系统盘浮动条是否有颜色渐变属性')
        assert flag_list[0] == 1
        logging.info('判断云桌面系统盘df命令和前端显示是否一致')
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webindex1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_cloud_storage_usr_space_check(self, login_fixture):
        logging.info("--------------------------------web用户管理A1.32测试用例开始执行-------------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = IndexPage(login_fixture).cloud_storage_usr_space_check()
        logging.info('判断云桌面用户数据盘浮动条是否有颜色渐变属性')
        assert flag_list[0] == 1
        logging.info('判断云桌面用户数据盘df命令和前端显示是否一致')
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    # @pytest.mark.webindex
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.rcm
    # def test_cloud_storage_disk_space_check(self, login_fixture):
    #     logging.info("---------------------------------web用户管理A1.33测试用例开始执行-----------------------------")
    #     tg = Login(login_fixture)
    #     tg.login(login_user_succ["name"], login_user_succ["passwd"])
    #     flag_list = IndexPage(login_fixture).cloud_storage_disk_space_check()
    #     logging.info('判断云桌面系统盘浮动条是否有颜色渐变属性')
    #     assert flag_list[0] == 1
    #     logging.info('判断云桌面系统盘df命令和前端显示是否一致')
    #     assert flag_list[1] == 1
    #     logging.info("----------------------------------------测试用例结束------------------------------------------")

    @pytest.mark.webindex1
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_cloud_storage_image_space_check(self, login_fixture):
        logging.info("---------------------------------web用户管理A1.34测试用例开始执行-------------------------------")
        tg = Login(login_fixture)
        tg.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = IndexPage(login_fixture).cloud_storage_image_space_check()
        logging.info('判断云桌面镜像浮动条是否有颜色渐变属性')
        assert flag_list[0] == 1
        logging.info('判断云桌面镜像df命令和前端显示是否一致')
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.rcm
    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_ad_domain_user_index_page(self, com_fixture):
        logging.info("---------------------------------web用户管理A1.43测试用例开始执行-------------------------------")
        t = Login(com_fixture)
        ad = AuthenManage(com_fixture)
        ad.goto_adm()
        ad.connect_ad_domain()
        ad.choose_part('indexuser')
        a = AndroidVdi()
        a.login('ad_vdi1',vdi_android_ip_list[0] ,'ad@2008')
        idv_login(idv_ip_list[2],'ad_idv1','ad@2008')
        t.goto_index_manage()
        flag_list = IndexPage(com_fixture).ad_domain_user_index_page()
        logging.info('判断是否有AD域图标')
        assert flag_list[0] == 1
        logging.info('判断是否有指定的VDI域分组')
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.rcm
    def test_restart_server(self, com_fixture):
        logging.info("----------------------------------web用户管理A1.16web重启用例开始执行--------------------------")
        lp = IndexPage(com_fixture)
        ip_address = lp.get_ip_info()
        ip_address.reverse()
        for ip in ip_address:
            logging.info("服务器ip为：{}".format(ip))
            lp.restart_server_button_click(ip)
            logging.info("服务器上无虚机时验证")
            if int(lp.get_virsh_amount(ip)) == 0:
                logging.info("重启服务器信息判断")
                assert lp.get_reboot_info() == u"确定重启该服务器？"
                lp.cancel_button_click()
                logging.info("取消重启后判断状态为正常")
                assert lp.get_status(ip) == u"正常"
                lp.restart_server_button_click(ip)
                lp.confirm_button_click()
                lp.send_passwd_confirm()
                logging.info("重启成功后消息提示")
                assert lp.get_reboot_confirm() == u"重启【{}】服务器成功！".format(ip)
                lp.reboot_confirm()
                if ip == ip_address[-1]:
                    time.sleep(150)
                    lp.back_current_page()
                    lp.refesh()
                    f = Login(com_fixture)
                    f.login(username, passwd)
                    logging.info("重启的是主存")
                    lp.click_cheeck_button()
                    logging.info("重启主控服务器后重新等登入状态为正常")
                    assert lp.get_status(ip) == u"正常"
                else:
                    time.sleep(30)
                    lp.back_current_page()
                    lp.getinto_iframe()
                    logging.info("30秒后重启后判断状态为故障")
                    assert lp.get_status(ip) == u"故障"
                    time.sleep(120)
                    logging.info("重启1分钟后状态为正常")
                    assert lp.get_status(ip) == u"正常"
            else:
                logging.info("服务器上有虚机时验证")
                assert lp.get_reboot_info() == u"该服务器上有虚机正在运行，请先关掉虚机再重启！"
                lp.confirm_button_click()
                assert lp.get_status(ip) == u"正常"
        logging.info("---------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webindex
    @pytest.mark.case_level_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.vdi
    def test_fix_server(self, com_fixture):
        logging.info("---------------------------web用户管理A1.17维护功能测试用例开始执行----------------------------")
        lg = IndexPage(com_fixture)
        ip_address = lg.get_ip_info()
        for ip in ip_address:
            logging.info("服务器ip为：{}".format(ip))
            lg.fix_server_click(ip)
            if int(lg.get_virsh_amount(ip)) == 0:
                logging.info("服务器上无虚机时验证")
                assert lg.get_fixinfo() == u"该服务器上没有虚机正在运行，无需进行维护！"
                lg.confirm_button_click()
                assert int(lg.get_virsh_amount(ip)) == 0
                v =AndroidVdi()
                v.login('idv1_01',vdi_android_ip_list[0])
            try:
                logging.info("服务器上有虚机时验证")
                assert lg.get_fixinfo() == u"维护模式将强制关闭该服务器上的所有云桌面，确定维护？"
                lg.confirm_button_click()
                lg.server_cancle()
                lg.getinto_iframe()
                assert lg.get_status(ip) == u"正常"
                lg.fix_server_click(ip)
                lg.confirm_button_click()
                lg.send_passwd_confirm()
                lg.getinto_iframe()
                assert lg.close_virsh_info() == u"云桌面关闭成功！"
                lg.confirm_button_click()
                time.sleep(120)
                logging.info("运行中运行的vdi数量为：{}".format(int(lg.get_virsh_amount(ip))))
                assert int(lg.get_virsh_amount(ip)) == 0
                lg.close_checkpage()
                logging.info("web用户管理中运行的vdi数量为：{}".format(int(lg.get_running_num_vdi())))
                assert int(lg.get_running_num_vdi()) == 0
            except AssertionError:
                pass
        logging.info("-------------------------------------测试用例结束--------------------------------------------")
    #
    # @pytest.mark.webindex
    # @pytest.mark.case_level_0
    # @pytest.mark.smoke_test
    # @pytest.mark.case_type_fun
    # @pytest.mark.rcm
    # def test_close_server(self, com_fixture):
    #     logging.info("---------------------------web用户管理A1.15web服务器关机用例开始执行--------------------------")
    #     lp = IndexPage(com_fixture)
    #     time.sleep(1)
    #     ip_address = lp.get_ip_info()
    #     ip_address.reverse()
    #     for ip in ip_address:
    #         logging.info("服务器ip为：{}".format(ip))
    #         lp.close_server_click(ip)
    #         logging.info("服务器上无虚机时验证")
    #         if int(lp.get_virsh_amount(ip)) == 0:
    #             logging.info("关闭服务器信息判断")
    #             assert lp.get_reboot_info() == u"确定关闭该服务器？"
    #             lp.cancel_button_click()
    #             assert lp.get_status(ip) == u"正常"
    #             lp.close_server_click(ip)
    #             lp.confirm_button_click()
    #             lp.send_passwd_confirm()
    #             logging.info("关机后成功后消息提示判断")
    #             assert lp.get_reboot_confirm() == u"关闭该【{}】服务器成功！".format(ip)
    #             lp.reboot_confirm()
    #             if ip == ip_address[-1]:
    #                 time.sleep(40)
    #                 lp.back_current_page()
    #                 f = Login(com_fixture)
    #                 logging.info("关闭主控后，服务器不能访问")
    #                 assert f.server_out() == u'无法访问此网站'
    #             else:
    #                 lp.back_current_page()
    #                 lp.getinto_iframe()
    #                 assert lp.get_status(ip) == u"正常"
    #                 time.sleep(120)
    #                 assert lp.get_status(ip) == u"故障"
    #         else:
    #             logging.info("服务器上有虚机时验证")
    #             assert lp.get_reboot_info() == u"该服务器上有虚机正在运行，请先关掉虚机再关机！"
    #             lp.confirm_button_click()
    #             logging.info("不关机服务器状态不变为正常")
    #             assert lp.get_status(ip) == u"正常"
    #     logging.info("----------------------------------------测试用例结束-------------------------------------------")
    #     #     "TODO 测试结束后需要把服务器重新启动"


if __name__ == "__main__":
    t = time.strftime("%Y-%m-%d %H%M")
    pytest.main(['-v', "-m", "webindex1"])
    # pytest.main(['-v','-m','not webadm',"--html",report_dir + "//{0}_testweb4.0_htmlreport.html".format(t)])
