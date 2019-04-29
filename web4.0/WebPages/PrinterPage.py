#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chenyilin && LinMengYao
@contact: chenyilin@ruijie.com
@software: PyCharm
@time: 2019/03/05 12:27
"""
import random
import time
import uiautomation as automation
from selenium.webdriver import ActionChains
from Common.Basicfun import BasicFun
from selenium.webdriver.common.keys import Keys
from Common.terminal_action import *
from TestData.Printermangerdata import *
from WebPages.LoginPage import Login
from WebPages.patchUpgradePage import *
import logging
from LoginPage import *

from Common.Basicfun import BasicFun


class PrinterPage(BasicFun):
    # 点击高级配置
    Advanced_xpath = u"//*[@class='el-submenu__title']//*[text()='高级配置']"
    # 点击打印机管理
    printer_manager_xpath = u"//*[@role='menuitem']//*[text()='打印机管理']"
    # 删除打印机
    delete_printer_xpath = '//*[@class="el-icon-delete"]/parent::button'
    # 删除时提示请选择一条数据
    delete_err_msg_xpath = "//*[@class='el-message el-message--warning']"
    # 获取所有打印机信息
    all_printer_info_xpath = "//tbody"

    # 编辑按钮
    edit_printer_button_xpath = u"//*[text()='编辑']/parent::button"
    # 打印机全选按钮
    choose_all_printer_xpath = "//*[@class='has-gutter']//*[@class='el-checkbox']"
    # 取消全选
    cancel_all_printer_xpath = "//*[@class='has-gutter']//*[@class='el-checkbox__input is-checked']"
    # 点击取消
    cancel_button_xpath = u"//*[contains(text(),'取消')]/parent::button"
    # 点击删除
    delete_button_xpath = u"//div[@class='el-message-box']//span[contains(.,'删除')]"
    # 点击确认
    confire_button_xpath = u"//span[contains(.,'确认')]/parent::button"
    # 获取选中的打印机数
    get_printer_num_xpath = "//*[@class='el-message-box__message']"
    # 点击选择一页多少条数据的下拉框
    page_printer_drop_down_xpath = "//*[@class='el-select__caret el-input__icon el-icon-arrow-up']"
    # 收起下拉框
    close_page_printer_num_xpath = "//*[@class='el-input__suffix-inner']"
    # 获取下拉框选中的数据
    get_page_printer_num_xpath = "//*[@class='el-select-dropdown__item selected hover']"
    # 搜索框
    search_text_xpath = "//*[@class='filter-item el-input el-input--suffix']//*[@class='el-input__inner']"
    # 搜索按钮
    search_button_xpath = "//*[@class='filter-item el-input el-input--suffix']//*[@class='el-input__suffix']"
    # 配置名称文本框
    config_name_input_xpath = u"//*[@class='el-dialog__body']//*[contains(text(),'配置名称')]/parent::div//input"
    # 备注文本框
    beizhu_input_xpath = u"//*[@class='el-dialog__body']//*[contains(text(),'备注')]/parent::div//textarea"
    # 关闭按钮
    close_button_xpath = "//*[@class='el-dialog__headerbtn']"
    # 确认按钮
    confirm_button_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"
    # 确定按钮
    confirm_xpath = "//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']"
    # 确定初始化配置
    confirm_init_config_btn_xpath = u"//*[@id='btns_ok']"
    # 打印机选中框
    choose_bar_xpath = "//div[contains(text(),'%s')]/../..//td[1]//label"
    # 确认密码
    confirm_passwd_xpath = "//input[@type='password']"
    # 信息条数
    total_count_xpath = "//span[@class='el-pagination__total']"
    # 内容列表
    content_list_xpath = "//td[%s]//div[contains(@class,'cell')]"
    # 打印机型号列表
    printer_model_list_xpath = "//td[3]//div[@class='cell el-tooltip']"
    # 顺序按钮
    seque_btn_xpath = u"//div[contains(text(),'%s')]/.."

    # 查看详情
    detail_info_xpath = u"//*[text()='详情']/parent::button"
    # 详细信息
    info_xpath = u"//*[@class='el-dialog__body']//*[contains(text(),'{0}')]/parent::div//span"
    # 关闭打印机配置管理
    close_printer_config_xpath = u"//*[contains(text(),'关闭打印机配置管理')]/ancestor::button"
    # 开启打印机管理
    open_printer_xpath = "//*[@class='open-view__body__foot-text']"
    #   跳转到用户管理页面xpath
    user_manage_xpath = "//*[@class='fa fa-user-circle']"
    # 选择一页显示多少打印机
    choose_page_printer_num_xpath = u"//*[@class='el-scrollbar__view el-select-dropdown__list']//*[contains(text(),'{}')]/parent::li"
    # 获取一页显示多少打印机
    get_page_printer_num = "//*[@class='el-scrollbar__view el-select-dropdown__list']//*[@class='el-select-dropdown__item selected']//span"
    # 下一页
    next_page_xpath = "//*[@class='btn-next']"
    # 上页
    prev_page_xpath = "//*[@class='btn-prev']"
    # 获取每页的打印机条数
    real_page_printer_xpath = "//tr"
    # 总页数
    page_num_xpath = "//*[@class='span-simple-pager']"
    # 初始化配置向导
    init_xpath = u"//*[@class='sk-navbar__items']//*[contains(text(),'初始化配置向导')]"
    # 将要查找的用户名填入text中
    find_username_xpath = "//*[@class='fl']//*[@class='el-input__inner']"
    # 查找按钮
    find_button_xpath = "// *[@class ='fl'] // *[@ class ='el-input__icon sk-icon-search sk-toolbar__icon el-tooltip item']"
    # 更多
    cdesk_more_operate = u"//*[contains(text(),'{0}')]/ancestor::tr//button"
    # 云桌面关机
    close_vdi_xpath = u"//li[contains(text(),'关机')]"
    # 确认关机
    confirm_close_button_xpath = u"//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']//*[contains(text(),'关机')]"
    # 保存
    keep_config_btn_xpath = u"//*[@value='保存']"
    # 确认初始化配置成功
    init_config_succ_btn = u"//*[contains(text(),'初始化配置向导成功，服务器将要重启，预计2-5分钟之后重启成功，请稍后重新登录。')]"
    # 用户名输入框
    username_input_xpath = "//*[@name='userName']"
    # 密码输入框
    passwd_input_xpath = "//*[@name='pwd']"
    # 登入按钮
    login_button_xpath = "//button[@type='button']"
    # iframe
    iframe_xpath = u"//iframe[@id='frameContent']"
    # 关闭RAID
    close_raid_xpath=u"//*[@id='configNavigationForm:isRaid']"



    def goto_printermanger_page(self):
        """进入打印机管理"""
        self.click_elem(self.Advanced_xpath)
        time.sleep(0.5)
        self.click_elem(self.printer_manager_xpath)
        time.sleep(0.5)

    def click_delete_printer(self):
        """点击删除打印机"""
        self.click_elem(self.delete_printer_xpath)

    def get_delete_printer_error_msg(self):
        """获取删除失败的提示信息"""
        try:
            return self.find_elem(self.delete_err_msg_xpath)
        except:
            return ''

    def get_all_printer_info(self):
        """获取页面上所有打印机信息"""
        return self.get_elem_text(self.all_printer_info_xpath)

    def choose_all_printer(self):
        """打印机全选"""
        self.click_elem(self.choose_all_printer_xpath)

    def cancel_choose_all_printer(self):
        """取消打印机全选"""
        self.click_elem(self.cancel_all_printer_xpath)

    def click_cancel_delete_printer(self):
        """点击取消删除"""
        self.click_elem(self.cancel_button_xpath)

    def get_printer_num(self):
        """获取选中的打印机个数"""
        text = self.get_elem_text(self.get_printer_num_xpath)
        text = re.findall("\d+", text)[0]
        return text

    def close_page_printer_num(self):
        """收起下拉框"""
        time.sleep(1)
        self.click_elem(self.close_page_printer_num_xpath)
        time.sleep(1)

    def edit_text(self, locator, text=''):
        """修改文本框"""
        time.sleep(1)
        self.find_elem(locator).click()
        time.sleep(1)
        self.find_elem(locator).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(locator).send_keys(text)
        return text

    def get_first_printer(self):
        """获取第一个打印机的配置名"""
        text = self.get_elem_text(self.all_printer_info_xpath)
        text = text[1:7]
        print text
        return text

    def search_a_printer(self, name):
        """搜索打印机"""
        self.edit_text(self.search_text_xpath, name)
        time.sleep(1)
        self.click_elem(self.search_button_xpath)
        time.sleep(2)

    def clear_search_text(self):
        """清空打印机"""
        self.edit_text(self.search_text_xpath)
        time.sleep(1)

    def edit_a_printer(self, name=None, beizhu=None):
        """编辑打印机"""
        self.click_elem(self.edit_printer_button_xpath)
        time.sleep(3)
        if name != None:
            self.edit_text(self.config_name_input_xpath, name)
            time.sleep(2)
        if beizhu != None:
            self.edit_text(self.beizhu_input_xpath, beizhu)
            time.sleep(2)
        if name != None or beizhu != None:
            self.click_elem(self.confirm_button_xpath)
            time.sleep(1)
            self.click_elem(self.confirm_xpath)
        if name == None and beizhu == None:
            self.click_elem(self.close_button_xpath)

    def get_detail_info(self):
        """获取打印机详细信息"""
        info = [0, 0, 0, 0, 0, 0]
        self.click_elem(self.detail_info_xpath)
        time.sleep(1)

        info[0] = self.get_elem_text(self.info_xpath.format(u'配置名称'))
        info[1] = self.get_elem_text(self.info_xpath.format(u'备注'))
        info[2] = self.get_elem_text(self.info_xpath.format(u'打印机模式'))
        info[3] = self.get_elem_text(self.info_xpath.format(u'打印机型号'))
        info[4] = self.get_elem_text(self.info_xpath.format(u'配置上传时间'))
        # info[5] = self.get_elem_text(self.info_xpath.format(u'上传配置的终端'))
        self.click_elem(self.close_button_xpath)
        time.sleep(1)
        return info

    def close_printer_config(self):
        """点击关闭打印机配置管理并确定"""
        self.click_elem(self.close_printer_config_xpath)
        time.sleep(1)
        self.click_elem(self.confirm_xpath)
        time.sleep(1)

    def send_passwd_confirm(self, pd=c_pwd):
        """输入密码点击确定"""
        self.find_elem(self.confirm_passwd_xpath).send_keys(pd)
        time.sleep(1)
        self.find_elem(self.confirm_button_xpath).click()

    def open_printer(self):
        """开启打印机管理"""
        self.click_elem(self.open_printer_xpath)

    def goto_usermanage_page_to_printer_page(self):
        """#跳转到用户管理页面在再跳转到打印机页面"""
        self.find_elem(self.user_manage_xpath).click()
        time.sleep(2)
        self.click_elem(self.printer_manager_xpath)

    def login_backup_pc(self):
        """登录备机查看打印机配置管理菜单"""
        try:
            self.goto_printermanger_page()
            flag = 1
        except:
            flag = 0

        return flag

    def choose_page_printer_num(self, num=None):
        """选择一页显示多少台打印机"""
        printer_num = [0, 0]
        self.click_elem(self.page_printer_drop_down_xpath)
        time.sleep(2)
        printer_num[0] = int(self.get_elem_text(self.get_page_printer_num))
        if num != None:
            if num > 0 and num <= 10:
                num = 10
            if num > 10 and num <= 20:
                num = 20
            if num > 20 and num <= 30:
                num = 30
            if num > 30 and num <= 50:
                num = 50
            printer_num[1] = num
            self.click_elem(self.choose_page_printer_num_xpath.format(num))
        else:
            self.close_page_printer_num()
        time.sleep(1)
        return printer_num

    def check_page(self):
        """点击上页下页"""
        flag = [0, 0, 0, 0]
        old_text = self.get_all_printer_info()
        old_now_page = self.get_now_page()
        time.sleep(1)
        self.click_elem(self.next_page_xpath)
        time.sleep(1)
        new_now_page = self.get_now_page()
        next_text = self.get_all_printer_info()
        time.sleep(1)
        self.click_elem(self.prev_page_xpath)
        time.sleep(1)
        prev_text = self.get_all_printer_info()
        if old_text != next_text:
            # 点击下一页是否正常（1：正常）
            flag[0] = 1
        if next_text != prev_text:
            # 点击上一页是否正常（1：正常）
            flag[1] = 1
        if old_text == prev_text:
            # 返回原页面是否正常（1：正常）
            flag[2] = 1
        if old_now_page != new_now_page:
            # 当前所在页面发生变化（1：正常）
            flag[3] = 1
        time.sleep(1)
        return flag

    def real_page_printer_num(self):
        """获取一页真实的打印机条数"""
        real_num = len(self.find_elems(self.real_page_printer_xpath))-1
        return real_num

    def get_page_num(self):
        """获取总页数"""
        num = self.get_elem_text(self.page_num_xpath)
        num = num.split('/')[1]
        num = re.findall("\d+", num)[0]
        return num

    def get_now_page(self):
        """获取当前在第几页"""
        num = self.get_elem_text(self.page_num_xpath)
        num = num.split('/')[0]
        num = re.findall("\d+", num)[0]
        return num

    def click_confirm_delete_printer(self):
        """点击确认删除"""
        self.click_elem(self.delete_button_xpath)

    def choose_a_printer(self, name):
        """选中某台打印机"""
        time.sleep(com_slp)
        self.click_elem(self.choose_bar_xpath % name)
        time.sleep(com_slp)

    def confirm_passwd(self):
        """删除时确认密码"""
        self.elem_send_keys(self.confirm_passwd_xpath, passwd)

    def click_confire(self):
        """点击确认"""
        self.click_elem(self.confire_button_xpath)

    def total_count(self):
        """信息总条数"""
        return int(re.findall(r'\d+', self.get_elem_text(self.total_count_xpath))[0])

    def get_config_content(self, seque, name):
        """在数据库中以升序或降序的方式取配置信息名称"""
        if seque == 'asc':
            return server_sql_qurey(vm_ip,
                                    r"select %s from fusion_printer_manager order by %s asc" % (name, name))
        elif seque == 'desc':
            return server_sql_qurey(vm_ip,
                                    r"select %s from fusion_printer_manager order by %s desc" % (name, name))

    def get_list_content(self, path):
        """取某一列所有文本信息"""
        elems = self.find_elems(self.content_list_xpath % path)
        list = []
        for i in range(len(elems)):
            temp = elems[i].text
            list.append(temp)
        return list

    # 点击顺序按钮
    def click_seque(self, btn):
        self.click_elem(self.seque_btn_xpath % btn)

    def judge_seque(self, btn):
        """判断升序还是降序"""
        if self.get_elem_attribute(self.seque_btn_xpath % btn, 'class').__contains__('ascending'):
            return 'asc'
        elif self.get_elem_attribute(self.seque_btn_xpath % btn, 'class').__contains__('descending'):
            return 'desc'

    def translate_mode(self, list_mode):
        """转换打印机模式"""
        list = []
        for temp in list_mode:
            if temp.__contains__(u'本地打印机'):
                list.append('L')
            elif temp.__contains__(u'网络打印机'):
                list.append('N')
            elif temp.__contains__(u'共享打印机'):
                list.append('S')
        return list

    def translate_time(self, list_time):
        """转换时间格式"""
        time = []
        for temp in list_time:
            templist = []
            templist = re.split(r'\W+', temp)
            str = ''.join(templist[::1])
            time.append(str)
        return time

    def init_printer(self):
        """初始化配置"""
        self.click_elem(self.init_xpath)
        time.sleep(1)
        self.click_elem(self.confirm_xpath)
        time.sleep(1)

    def refresh_webdriver(self):
        """刷新服务器"""
        self.driver.refresh()

    def get_open_printer_button(self):
        """找开启打印机管理的按钮"""
        try:
            return self.elem_is_exist(self.open_printer_xpath)
        except:
            return ''

    def find_user(self, username):
        """查找用户"""
        self.find_elem(self.find_username_xpath).click()
        self.edit_text(self.find_username_xpath, username)
        self.find_elem(self.find_button_xpath).click()

    def close_vdi_desktop(self, user, passwd=c_pwd):
        """关闭vdi云桌面"""
        self.find_user(user)
        time.sleep(1)
        self.find_elem(self.cdesk_more_operate.format(user)).click()
        time.sleep(1)
        self.find_elem(self.close_vdi_xpath).click()

        time.sleep(1)
        self.find_elem(self.confirm_close_button_xpath).click()

        self.send_passwd_confirm(passwd)


    def init_wait(self):
        """查看初始化是否完成"""
        flag = 0
        for i in range(1, 180):
            time.sleep(10)
            if self.elem_is_exist(self.passwd_input_xpath) == 0:
                flag = 1
                break
        return flag

    def click_keep_config(self):
        """点击保存"""
        self.get_ciframe(self.find_elem(self.iframe_xpath))
        # ele = self.find_elem(self.keep_config_btn_xpath)
        # ActionChains(self.driver).move_to_element(ele).perform()
        self.scroll_into_view(self.close_raid_xpath)
        time.sleep(2)
        self.click_elem(self.keep_config_btn_xpath)
        time.sleep(5)
        self.click_elem(self.confirm_init_config_btn_xpath)

    # 登入
    def admin_login(self, name=c_user, pwd=c_pwd):
        self.find_elem(self.username_input_xpath).send_keys(name)
        self.find_elem(self.passwd_input_xpath).send_keys(pwd)
        self.find_elem(self.login_button_xpath).click()


if __name__ == "__main__":
    print server_sql_qurey('172.21.112.172', "select * from fusion_printer_manager")
