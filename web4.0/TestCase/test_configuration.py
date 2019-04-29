#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: houjinqi
@contact: houjinqi@ruijie.com
@software: PyCharm
@time: 2018/12/14 16:50
"""
import pytest, re
from Common.serverconn import *
from TestData.Logindata import *
from WebPages.ConfigurationPage import *
from TestData.Configurationdata import *
from selenium import webdriver
from selenium.webdriver.support.select import Select
from dateutil import parser
import datetime


class Test_Configurations:

    @pytest.mark.configurations
    def test_customer_info(self, com_fixture):
        logging.info("----------------------------------高级配置A1.2 客户信息开始执行------------------------------")
        p = ConfigurationPage(com_fixture)
        p.goto_customerinfo_page()
        customerinfo = p.customerinfo_edit()
        logging.info("校验修改用户信息后，是否信息正确")
        assert p.check_customerinfo(customerinfo)
        logging.info("----------------------------------测试用例结束------------------------------")

    @pytest.mark.configurations
    def test_sync_time(self, login_fixture):
        logging.info("----------------------------------高级配置A1.3 修改系统时间开始------------------------------")
        try:
            p = ConfigurationPage(login_fixture)
            p.login(username, passwd)
            p.goto_system_time_page()
            p.setting_time_by_hand(time_sleep=300)
            p.login(username, passwd)
            p.goto_system_time_page()
            p.get_ciframe(p.iframe_id)
            logging.info("比较手动设置的时间是否生效")
            assert int(p.elem_text(p.system_time_local_xpath).split('-')[1]) == int(p.return_ntp().split('-')[1]) + 1
            p.back_current_page()
            p.setting_time_by_ntp(time_sleep=300)
            p.login(username, passwd)
            p.goto_system_time_page()
            p.get_ciframe(p.iframe_id)
            logging.info("比较ntp设置的时间是否生效")
            assert int(p.elem_text(p.system_time_local_xpath).split('-')[1]) == int(p.return_ntp().split('-')[1])
            p.back_current_page()
            p.setting_time_by_local()
            p.get_ciframe(p.iframe_id)
            logging.info("比较同步本地时间是否生效")
            assert time.strftime('%Y-%m-%d', time.localtime(time.time())) == p.elem_text(p.system_time_local_xpath).split(' ')[0]
            p.back_current_page()
            logging.info("----------------------------------测试用例结束------------------------------")
        finally:
            p.back_current_page()
            p.goto_system_time_page()
            p.setting_time_by_ntp(time_sleep=300)

    # @pytest.mark.configurations  (4.0密码修改界面发生版本迭代，后期维护）
    # def test_passwd_edit(self, login_fixture):
    #     logging.info("----------------------------------高级配置A1.4 密码修改开始执行------------------------------")
    #     try:
    #         p = ConfigurationPage(login_fixture)
    #         p.login(username, passwd)
    #         new_passwd = p.passwd_edit()
    #         p.logout()
    #         logging.info("校验修改密码后，是否成功登录")
    #         assert p.login(username, new_passwd)
    #     except Exception as e:
    #         logging.info("用例执行异常，原因是：" + e)
    #     finally:
    #         p.passwd_recover(passwd)
    #     logging.info("----------------------------------测试用例结束------------------------------")

    # @pytest.mark.configurations (4.0密码修改界面发生版本迭代，后期维护）
    # def test_passwd_error(self, com_fixture):
    #     logging.info("----------------------------------高级配置A1.4 密码修改错误输入开始执行------------------------------")
    #     p = ConfigurationPage(com_fixture)
    #     p.goto_passwdedit_page()
    #     p.get_ciframe(p.iframe_id)
    #     p.find_elem(p.passwd_sure_button_xpath).click()
    #     logging.info("校验全输入空的密码，是否提示错误")
    #     assert p.find_elem(p.old_passwd_mesg_xpath).is_displayed()
    #     assert p.find_elem(p.new_passwd_mesg_xpath).is_displayed()
    #     assert p.find_elem(p.confirm_passwd_mesg_xpath).is_displayed()
    #     com_fixture.refresh()
    #     time.sleep(2)
    #     p.get_ciframe(p.iframe_id)
    #     p.edit_text(p.old_passwd_xpath, passwd)
    #     p.edit_text(p.confirm_passwd_xpath, passwd)
    #     p.find_elem(p.passwd_sure_button_xpath).click()
    #     logging.info("校验输入空的新密码，是否提示错误")
    #     assert p.find_elem(p.new_passwd_mesg_xpath).is_displayed()
    #     com_fixture.refresh()
    #     time.sleep(2)
    #     p.get_ciframe(p.iframe_id)
    #     p.edit_text(p.old_passwd_xpath, '123')
    #     p.edit_text(p.new_passwd_xpath, passwd)
    #     p.edit_text(p.confirm_passwd_xpath, passwd)
    #     p.find_elem(p.passwd_sure_button_xpath).click()
    #     p.back_current_page()
    #     time.sleep(2)
    #     p.get_ciframe(p.mesg_iframe)
    #     logging.info("校验输入错误的旧密码，是否提示错误")
    #     assert p.find_elem(p.old_passwd_error_xpath).is_displayed()
    #     p.find_elem(p.mesg_sure_button_xpath).click()
    #     p.back_current_page()
    #     logging.info("----------------------------------测试用例结束------------------------------")

    @pytest.mark.configurations
    def test_show_time(self, com_fixture):
        logging.info("----------------------------------高级配置A2.1 系统时间获取开始执行------------------------------")
        p = ConfigurationPage(com_fixture)
        p.goto_system_time_page()
        p.get_ciframe(p.iframe_id)
        p.click_elem(p.system_time_refresh_xpath)
        read = server_conn(mainip, get_server_time).replace('\r\n', '')
        logging.info("检测当前显示的时间与服务端时间是否一致")
        assert p.compare_time(p.get_elem_text(p.system_time_local_xpath), read) < 5
        logging.info("----------------------------------测试用例结束------------------------------")

    @pytest.mark.configurations
    def test_sync_by_ntp_low(self, com_fixture):
        logging.info("----------------------------------高级配置A2.2 系统时间修改（小于一分钟）开始执行------------------------------")
        p = ConfigurationPage(com_fixture)
        ts = parser.parse(p.return_ntp()) + datetime.timedelta(seconds=10)  # 调整时间不足1分钟，不重启
        server_conn(mainip, set_server_time.format(ts.strftime('%H:%M:%S')))
        for server_ip_single in server_ip:
            server_conn(server_ip_single, set_server_time.format(ts.strftime('%H:%M:%S')))
        p.goto_system_time_page()
        p.setting_time_by_ntp(time_sleep=20)
        p.back_current_page()
        p.get_ciframe(p.mesg_iframe)
        p.click_elem(p.mesg_sure_button_xpath)
        p.back_current_page()
        logging.info("检测当前显示的时间与服务端时间是否一致")
        p.get_ciframe(p.iframe_id)
        p.click_elem(p.system_time_refresh_xpath)
        assert p.compare_time(p.return_ntp(), p.get_elem_text(p.system_time_local_xpath)) < 5
        p.back_current_page()
        logging.info("----------------------------------测试用例结束------------------------------")

    @pytest.mark.configurations
    def test_sync_by_ntp2_high(self, com_fixture):
        logging.info("----------------------------------高级配置A2.2 系统时间修改（大于一分钟）开始执行------------------------------")
        p = ConfigurationPage(com_fixture)
        ts = parser.parse(p.return_ntp()) + datetime.timedelta(seconds=200)  # 调整时间不足1分钟，不重启
        server_conn(mainip, set_server_time.format(ts.strftime('%H:%M:%S')))
        for server_ip_single in server_ip:
            server_conn(server_ip_single, set_server_time.format(ts.strftime('%H:%M:%S')))
        p.goto_system_time_page()
        p.setting_time_by_ntp(time_sleep=300)
        p.login(username, passwd)
        p.goto_system_time_page()
        logging.info("检测当前显示的时间与服务端时间是否一致")
        p.get_ciframe(p.iframe_id)
        p.click_elem(p.system_time_refresh_xpath)
        time.sleep(2)
        assert p.compare_time(p.return_ntp(), p.get_elem_text(p.system_time_local_xpath)) < 5
        p.back_current_page()
        logging.info("----------------------------------测试用例结束------------------------------")


if __name__ == '__main__':

    pytest.main(["-k", "test_sync_by_ntp_low"])
