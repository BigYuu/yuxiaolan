#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: houjinqi
@contact: houjinqi@ruijie.com
@software: PyCharm
@time: 2018/12/14 11:21
"""
from Common.Basicfun import BasicFun
from Common.serverconn import *
from TestData.Configurationdata import *
from WebPages.LoginPage import *
from random import *
import time
import ntplib
from dateutil import parser


class ConfigurationPage(BasicFun):
    # 元素定位
    # 用户名输入框
    username_input_xpath = u"//*[@name='userName']"
    # 密码输入框
    passwd_input_xpath = u"//*[@name='pwd']"
    # 登入按钮
    login_button_xpath = u"//button[@type='button']"
    # 注销
    logout_xpath = "//i[@class='sk-icon sk-icon-logout']"

    # 打开高级配置框xpath
    configurations_xpath = u"//*[contains(text(),'高级配置')]"
    # 打开系统设置框xpath
    systemconf_xpath = u"//*[contains(text(),'系统设置')]"

    # 跳转到客户信息页面xpath
    customer_xpath = u"//*[contains(text(),'客户信息')]"
    # 界面iframe的id
    iframe_id = "frameContent"
    # 用户信息修改按钮
    edit_button_xpath = u"//*[@id='customerInfoListForm']//a[contains(text(), '修改')]"
    # 修改用户信息界面iframe的id
    edit_iframe_id = "customerEditPanel"
    # 客户信息-省会xpath
    edit_prov_xpath = u"//*[@id='city_4']//select[@class='prov']"
    # 客户信息-城市xpath
    edit_city_xpath = u"//*[@id='city_4']//select[@class='city']"
    # 客户信息-组织xpath
    name_xpath = u"//*[@id='customerInfoListForm:name']"
    edit_name_xpath = u"//*[@id='customerInfoAddForm:name']"
    # 客户信息-行业下拉表xpath
    customertype_xpath = u"//*[@id='customerInfoListForm:customerType']"
    edit_customertype_xpath = u"//*[@id='customerInfoAddForm:customerType']"
    # 客户信息-渠道xpath
    channel_xpath = u"//*[@id='customerInfoListForm:channel']"
    edit_channel_xpath = u"//*[@id='customerInfoAddForm:channel']"
    # 客户信息-渠道电话xpath
    channeltel_xpath = u"//*[@id='customerInfoListForm:channelTel']"
    edit_channeltel_xpath = u"//*[@id='customerInfoAddForm:channelTel']"
    # 客户信息-维护人员xpath
    maintainer_xpath = u"//*[@id='customerInfoListForm:maintainer']"
    edit_maintainer_xpath = u"//*[@id='customerInfoAddForm:maintainer']"
    # 客户信息-联系电话xpath
    telephone_xpath = u"//*[@id='customerInfoListForm:telephone']"
    edit_telephone_xpath = u"//*[@id='customerInfoAddForm:telephone']"
    # 确定按钮xpath
    # cus_sure_button_xpath = u"//*[@id='customerInfoAddForm:j_id117']"
    cus_sure_button_xpath = u"//*[@class='panelButton']//input[@value='确定']"
    # 密码修改按钮xpath
    passwd_xpath = u"//*[contains(text(),'密码修改')]"
    # 系统时间按钮xpath
    system_time_xpath = u"//*[contains(text(),'系统时间')]"
    # 密码修改-原密码输入框xpath
    old_passwd_xpath = u"//*[@id='confLogForm:oldPassword']"
    # 密码修改-原密码输入为空提示xpath
    old_passwd_mesg_xpath = u"//*[@id='confLogForm:oldPassword_messagePanel']"
    # 密码修改-新密码输入框xpath
    new_passwd_xpath = u"//*[@id='confLogForm:newPassword']"
    # 密码修改-新密码输入为空提示xpath
    new_passwd_mesg_xpath = u"//*[@id='confLogForm:newPassword_messagePanel']"
    # 密码修改-新密码确认输入框xpath
    confirm_passwd_xpath = u"//*[@id='confLogForm:confirmPassword']"
    # 密码修改-新密码确认输入为空提示xpath
    confirm_passwd_mesg_xpath = u"//*[@id='confLogForm:confirmPassword_messagePanel']"
    # 修改确定按钮xpath
    passwd_sure_button_xpath = u"//*[@id='confLogForm:j_id51']"
    # 弹出框确定按钮xpath
    mesg_sure_button_xpath = u"//*[@class='dialogLayout titlePanel']//descendant::input"
    mesg_iframe = u"messageDialog"
    # 原密码错误提示框
    old_passwd_error_xpath = u"//*[@class='messageServrity errorSeverityStyle']//*[contains(text(),'原密码错误')]"
    # 从网络NTP同步
    ntp_time_sync_xpath = u"//*[@id='sysTimeForm:setType:0']"
    # 手动设置
    hand_time_sync_xpath = u"//*[@id='sysTimeForm:setType:1']"
    # 从网络NTP同步
    local_time_sync_xpath = u"//*[@id='sysTimeForm:setType:2']"
    # 手动设置弹出的时间选择框-时间选择四个按钮
    hand_setting_time_xpath = u"//*[@class='rich-calendar-tool']//*[@class='rich-calendar-tool-btn']"
    # 手动设置弹出的时间选择框- 每个月1日
    hand_setting_time_1th_xpath = u"//*[@id='sysTimeForm:j_id53WeekNum1']//td[text()='1']"
    # 系统时间-确定按钮
    system_time_enter_xpath = u"//*[@id='sysTimeForm:j_id61']"
    # 系统时间-服务端系统时间
    system_time_local_xpath = u"//*[@id='sysTimeForm:currentTime']"
    # 系统时间-NTP服务IP选择下拉框
    ntp_ip_xpath = u"//*[@id='sysTimeForm:j_id42comboboxField']"
    # 系统时间-刷新按钮
    system_time_refresh_xpath = u"//*[@id='sysTimeForm:j_id23']"

    # 打开高级配置框
    def open_configurations_list(self):
        self.find_elem(self.configurations_xpath).click()

    # 打开系统设置框
    def open_systemconf_list(self):
        self.find_elem(self.systemconf_xpath).click()

    # 登入
    def login(self, name, passwd):
        self.find_elem(self.username_input_xpath).send_keys(name)
        self.find_elem(self.passwd_input_xpath).send_keys(passwd)
        self.find_elem(self.login_button_xpath).click()
        return True

    # 注销
    def logout(self):
        self.back_current_page()
        self.find_elem(self.logout_xpath).click()

    # 跳转到用户管理页面
    def goto_customerinfo_page(self):
        self.open_configurations_list()
        self.open_systemconf_list()
        self.find_elem(self.customer_xpath).click()

    # 跳转到修改密码页面
    def goto_passwdedit_page(self):
        self.open_configurations_list()
        self.open_systemconf_list()
        self.find_elem(self.passwd_xpath).click()
        time.sleep(2)

    # 跳转到系统时间页面
    def goto_system_time_page(self):
        self.open_configurations_list()
        self.open_systemconf_list()
        self.find_elem(self.system_time_xpath).click()
        time.sleep(2)

    # 修改文本框
    def edit_text(self, locator, text=''):
        self.find_elem(locator).click()
        self.find_elem(locator).clear()
        self.find_elem(locator).send_keys(text)
        return text

    # 元素文本内容
    def elem_text(self, locator):
        return self.find_elem(locator).text

    # 修改客户信息
    def customerinfo_edit(self):
        # 进入修改界面
        time.sleep(2)
        self.get_ciframe(self.iframe_id)
        self.find_elem(self.edit_button_xpath).click()
        self.back_current_page()
        time.sleep(2)
        self.get_ciframe(self.edit_iframe_id)
        # 修改组织名称
        name = self.edit_text(self.edit_name_xpath, sample(name_list, 1)[0])
        customer_info_list.append(name)
        # 修改用户行业信息
        self.select_list_chose2(self.edit_customertype_xpath, 4)
        customertype = self.select_chose_text(self.edit_customertype_xpath)
        customer_info_list.append(customertype)
        # 修改渠道信息
        channel = self.edit_text(self.edit_channel_xpath, sample(channel_list, 1)[0])
        customer_info_list.append(channel)
        # 修改渠道电话
        channeltel = self.edit_text(self.edit_channeltel_xpath, sample(telephone_list, 1)[0])
        customer_info_list.append(channeltel)
        # 修改维护人员
        maintainer = self.edit_text(self.edit_maintainer_xpath, sample(maintainer_list, 1)[0])
        customer_info_list.append(maintainer)
        # 修改联系电话
        telephone = self.edit_text(self.edit_telephone_xpath, sample(telephone_list, 1)[0])
        customer_info_list.append(telephone)
        # 修改省会
        self.select_list_chose2(self.edit_prov_xpath, 27)
        customertype = self.select_chose_text(self.edit_prov_xpath)
        customer_info_list.append(customertype)
        # 修改城市
        self.select_list_chose2(self.edit_city_xpath, 6)
        customertype = self.select_chose_text(self.edit_city_xpath)
        customer_info_list.append(customertype)
        # 退出修改
        self.find_elem(self.cus_sure_button_xpath).click()
        self.back_current_page()
        time.sleep(2)
        return customer_info_list

    def check_customerinfo(self, customerinfo):
        """
        判断 customerinfo是否正确
        :param customerinfo:
        :return:
        """
        self.back_current_page()
        self.get_ciframe(self.iframe_id)
        return self.find_elem(self.name_xpath).text == customerinfo[0] \
               and self.find_elem(self.customertype_xpath).text == customerinfo[1] \
               and self.find_elem(self.channel_xpath).text == customerinfo[2] \
               and self.find_elem(self.channeltel_xpath).text == customerinfo[3] \
               and self.find_elem(self.maintainer_xpath).text == customerinfo[4] \
               and self.find_elem(self.telephone_xpath).text == customerinfo[5]

    # 修改密码
    def passwd_edit(self):
        # 进入修改界面
        self.goto_passwdedit_page()
        time.sleep(2)
        self.get_ciframe(self.iframe_id)
        self.edit_text(self.old_passwd_xpath, passwd)
        new_passwd = sample(test_passwd, 1)[0]
        self.edit_text(self.new_passwd_xpath, new_passwd)
        self.edit_text(self.confirm_passwd_xpath, new_passwd)
        self.find_elem(self.passwd_sure_button_xpath).click()
        self.back_current_page()
        time.sleep(2)
        self.get_ciframe(self.mesg_iframe)
        self.find_elem(self.mesg_sure_button_xpath).click()
        self.back_current_page()
        time.sleep(2)
        return new_passwd

    # 还原密码
    def passwd_recover(self, new_passwd):
        self.goto_passwdedit_page()
        time.sleep(2)
        self.get_ciframe(self.iframe_id)
        self.edit_text(self.old_passwd_xpath, new_passwd)
        self.edit_text(self.new_passwd_xpath, passwd)
        self.edit_text(self.confirm_passwd_xpath, passwd)
        self.find_elem(self.passwd_sure_button_xpath).click()
        self.back_current_page()
        time.sleep(2)
        self.get_ciframe(self.mesg_iframe)
        self.find_elem(self.mesg_sure_button_xpath).click()
        self.back_current_page()

    def setting_time_by_hand(self, time_sleep=1):
        """
        通过手动设置，修改系统时间
        :return:
        """
        self.get_ciframe(self.iframe_id)
        self.click_elem(self.hand_time_sync_xpath)
        self.find_elems(self.hand_setting_time_xpath)[2].click()
        self.click_elem(self.hand_setting_time_1th_xpath)
        self.click_elem(self.system_time_enter_xpath)
        self.back_current_page()
        time.sleep(time_sleep)

    def setting_time_by_ntp(self, time_sleep=1):
        """
        通过网络NTP同步时间
        :return:
        """
        time.sleep(3)
        self.get_ciframe(self.iframe_id)
        self.click_elem(self.ntp_time_sync_xpath)
        self.edit_text(self.ntp_ip_xpath, u"cn.pool.ntp.org")
        self.click_elem(self.system_time_enter_xpath)
        self.back_current_page()
        time.sleep(time_sleep)

    def setting_time_by_local(self):
        """
        同步本地时间
        :return:
        """
        time.sleep(3)
        self.get_ciframe(self.iframe_id)
        self.click_elem(self.local_time_sync_xpath)
        self.click_elem(self.system_time_enter_xpath)
        self.back_current_page()
        time.sleep(30)
        self.get_ciframe(self.mesg_iframe)
        self.click_elem(self.mesg_sure_button_xpath)
        self.back_current_page()
        time.sleep(3)

    def compare_time(self, first_time, second_time):
        """
        比较两个时间的差值
        :return:差几秒
        """
        a = int((parser.parse(first_time) - parser.parse(second_time)).seconds)
        return int((parser.parse(first_time) - parser.parse(second_time)).seconds)

    def return_ntp(self):
        """
        返回NTP时间
        :return:
        """
        client = ntplib.NTPClient()
        response = client.request('ntp5.aliyun.com', timeout=30)  # ntp服务器ip
        ts = response.tx_time
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ts))


if __name__ == '__main__':
    pass
