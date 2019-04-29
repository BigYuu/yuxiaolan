#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chenyilin
@contact: chenyilin@ruijie.com
@software: PyCharm
@time: 2019/03/05 12:27
"""
import random

import pytest
from uiautomation import Keys

from Common.serverconn import *
from TestData.Printermangerdata import *
from Common import file_dir
from TestCase.conftest import login_fixture
from TestData.Printermangerdata import *

from TestData.Logindata import *

from WebPages.LoginPage import Login
from WebPages.PrinterPage import *
from WebPages.adnroid_vdi_page import AndroidVdi


class Test_PrinterMange:

    @pytest.mark.printer
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_delete_printer_without_choose_printer(self, com_fixture):
        """
        测试点：web-打印机配置管理-删除-未选中目标
        操作步骤：未中删除目标，选中删除时。
        校验点：1、有错误提示”未选中删除目标“，自动消失。
                2、所有配置信息在配置信息列表中。
        """
        logging.info("----------------------------------web打印机A1.127用例开始------------------------------")

        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        printer_info = pm.get_all_printer_info()
        pm.click_delete_printer()
        time.sleep(2)
        logging.info("点击删除按钮，提示需要选中一条数据")
        assert pm.get_delete_printer_error_msg() != ''
        logging.info("点击删除按钮，所有配置信息在配置信息列表中。")
        assert printer_info==pm.get_all_printer_info()
        logging.info("----------------------------------web打印机A1.127用例结束------------------------------")

    @pytest.mark.printer
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_cancel_delete_printer(self, com_fixture):
        """
        测试点：web-打印机配置管理-删除-取消-不删除
        步骤：选中删除目标，选中删除时。
        校验点：1、会有删除记录条数提示框，取消删除
                2、该条配置信息在配置信息列表中。
                3、查看数据，有该条配置信息
        """

        logging.info("----------------------------------web打印机A1.126用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        printer_info = pm.get_all_printer_info()

        pm.choose_all_printer()
        pm.click_delete_printer()
        time.sleep(2)
        pm.click_cancel_delete_printer()
        text = pm.get_printer_num()

        logging.info("删除时提示选中多少条数据")
        text = int(text)
        assert text ==pm.real_page_printer_num()
        pm.cancel_choose_all_printer()
        time.sleep(1)
        logging.info("未被删除且所有配置信息在配置信息列表中。")
        assert printer_info==pm.get_all_printer_info()
        logging.info("----------------------------------web打印机A1.126用例结束------------------------------")

    @pytest.mark.printer
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_edit_printer_config_name(self, com_fixture):
        """
        测试点：web-打印机配置管理-配置名/备注功能
        校验点：1、配置名/备注修改，确认修改成功后该打印机列表中，配置名和备注要更新，不能出现错字，异常等现象，查看详细中相关信息也更新。
                2、配置上传时间不变更
        """
        logging.info("----------------------------------web打印机A1.117用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        printer_name = pm.get_first_printer()
        time.sleep(2)
        pm.search_a_printer(printer_name)
        time.sleep(2)
        old_info = pm.get_detail_info()
        time.sleep(2)
        pm.edit_a_printer(new_printer_name, new_printer_beizhu)
        time.sleep(3)
        pm.search_a_printer(new_printer_name)
        time.sleep(1)
        info = pm.get_detail_info()
        time.sleep(1)
        logging.info('判断配置姓名和备注是否修改成功')
        assert info[0] == new_printer_name
        assert info[1] == new_printer_beizhu
        logging.info('判断配置上传时间不变更')
        assert info[4] == old_info[4]
        time.sleep(2)
        logging.info('还原环境，将打印机配置名称，备注还原')
        pm.edit_a_printer(old_info[0], old_info[1])
        time.sleep(2)
        logging.info("----------------------------------web打印机A1.117用例结束------------------------------")

    @pytest.mark.printer
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_search_printer(self, com_fixture):
        """
        测试点：web-打印机配置管理-配置检索功能-正常功能
        步骤：输入包含配置名/打印机名部分字段
        校验点：检索功能正常，列表中所有的字段都可被检索出来

        """
        logging.info("----------------------------------web打印机A1.118用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()

        pm_name = server_sql_qurey(vm_ip,
                                   "select config_name from fusion_printer_manager where id = (SELECT MIN(id) from fusion_printer_manager)")
        pm_name = pm_name[0][0]
        time.sleep(3)
        pm.search_a_printer(pm_name[1:5])
        time.sleep(1)
        logging.info('用配置名称中包含的内容可找到对应打印机')
        assert pm.get_all_printer_info() != ''
        time.sleep(2)
        printer_model = server_sql_qurey(vm_ip,
                                         "select printer_model from fusion_printer_manager where id = (SELECT MIN(id) from fusion_printer_manager)")
        time.sleep(3)
        printer_model = printer_model[0][0]
        pm.search_a_printer(printer_model[1:5])
        logging.info('用打印机型号中包含的内容可找到对应打印机')
        assert pm.get_all_printer_info() != ''
        time.sleep(2)

        logging.info("----------------------------------web打印机A1.118用例结束------------------------------")

    @pytest.mark.printer
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_delete_printer(self,com_fixture):
        """
        测试点：web-打印机配置管理-删除-基本功能
        步骤：选中删除目标，选中删除时。
        校验点：1、会有删除记录条数提示框，确认删除。
               2、删除后，该条配置信息在配置信息列表中被删除。
               4、列表中的其他打印机不变。
               3、查看数据，无该条配置信息
        """
        logging.info("----------------------------------web打印机A1.125用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        delete_name = pm.get_first_printer()
        pm.choose_a_printer(pm.get_first_printer())
        pm.click_delete_printer()
        text = pm.get_printer_num()
        logging.info("删除时提示选中多少条数据")
        text = int(text)
        assert text==1
        pm.click_confirm_delete_printer()
        pm.confirm_passwd()
        pm.click_confire()
        time.sleep(3)
        logging.info("删除后不在列表中")
        pm.search_a_printer(delete_name)
        assert pm.total_count() == 0
        time.sleep(com_slp)
        logging.info("----------------------------------web打印机A1.125用例结束------------------------------")
    @pytest.mark.printer
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_search_special_field(self,com_fixture):
        """
        测试点：web-打印机配置管理-配置检索功能-特殊字段
        步骤：特殊字段请参考“备注/配置名”特殊字符串
        校验点：检索功能正常，列表中不显示信息；
        """
        logging.info("----------------------------------web打印机A1.119用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        pr_name = random.sample(special_field,10)
        pm.search_a_printer(pr_name)
        assert pm.total_count() == 0
        time.sleep(com_slp)
        logging.info("----------------------------------web打印机A1.119用例结束------------------------------")

    @pytest.mark.printer
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_open_printer(self, com_fixture):
        """
        测试点：关闭打印机配置管理
        校验点：1、界面跳转到打印配置界面
                2、打印机配置管理处于关闭状态
                3、打印机列表可见
                4、打印配置管理打开，即跳转到打印列表界面，只要开启打印，后续点击配置管理，都是进入打印列表界面，配置列表信息都在，页码显示无异常，放大缩小页面也无乱码等异常。

        """
        logging.info("----------------------------------web打印机A1.128用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        time.sleep(2)
        pm.close_printer_config()
        time.sleep(1)
        pm.send_passwd_confirm()
        time.sleep(3)
        pm.open_printer()
        time.sleep(1)
        text1 = pm.get_all_printer_info()
        time.sleep(1)
        page_num_old = pm.get_page_num()
        page_printer = pm.choose_page_printer_num(20)
        real_printer_num = pm.real_page_printer_num()
        logging.info('当每页条数修改后，每页总条数与设定一致')
        assert page_printer[1] == real_printer_num
        page_num_new = pm.get_page_num()
        logging.info('当每页条数修改后，页码跟着修改')
        assert page_num_old != page_num_new
        time.sleep(3)
        flag = pm.check_page()
        logging.info('点击上下页正常')
        assert flag == [1, 1, 1, 1]
        time.sleep(2)

        pm.goto_usermanage_page_to_printer_page()
        time.sleep(0.5)
        text2 = pm.get_all_printer_info()
        logging.info('后续点击配置管理，都是进入打印列表界面，配置列表信息都在')
        assert text1 == text2
        time.sleep(2)
        logging.info("----------------------------------web打印机A1.128用例结束------------------------------")

    reserve_url = patch_upgradePage.get_reserve_url()
    @pytest.mark.printer
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    # @pytest.mark.parametrize('url', reserve_url)
    def test_backup_pc_printer(self, url_fixture, url):
        """
        测试点：web-非主控-无打印机配置管理
        步骤：通过ip登录备机/计算节点/主备存的web界面
        校验点：都不可见打印机配置管理菜单
        """
        logging.info("----------------------------------web打印机A1.131用例开始------------------------------")
        pm = PrinterPage(url_fixture)
        logging.info('不可见打印机配置管理菜单')
        assert pm.login_backup_pc() == 0
        # time.sleep(2)
        logging.info("----------------------------------web打印机A1.131用例结束------------------------------")

    @pytest.mark.printer
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_search_a_non_existen_printer(self, com_fixture):
        """
        测试点：web-打印机配置管理-配置检索功能-不存在字段
        步骤：输入打印机列表中不存在字段
        校验点：检索功能正常，列表中所有的字段都可被检索出来
                删除检索字段后，所有打印机信息有正常显示
        """
        logging.info("----------------------------------web打印机A1.120用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        time.sleep(2)
        pm.search_a_printer(non_existen_printer)
        logging.info('查找不存在的打印机')
        assert pm.get_all_printer_info() == ''
        time.sleep(1)
        pm.clear_search_text()
        time.sleep(10)
        logging.info('删除检索字段后，所有打印机信息有正常显示')
        assert pm.get_all_printer_info() != ''

        logging.info("----------------------------------web打印机A1.120用例结束------------------------------")

    @pytest.mark.printer
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_printer_page(self, com_fixture):
        """
        测试点：web-打印机配置管理-页码功能测试
        校验点：风格和功能与用户管理相同，可以修改每页显示打印机配置信息条数，可以指定跳转到哪一页，显示总页码，当每页条数修改后，页码跟着修改，且每页总条数与设定一致，且不能出现异常。
        """
        logging.info("----------------------------------web打印机A1.116用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        page_num_old = pm.get_page_num()
        page_printer = pm.choose_page_printer_num(20)
        real_printer_num = pm.real_page_printer_num()
        logging.info('当每页条数修改后，每页总条数与设定一致')
        assert page_printer[1] == real_printer_num
        page_num_new = pm.get_page_num()
        logging.info('当每页条数修改后，页码跟着修改')
        assert page_num_old != page_num_new
        time.sleep(3)
        flag = pm.check_page()
        logging.info('点击上下页正常')
        assert flag == [1, 1, 1, 1]
        time.sleep(2)
        logging.info("----------------------------------web打印机A1.116用例结束------------------------------")


    @pytest.mark.printer
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_connect_mode_sort(self,com_fixture):
        """
        测试点：web-打印机配置管理-排序-打印机模式
        执行步骤：1、点击向上三角型打印机模式排序
        校验点：1、按字母升序排序
               2、点击三角向下，为字母降序排序跟着修改，且每页总条数与设定一致，且不能出现异常。
        """
        logging.info("----------------------------------web打印机A1.122用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        for i in range(0,2):
            pm.click_seque(u'打印机模式')
            seque = pm.judge_seque(u'打印机模式')
            temp = pm.get_list_content('3')
            time.sleep(com_slp)
            temp = pm.translate_mode(temp)
            list = pm.get_config_content(seque,'connect_mode')
            for i in range(0,len(temp)/2):
                assert  list[i][0] == temp[i]
        logging.info("----------------------------------web打印机A1.122用例结束------------------------------")
    @pytest.mark.printer
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_printer_model_sort(self,com_fixture):
        """
        测试点：web-打印机配置管理-排序-打印机型号
        执行步骤：1、点击向上三角型打印机模式排序
        校验点：1、按字母升序排序
               2、点击三角向下，为字母降序排序
        """
        logging.info("----------------------------------web打印机A1.123用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        for i in range(0,2):
            pm.click_seque(u'打印机型号')
            seque = pm.judge_seque(u'打印机型号')
            temp = pm.get_list_content('4')
            time.sleep(com_slp)
            list = pm.get_config_content(seque,'printer_model')
            for i in range(0,len(temp)/2):
                assert  list[i][0] == temp[i]
        logging.info("----------------------------------web打印机A1.123用例结束------------------------------")

    @pytest.mark.printer
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_config_time_sort(self,com_fixture):
        """
        测试点：web-打印机配置管理-排序-上传配置时间
        执行步骤：1、点击向上三角型上传配置时间排序
        校验点：1、按上传时间先后排序
               2、点击三角向下，为上传时间后先排序
        """
        logging.info("----------------------------------web打印机A1.124用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        for i in range(0,2):
            pm.click_seque(u'配置上传时间')
            seque = pm.judge_seque(u'配置上传时间')
            temp = pm.get_list_content('5')
            time.sleep(com_slp)
            temp = pm.translate_time(temp)
            list = pm.get_config_content(seque,'config_time')
            for i in range(0,len(temp)/2):
                assert  str(list[i][0]).find(temp[i])>=0
        logging.info("----------------------------------web打印机A1.124用例开始------------------------------")




    @pytest.mark.printer1
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_tm_upload_config_msg(self,vdi_fixture,com_fixture):
        """
        测试点：web-打印机配置管理-详情-终端上传配置信息后
        步骤：1、终端上传一条配置信息
        校验点：配置名，备注，打印机模式，打印机型号，配置上传时间，上传配置的终端等信息等信息与实际相同。
        """
        logging.info("----------------------------------web首页A1.121用例开始------------------------------")
        # TODO:
        a = AndroidVdi()
        # 连接vdi终端设备
    #   a.vdi_connect(android_vdi_ip)
        # 登录vdi云桌面
    #   a.login(vdiGroupName + '1', '', vdi_init_pwd)
    #   time.sleep(100)
        """缺少在终端上获取打印机的配置信息方法"""

        #在web页面获取新上传的配置信息并与终端信息比对
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        # pm.search_a_printer(printer_name)
        info = pm.get_detail_info()
        # assert info[0] == config_name
        # assert info[1] == remarks
        # assert info[2] == printer_mode
        # assert info[3] == printer_model
        # assert info[4] == config_time
        # assert info[5] == upload_tm_name
        logging.info("----------------------------------web首页A1.121用例结束------------------------------")

    @pytest.mark.printer
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_init(self, com_fixture):
        """
        测试点：web-初始化配置向导-打印机配置管理为关
        步骤：将主控初始化向导
        校验点：1、打印机配置管理为关闭
               2、开启打印机配置管理后，查看列表为空，查看数据库也为空。
        """
        logging.info("----------------------------------web打印机A1.130用例开始------------------------------")
        pm = PrinterPage(com_fixture)
        pm.goto_printermanger_page()
        pm.init_printer()
        pm.send_passwd_confirm()
        time.sleep(2)
        pm.click_keep_config()
        pm.init_wait()
        pm.refresh_webdriver()
        pm.admin_login(username, passwd)
        pm.goto_printermanger_page()
        logging.info("初始化后打印机配置管理关闭")

        assert pm.get_open_printer_button() == 0
        printer = server_sql_qurey(vm_ip,"select * from fusion_printer_manager")

        time.sleep(2)
        logging.info("数据库清空")
        assert printer == None

        logging.info("----------------------------------web打印机A1.130用例结束------------------------------")


if __name__ == "__main__":
    pytest.main(["-m", "printer"])
