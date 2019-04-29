#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/8/26 14:49
"""
from Common.Basicfun import BasicFun
from TestData.Logindata import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class Login(BasicFun):
    # 元素定位
    # 用户名输入框
    username_input_xpath = "//*[@name='userName']"
    # 密码输入框
    passwd_input_xpath = "//*[@name='pwd']"
    # 登入按钮
    login_button_xpath = "//button[@type='button']"
    # 用户名密码错误提示
    error_messg_xpath = "//*[@class='el-message__content']"
    # 未填写用户名密码错误提示信息
    null_messg_xpath = "//*[@class='el-form-item__error']"
    # 利旧客户端下载图片
    old_client_xpath = u"//*[@title='下载利旧客户端用于瘦终端（vdi）用户登录']/img"
    # HALO工具下载图片
    halo_dowload_xpath = u"//*[@title='Halo体验工具下载']/img"
    # halo页面下载图标
    halo_page_dowlade_xpath = "//*[@class='item slide_img']/img"
    # 技术支持论坛
    technology_link_xpath = u"//*[text()='技术支持论坛']"
    # 在线客服
    online_service_xpath = "//*[text()='在线客服']"
    # 智能客服闪电兔选择产品
    product_xpath = "//*[@class='wms-tab-item']/li[{}]".format(lindex)
    # 闪电兔客服咨询框id
    anser_session_id = "js-inputMsg"
    # 发送框id
    send_messg_id = "sendBtn"
    # 信息接收框
    back_anser_xpath = "//*[@class='msgDiv']/div"
    # 跳转到首页页面xpath
    index_xpath = u"//span[text()='首页']"
    # 跳转到云桌面管理页面xpath
    cloud_manage_xpath = u"//span[text()='云桌面管理']"
    #   跳转到用户管理页面xpath
    user_manage_xpath = u"//span[text()='用户管理']"
    # 跳转到高级配置页面
    ad_setting_xpath = u"//span[text()='高级配置']"
    # 系统设置
    sys_set_xpath = u"//span[text()='系统设置']"
    # 管理员账号设置
    manage_user_set_xpath = u"//span[text()='管理员账号设置']"
    # 注销
    logout_xpath = "//i[@class='sk-icon sk-icon-logout']"
    # 密码输入和确认框
    confirm_pwd_xpath = "//input[@type='password']"
    pwd_confirm_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"
    # 跳转到终端管理页面
    terminal_xpath = u"//*[text()='终端管理']"
    # 到瘦终端页面
    go_vdi_terminal_page_xpath = u"//*[contains(@class,'el-menu-item')]//*[text()='瘦终端（VDI）']"
    # 到胖瘦终端页面
    go_idv_terminal_page_xpath = u"//*[contains(@class,'el-menu-item')]//*[text()='胖终端（IDV）']"
    # 镜像管理页面
    image_page_xpath = u"//span[contains(text(),'镜像管理')]"

    # 登入
    def login(self, name, pwd):
        self.find_elem(self.username_input_xpath).send_keys(name)
        self.find_elem(self.passwd_input_xpath).send_keys(pwd)
        self.click_elem(self.login_button_xpath)

    # 获取用户、密码输入错误提示信息
    def get_error_info(self):
        return self.find_elem(self.error_messg_xpath).text

    # 获取用户、密码输入为空提示信息
    def get_null_info(self):
        return self.find_elem(self.null_messg_xpath).text

    # 清除用户、密码输入信息
    def clear_info(self):
        self.find_elem(self.username_input_xpath).send_keys(Keys.CONTROL, 'a')
        self.find_elem(self.username_input_xpath).send_keys(Keys.BACK_SPACE)
        self.find_elem(self.passwd_input_xpath).send_keys(Keys.CONTROL, 'a')
        self.find_elem(self.passwd_input_xpath).send_keys(Keys.BACK_SPACE)

    # 可优化等待窗口出现再操作不需要强制等待TODO
    # 利旧客户端下载
    def old_client_dowload(self, a):
        self.find_elem(self.old_client_xpath).click()
        time.sleep(2)
        self.download()
        time.sleep(a)

    #     HALO下载
    def halo_dowload(self, a):
        self.find_elem(self.halo_dowload_xpath).click()
        time.sleep(0.5)
        self.get_cwind(-1)
        self.find_elem(self.halo_page_dowlade_xpath).click()
        time.sleep(1)
        self.get_cwind(-1)
        time.sleep(3)
        self.download()
        time.sleep(a)

    # 在线客服发送信息
    def online_service(self):
        self.find_elem(self.online_service_xpath).click()
        self.get_cwind(-1)
        self.find_elem(self.product_xpath).click()
        self.get_cwind(-1)
        self.find_elem(self.anser_session_id, by=By.ID).send_keys(questions)
        self.find_elem(self.send_messg_id, By.ID).click()

    # 获取消息框中的文本信息
    def get_questions(self):
        time.sleep(1)
        return self.find_elem(self.back_anser_xpath).text

    # 跳转到技术支持论坛页面
    def get_technology_page(self):
        self.find_elem(self.technology_link_xpath).click()
        self.get_cwind(-1)
        time.sleep(0.5)
        return self.driver.title

    # 登录界面点击
    def login_page_click(self):
        self.find_elem(self.username_input_xpath).click()
        self.find_elem(self.passwd_input_xpath).click()
        # 页面不能登入

    def server_out(self):
        return self.find_elem('//h1').text

    # 跳转的到云桌面管理页面
    def goto_cloud_desk_manage(self):
        time.sleep(2)
        self.click_elem(self.cloud_manage_xpath)
    # 退出登入
    def logout_user(self):
        self.back_current_page()
        self.find_elem(self.logout_xpath).click()

    #    跳转到用户管理页面
    def go_to_user_manage_page(self):
        self.find_elem(self.user_manage_xpath).click()

    #    跳转到用户管理页面
    def go_to_permission_page(self):
        self.find_elem(self.ad_setting_xpath).click()
        self.find_elem(self.sys_set_xpath).click()
        self.find_elem(self.manage_user_set_xpath).click()

    def send_pwd_confirm(self, pd=c_pwd):
        """输入账号密码"""
        self.back_current_page()
        self.find_elem(self.confirm_pwd_xpath).send_keys(pd)
        self.click_elem(self.pwd_confirm_xpath)

    def go_to_vdi_terminal_page(self):
        """跳转到瘦终端页面"""
        self.find_elem(self.terminal_xpath).click()
        time.sleep(0.5)
        self.find_elem(self.go_vdi_terminal_page_xpath).click()

    def go_to_idv_terminal_page(self):
        """跳转到胖终端页面"""
        self.find_elem(self.terminal_xpath).click()
        time.sleep(0.5)
        self.find_elem(self.go_idv_terminal_page_xpath).click()

    def goto_image_page(self):
        """跳转到镜像管理页面"""
        self.click_elem(self.image_page_xpath)


    def goto_index_manage(self):
        """跳转的到首页页面"""
        time.sleep(2)
        self.scroll_into_view(self.index_xpath)