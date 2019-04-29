#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/10/19 15:26
"""
from __future__ import division
from Common.Basicfun import BasicFun
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from Common.terminal_action import *
import logging
import time
import re
import math
from Common import terminal_action
from Common import serverconn
from TestData.Logindata import passwd


class IdvPage(BasicFun):
    # 整个页面iframe frameContent
    all_page_iframe_id = "frameContent"
    # 整个页面右边iframe
    main_page_iframe_id = "content"
    # idv搜索框
    idv_search_xpath = "//*[@class='search_input1']"
    # 点击搜索
    click_search_xpath = "//*[@class='search_img1']"
    # vdi终端用户名
    terminal_name_xpath = u"//*[text()='{}']/ancestor::tr//td[2]//div"
    # VD状态xpath
    idv_state_xpath = u"//*[text()='{}']/ancestor::tr//td[11]//div"
    # vdi所属分组信息
    vdi_group_name_xpath = u"//*[text()='{}']/ancestor::tr//td[3]//div"
    # vdi终端选择框
    vdi_terminal_chose_xpath = u"//*[text()='{}']/ancestor::tr//input"
    # vdi删除终端
    vdi_terminal_delete_xpath = u'//*[@id="delete_terminal"]'
    # vdi终端批量关机
    vdi_terminal_close_xpath = '//*[@id="halt_terminal"]'
    # 变更分组按钮
    chang_group_xpath = u"//*[@id='btn_change_group']"
    # 跳转到终端管理页面
    terminal_xpath = u"//*[text()='终端管理']"
    # 到瘦终端页面
    go_vdi_terminal_page_xpath = u"//*[contains(@class,'el-menu-item')]//*[text()='瘦终端（VDI）']"
    # 到胖瘦终端页面
    go_idv_terminal_page_xpath = u"//*[contains(@class,'el-menu-item')]//*[text()='胖终端（IDV）']"
    # 终端选择框
    chose_terminal_xpath = u"//*[text()='{}']/ancestor::tr//input"
    # 点击更改分组弹出页面iframe
    common_frame_xpath = "layui-layer-iframe{}"
    # 新建分组按钮
    click_new_group_xpath = u"//*[@id='add_group']"
    # 新建分组输入框
    new_group_name_xpath = "//*[@id='terminal_group_name']"
    # 新建用户点击确定
    confirm_xpath = "//*[@id='btns_ok']"
    #  选择分组xpath
    chose_group_xpath = "//*[@class='input_text2']"
    #  点击确定xpath
    confirm_chose_xpath = "//*[@class='btn_sq_dark btn_left']"
    #  点击更多操作
    idv_more_operate_xpath = u"//*[text()='{}']/ancestor::tr//div[@class='more']"
    #  idv点击编辑
    idv_edit_xpath = u"//*[text()='{}']/ancestor::tr//div[@class='btn first']"
    # idv详情按钮
    idv_info_xpath = '//*[text()="{}"]/ancestor::tr//div[@id="detail"]'
    #  idv点击初始化终端
    terminal_init_xpath = u"//*[text()='{}']/ancestor::tr//div[text()='终端初始化']"
    # idv选择镜像frame的id
    chose_mirror_frame_id_xpath = u"//*[text()='选择镜像']/parent::div[@class='layui-layer layui-layer-iframe']"
    #  获取idv编辑页面的iframe的id的div
    iframe_id_xpath = "//*[@class='layui-layer layui-layer-iframe']"
    #  编辑页面终端分组下拉框
    idv_change_group_xpath = u"//*[@id='terminalGroup']"
    #  编辑vdi用户修改后确定按钮
    idv_confirm_button = "//*[@id='btns_ok']"
    #  瘦终端页面详情按钮
    thin_terminal_info_button_xpath = "//*[text()={}']/ancestor::tr//td[11]//div[@class='btn_light']"
    #  vdi详情页面终端操作系统类型
    operate_type_xpath = "//*[@id='os_type']"
    # vdi详情页面终端主机名称
    info_name_xpath = '//*[@id="terminal_name"]'
    # vdi详情页面终端产品序列号
    info_sn_num_xpath = '//*[@id="terminal_sn"]'
    # vdi详情页面终端版本号
    info_version_num_xpath = '//*[@id="terminal_sys_version"]'
    # vdi详情页面终端mac
    info_terminal_mac_xpath = '//*[@id="terminal_mac"]'
    # vdi详情页面终端cpu
    info_terminal_cpu_xpath = '//*[@id="terminal_cpu"]'
    # vdi详情页面终端内存
    info_terminal_men_xpath = '//*[@id="terminal_mem"]'
    # vdi详情页面终端bios
    info_terminal_bios_xpath = '//*[@id="terminal_bios"]'
    # vdi详情页面终端主板
    info_terminal_mainbord_xpath = '//*[@id="terminal_mainboard"]'
    # vdi详情页面终端存储
    info_terminal_storage_xpath = '//*[@id="terminal_storage"]'
    # 确定xpath
    sure_xpath = u"//*[@class='layui-layer-btn0']"
    # 密码输入和确认框
    confirm_passwd_xpath = "//input[@type='password']"
    passwd_confirm_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"
    # 重启终端
    reboot_button_xpath = "//*[@id='reboot_terminal']"
    # 选择终端单框
    check_box_xpath = u"//*[text()='{}']/ancestor::tr//td[1]/input"
    # 重启终端确定按钮
    confirm_reboot_xpath = u"//*[text()='确定']"
    # 瘦终端用户组编辑按钮
    vdi_group_edit_xpath = u"//*[text()='{}']/parent::div/*[@class='operate_edit']"
    # 瘦终端用户组删除按钮
    vdi_group_delete_xpath = u"//*[text()='{}']/parent::div/*[@class='operate_delete']"
    # 用户组查询xpath
    group_name_xpath = u"//*[@class='item']//*[text()='{}']"
    # 新建用户组用户名含有特殊字符提示  名称只允许字母、汉字、数字及下划线
    special_group_name_info_xpath = "//*[@id='errorName']"
    # 新建用户组时组名为空提示
    null_group_name_xpath = "//*[@id='error_message']"
    # 取消按钮
    cancel_button_xpath = "//*[@id='btns_cancel']"
    # 用户组名已存在判断
    exist_name_xpath = "//*[@class='layui-layer-content layui-layer-padding']"
    # 新建idv终端选择桌面类型
    idv_group_type_xpath = "//*[@id='restoreModel']"
    # 选择绑定的idv镜像
    idv_group_mirror_add_xpath = "//*[@id='btn_selectImage']"
    # 选择镜像
    mirror_chose_xpath = "//*[@class='image_unselect']//*[@class='select_item input_checkbox2_unselect']"
    # 修改系统盘大小
    change_disk_size_xpath = "//*[@name='system_disk_size']"
    # 新建用户组其他设置
    other_set_xpath = '//*[@id="enableUseLocalDisk"]/following-sibling::span'
    # 新增无线白名单
    white_list_xpath = '//*[@class="ssid-add-btn"]'
    # 无线白名单输入框
    white_list_input_xpath = '//*[@id="ssid_input_{}"]'
    # 终端全选按钮
    select_all_terminal_xpath = '//*[@id="content_table_selectTrueOrFalse"]'
    # 页面信息条数
    total_count_xpath = '//*[@id="total_count"]'
    # 检查终端获取检查结果
    check_result_xpath = '//*[text()="{}"]/ancestor::tr//*[@class="check_normal_text"]'
    # 检测全部终端
    check_all_terminal_xpath = '//*[@id="check_all_terminal"]'
    # 获取终端ip
    terminal_ip_xpath = u"//*[text()='{}']/ancestor::tr//td[6]//div"
    # 批量关闭终端页面所有终端数量
    close_terminal_amount_xpath = '//*[@id="allCount"]'
    # 关机成功数量
    close_success_xpath = '//*[@id="normalCount"]'
    # 关机失败数量
    close_fail_xpath = '//*[@id="errorCount"]'
    # 终端正常关机进度信息
    terminal_close_success_state_xpath = '//*[@class="check_normal_text"]'
    # 终端未成功关机进度信息
    terminal_close_fail_state_xpath = '//*[@class="check_abnormal_text"]'
    # 点击确定关闭终端关闭信息页面
    terminal_close_confirm_xpath = "//*[@id='btn_ok']"
    # 修改用户组选择框
    change_group_name_xpath = '//*[@id="terminalGroup"]'
    # 检测终端终端状态获取
    check_terminal_state_xpath = '//*[text()="{}"]/ancestor::tr//div[@class="check_time"]/preceding-sibling::div'
    # 单用户终端页面
    single_user_page_xpath = '//*[@id="SINGLE"]'
    # 多用户终端页面
    mul_user_page_xpath = '//*[@id="MULT"]'
    # 终端检测结果
    allCount_xpath = "//*[@id='allCount']"
    # 终端解绑信息
    unbing_info = u"//*[contains(text(),'解绑会清空终端上保存的用户数据')]"

    # 跳转到右边页面的frame
    def go_main_iframe(self):
        self.back_current_page()
        time.sleep(2)
        self.get_ciframe(self.all_page_iframe_id)
        self.get_ciframe(self.main_page_iframe_id)

    #  获取该页面显示的终端总数量
    def total_count(self):
        self.go_main_iframe()
        return int(self.get_elem_text(self.total_count_xpath))

    # vdi点击终端分组
    def click_group_name(self, name):
        self.back_current_page()
        time.sleep(2)
        self.get_ciframe(self.all_page_iframe_id)
        self.click_elem(self.group_name_xpath.format(name))

    # 获取终端ip
    def get_terminal_ip(self, name):
        self.back_current_page()
        self.go_main_iframe()
        return self.get_elem_text(self.terminal_ip_xpath.format(name))

    # vdi点击检测全部终端
    def check_all_terminal(self):
        self.back_current_page()
        self.go_main_iframe()
        self.click_elem(self.check_all_terminal_xpath)

    # 查找idv
    def search_terminal(self, name):
        time.sleep(0.3)
        self.back_current_page()
        self.go_main_iframe()
        self.find_elem(self.idv_search_xpath).send_keys(name, Keys.ENTER)
        self.find_elem(self.idv_search_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)

    unrecord_xpath = u"//*[contains(text(),'无记录信息')]"

    # 智能查找终端
    def search_terminal_anayway(self, name, ty=0):
        """
        ty=0:查找公用终端组下的终端
        ty=1:查找单用户终端下的终端
        """
        time.sleep(0.3)
        self.back_current_page()
        self.go_main_iframe()
        self.find_elem(self.idv_search_xpath).send_keys(name, Keys.ENTER)
        self.find_elem(self.idv_search_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)
        # 查找多用户终端组下的终端，若无终端则去单用户终端组查找并修改为多用户终端，返回多用户终端组页面
        if ty == 0:
            if self.elem_is_exist(self.unrecord_xpath, 6) == 0:
                self.back_current_page()
                self.goto_idv_terminal_single_terminal_group_page()
                if self.elem_is_exist(self.remove_bingding_xpath) == 0:  # 单用户终端绑定用户，先进行解绑
                    self.remove_bingding_user(name)
                    time.sleep(1)
                self.modify_idv(tm_name=name, tm_type=u"多用户")
                self.back_current_page()
                self.goto_idv_terminal_moreandpub_terminal_group_page()
        # 查找单用户组下的终端，查找无记录则去多用户终端组查找并修改为单用户终端，返回单用户终端组
        if ty == 1:
            if self.elem_is_exist(self.unrecord_xpath, 6) == 0:
                self.back_current_page()
                self.goto_idv_terminal_moreandpub_terminal_group_page()
                self.modify_idv(tm_name=name, tm_type=u"单用户")
                self.back_current_page()
                self.goto_idv_terminal_single_terminal_group_page()

    # 获取组内所有idv状态
    def get_idv_state(self, name):
        self.go_main_iframe()
        time.sleep(0.5)
        return self.find_elem(self.idv_state_xpath.format(name)).text

    # 从首页获取idv终端名称列表
    def get_treminal_name_list(self, group):
        self.go_main_iframe()
        elems = self.find_elems(self.terminal_name_xpath.format(group))
        list_name = []
        for i in range(len(elems)):
            temp = elems[i].text
            list_name.append(temp)
        self.back_current_page()
        return list_name

    #  跳转到vdi终端管理页面
    def goto_vdi_terminal_page(self):
        if self.elem_is_exist(self.go_vdi_terminal_page_xpath) == 1:
            self.click_elem(self.terminal_xpath)
            time.sleep(0.3)
        self.click_elem(self.go_vdi_terminal_page_xpath)

    # 点击更改vdi用户组
    def click_vdi_change_group(self, group_name):
        self.back_current_page()
        time.sleep(2)
        self.go_main_iframe()
        self.click_elem(self.chang_group_xpath)
        self.vdi_new_group_info(group_name)

    #    选择vdi用户即点击单选框
    def chose_user(self, name):
        self.find_elem(self.chose_terminal_xpath.format(name)).click()

    #   修改用户分组选择分组点击确认
    def chose_change_group(self, group):
        self.go_common_frame()
        s = self.find_elem(self.chose_group_xpath)
        Select(s).select_by_value(group)
        time.sleep(1)
        self.find_elem(self.confirm_chose_xpath).click()

    #  点击初始化终端
    def terminal_init(self, ip):
        self.back_current_page()
        time.sleep(2)
        self.get_ciframe(self.all_page_iframe_id)
        if get_terminal_mode(ip).__contains__('0'):
            self.click_elem(self.single_user_page_xpath)
        else:
            self.click_elem(self.mul_user_page_xpath)
        self.search_terminal(ip)
        self.click_idv_more_operate(ip)
        self.find_elem(self.terminal_init_xpath.format(ip)).click()
        self.back_current_page()
        self.click_sure()
        self.send_passwd_confirm()
        self.click_sure()

    terminal_init_tips = u"//div[contains(text(),'提示')]"

    #  点击初始化终端
    def terminal_init1(self, name):
        self.search_terminal(name)
        self.click_idv_more_operate(name)
        self.find_elem(self.terminal_init_xpath.format(name)).click()
        self.back_current_page()
        self.click_sure()
        self.send_passwd_confirm()
        flag = 1
        time.sleep(1)
        self.click_sure()
        if self.elem_is_exist(self.terminal_init_tips) == 0:  # 当终端正在初次部署时会弹出该提示弹窗
            self.click_elem(self.sure_xpath)
        return flag

    # 重启终端
    def reboot_terminal(self, name):
        self.search_terminal(name)
        time.sleep(0.5)
        self.click_elem(self.check_box_xpath.format(name))
        self.click_elem(self.reboot_button_xpath)
        self.back_current_page()
        self.click_elem(self.confirm_reboot_xpath)
        time.sleep(1)
        self.click_elem(self.confirm_reboot_xpath)

    #  跳转到idv终端管理页面
    def goto_idv_terminal_page(self):
        if self.elem_is_exist(self.go_idv_terminal_page_xpath) == 1:
            self.find_elem(self.terminal_xpath).click()
            time.sleep(0.3)
        self.find_elem(self.go_idv_terminal_page_xpath).click()

    # 点击胖终端页面
    def goto_idvtm_page(self):
        self.find_elem(self.go_idv_terminal_page_xpath).click()

    #     vdi终端变更分组
    def click_idv_more_operate(self, name):
        self.find_elem(self.idv_more_operate_xpath.format(name)).click()

    #   idv终端点击编辑
    def click_idv_edit(self, name):
        self.find_elem(self.idv_edit_xpath.format(name)).click()

    # 跳转到公用frame页面
    def go_common_frame(self):
        self.back_current_page()
        time.sleep(1)
        fid = self.get_frame_id()
        self.get_ciframe(self.common_frame_xpath.format(fid))

    #     点击详情页面
    def click_vdi_info(self, name):
        self.search_terminal(name)
        self.find_elem(self.idv_info_xpath.format(name)).click()
        self.go_common_frame()
        time.sleep(1)
        info_list = dict()
        info_list['name'] = self.get_elem_text(self.info_name_xpath)
        info_list['sys'] = self.get_elem_text(self.operate_type_xpath)
        info_list['sn'] = self.get_elem_text(self.info_sn_num_xpath)
        info_list['version'] = self.get_elem_text(self.info_version_num_xpath)
        info_list['mac'] = self.get_elem_text(self.info_terminal_mac_xpath)
        info_list['cpu'] = self.get_elem_text(self.info_terminal_cpu_xpath)
        info_list['men'] = self.get_elem_text(self.info_terminal_men_xpath)
        info_list['bios'] = self.get_elem_text(self.info_terminal_bios_xpath)
        info_list['mainboard'] = self.get_elem_text(self.info_terminal_mainbord_xpath)
        info_list['storage'] = self.get_elem_text(self.info_terminal_storage_xpath)
        return info_list

    # 点击检测终端
    def click_terminal_check(self):
        self.go_main_iframe()
        self.click_elem(self.check_all_terminal_xpath)

    # 获取检测终端结果
    def get_check_state_info(self, name):
        self.get_elem_text(self.check_terminal_state_xpath.format(name), wait_times=300)

    #     修改分组镜像frame id
    def get_group_mirror_frame_id(self):
        self.back_current_page()
        ele = self.find_elem(self.chose_mirror_frame_id_xpath)
        s = ele.get_attribute("id")
        return re.findall('.*?(\d+)', s)[0]

    #     idv修改分组frame id
    def get_frame_id(self):
        self.back_current_page()
        ele = self.find_elem(self.iframe_id_xpath)
        s = ele.get_attribute("id")
        return re.findall('.*?(\d+)', s)[0]

    #  idv修改分组
    def idv_edit_change_group(self, ip, group):
        self.search_terminal(ip)
        time.sleep(0.5)
        self.click_idv_more_operate(ip)
        self.click_idv_edit(ip)
        self.back_current_page()
        self.go_common_frame()
        default_group = self.select_chose_text(self.idv_change_group_xpath)
        ele2 = self.find_elem(self.idv_change_group_xpath)
        Select(ele2).select_by_visible_text(group)
        self.find_elem(self.idv_confirm_button).click()
        self.back_current_page()
        self.click_elem(self.sure_xpath)
        time.sleep(0.5)
        if default_group.__contains__(group):
            pass
        else:
            self.send_passwd_confirm(c_pwd)
        time.sleep(0.5)

    #     点击新建分组
    def click_new_group(self):
        time.sleep(1)
        self.back_current_page()
        self.get_ciframe(self.all_page_iframe_id)
        self.click_elem(self.click_new_group_xpath)

    # 新建vdi分组
    def vdi_new_group(self, name):
        self.click_new_group()
        self.go_common_frame()
        self.find_elem(self.new_group_name_xpath).send_keys('{}'.format(name), Keys.ENTER)
        self.click_elem(self.confirm_xpath)

    # 修改vdi分组信息
    def vdi_new_group_info(self, group=u'未分组'):
        self.go_common_frame()
        self.select_list_chose(self.change_group_name_xpath, group)
        self.click_elem(self.confirm_xpath)
        time.sleep(2)

    # 选择vdi
    def vdi_chose(self, name):
        self.search_terminal(name)
        self.click_elem(self.vdi_terminal_chose_xpath.format(name))

    # vdi点击全选
    def vdi_select_all(self):
        self.go_main_iframe()
        self.click_elem(self.select_all_terminal_xpath)

    # 点击删除vdi
    def vdi_terminal_delete(self):
        self.click_elem(self.vdi_terminal_delete_xpath)
        self.click_sure()

    # vdi终端批量关机
    def vdi_terminal_bach_close(self):
        self.click_elem(self.vdi_terminal_close_xpath)
        self.click_sure()
        time.sleep(5)
        self.go_common_frame()

    #  获取终端总数量
    def vdi_close_amount(self):
        return int(self.get_elem_text(self.close_terminal_amount_xpath))

    #  获取终端关机成功数量
    def vdi_close_success_amount(self):
        return int(self.get_elem_text(self.close_success_xpath))

    #  获取终端关机失败数量
    def vdi_close_fail_amount(self):
        return int(self.get_elem_text(self.close_fail_xpath))

    #  获取终端关机失败信息
    def vdi_close_fail_info(self):
        return self.get_elem_text(self.terminal_close_fail_state_xpath)

    #  获取终端关机成功信息
    def vdi_close_success_info(self):
        return self.get_elem_text(self.terminal_close_success_state_xpath)

    # 点击确认关闭终端关机页面
    def vdi_close_confirm(self):
        self.click_elem(self.terminal_close_confirm_xpath)

    # 新建idv分组
    def idv_new_group(self, name, desk_type=u'还原', size=40, other_set='open', white_list=None, white_name=None):
        """默认桌面类型为还原，
        ::desk_type默认桌面类型为还原，传入参数个性可修改为个性类型
        ::size为系统盘大小，默认为40
        ::other_set 其他设置默认是开启的，传入参数close可关闭
        ::white_list 无线白名单默认为空,white_name无线白名单名称，传入内容为列表"""
        self.click_new_group()
        self.go_common_frame()
        self.find_elem(self.new_group_name_xpath).send_keys('{}'.format(name), Keys.ENTER)
        self.idv_chose_disk_type(desk_type)
        img = self.idv_chose_mirror()
        self.idv_set_disk_size(size)
        self.idv_other_set(other_set)
        if white_list is not None:
            self.idv_white_list_add(white_name)
        self.click_confirm()
        return img

    #      idv终端分组选择桌面类型
    def idv_chose_disk_type(self, desk_type=u'还原'):
        # self.go_common_frame()
        self.select_list_chose(self.idv_group_type_xpath, desk_type)

    # idv分组选择其他设置
    def idv_other_set(self, other_set):
        class_info = self.get_elem_attribute(self.other_set_xpath, 'class')
        flag = 0
        if other_set == 'close':
            if class_info.__contains__("_unselect"):
                pass
            elif class_info.__contains__("_select"):
                self.click_elem(self.other_set_xpath)
                flag = 1
        elif other_set == 'open':
            if class_info.__contains__("_select"):
                pass
            elif class_info.__contains__("_unselect"):
                self.click_elem(self.other_set_xpath)
                flag = 1
        else:
            logging.error("输入参数有误")
        return flag

    # idv 新建分组选择修改镜像
    def idv_chose_mirror(self):
        self.go_common_frame()
        time.sleep(0.5)
        self.click_elem(self.idv_group_mirror_add_xpath)
        fid = self.get_group_mirror_frame_id()
        self.get_ciframe(self.common_frame_xpath.format(fid))
        time.sleep(0.5)
        self.click_elem(self.mirror_chose_xpath)
        img = self.get_elem_text(self.selected_img_xpath)
        self.click_confirm()
        return img

    #     idv修改系统盘大小
    def idv_set_disk_size(self, size):
        self.go_common_frame()
        time.sleep(0.5)
        self.clear_text_info(self.change_disk_size_xpath)
        self.elem_send_keys(self.change_disk_size_xpath, size)

    # idv 新增无线白名单
    def idv_white_list_add(self, white_name):
        self.go_common_frame()
        time.sleep(0.5)
        for i in range(len(white_name)):
            self.click_elem(self.white_list_xpath)
            self.elem_send_keys(self.white_list_input_xpath.format(i), white_name[i])

    # 新建分组点击确定
    def click_confirm(self):
        self.click_elem(self.confirm_xpath)

    #     新建分组点击取消
    def click_cancel(self):
        self.click_elem(self.cancel_button_xpath)

    # 新建分组用户名不规范提示
    def vdi_group_name_error_info(self):
        return self.get_elem_attribute(self.special_group_name_info_xpath, 'style')

    # 点击删除分组的确定按钮
    def click_sure(self):
        self.back_current_page()
        self.click_elem(self.sure_xpath)

    # 新建分组用户名为空
    def vdi_group_name_null_info(self):
        return self.get_elem_attribute(self.null_group_name_xpath, 'style')

    #  用户组名已存在提示信息
    def get_exist_info(self):
        return self.get_elem_text(self.exist_name_xpath)

    #    删除分组
    def delete_group(self, name):
        self.back_current_page()
        self.get_ciframe(self.all_page_iframe_id)
        time.sleep(0.5)
        self.chainstay(self.group_name_xpath.format(name))
        self.click_elem(self.vdi_group_delete_xpath.format(name))
        self.click_sure()

    # 查找vdi用户分组
    def find_group(self, name):
        flag = 0
        try:
            self.back_current_page()
            self.get_ciframe(self.all_page_iframe_id)
            self.find_elem(self.group_name_xpath.format(name))
            flag = 1
        except Exception as not_find_error:
            logging.exception(not_find_error)
        return flag

    #  获取vdi终端用户信息
    def get_vdi_group_name(self, name):
        self.search_terminal(name)
        return self.get_elem_text(self.vdi_group_name_xpath.format(name))

    # 输入密码点击确定
    def send_passwd_confirm(self, pd=passwd):
        self.back_current_page()
        self.find_elem(self.confirm_passwd_xpath).send_keys(pd)
        self.find_elem(self.passwd_confirm_xpath).click()

    u"--------------------------整合web组----------------------------------"
    # 选中终端名
    get_unbinding_group_checkbox = u"//*[text()='{}']/parent::td/preceding-sibling::td/child::input[@type='checkbox']"
    # 获取单用户终端全局删除按钮
    get_single_terminal_delete_btn = "//div[@id='delete_terminal']"
    # 获取单用户终端删除确认按钮
    get_terminal_delete_confirm_ok_btn = u"//a[text()='确定']"
    # 删除操作成功点击确认
    get_terminal_confirm_btn = u"//div[@class='layui-layer layui-layer-dialog']/child::div/child::a[text()='确定']"

    def delete_idv_terminal(self, name):
        time.sleep(10)
        self.get_ciframe("frameContent")
        self.click_elem(self.single_user_page_xpath)
        self.search_terminal(name)
        try:
            self.click_elem(locator=self.get_unbinding_group_checkbox.format(name), wait_times=5)
        except Exception as not_find_error:
            return

        self.click_elem(self.more_xpath)
        self.click_elem(self.get_single_terminal_delete_btn)
        self.back_current_page()
        self.click_elem(self.get_terminal_delete_confirm_ok_btn)

        self.send_passwd_confirm(pd=passwd)
        time.sleep(2)
        self.click_elem(self.get_terminal_confirm_btn)
        time.sleep(2)

    # 查找终端名是否是未绑定终端组
    get_unbinding_group_text = u"//*[text()='{}']/parent::td/following-sibling::td/child::div[text()='未绑定用户终端组']"

    # 确认是否在未绑定用户终端组
    def is_in_unbinding_group(self, name):
        time.sleep(10)
        self.get_ciframe("frameContent")
        self.click_elem(self.single_user_page_xpath)
        self.search_terminal(name)
        elem = self.find_elem(self.get_unbinding_group_text.format(name))

        return elem is not None

    # 点击展开所有单用户终端组
    open_all_single_terminal_group_xpath = '//*[contains(@class, "noline_close")]'
    # 获取所有单用户终端组组名
    get_all_single_terminal_group_name_xpath = '//*[@treenode_a and @onclick and @target="_blank"]'

    # 单用户终端组所有组名
    def get_all_single_terminal_group_name(self):
        self.get_ciframe("frameContent")

        level = 10
        i = 0
        while i < level:
            try:
                elems = self.find_elems(self.open_all_single_terminal_group_xpath)
            except Exception as timeout:
                logging.info("所有节点已经展开")
                break
            else:
                for elem in elems:
                    elem.click()
                    time.sleep(0.5)
                i = i + 1

        list = []
        time.sleep(1)
        elems = self.find_elems(self.get_all_single_terminal_group_name_xpath)

        for elem in elems:
            list.append(elem.get_attribute('title'))

        self.back_current_page()

        return list

    #   跳转到用户管理页面xpath
    user_manage_xpath = u"//*[text()='用户管理']"

    # 进入用户管理页面
    def goto_user_manage_page(self):
        self.find_elem(self.user_manage_xpath).click()

    # 点击展开所有用户组
    open_all_user_group_xpath = '//*[@class="el-tree-node__expand-icon el-icon-caret-right"]'
    # 获取用户组树的名称
    get_all_user_group_name_path = "//div[contains(@class, 'custom-node-label')]"

    # 获取所有用户组组名
    def get_all_user_group_name(self):

        level = 10
        i = 0
        while i < level:
            try:
                elems = self.find_elems(self.open_all_user_group_xpath)
            except Exception as timeout:
                logging.info("所有节点已经展开")
                break
            else:
                for elem in elems:
                    elem.click()
                    time.sleep(0.5)
                i = i + 1

        list = []
        time.sleep(1)
        elems = self.find_elems(self.get_all_user_group_name_path)

        for elem in elems:
            list.append(elem.get_attribute('innerText'))

        return list

    u"--------------------------整合web组----------------------------------"

    # ---------- LinMengYao 2019/1/8 ----------

    # 终端参数修改-终端模式下拉框
    tm_type_xpath = "//*[@id='loginType']"
    # 终端参数修改-终端模式选项
    tm_type_option_xpath = u"//*[@id='loginType']/option[text()='{}']"
    # 终端参数修改-终端名称输入框
    tm_name_xpath = "//*[@id='hostName']"
    # 终端参数修改-所属分组下拉框
    tm_group_xpath = "//*[@id='terminalGroup']"
    # 终端参数修改-所属分组选项
    tm_group_option_xpath = u"//*[@id='terminalGroup']/option[text()='{}']"
    # 终端参数修改-桌面类型下拉框
    desk_type_xpath = "//*[@id='restoreModel']"
    # 终端参数修改-系统盘输入框
    sys_disk_xpath = "//*[@id='system_disk_size']"
    # 终端参数修改-允许使用本地盘勾选框
    enable_d_disk_xpath = "//*[@id='enableUseLocalDiskId']"
    # 终端参数修改-描述
    tm_note_xpath = "//*[@id='note']"
    # 终端参数修改-确定按钮
    submit_btn_xpath = "//*[@id='btns_ok']"
    # 终端参数修改-提示-确定
    confirm_btn_xpath = "//*[@class='layui-layer layui-layer-dialog']"
    # 终端分组-选择镜像-选中的镜像
    selected_img_xpath = "//*[@class='select_item input_checkbox2_select']/parent::div/following-sibling::div/div[2]"
    # 胖终端IP
    idv_ip_xpath = u"//*[text()='{}']/ancestor::tr//td[7]//div"
    # 胖终端桌面IP
    idv_desk_ip_xpath = u"//*[text()='{}']/ancestor::tr//td[8]//div"
    # 胖终端所属分组
    idv_gp_xpath = u"//*[text()='{}']/ancestor::tr//td[4]//div"
    # 胖终端模式
    idv_mode_xpath = u"//*[text()='{}']/ancestor::tr//td[3]//div"
    # 修改终端分组-绑定镜像
    gp_img_xpath = u"//*[@id='imageName']"
    # 修改终端分组-删除镜像
    gp_img_del_xpath = "//*[@id='btn_closeImage']"
    # 修改终端分组-选择镜像-镜像名
    cb_img_name_xpath = "//*[@class='image_unselect']//*[@class='image_os_label']"
    # 修改终端分组-选择镜像-勾选框
    cb_img_combo_xpath = u"//*[text()='{}']/parent::div/preceding-sibling::div"
    # 请确认密码
    confirm_pwd = u"//div[text()='请确认密码']"

    # 修改idv终端参数
    def modify_idv(self, tm_name, tm_type=None, tm_rename=None, tm_group=None, desk_type=None, sys_disk=None,
                   enable_d_disk=None):
        """不传参即跳过不进行修改"""
        self.search_terminal(tm_name)
        self.click_idv_more_operate(tm_name)
        self.click_idv_edit(tm_name)
        self.go_common_frame()
        if tm_type is not None:  # 终端类型
            self.select_list_chose(self.tm_type_xpath, tm_type)
        if tm_rename is not None:  # (重命名)终端名称
            self.clear_text_info(self.tm_name_xpath)
            self.elem_send_keys(self.tm_name_xpath, tm_rename)
        if tm_group is not None:  # 终端组
            self.select_list_chose(self.tm_group_xpath, tm_group)
        if desk_type is not None:  # 桌面类型
            self.select_list_chose(self.desk_type_xpath, desk_type)
        if sys_disk is not None:  # 系统盘
            self.clear_text_info(self.sys_disk_xpath)
            self.elem_send_keys(self.sys_disk_xpath, sys_disk)
        if enable_d_disk is not None:  # 是否启用本地盘
            self.click_elem(self.enable_d_disk_xpath)
        self.click_elem(self.submit_btn_xpath)
        self.back_current_page()
        self.click_elem(self.confirm_btn_xpath)
        self.click_sure()
        flag = 0
        if self.elem_is_exist(self.confirm_passwd_xpath) == 0:
            self.send_passwd_confirm()
            flag = 1
            time.sleep(8)
        return flag

    # 获取胖终端IP
    def get_idv_ip(self, tm_name):
        self.back_current_page()
        self.go_main_iframe()
        return self.get_elem_text(self.idv_ip_xpath.format(tm_name))

    # 获取多用户胖终端桌面IP
    def get_idv_desk_ip(self, tm_name):
        self.back_current_page()
        self.go_main_iframe()
        return self.get_elem_text(self.idv_desk_ip_xpath.format(tm_name))

    # 获取终端所属分组
    def get_idv_gp(self, tm_name):
        self.back_current_page()
        self.go_main_iframe()
        return self.get_elem_text(self.idv_gp_xpath.format(tm_name))

    tm_name = u"//*[text()='{}']/ancestor::tr//td[2]//div"

    # 获取vdi终端名称
    def get_vdi_name(self, search_key):
        self.back_current_page()
        self.go_main_iframe()
        return self.get_elem_text(self.tm_name.format(search_key))

    sn_info = u"//*[text()='{}']/ancestor::tr//td[5]//div"

    # 获取vdi终端序列号
    def get_vdi_sn(self, search_key):
        self.back_current_page()
        self.go_main_iframe()
        return self.get_elem_text(self.sn_info.format(search_key))

    # 点击胖终端组编辑按钮
    def click_gp_edit_btn(self, gp_name):
        self.back_current_page()
        time.sleep(1)
        self.get_ciframe(self.all_page_iframe_id)
        self.chainstay(self.group_name_xpath.format(gp_name))
        self.click_elem(self.vdi_group_edit_xpath.format(gp_name))

    # 编辑胖终端组
    def edit_idv_gp(self, tm_name=None, gp_name=None, rename=None, desk_type=None, img=None, sys_disk=None,
                    local_disk=None, note=None, ty=0):
        self.back_current_page()
        self.go_left_iframe()
        if ty == 1 and gp_name is not None:
            self.click_gp_edit_btn(gp_name)
        elif ty == 0 and tm_name is not None:
            gp_name = self.get_idv_gp(tm_name)
            self.click_gp_edit_btn(gp_name)
        self.go_common_frame()
        if rename is not None:
            self.clear_text_info(self.new_group_name_xpath)
            self.find_elem(self.new_group_name_xpath).send_keys('{}'.format(rename), Keys.ENTER)
        if desk_type is not None:
            self.idv_chose_disk_type(desk_type)
        img_current = u''
        if img is not None:
            img_current = self.edit_idv_gp_img()
        sys_disk_a = '0'
        sys_disk_b = '0'
        if sys_disk is not None:
            self.idv_set_disk_size(sys_disk)
            sys_disk_b = self.get_elem_attribute(self.change_disk_size_xpath, 'aria-valuenow')  # 获取系统盘设置前大小
            sys_disk_a = self.get_elem_attribute(self.change_disk_size_xpath, 'value')  # 获取系统盘设置后大小
        flag = 0
        if local_disk is not None:
            flag = self.idv_other_set(local_disk)
        if note is not None:
            self.idv_gp_note(note)
        self.click_confirm()
        self.click_sure()
        if (int(sys_disk_a) > int(sys_disk_b)) or (flag == 1):
            self.back_current_page()
            if self.elem_is_exist(self.confirm_passwd_xpath) == 0:
                self.send_passwd_confirm()
        return img_current, sys_disk_a

    # 获取终端模式
    def get_idv_mode(self, tm_name):
        self.back_current_page()
        self.go_main_iframe()
        return self.get_elem_text(self.idv_mode_xpath.format(tm_name))

    # 换算从winrm返回的盘大小信息
    def convert_size(self, info):
        ls = info.split()
        size = ls[1].strip()
        cv_size = int(size) / 1073741824  # 从Byte换算为GB
        return int(math.ceil(cv_size))  # 数值向上取整

    # 终端登录到虚机内获取cmd信息
    def idv_login_cmd(self, tm_type, idv_usr_name, idv_usr_pwd, cmd, assert_info):
        tm_ip = self.get_idv_ip('test_my_1')
        if tm_type == u'多用户':
            flag = terminal_action.idv_in_login_page(tm_ip)
            logging.info("判断多用户终端是否已停留在登录界面")
            assert flag == 1
            terminal_action.idv_login(tm_ip, idv_usr_name, idv_usr_pwd)
        elif tm_type == u'公用':
            time.sleep(50)
        else:
            raise Exception
        desk_ip = self.get_idv_desk_ip('test_my_1')
        time.sleep(220)
        info = serverconn.get_win_conn_info(desk_ip, 'Administrator', 'rcd', cmd)
        logging.info("验证虚机盘是否存在/大小")
        assert info.__contains__(assert_info) is True

    # 编辑胖终端组-描述
    def idv_gp_note(self, note):
        self.scroll_into_view(self.tm_note_xpath)
        self.clear_text_info(self.tm_note_xpath)
        self.elem_send_keys(self.tm_note_xpath, note)
        current_note = self.get_elem_text(self.tm_note_xpath)
        if len(note) <= 60:
            pass
        else:
            spare = len(note) - 60
            note = note[:-spare]
            logging.info("验证胖终端组描述字符不超过60")
            assert current_note == note

    # 编辑胖终端组-镜像
    def edit_idv_gp_img(self):
        if self.get_elem_attribute(self.idv_group_mirror_add_xpath, 'style').__contains__('inline-block'):
            self.idv_chose_mirror()
        else:
            self.go_common_frame()
            time.sleep(0.5)
            img_b = self.get_elem_text(self.gp_img_xpath)  # 获取修改前的镜像名
            self.click_elem(self.gp_img_del_xpath)  # 删除该镜像的绑定
            self.click_elem(self.idv_group_mirror_add_xpath)  # 点击“+”
            fid = self.get_group_mirror_frame_id()
            self.get_ciframe(self.common_frame_xpath.format(fid))
            time.sleep(0.5)
            img_name_list = self.find_elems(self.cb_img_name_xpath)  # 获取所有可选镜像（名）
            img_a = u''
            for i in range(len(img_name_list)):
                img_a = img_name_list[i].text
                if img_a != img_b:
                    break
            self.click_elem(self.cb_img_combo_xpath.format(img_a))
            self.click_confirm()
            self.go_common_frame()
            return img_a

    u"-------------------------------------余小兰封装部分--------------------------------------------"
    # 未分组-镜像绑定-红星（非必填）
    weifenzu_feibit = "//*[@id='dv_image_name']//div[contains(@class,'red_star')]"
    # vdi-更多-详情
    detail_xpath = "//*[@id='detail']"
    # 终端产品型号
    productid_xpath = "//*[@id='productId']"
    # 获取硬件版本
    hardwareVersion_xpath = "//*[@id='hardwareVersion']"
    # 终端编辑中各参数-是否允许使用本地盘
    enableUseLocalDiskId = "//*[@id='enableUseLocalDiskId']"
    # 终端编辑中各参数-终端模式
    idv_tm_type = "//*[@id='loginType']"
    # 终端编辑中各参数-终端名称
    idv_tm_name = "//*[@id='hostName']"
    # 终端编辑中各参数-终端分组
    idv_tm_group = "//*[@id='terminalGroup']"
    # 终端编辑中各参数-终端桌面类型
    idv_tm_desk_type = "//*[@id='restoreModel']"
    # 终端编辑中各参数-系统盘
    system_disk_size = "//*[@id='system_disk_size']"
    # 在线终端不能删除提示信息
    tips_text = "//div[@class='layui-layer-content layui-layer-padding']"

    # 获取终端产品系列
    def get_terminal_productserial(self, tm_name):
        self.click_idv_more_operate(tm_name)
        self.find_elem(self.detail_xpath).click()
        self.go_common_frame()
        a = self.get_elem_text(self.productid_xpath)
        serial = a[4:7]  # 截取产品系列
        print(u"终端的系列为：" + serial)
        return serial

    # 获取终端版本号
    def get_terminal_productversion(self):
        a = self.get_elem_text(self.hardwareVersion_xpath)
        version = a[1]
        print(u"终端的硬件版本为：" + version)
        return version

    # 关闭终端详情页面
    def close_terminal_detail(self):
        self.click_elem(self.submit_btn_xpath)

    # 根据镜像名称选择
    bang_img_name = "//div[contains(text(),'{}')]/..//preceding-sibling::div[@class='checkbox_item']"
    # 终端页面搜索终端名获取镜像
    terminal_img_xpath = "//*[@id='content_table_tableContent']//td[5]//span"

    # idv 新建分组选择修改镜像
    def idv_chose_img(self, img_name):
        self.go_common_frame()
        time.sleep(0.5)
        self.click_elem(self.idv_group_mirror_add_xpath)  # 点击添加
        fid = self.get_group_mirror_frame_id()
        self.get_ciframe(self.common_frame_xpath.format(fid))
        time.sleep(0.5)
        self.click_elem(self.bang_img_name.format(img_name))
        self.click_confirm()

    # 新建idv分组
    def idv_creat_group(self, name, img_name, desk_type=u'还原', size=40, other_set='open', white_list=None,
                        white_name=None):
        """默认桌面类型为还原，
        ::desk_type默认桌面类型为还原，传入参数个性可修改为个性类型
        ::size为系统盘大小，默认为40
        ::other_set 其他设置默认是开启的，传入参数close可关闭
        ::white_list 无线白名单默认为空,white_name无线白名单名称，传入内容为列表"""
        self.click_new_group()
        self.go_common_frame()
        self.find_elem(self.new_group_name_xpath).send_keys('{}'.format(name), Keys.ENTER)
        self.idv_chose_disk_type(desk_type)
        self.idv_chose_img(img_name)  # 选择镜像
        self.idv_set_disk_size(size)
        self.idv_other_set(other_set)
        if white_list is not None:
            self.idv_white_list_add(white_name)
        self.click_confirm()

    # 获取值
    def get_value(self, locator):
        return self.get_elem_text(locator)

    # 进入到终端分组frame
    def go_left_iframe(self):
        self.back_current_page()
        time.sleep(2)
        self.get_ciframe(self.all_page_iframe_id)

    btn_close_image = "//*[@id='btn_closeImage']"

    # idv-删除未分组绑定的镜像
    def del_weifenzu_imgisexit(self):
        self.go_common_frame()
        if self.elem_is_exist(self.btn_close_image) == 0:
            self.click_elem(self.btn_close_image)  # 解除镜像绑定
        self.click_elem(self.submit_btn_xpath)  # 点击确定
        self.back_current_page()
        self.click_elem(self.sure_xpath)  # 二次确认
        time.sleep(1)

    # 获取终端idv-ip
    def get_terminal_idv_ip(self, name):
        self.search_terminal(name)
        self.back_current_page()
        self.go_main_iframe()
        terminal_ip = self.get_elem_text(self.idv_ip_xpath.format(name))
        return terminal_ip

    # 当未分组未绑定镜像时，绑定镜像，
    def add_weifenzu_image(self, img_name=None):
        self.go_common_frame()
        if self.elem_is_exist(self.btn_close_image) == 1:  # 元素不存在，添加镜像
            self.idv_chose_img(img_name=img_name)  # 添加镜像
            self.go_common_frame()
        self.click_elem(self.submit_btn_xpath)  # 点击确定
        self.back_current_page()
        self.click_elem(self.sure_xpath)  # 二次确认

    terminal_idv_image = "//*[text()='{}']/ancestor::tr//td[5]//div"

    # 获取终端绑定镜像
    def get_terminal_img(self, name):
        self.search_terminal(name)
        self.back_current_page()
        self.go_main_iframe()
        terminal_image = self.get_elem_text(self.terminal_idv_image.format(name))
        print(terminal_image)
        return terminal_image

    terminal_idv_group = "//*[text()='{}']/ancestor::tr//td[4]//div"

    # 获取终端分组信息
    def get_terminal_group(self, name):
        self.search_terminal(name)
        terminal_group = self.get_elem_text(self.terminal_idv_group.format(name))
        print(terminal_group)
        return terminal_group

    # 创建不存在多用户&公用终端组
    def add_more_pub_tmgroup_notexist(self, name, img_name, desk_type=u'还原', size=40, other_set='open', white_list=None,
                                      white_name=None):
        self.back_current_page()
        self.go_left_iframe()
        if name not in self.get_elem_text(self.all_group):
            self.idv_creat_group(name, img_name, desk_type=desk_type, size=size, other_set=other_set,
                                 white_list=white_list, white_name=white_name)

    # 点击单用户终端组
    def click_single_group(self):
        self.go_left_iframe()
        self.click_elem("//*[@id='SINGLE']")

    # 点击多用户终端组
    def click_mult_group(self):
        self.go_left_iframe()
        self.click_elem("//*[@id='MULT']")

    # 终端分组下-未绑定用户终端组
    unband_user_xpath = u"//span[contains(text(),'未绑定用户终端组')]"
    image_name_xpath = u"//*[contains(@id,'image')]"
    close_btns = u"//*[@id='btns_ok']"

    # 查看单用户终端分组详情
    def get_detailBtn(self):
        self.scroll_into_view(self.unband_user_xpath, click_type=1)
        self.chainstay(self.unband_user_xpath)
        self.click_elem(u"//*[@id='detailBtn_-2']")  # 点击详情
        self.back_current_page()
        self.go_common_frame()
        return self.get_elem_text(self.image_name_xpath)  # 获取绑定镜像名称

    # 获取终端状态
    terminal_idv_status = "//*[text()='{}']/ancestor::tr//td[11]//div"

    def get_terminal_status(self, name):
        self.search_terminal(name)
        terminal_status = self.get_elem_text(self.terminal_idv_status.format(name))
        return terminal_status

    # 刷新按钮
    refresh_btn = "//*[@id='btn_refresh']"

    # 点击刷新
    def click_refresh(self):
        self.go_main_iframe()
        self.click_elem(self.refresh_btn)

    terminal_idv_desk_type = "//*[text()='{}']/ancestor::tr//td[10]//div"

    # 获取终端桌面类型
    def get_terminal_desk_type(self, name):
        self.search_terminal(name)
        self.back_current_page()
        self.go_main_iframe()
        desk_type = self.get_elem_text(self.terminal_idv_desk_type.format(name))
        print(desk_type)
        return desk_type

    # 多用户&公用终端组
    all_group = "//*[@id='all_group']"

    # 删除已存在的分组
    def del_gp_exist(self, name):
        self.back_current_page()
        time.sleep(0.5)
        self.go_left_iframe()
        if name in self.get_elem_text(self.all_group):
            time.sleep(0.5)
            self.chainstay(self.group_name_xpath.format(name))
            self.click_elem(self.vdi_group_delete_xpath.format(name))
            self.click_sure()
            self.back_current_page()
            self.get_ciframe(self.all_page_iframe_id)
            time.sleep(0.5)
            flag = 0
            self.send_passwd_confirm(pd=passwd)
            flag = 1
            return flag
            # self.delete_group(name)
        self.back_current_page()

    # 根据终端名称搜索并点击编辑
    def search_tm_click_edit(self, tm_name):
        self.search_terminal(tm_name)
        self.click_idv_more_operate(tm_name)
        self.click_idv_edit(tm_name)
        self.go_common_frame()

    #  跳转到idv终端管理多用户&公用终端组
    def goto_idv_terminal_single_terminal_group_page(self):
        time.sleep(1)
        self.get_ciframe("frameContent")
        self.click_elem(self.single_user_page_xpath)
        self.back_current_page()

    # 跳转到所用户&公用户页面
    def goto_idv_terminal_moreandpub_terminal_group_page(self):
        time.sleep(2)
        self.get_ciframe("frameContent")
        self.click_elem(self.mul_user_page_xpath)
        self.back_current_page()

    # 获取单用户终端组的信息
    single_gp_xpath = "//*[text()='{}']/ancestor::tr//td[5]//div"

    def get_single_tm_gp(self, name):
        self.search_terminal(name)
        terminal_gp = self.get_elem_text(self.single_gp_xpath.format(name))
        return terminal_gp

    single_img_xpath = u"//*[text()='{}']/ancestor::tr//td[6]//div"

    # 获取单用户终端组的镜像
    def get_single_tm_image(self, tm_name):
        self.search_terminal(tm_name)
        terminal_img = self.get_elem_text(self.single_img_xpath.format(tm_name))
        return terminal_img

    single_tm_ip_xpath = u"//*[text()='{}']/ancestor::tr//td[8]//div"

    # 获取单用户终端的ip
    def get_single_tm_ip(self, tm_name):
        print self.single_tm_ip_xpath.format(tm_name)
        terminal_ip = self.get_elem_text(self.single_tm_ip_xpath.format(tm_name))
        return terminal_ip

    moreandpub_tm_ip_xpath = u"//*[text()='{}']/ancestor::tr//td[7]//div"

    # 获取多用户、公用终端的ip
    def get_moreandpub_tm_ip(self, tm_name):
        print self.single_tm_ip_xpath.format(tm_name)
        terminal_ip = self.get_elem_text(self.single_tm_ip_xpath.format(tm_name))
        return terminal_ip

    single_tm_desk_type_xpath = u"//*[text()='{}']/ancestor::tr//td[9]//div"

    # 获取单用户终端组的云桌面ip
    def get_single_tm_desk_type(self, tm_name):
        terminal_desk_type = self.get_elem_text(self.single_tm_desk_type_xpath.format(tm_name))
        return terminal_desk_type

    # 获取多用户胖终端桌面IP
    def get_single_tm_desk_type_bytm_ip(self, tm_ip):
        self.back_current_page()
        self.go_main_iframe()
        return self.get_elem_text(self.single_tm_desk_type_xpath.format(tm_ip))


    # 提示信息
    def get_tips_text(self):
        return self.get_elem_text(self.tips_text)

    # 点击取消按钮
    def click_cancel_button(self):
        self.click_elem(self.cancel_button_xpath)
        self.back_current_page()

    # 还原镜像
    restore_image = "//*[@id='batchRecoverTerminalImage']"
    # 全局-更多按钮
    more_xpath = "//*[contains(@id,'reboot_terminal')]/..//*[contains(@class,'moreActions')]"

    # 还原镜像
    def restore_img(self, name):
        self.search_terminal(name)
        self.click_elem(self.check_box_xpath.format(name))
        self.click_elem(self.more_xpath)
        time.sleep(1)
        self.find_elem('//div[@id="batchRecoverTerminalImage"]').click()
        self.back_current_page()
        self.click_elem(self.confirm_reboot_xpath)
        time.sleep(1)
        flag = 0
        self.send_passwd_confirm(pd=passwd)
        flag = 1
        time.sleep(1)
        self.click_elem(self.sure_xpath)
        return flag

    # 单用户终端绑定用户按钮
    bingding_xpath = u"//div[text()='绑定']"
    user_dingd = "//*[@id='userId12']"

    # 单用户终端绑定用户
    def single_bingding_user(self, tm_name, user_name):
        self.search_terminal_anayway(name=tm_name, ty=1)
        if self.elem_is_exist(self.remove_bingding_xpath) == 0:  # 单用户终端绑定用户，先进行解绑
            self.remove_bingding_user(tm_name)
            self.back_current_page()
            self.go_main_iframe()
        self.search_terminal(tm_name)
        self.click_elem(self.bingding_xpath)
        self.go_common_frame()
        self.find_elem(self.user_dingd).send_keys(user_name)
        self.click_elem(self.confirm_xpath)  # 点击确定
        time.sleep(4)

    # 单用户终端绑定用户按钮
    remove_bingding_xpath = u"//div[text()='解绑']"

    # 单用户终端取消绑定
    def remove_bingding_user(self, tm_name):
        self.search_terminal(tm_name)
        self.click_elem(self.remove_bingding_xpath)
        self.go_common_frame()
        self.click_elem(self.confirm_xpath)
        self.send_passwd_confirm(pd=passwd)
        time.sleep(3)

    # 点击编辑按钮获取获取终端属性
    def get_terminal_attribute(self, locator, attribute):
        self.go_common_frame()
        time.sleep(0.5)
        return self.get_elem_attribute(locator=locator, attribute=attribute)

    # 终端mac
    tm_mac = u"//*[text()='{}']//ancestor::tr//td[6]/div"

    # 获取终端MAC(多用户)
    def get_idv_mac(self, tm_name):
        self.search_terminal(tm_name)
        self.back_current_page()
        self.go_main_iframe()
        return self.get_elem_text(self.tm_mac.format(tm_name))

    # 终端mac-单用户
    tm_mac_single = u"//*[text()='{}']//ancestor::tr//td[7]/div"

    # 获取终端MAC(多用户)
    def get_idv_mac_single(self, tm_name):
        self.search_terminal(tm_name)
        self.back_current_page()
        self.go_main_iframe()
        return self.get_elem_text(self.tm_mac_single.format(tm_name))

    # 还原云桌面
    restore_cd_xpath = u"//div[@title='还原云桌面']"

    # 还原云桌面
    def restore_cloud_desk(self, name):
        self.search_terminal(name)
        self.click_idv_more_operate(name)
        self.click_elem(self.restore_cd_xpath)  # 点击还原云桌面
        self.back_current_page()
        self.click_elem(self.confirm_reboot_xpath)
        time.sleep(1)
        flag = 0
        self.send_passwd_confirm(pd=passwd)
        flag = 1
        time.sleep(0.5)
        self.click_elem(self.sure_xpath)
        return flag

    clear_d = u"//div[@title='D盘清空']"

    # 清空D盘
    def clear_Ddisk(self, tm_name):
        self.search_terminal(tm_name)
        self.click_idv_more_operate(tm_name)
        self.click_elem(self.clear_d)  # 点击清空D盘操作
        self.back_current_page()
        self.click_elem(self.sure_xpath)
        flag = 0
        self.send_passwd_confirm(pd=passwd)
        flag = 1
        return flag

    tableContent_xpath = '//*[@id="content_table_tableContent"]'

    #  搜索终端名称后，获取搜索后的信息
    def getinfo_by_search_after(self):
        return self.get_elem_text(self.tableContent_xpath)

    tm_gp = u"//*[@class='navLeft']//*[contains(text(),'{}')]"

    # 将某个终端组中的所有终端关机
    def click_tm_gp_and_close_tm(self, group_name):
        self.get_ciframe(self.all_page_iframe_id)
        self.scroll_into_view(self.tm_gp.format(group_name))
        self.get_ciframe(self.main_page_iframe_id)
        self.click_elem(self.select_all_terminal_xpath)  # 点击全选
        self.go_main_iframe()
        self.click_elem(self.vdi_terminal_close_xpath)
        self.back_current_page()
        self.click_elem(self.confirm_reboot_xpath)
        time.sleep(1)
        self.click_elem(self.confirm_reboot_xpath)

    terminal_log = u"//div[contains(text(),'终端日志')]"
    download_log = u"//span[@title='点击下载日志']"
    # 终端日志下载后关闭
    btns_close = u"//*[@id='btns_close']"

    #  搜集终端日志
    def search_terminal_log(self, name):
        self.search_terminal(name)
        self.click_idv_more_operate(name)
        self.find_elem(self.terminal_log).click()
        time.sleep(5)
        self.back_current_page()
        self.go_common_frame()
        self.click_elem(self.download_log)
        self.download()  # 点击下载
        self.click_elem(self.btns_close)  # 点击关闭

    # ip设置
    ip_set_xpath = u"//div[@title='IP设置']"
    # 终端网络配置-点击自动获取ip单选框
    tm_ip_auto_radio = u"//div[contains(text(),'终端网络配置')]/..//following-sibling::div[1]//span"
    # 终端网络配置-点击使用下面的IP地址单选框
    tm_ip_set_radio = u"//div[contains(text(),'终端网络配置')]/..//following-sibling::div[2]//span"
    # ip 输入框
    ip_send_text = "//*[@id='ip']"
    ip_send_text1 = "//*[@id='vm_ip']"
    # 云桌面网络配置-点击自动获取ip单选框
    cd_ip_auto_radio = u"//div[contains(text(),'云桌面网络配置')]/..//following-sibling::div[1]//span"
    # 云桌面网络配置-点击使用下面的IP地址单选框
    cd_ip_set_radio = u"//div[contains(text(),'云桌面网络配置')]/..//following-sibling::div[2]//span"

    # 修改终端ip和设置云桌面ip
    def terminal_ip_set(self, tm_name, terminal_ip=None, cd_ip=None):
        self.search_terminal(tm_name)
        self.click_idv_more_operate(tm_name)
        self.click_elem(self.ip_set_xpath)  # 点击ip设置
        self.go_common_frame()
        if terminal_ip != None:
            self.click_elem(self.tm_ip_set_radio)  # 点击设置ip地址
            self.clear_text_info(self.ip_send_text)  # 清除文本信息
            self.find_elem(self.ip_send_text).send_keys(terminal_ip)
        else:
            self.click_elem(self.tm_ip_auto_radio)  # 点击自动获取ip
        self.scroll_into_view(self.cd_ip_auto_radio, click_type=1)  # 鼠标滚动到当前位置
        if cd_ip != None:
            self.click_elem(self.cd_ip_set_radio)  # 点击设置ip地址
            self.clear_text_info(self.ip_send_text1)  # 清除文本信息
            self.find_elem(self.ip_send_text1).send_keys(cd_ip)
        else:
            self.click_elem(self.cd_ip_auto_radio)
        self.click_elem(self.submit_btn_xpath)  # 点击确定

    # 将某个终端组中的所有终端重启
    def click_tm_gp_and_reboot_tm(self, group_name):
        self.get_ciframe(self.all_page_iframe_id)
        self.scroll_into_view(self.tm_gp.format(group_name))
        self.get_ciframe(self.main_page_iframe_id)
        self.click_elem(self.select_all_terminal_xpath)  # 点击全选
        self.go_main_iframe()
        self.click_elem(self.reboot_button_xpath)  # 点击重启
        self.back_current_page()
        self.click_elem(self.confirm_reboot_xpath)
        time.sleep(1)
        self.click_elem(self.confirm_reboot_xpath)

    # 将某个终端组中的所有终端删除
    def click_tm_gp_and_del_tm(self, group_name):
        self.get_ciframe(self.all_page_iframe_id)
        self.scroll_into_view(self.tm_gp.format(group_name))
        self.get_ciframe(self.main_page_iframe_id)
        self.click_elem(self.select_all_terminal_xpath)  # 点击全选
        self.click_elem(self.more_xpath)
        time.sleep(1)
        self.find_elem('//div[@id="delete_terminal"]').click()  # 点击删除按钮
        self.back_current_page()
        self.click_elem(self.confirm_reboot_xpath)
        time.sleep(1)
        flag = 0
        self.send_passwd_confirm(pd=passwd)
        flag = 1
        return flag

    # 设置终端模式
    login_type = "//*[@id='loginType']"

    # 变更某个终端组所有终端
    def click_tm_gp_and_change_tm_type(self, group_name, terminal_type):
        self.click_gp_modify_tmtype(group_name)
        self.go_common_frame()
        self.select_list_chose(locator=self.login_type, text=terminal_type)  # 设置终端模式
        self.click_elem(self.submit_btn_xpath)  # 设置终端模式-确定
        self.back_current_page()
        self.click_elem(self.confirm_reboot_xpath)  # 提示信息-确定
        time.sleep(1)
        flag = 0
        self.send_passwd_confirm(pd=passwd)
        flag = 1
        return flag

    # 点击终端组，变更终端模式
    def click_gp_modify_tmtype(self, group_name):
        self.get_ciframe(self.all_page_iframe_id)
        self.scroll_into_view(self.tm_gp.format(group_name))
        self.get_ciframe(self.main_page_iframe_id)
        self.click_elem(self.select_all_terminal_xpath)  # 点击全选
        self.click_elem(self.more_xpath)
        time.sleep(1)
        self.find_elem('//div[@id="set_login_type"]').click()  # 点击变更终端模式
        self.back_current_page()

    # 搜索用户变更终端模式
    def click_change_tm_type(self, tm_name):
        self.search_terminal(tm_name)
        self.go_main_iframe()
        self.click_elem(self.select_all_terminal_xpath)  # 点击全选
        self.click_elem(self.more_xpath)
        time.sleep(1)
        self.find_elem('//div[@id="set_login_type"]').click()  # 点击变更终端模式

    """=====================访客登入设置============================="""
    # idv访客登入设置按钮xpaht
    guest_login_set_xpath = '//*[@id="set_guest_login_type"]'
    # idv访客登入设置开启和禁用下拉xpath
    guest_login_set_chose_xpath = "//*[@id='guestLoginType']"
    # vdi访客登入按钮xpath
    vdi_guest_set_xpath = "//*[contains(text(),'访客登录')]"
    # 未分组xpath
    used_group_xpath = u"//div[@id='all_group']//*[contains(text(),'{}')]"
    # idv终端访客登入详情的
    guest_set_info_xpath = '//*[@id="guest_login_status"]'

    def click_guest_login_set(self, name, chose_user=1, chose_type=u'启用'):
        """用户访客登入权限设置
        chose_user 为1时输入用户名为2时输入是组名
        """
        if chose_user == 1:
            self.search_terminal(name)
            self.chose_user(name)
        elif chose_user == 2:
            self.back_current_page()
            self.get_ciframe(self.all_page_iframe_id)
            self.click_elem(self.used_group_xpath.format(name))
            self.get_ciframe(self.main_page_iframe_id)
            self.click_elem(self.select_all_terminal_xpath)
        self.click_elem(self.more_xpath)
        self.click_elem(self.guest_login_set_xpath)
        self.go_common_frame()
        time.sleep(0.3)
        if chose_type == u'启用':
            self.select_list_chose(self.guest_login_set_chose_xpath, u'启用')
        elif chose_type == u'禁用':
            self.select_list_chose(self.guest_login_set_chose_xpath, u'禁用')
        else:
            logging.error("输入的启用方式有误")
        self.click_elem(self.confirm_xpath)
        self.back_current_page()
        self.click_elem(self.sure_xpath)
        self.send_passwd_confirm()

    def vdi_page_exist_guest_set_button(self):
        """返回瘦终端页面是否存在访客设置按钮"""
        return self.elem_is_exist(self.vdi_guest_set_xpath)

    def get_group_all_user(self, name):
        """获取用户组的所有终端IP和云桌面IP"""
        self.go_main_iframe()
        time.sleep(1)
        group_ip_dic = dict()
        elements = self.find_presence_elems(self.idv_ip_xpath.format(name))
        for elem in elements:
            group_ip_dic[elem.text] = self.get_elem_text(self.idv_desk_ip_xpath.format(elem.text))
        return group_ip_dic

    def get_idv_guest_set_info(self, name):
        """获取终端访客登入开启信息"""
        self.click_elem(self.idv_more_operate_xpath.format(name))
        self.click_elem(self.idv_info_xpath.format(name))
        self.go_common_frame()
        return self.get_elem_text(self.guest_set_info_xpath)

    status_info = u"//*[@id='content_table_tableContent']//tr[{}]//td[11]"
    offline_name_xpath = u"//*[@id='content_table_tableContent']//tr[{}]//td[2]"

    def get_offline_tm(self):
        """获取所有离线终端信息"""
        self.go_main_iframe()
        offline_tm = []
        total_count = int(self.get_value(self.total_count_xpath))
        for i in range(1, total_count + 1):
            text_info = self.get_value(self.status_info.format(i))
            if text_info == u"离线":
                offline_name = self.get_value(self.offline_name_xpath.format(i))
                offline_tm.append(offline_name)
            i += 1
        return offline_tm

    terminal_idv_single_status = "//*[text()='{}']/ancestor::tr//td[12]//div"

    def wait_tm_reboot_success(self, name, tm=0):
        """
        tm=0:代表单用户终端组下的终端
        tm!=0:代表多用户&公用终端组下的终端
        """
        self.back_current_page()
        self.click_refresh()  # 点击刷新
        self.back_current_page()
        self.search_terminal(name)
        if tm == 0:
            terminal_status = self.get_elem_text(self.terminal_idv_single_status.format(name))
        else:
            terminal_status = self.get_terminal_status(name=name)
        n = 1
        while n < 35:
            if u"在线" in terminal_status:
                break
            else:
                self.click_refresh()  # 点击刷新
                self.back_current_page()
                self.search_terminal(name)
                if tm == 0:
                    terminal_status = self.get_elem_text(self.terminal_idv_single_status.format(name))
                else:
                    terminal_status = self.get_terminal_status(name=name)
                time.sleep(3)
            n = n + 1
        while n > 35:
            raise NotImplementedError(u"终端已离线")

    # 变更分组xpath
    change_vdi_group_xpath = u"//*[contains(text(),'变更分组')]"

    def chang_vdi_group(self, name, group):
        """用户管理修改用户分组"""
        self.go_main_iframe()
        self.chose_user(name)
        self.click_elem(self.change_vdi_group_xpath)
        time.sleep(0.3)
        self.vdi_new_group_info(group)


if __name__ == "__main__":
    IdvPage.convert_size(IdvPage(BasicFun), 'SIZE    42423283712 ')
