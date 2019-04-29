#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll / zhouxihong
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/10/22 9:49
"""
from TestData.Cdmdata import *
from WebPages.LoginPage import *
from Common.Basicfun import BasicFun
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from Common import Mylog
import logging
import win32gui, win32con
import time, re


class CDeskMange(BasicFun):
    # 云桌面条件管理输入框
    search_condition_xpath = u"//*[@class='filter-item el-input el-input--suffix']//*[@class='el-input__inner']"
    # 点击搜索按钮
    search_button_xpath = u"//*[@class='el-input__icon sk-icon-search sk-toolbar__icon el-tooltip item']"
    # 获取搜索结条行数
    result_amount_xpath = u"//*[@class='el-pagination__total']"
    # 运行vdi数量
    # vdi_running_xpath = u"//span[text()='{}']/ancestor::tr//span[@class='sk-icon-status__content sk-icon-status__content--normal']"
    # # 离线vdi数量
    # vdi_outline_xpath =u"//span[text()='{}']/ancestor::tr//span[@class='sk-icon-status__content sk-icon-status__content--offline']"
    # # vdi休眠xpath
    # vdi_sleep_xpath =u"//span[text()='{}']/ancestor::tr//span[@class='sk-icon-status__content sk-icon-status__content--stop']"
    # # 管理员关机中状态sk-icon-status sk-icon-status--ing  sk-icon-status__content sk-icon-status__content--ing
    # vdi_closing_xpath =u"//span[text()='{}']/ancestor::tr//span[@class='sk-icon-status__content sk-icon-status__content--ing']"
    # 获取用户名
    group_user_name_xpath = u"//span[contains(text(),'{}')]/ancestor::tr//td[2]//span"
    # vdi分组虚机数量显示（输入用户组名为参数）
    vdi_group_num_xpath = u"//*[contains(text(),'云桌面VDI')]/parent::div/following-sibling::div//div[text()='{}']" \
                          u"/parent::td/following-sibling::td//span[@class='sk-link--normal']"
    # 登入用户名
    vm_user_name_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[2]//span"
    # 终端类型
    type_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[6]//span"
    # 云桌面ip
    cloud_ip_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[8]//span"
    # 云主机ip
    host_sever_ip_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[15]//span"
    # idv 终端ip
    ip_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[13]//span"
    # 终端mac
    mac_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[14]//span"
    # 云桌面mac
    desk_mac_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[9]//span"
    # 终端名称
    name_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[11]//span"
    # 终端分组名称
    group_name_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[12]//span"
    # 更多操作按钮
    more_operate_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//button"
    # 虚机状态
    status_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[5]//" \
                   u"span[contains(@class,'sk-icon-status__content sk-icon-status__content')]"
    # 跳转到云桌面管理页面xpath
    cloud_manage_xpath = u"//span[text()='云桌面管理']"
    # 远程协助按钮
    remote_assistance_xpath = u"//ul[contains(@x-placement,'bottom')]//li[contains(text(),'远程协助')]"
    # 更多关机
    web_close_xpath = u"//ul[contains(@x-placement,'bottom')]//li[contains(text(),'关机')]"
    # 关机提示信息
    get_web_close_info_xpath = "//*[@class='el-message-box__message']/p"
    # 关机确认
    close_confirm_xpath = "//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']"
    # 关机成功提示
    web_close_success_info_xpath = "//*[@class='el-message__content']"
    # 远程协助iframe的id
    assistance_iframe_id_xpath = "//div[@class='layui-layer layui-layer-iframe']"
    # 远程协助iframe
    assistance_iframe_xpath = u"layui-layer-iframe{}"
    # 远程协助成功提示
    assistance_info_xpath = "//*[@id='info']"
    # 远程协助关闭按钮
    close_assistance_xpath = "//*[@id='btns_close']"
    # 输入密码点击确认
    confirm_passwd_xpath = "//input[@type='password']"
    passwd_confirm_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"
    # 更多还原云桌面图标
    web_image_restore_xpath = u"//ul[contains(@x-placement,'bottom')]//li[contains(text(),'还原云桌面')]"
    # 还原云桌面不可操作提示
    unable_operate_restore_desk_xpath = u"//*[contains(text(),'无法对还原类型的云桌面操作')]"
    # 访客还原云桌面不可操作提示
    unable_operate_guest_desk_xpath = u"//*[contains(text(),'无法对访客登入的云桌面操作')]"
    # 未绑定镜像用户不可还原云卓面
    unable_operate_unbind_user_xpath = u"//*[contains(text(),'无法对非绑定用户登录的云桌面操作')]"
    # 显示还原云桌面的用户
    image_user_xpath = u"//*[@class='success-text']"
    # 点击还原云桌面确定按钮
    restore_buftton_xpath = "//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']"
    # 用户镜像信息
    mirror_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[10]//span"
    # 用户镜像信息（搜索后的用户）
    img_msg = u"//*[@class='el-table__row']//td[10]//span"

    # 点击云桌面管理
    def click_cloud_desk_manage(self):

        self.find_elem(self.cloud_manage_xpath).click()

    # 到云桌面管理页面
    def goto_cloud_desk_manage(self):
        self.back_current_page()
        time.sleep(0.3)
        self.click_elem(self.cloud_manage_xpath)

    # 输入密码点击确认
    def send_passwd_confirm(self, pd=c_pwd):
        self.back_current_page()
        self.find_elem(self.confirm_passwd_xpath).send_keys(pd)
        self.find_elem(self.passwd_confirm_xpath).click()

    # 输入搜索信息点击回车
    def search_info(self, name):
        self.find_elem(self.search_condition_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)
        self.find_elem(self.search_condition_xpath).send_keys(name, Keys.ENTER)

    # 火狐浏览器搜索
    def firefox_clear_search_info(self):
        self.chainsdubclick(self.search_condition_xpath)
        self.find_elem(self.search_condition_xpath).send_keys(Keys.BACK_SPACE)
        # 获取搜索结果数量

    def get_search_amount(self):
        temp = self.find_elem(self.result_amount_xpath).text
        s = temp.replace(u'共', '')
        return s.replace(u"条", "")

        # 获取用户名

    def get_user_name(self, name):
        self.search_info(name)
        return self.get_elem_text(self.group_user_name_xpath.format(name)).strip()
        # 关机后vdi状态为管理员关机中

    # def get_closingvdi_state(self,name):
    #     return self.find_elem(self.vdi_closing_xpath.format(name)).text
    #     # 关机后vdi状态为离线
    # def get_closedvdi_state(self, name):
    #    return self.find_elem(self.vdi_outline_xpath.format(name),wait_times=5).text

    # 获取用户名，传入用户组为参数
    def get_group_user_name(self, name):
        time.sleep(1)
        self.find_elem(self.vdi_group_num_xpath.format(name)).click()
        elems = self.find_elems(self.group_user_name_xpath.format(name))
        username_list = []
        for i in range(len(elems)):
            temp = elems[i].text
            username_list.append(temp)
        return username_list

        # 获取用组用户ip，传入用户组为参数

    def get_group_user_ip_list(self, name):
        time.sleep(1)
        self.find_elem(self.vdi_group_num_xpath.format(name)).click()
        elems = self.find_elems(self.ip_xpath.format(name))
        username_list = []
        for i in range(len(elems)):
            temp = elems[i].text
            username_list.append(temp)
        return username_list

    #     获取idv终端ip
    def get_terminal_ip(self, name):
        return self.get_elem_text(self.ip_xpath.format(name)).strip()

    #     获取idv终端ip
    def get_desk_mac(self, name):
        return self.get_elem_text(self.desk_mac_xpath.format(name)).strip()

    # 获取云主机ip
    def get_sever_host_ip(self, name):
        return self.find_elem(self.host_sever_ip_xpath.format(name)).text.strip()

    # 点击更多操作
    def click_more_operate(self, name):
        self.search_info(name)
        time.sleep(1)
        self.scroll_into_view(self.more_operate_xpath.format(name))

    def close_cloud_desk(self, name):
        self.goto_cloud_desk_manage()
        self.click_more_operate_close(name)
        self.click_confirm_close()
        self.send_passwd_confirm()

    # 点击关机
    def click_more_operate_close(self, name):
        self.click_more_operate(name)
        self.find_elem(self.web_close_xpath).click()

    # 点击取消关机
    def click_confirm_close(self):
        self.find_elem(self.close_confirm_xpath).click()

    #       获取关机按钮可点击的属性
    def get_close_attribute(self):
        return self.find_elem(self.web_close_xpath).get_attribute("aria-disabled")

    #    点击关机提示消息
    def get_web_close_info(self):
        return self.find_elem(self.get_web_close_info_xpath).text

    #    关机成功提示信息
    def web_close_success_info(self):
        return self.find_elem(self.web_close_success_info_xpath).text

    #     点击云桌面还原
    # 点击确定还原
    sure_restore_xpath = u"//button/span[contains(text(),'还原')]"

    def click_image_restore(self, name):
        self.click_more_operate(name)
        return  self.get_image_attriubt()


    #  点击还原云桌面
    def click_restore2(self):
        self.find_elem(self.web_image_restore_xpath).click()
        if self.elem_is_exist2(self.sure_restore_xpath):
            self.click_elem(self.sure_restore_xpath)
        self.send_passwd_confirm(c_pwd)



    # 云桌面还原用户信息
    def get_image_restor_user(self):
        return self.get_elem_text(self.image_user_xpath)

    #    点击还原
    def click_restore(self):
        self.find_elem(self.restore_buftton_xpath).click()

    #     还原云桌面操作点击属性
    def get_image_attriubt(self):
        return self.find_elem(self.web_image_restore_xpath).get_attribute("aria-disabled")

    def exist_desk_restore_info(self, locator, times=10):
        """判断还原云桌面按钮是否可点击，"""
        try:
            self.chainstay(self.web_image_restore_xpath)
            self.find_presence_elem(locator, wait_times=times)
            flag = u'不支持云桌面还原'
        except:
            flag = u'支持云桌面还原'
        return flag

    def judge_cloud_desk_is_clickable(self, times=10):
        """判断还原用户还原云桌面按钮是否可点击，"""
        return self.exist_desk_restore_info(self.unable_operate_restore_desk_xpath, times)

    def judge_guest_cloud_desk_is_clickable(self, times=10):
        """判断访客登入还原云桌面按钮是否可点击，"""
        return self.exist_desk_restore_info(self.unable_operate_guest_desk_xpath, times)

    def judge_unbinduser_cloud_desk_is_clickable(self, times=5):
        """判断单用户终端未绑定用户还原云桌面按钮是否可点击，"""
        if self.judge_cloud_desk_is_clickable(times) == u'不支持云桌面还原' \
                or self.exist_desk_restore_info(self.unable_operate_unbind_user_xpath, times) == u'不支持云桌面还原':
            return u'不支持云桌面还原'
        else:
            logging.error("单用户终端非绑定用户登入可执行还原云桌面操作")
            return None

    #   获取终端的状态
    def get_status(self, name):
        self.search_info(name)
        return self.get_elem_text(self.status_xpath.format(name), wait_times=5)

    #   获取终端分组
    def get_user_group(self, name):
        return self.get_elem_text(self.group_name_xpath.format(name)).strip()

    #   获取终端名称
    def get_terminal_name(self, name):
        return self.get_elem_text(self.name_xpath.format(name)).strip()

    #   获取终端MAC
    def get_terminal_mac(self, name):
        return self.get_elem_text(self.mac_xpath.format(name)).strip()

    # 获取终端类型
    def get_terminal_type(self, name):
        return self.get_elem_text(self.type_xpath.format(name)).strip()

    #     获取终端云桌面ip
    def get_cloud_desk_ip(self, name):
        return self.get_elem_text(self.cloud_ip_xpath.format(name)).strip()

    # 获取终端镜像信息
    def get_terminal_mirror(self, name):
        time.sleep(0.5)
        return self.get_elem_text(self.mirror_xpath.format(name)).strip()

    # 点击远程协助按钮
    def click_remote_assistance(self, name):
        self.back_current_page()
        self.click_more_operate(name)
        self.click_elem(self.remote_assistance_xpath)

    #     点击远程协助关闭按钮
    def click_close_assistion_button(self):
        self.back_current_page()
        ele = self.find_elem(self.assistance_iframe_id_xpath)
        s = ele.get_attribute("id")
        fid = re.findall('.*?(\d+)', s)[0]
        self.get_ciframe(self.assistance_iframe_xpath.format(fid))
        self.find_elem(self.close_assistance_xpath).click()
        time.sleep(1)

    # 获取远程协助返回的信息提示
    def get_assistance_info(self):
        self.back_current_page()
        time.sleep(1)
        ele = self.find_elem(self.assistance_iframe_id_xpath)
        s = ele.get_attribute("id")
        fid = re.findall('.*?(\d+)', s)[0]
        self.get_ciframe(self.assistance_iframe_xpath.format(fid))
        return self.find_elem(self.assistance_info_xpath).text

    #    远程协助断开获取窗口
    def assistance_break(self):
        flag = 0
        try:
            dialog = win32gui.FindWindow("#32770", u"消息提示")
            button = win32gui.FindWindowEx(dialog, 0, "Button", u"关闭")
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
            flag = 1
        except Exception as e:
            logging.exception(e)
            logging.info("拒接协助，弹出框不存在")
            pass
        return flag

    #  打开火狐浏览器
    def open_firefox(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(url)
        t = Login(driver)
        t.login(username, passwd)
        t.goto_cloud_desk_manage()
        return driver

    # 获取登入虚机用户名 vm_user_name_xpath
    def get_vm_user_name(self, name):
        return self.find_elem(self.vm_user_name_xpath.format(name), wait_times=5).text

    def vm_login_success(self, ip, name, times=30):
        """页面显示指定登入终端，即虚机登录成功,输入ip和用户名,0登入成功1失败"""
        n = 0
        flag = 1
        while n < times:
            try:
                self.search_info(ip)
                if self.get_status(ip) == u'运行':
                    if self.get_vm_user_name(ip) == name:
                        flag = 0
                        break
                    else:
                        time.sleep(3)
            except:
                time.sleep(3)
            n = n + 1
        return flag

    def terminal_offline(self, ip):
        """页面显示终端是否离线，离线或返回0 ，在线返回1"""
        flag = 1
        try:
            self.search_info(ip)
            if self.elem_is_exist2(self.status_xpath.format(ip)) is not None:
                if self.get_status(ip) == u'离线':
                    flag = 0
        except:
            logging.info("未知错误")
        return flag

    def terminal_exist(self, ip):
        """页面显示终端是否存在，存在或返回0 ，不存在返回1"""
        flag = 1
        try:
            self.search_info(ip)
            if self.get_search_amount() == 0:
                flag = 0
        except:
            logging.info("未知错误")
        return flag

    #####################################
    # 注销
    logout_xpath = "//i[@class='sk-icon sk-icon-logout']"
    # 未被选择的列
    not_select_column = "//*[@class='has-gutter']//node()[contains(@class,'is-noshow')]"
    # 所有列
    all_column = "//*[@class='has-gutter']//th[contains(@class,'is-leaf')]"
    # 云桌面管理栏 Xpath
    cdeskmange_xpath = "//span[contains(.,'云桌面管理')]"
    # 自定义列表按钮
    custom_list_button_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round is-noLabel el-dropd" \
                               "own-selfdefine']"
    # 自定义列表已勾选的列
    custom_list_selected_xpath = "//*[@class='el-icon-check']/../..//*[@class='sk-column-item']//*[@class='el-ic" \
                                 "on-check']"
    # 自定义列表未勾选的列
    custom_list_unselected_xpath = "//*[@class='icon-empty']"
    # 返回的搜索的所有结果
    all_search_results_xpath = "//*[@class='el-table__row']/.."
    # 返回的搜索结果为空
    search_results_empty_xpath = "//*[@class='el-table__empty-block']"
    # 分页选择图标
    pagination_select_ico_xpath = "//*[@class='el-input el-input--mini el-input--suffix']"
    # 分页选择下拉框,{0}中为 10 20 30 50
    pagination_select_box_xpath = "//*[@class='el-scrollbar__view el-select-dropdown__list']//node()[contains" \
                                  "(@class,el-select-dropdown__item)]//*[contains(.,{0})]/.."
    # 云桌面管理按列增序排列
    column_sort_ascending_xpath = u"//*[@class='caret-wrapper']/../..//*[contains(.,'{0}')]//node()[@class='sort" \
                                  u"-caret ascending']"
    # 云桌面管理按列降序排列
    column_sort_descending_xpath = u"//*[@class='caret-wrapper']/../..//*[contains(.,'{0}')]//node()[@class='sort" \
                                   u"-caret descending']"
    # 云桌面管理单独选择列 format传参选择
    column_select_xpath = u"//*[contains(@class,'has-gutter')]//div[contains(.,'{0}')]/.."
    # 云桌面管理用户名选择
    cloud_desk_manage_usr_xpath = u"//*[contains(@class,'el-table__row')]//*[contains(.,'{0}')]/..//*[contains" \
                                  u"(@class,'not-drag-position')]//*[contains(@class,'el-tooltip')]"
    # 云桌面管理根据用户名选择当前行
    usr_select_all_row_xpath = u"//*[contains(@class,'el-table__row')]//*[contains(.,'{0}')]/..//*[contains(@class," \
                               u"'not-drag-position')]//*[contains(@class,'el-tooltip')]/../.."

    def custom_list(self):
        flag_list = [0, 0]
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.custom_list_button_xpath).click()
        time.sleep(com_slp)
        while self.elem_is_exist(self.custom_list_selected_xpath) == 0:
            self.find_elem(self.custom_list_selected_xpath).click()
        if len(self.find_elems(self.all_column)) - len(self.find_presence_elems(self.not_select_column)) - 3 == 0:
            flag_list[0] = 1
        while self.elem_is_exist(self.custom_list_unselected_xpath) == 0:
            self.find_elem(self.custom_list_unselected_xpath).click()
        if self.elem_is_exist(self.not_select_column) == 1 \
                and len(self.find_elems(self.all_column)) - 1 == 15:
            flag_list[1] = 1
        elif self.elem_is_exist(self.not_select_column) == 0 \
                and len(self.find_elems(self.all_column)) - len(
            self.find_presence_elems(self.not_select_column)) - 1 == 15:
            flag_list[1] = 1
        return flag_list

    def search_box(self):
        flag_list = [0, 0]
        split_str = u'更多'
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.search_condition_xpath).send_keys(search_ip)
        self.find_elem(self.search_button_xpath).click()
        temp_text = self.find_elem(self.all_search_results_xpath).text
        temp_text1 = temp_text.replace('\n', ' ' * 4)
        temp_text2 = temp_text1.split(split_str)
        while '' in temp_text2:
            temp_text2.remove('')
        for i in range(len(temp_text2)):
            if search_ip in temp_text2[i]:
                flag_list[0] = 1
            else:
                flag_list[0] = 0
        self.find_elem(self.search_condition_xpath).clear()
        time.sleep(com_slp)
        self.find_elem(self.search_condition_xpath).send_keys(search_name)
        self.find_elem(self.search_button_xpath).click()
        time.sleep(com_slp)
        temp_text = self.find_elem(self.all_search_results_xpath).text
        temp_text1 = temp_text.replace('\n', ' ' * 4)
        temp_text2 = temp_text1.split(split_str)
        while '' in temp_text2:
            temp_text2.remove('')
        for i in range(len(temp_text2)):
            if search_name in temp_text2[i]:
                flag_list[1] = 1
            else:
                flag_list[1] = 0
        return flag_list

    def search_box_not_exist(self):
        flag_list = [0, 0]
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.search_condition_xpath).send_keys('!@#$%^&*')
        self.find_elem(self.search_button_xpath).click()
        if self.find_elem(self.search_results_empty_xpath).text == u'暂无数据':
            flag_list[0] = 1
        time.sleep(com_slp)
        self.driver.refresh()
        time.sleep(5 * com_slp)
        self.find_elem(self.search_button_xpath).click()
        if self.find_elem(self.all_search_results_xpath).text != '':
            if self.find_elem(self.result_amount_xpath).text != u'共0条':
                flag_list[1] = 1
        return flag_list

    def search_box_sql_injection(self):
        flag_list = [0]
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.search_condition_xpath).send_keys('or 1=1')
        self.find_elem(self.search_button_xpath).click()
        if self.find_elem(self.search_results_empty_xpath).text == u'暂无数据':
            flag_list[0] = 1
        return flag_list

    def pagination_record(self):
        flag_list = [0, 0, 0, 0]
        split_str = u'更多'
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        record = [10, 20, 30, 50]
        time.sleep(com_slp)
        for i in range(len(record)):
            self.find_elem(self.pagination_select_ico_xpath).click()
            time.sleep(com_slp)
            self.find_elem(self.pagination_select_box_xpath.format(record[i])).click()
            time.sleep(2 * com_slp)
            temp_text = self.find_elem(self.all_search_results_xpath).text
            temp_text1 = temp_text.replace('\n', ' ' * 4)
            temp_text2 = temp_text1.split(split_str)
            while '' in temp_text2:
                temp_text2.remove('')
            if record[i] == len(temp_text2):  # 判断当前页面的记录条数
                flag_list[i] = 1
            elif len(temp_text2) < record[i] and i != 0 and record[i] >= record[i - 1]:
                flag_list[i] = 1
            elif i == 0 and len(temp_text2) < record[i]:
                flag_list[i] = 1
        return flag_list

    def custom_sort_settings(self):
        flag_list = [0, 0]
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.custom_list_button_xpath).click()
        time.sleep(com_slp)
        try:
            while len(self.find_elems(self.custom_list_selected_xpath)) != 0:
                self.find_elem(self.custom_list_selected_xpath).click()
        except:
            logging.info("不存在已经勾选的项")
            pass
        while len(self.find_elems(self.custom_list_unselected_xpath)) != 4:
            self.find_elem(self.custom_list_unselected_xpath).click()
        num1 = len(self.find_elems(self.all_column)) - len(self.find_presence_elems(self.not_select_column)) - 1
        print str(num1) + '\n'
        time.sleep(com_slp)
        self.find_elem(self.logout_xpath).click()
        self.find_elem(Login.username_input_xpath).send_keys(username)
        self.find_elem(Login.passwd_input_xpath).send_keys(passwd)
        self.find_elem(Login.login_button_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        num2 = len(self.find_elems(self.all_column)) - len(self.find_presence_elems(self.not_select_column)) - 1
        if num1 == num2:
            flag_list[0] = 1
        print str(num2) + '\n'
        self.driver.delete_all_cookies()
        time.sleep(com_slp * 3)
        self.find_elem(Login.username_input_xpath).send_keys(username)
        self.find_elem(Login.passwd_input_xpath).send_keys(passwd)
        self.find_elem(Login.login_button_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        num3 = len(self.find_elems(self.all_column)) - len(self.find_presence_elems(self.not_select_column)) - 1
        if num2 == num3:
            flag_list[1] = 1
        print str(num3) + '\n'
        return flag_list

    def custom_sort_rule(self):
        flag_list = [0, 0, 0, 0]
        split_str = u'更多'
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.custom_list_button_xpath).click()
        try:
            while len(self.find_elems(self.custom_list_unselected_xpath)) != 0:
                self.find_elem(self.custom_list_unselected_xpath).click()
        except:
            logging.info("不存在没有勾选的项")
            pass
        sort_value_list = [u'用户名', u'姓名', u'用户组', u'云桌面IP', u'状态']
        for i in range(len(sort_value_list)):
            self.find_elem(self.column_sort_ascending_xpath.format(sort_value_list[i])).click()
            time.sleep(2 * com_slp)
            temp_text = self.find_elem(self.all_search_results_xpath).text
            temp_text = temp_text.replace(' ', ' ' * 4)
            temp_text1 = temp_text.replace('\n', ' ' * 4)
            temp_text2 = temp_text1.split(split_str)
            temp_text3 = []
            while '' in temp_text2:
                temp_text2.remove('')
            if i == 3:
                for j in range(3):
                    package_info = re.compile(
                        "(?:(?:2[0-4][0-9]\.)|(?:25[0-5]\.)|(?:1[0-9][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}(?:(?:2[0-5][0-5])|(?:25[0-5])|(?:1[0-9][0-9])|(?:[1-9][0-9])|(?:[0-9]))")
                    ip = package_info.findall(temp_text2[j].strip())[0]
                    temp_text3.append(ip)
                a = sorted(temp_text3)
                if a.__eq__(temp_text3):
                    flag_list[1] = 1
                else:
                    flag_list[1] = 0
                continue
            if i < 3:
                for j in range(len(temp_text2)):
                    temp_text3.append(temp_text2[j].strip().split(' ' * 4)[i])
                tmp_list = []  # 忽略大小写进行排序，需要进行特殊处理才能比较
                for tmp in temp_text3:
                    tmp_list.append(tmp.lower())
                b = sorted(tmp_list)
                for index in range(0, len(b)):
                    if b[index].encode("utf-8") != tmp_list[index].encode("utf-8").lower():
                        flag_list[0] = 0
                        break
                    else:
                        flag_list[0] = 1
            if i == 4:
                for j in range(len(temp_text2)):
                    temp_text3.append(temp_text2[j].strip().split(' ' * 4)[i - 1])
                if len(set(temp_text3)) == 2:
                    if temp_text3.index(u'运行') < temp_text3.index(u'离线'):
                        flag_list[2] = 1
                        continue
                if len(set(temp_text3)) > 2:
                    if u'离线' in temp_text3:
                        if temp_text3.index(u'运行') < temp_text3.index(u'休眠'):
                            if u'离线' in temp_text3:
                                if temp_text3.index(u'休眠') < temp_text3.index(u'离线'):
                                    flag_list[2] = 1
                                    continue
                            else:
                                flag_list[2] = 1
                                continue
                    else:
                        flag_list[2] = 1
                        continue
                if len(set(temp_text3)) == 1:
                    flag_list[2] = 1
        sort_value_list = [u'云桌面MAC', u'镜像', u'终端MAC']
        for i in range(len(sort_value_list)):
            temp_text = self.get_elem_attribute(self.column_select_xpath.format(sort_value_list[i]), 'class')
            if temp_text.__contains__('is-sortable'):
                flag_list[3] = 0
            else:
                flag_list[3] = 1
        return flag_list

    def custom_list_drag(self):
        flag_list = [0, 0]
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.custom_list_button_xpath).click()
        try:
            while len(self.find_elems(self.custom_list_selected_xpath, wait_times=10)) != 0:
                self.find_elem(self.custom_list_selected_xpath).click()
        except:
            logging.info("不存已勾选的项")
            pass
        while len(self.find_elems(self.custom_list_unselected_xpath)) != 2:
            self.find_elem(self.custom_list_unselected_xpath).click()
        if self.elem_is_exist2(self.not_select_column) is None:
            if len(self.find_elems(self.all_column)) - len(self.find_presence_elems(self.not_select_column)) - 1 == 13:
                flag_list[0] = 1
        self.driver.refresh()
        time.sleep(5 * com_slp)
        temp_text1 = self.find_elem(self.column_select_xpath.format(u'姓名')).get_attribute('class')
        temp_text2 = self.find_elem(self.column_select_xpath.format(u'用户组')).get_attribute('class')
        if temp_text1.__contains__('can-drag-sort') and temp_text2.__contains__('can-drag-sort'):
            flag_list[1] = 1
        return flag_list

    def list_info_display_1(self):
        flag_list = [0, 0]
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        temp_text = self.find_elem(self.cloud_desk_manage_usr_xpath.format(search_data_17)).get_attribute("class")
        temp_text1 = self.find_elem(self.cloud_desk_manage_usr_xpath.format(search_data_17)).get_attribute("style")
        if temp_text.__contains__('tooltip'):
            flag_list[0] = 1
        if temp_text1.__contains__('width'):
            flag_list[1] = 1
        return flag_list

    def search_performance(self):
        flag_list = [0]
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.search_condition_xpath).send_keys(search_data_23)
        self.find_elem(self.search_button_xpath).click()
        temp_text = self.find_elem(self.cloud_desk_manage_usr_xpath.format(search_data_23)).text
        time.sleep(1)
        if temp_text.__eq__(search_data_23):
            flag_list[0] = 1
        return flag_list

    def only_login_vdi(self):
        flag_list = [0, 0, 0]
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        if self.find_elem(self.usr_select_all_row_xpath.format(status_dict[u'运行'])).text.__contains__(u'运行'):
            flag_list[0] = 1
        if self.find_elem(self.usr_select_all_row_xpath.format(status_dict[u'休眠'])).text.__contains__(u'休眠'):
            flag_list[1] = 1
        if self.find_elem(self.usr_select_all_row_xpath.format(status_dict[u'离线'])).text.__contains__(u'离线'):
            flag_list[2] = 1
        return flag_list

    def custom_sort_display1(self):
        flag_list = [0]
        split_str = u'更多'
        time.sleep(com_slp)
        self.find_elem(self.cdeskmange_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.custom_list_button_xpath).click()
        try:
            while len(self.find_elems(self.custom_list_unselected_xpath, wait_times=10)) != 0:
                self.find_elem(self.custom_list_unselected_xpath).click()
        except:
            logging.info("未存在么有选中的选项")
            pass
        sort_value_list = [u'用户名']
        for i in range(len(sort_value_list)):
            self.find_elem(self.column_sort_ascending_xpath.format(sort_value_list[i])).click()
            time.sleep(2 * com_slp)
            temp_text = self.find_elem(self.all_search_results_xpath).text
            temp_text = temp_text.replace(' ', ' ' * 4)
            temp_text1 = temp_text.replace('\n', ' ' * 4)
            temp_text2 = temp_text1.split(split_str)
            temp_text3 = []
            while '' in temp_text2:
                temp_text2.remove('')
            for j in range(len(temp_text2)):
                temp_text3.append(temp_text2[j].strip().split(' ' * 4)[i])

            tmp_list = []  # 忽略大小写进行排序，需要进行特殊处理才能比较
            for tmp in temp_text3:
                tmp_list.append(tmp.lower())
            b = sorted(tmp_list)
            for index in range(0, len(b)):
                if b[index].encode("utf-8") != tmp_list[index].encode("utf-8").lower():
                    flag_list[0] = 0
                    break
                else:
                    flag_list[0] = 1

            # b = sorted(temp_text3)
            # if b.__eq__(temp_text3):
            #     flag_list[0] = 1
            # else:
            #     flag_list[0] = 0
        return flag_list

    u"--------------------------------------余小兰封装部分--------------------------------"
    cd_ip = u"//*[@class='el-table__row']//td[8]//span"
    # 用户在线状态
    terminal_online_status = "//*[@class='el-table__row']//td[5]/div/span/span"

    # 获取元素值
    def get_value(self, locator):
        return self.get_elem_text(locator=locator)

    # 单选框
    more_box = u"//*[@class='has-gutter']//label[1]//span[@class='el-checkbox__inner']"
    # 批量关机
    batch_close = u"//span[contains(text(),'批量关机')]"
    # 云桌面管理按钮
    cloud_desktop_manage_xpath = u"//li[contains(.,'云桌面管理')]"
    # 云桌面管理下的搜索按钮
    cloud_desktop_manage_lookup_xpath = u"//input[@placeholder='用户名/终端名称/用户组/终端组/IP地址']"
    # 云桌面管理下的更多按钮
    cloud_desktop_manage_more_xpath = u"//span[contains(.,'%s')]//ancestor::tr//span[contains(.,'更多')]"
    # 云桌面管理-更多按钮-还原云桌面
    cloud_desktop_manage_more_reduction_xpath = u"//*[@x-placement='bottom-start']//li[contains(.,'还原云桌面')]"
    # 云桌面管理-更多按钮-还原云桌面-确定
    cloud_desktop_manage_more_reduction_y_xpath = u"//*[text()='确认 ']"
    # 云桌面管理-更多按钮-还原云桌面-取消
    cloud_desktop_manage_more_reduction_n_xpath = u"//*[contains(text(),'取消')]"
    # 用户的还原属性
    user_reduction_xpath = u"//button//*[contains(text(),'还原')]"

    def close_img(self, password):
        """云桌面关机操作"""
        self.click_elem(self.more_box)  # 选中所有操作
        self.click_elem(self.batch_close)  # 点击批量关机
        self.click_elem(self.close_confirm_xpath)  # 关机确认
        if self.elem_is_exist(self.confirm_passwd_xpath) == 0:
            self.send_passwd_confirm(password)  # 输入密码并确认
        time.sleep(23)

    def cd_manage_recovery(self, search_key, password=c_pwd):
        """关机在线终端"""
        self.driver.refresh()
        self.back_current_page()
        time.sleep(1)
        self.goto_cloud_desk_manage()
        time.sleep(1)
        self.search_info(search_key)
        if self.elem_is_exist("//tr[@class='el-table__row'][1]") == 0:
            self.close_img(password)

    # 选中用户
    chose_user_xpath = "//*[contains(text(),'{}')]/ancestor::tr/td[1]//span"

    def close_chose_user(self, name, pwd=c_pwd):
        """选中用户批量关机"""
        self.search_info(name)
        self.click_elem(self.chose_user_xpath.format(name))
        self.click_elem(self.batch_close)  # 点击批量关机
        self.click_elem(self.close_confirm_xpath)  # 关机确认
        self.send_passwd_confirm(pwd)  # 输入密码并确认
        time.sleep(23)

    # 跳转云桌面
    def goto_cloud_desktop(self):
        self.find_elem(self.cloud_desktop_manage_xpath).click()
        # 清空云桌面搜索

    def goto_cloud_desktop_search_clean(self):
        self.find_elem(self.cloud_desktop_manage_lookup_xpath).send_keys(Keys.CONTROL, 'a')
        self.find_elem(self.cloud_desktop_manage_lookup_xpath).send_keys(Keys.BACK_SPACE)
        # 跳转云桌面搜索

    def goto_cloud_desktop_search(self, name):
        self.find_elem(self.cloud_desktop_manage_lookup_xpath).send_keys(name, Keys.ENTER)
        self.goto_cloud_desktop_search_clean()

    # 跳转云桌面更多
    def goto_cloud_desktop_more(self, name):
        self.find_elem(self.cloud_desktop_manage_more_xpath % name).click()

    # 点击还原云桌面
    def click_reduction(self):
        self.find_elem(self.cloud_desktop_manage_more_reduction_xpath).click()
        self.find_elem(self.user_reduction_xpath).click()

    @staticmethod
    def check_device_online(device_ip):
        print("check_device_online " + device_ip)
        flag = True
        cmd = "ping -w 1 " + device_ip
        back_info = os.popen(cmd)
        s1 = back_info.read()
        b = s1.splitlines()[2]
        if b.decode("gbk").__contains__(u'请求超时'):
            flag = False
        print("check_device_online return " + str(flag))
        return flag

if __name__ == "__main__":
    pass
