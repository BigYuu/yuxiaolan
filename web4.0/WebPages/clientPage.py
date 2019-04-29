#!/usr/bin/python
# -*- coding: UTF-8 -*-

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from Common.Basicfun import BasicFun
from Common.terminal_action import *
from pymouse import PyMouse
# from pykeyboard import PyKeyboard
from TestData.clientdata import *
from TestData.Logindata import *
from os import system

"""
@author: huangqiaofen
@contact: huangqiaofen@ruijie.com
@software: PyCharm
@time: 2019/1/14
"""

class Client (BasicFun):
    # 利旧客户端下载图片
    old_client_xpath = u"//*[@title='下载利旧客户端用于瘦终端（vdi）用户登录']/img"
    # 所测试的用户所在的用户组
    vdi_user_group_xpath = ur"//div[@class='custom-tree-node']/descendant::div[contains(text(),'{0}')]"
    # 新建用户按钮
    new_user_button_xpath = ur"//*[@class='sk-toolbar']/div//*[contains(., '新建用户')]/span"
    # 新建用户的用户名框
    new_user_name_xpath = u"//*[text()='用户名：']/parent::div/descendant::input"
    # 新建用户的姓名框
    new_user_xpath = u"//*[text()='姓名：']/parent::div/descendant::input"
    # 用户管理界面
    user_xpath = u"//*[text()='首页']"
    user_manage_xpath = u"//*[text()='用户管理']"
    # 所测试的用户组所在的用户组
    select_user_group_xpath = ur"//div[@class='custom-tree-node']/descendant::div[contains(text(),'{0}')]/" \
                              ur"ancestor::div[@class='el-tree-node__content']/span"
    # 点击外设策略
    vdi_Peripheral_strategy_xpath = ur"//*[text()='外设策略']"
    # 确认编辑按钮
    confirm_compile_button_xpath = ur"//*[contains(text(),'{0}')]/ancestor::div[@class='el-dialog']" \
                                   ur"/div[@class='el-dialog__footer']/div/button"



    # 可优化等待窗口出现再操作不需要强制等待TODO
    # 利旧客户端下载
    def old_client_dowload(self, a):
        self.find_elem(self.old_client_xpath).click()
        time.sleep(2)
        self.download()
        time.sleep(a)

    # 在测试的用户组下新建测试用户
    def new_test_user ( self, u_group, u_name ):
        """
        :param u_group:  所要新建用户所在的二级用户组
        :param u_name:   所要新建的用户名，姓名
        :return:
        """
        self.click_elem(self.user_manage_xpath)  # 进入用户管理
        self.click_elem (self.vdi_user_group_xpath.format (u_group))
        self.click_elem (self.new_user_button_xpath)
        self.elem_send_keys (self.new_user_name_xpath, u_name)
        self.elem_send_keys (self.new_user_xpath,u_name)
        self.click_elem(self.vdi_Peripheral_strategy_xpath)  # 点击外设策略，用于退出镜像的选择，显示出确认按钮
        self.click_elem(self.confirm_compile_button_xpath.format("新建用户"))  # 确认编辑

    def client_login( self ):
        flag_list = [0,0]
        self.new_test_user('client',cli_name)
        a = get_client_winds_siaze ()
        time.sleep (2)
        size = (a[2] - a[0], a[3] - a[1])
        m = PyMouse ()
        k = PyKeyboard ()
        if get_client_guest_info () == 'FALSE' or get_client_guest_info () is None:
            m.click(int(a[0] + size[0] * 0.62), int(a[1] + size[1] * 0.59))
        else:
            m.click (int (a[0] + size[0] * 0.62), int (a[1] + size[1] * 0.54))
        self.get_revise_password_siaze()
        self.client_revise_password(cli_name,old_passwd,new_passwd)
        te=server_sql_qurey(mainip, "SELECT user_pwd FROM lb_seat_info WHERE user_name='{0}'".format(cli_name))
        if str (te).__contains__ (u'123'):
            flag_list[0] = 1
        try:
          client_login(cli_name,new_passwd)
          flag_list[1] = 1
        except Exception as e:
                print(e)
        return flag_list



    def client_abnormal_login(self):
        flag_list = [0, 0, 0, 0]
        client_login (right_name, error_passwd)
        try :
             client_error_passwd_click()
             flag_list[0] = 1
        except Exception as e:
                print(e)
        client_login (error_name, right_passwd)
        try :
             client_error_passwd_click()
             flag_list[1] = 1
        except Exception as e:
                print(e)
        client_login (name32, right_passwd)
        try :
             client_error_passwd_click()
             flag_list[2] = 1
        except Exception as e:
                print(e)
        client_login (right_name, passwd32)
        try :
             client_error_passwd_click()
             flag_list[3] = 1
        except Exception as e:
                print(e)

    def get_revise_password_siaze( self ):
        """获取修改窗口位置"""
        try:
            dialog = win32gui.FindWindow ("RCD_WINDOW_CLIENT_MAIN_WND", "RCC-Client","DUIAdministratorWnd")
            win32gui.SetForegroundWindow (dialog)
            a = win32gui.GetWindowRect (dialog)
            return a
        except Exception as error:
            logging.exception ("未打开修改密码框")
            raise error

    def get_client_remember_password( self ):
        """查看利旧客户端是否开启记住密码"""
        with open ('C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
            p = f.read ()
            info = re.findall (r'.*SavePass=([A-Z]+).*', p)
            if info == []:
                return None
            else:
                return info[0]

    def client_revise_password(self,name,oldpwd,newpd):
        """修改密码输入框"""
        win = automation.PaneControl (ClassName='DUIAdministratorWnd')
        a = self.get_revise_password_siaze()
        time.sleep (2)
        size = (a[2] - a[0], a[3] - a[1])
        m = PyMouse ()
        k = PyKeyboard ()
        time.sleep (0.5)
        m.click (int (a[0] + size[0] * 0.51), int (a[1] + size[1] * 0.28))
        k.type_string (name)
        k.tap_key (k.return_key)
        m.click (int (a[0] + size[0] * 0.51), int (a[1] + size[1] * 0.42))
        k.type_string (oldpwd)
        k.tap_key (k.return_key)
        m.click (int (a[0] + size[0] * 0.51), int (a[1] + size[1] * 0.54))
        k.type_string (newpd)
        k.tap_key (k.return_key)
        m.click (int (a[0] + size[0] * 0.51), int (a[1] + size[1] * 0.67))
        k.type_string (newpd)
        k.tap_key (k.return_key)
        win.Click (0.42, 0.91)


    # 勾选记住密码
    def remember_password( self):
        """  输入用户名，密码，勾选记住密码，登入利旧，重启利旧
        :return: 返回配置文件里保存的用户密码
        """
        a=get_client_winds_siaze()
        time.sleep (2)
        size = (a[2] - a[0], a[3] - a[1])
        m = PyMouse ()
        k = PyKeyboard ()
        time.sleep (0.5)
        if get_client_guest_info () == 'FALSE' or get_client_guest_info () is None:
            m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.46))
            clear_info ()
            k.type_string (right_name)
            k.tap_key (k.return_key)
            m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.52))
            clear_info ()
            k.type_string (right_passwd)
            k.tap_key (k.return_key)
            if self.get_client_remember_password() == 'FALSE' or self.get_client_remember_password() is None:
                m.click (int (a[0] + size[0] * 0.35), int (a[1] + size[1] * 0.59))
            else:
                logging.exception ("已开启记住密码")
            m.click(int (a[0] + size[0] * 0.49), int (a[1] + size[1] * 0.68))
        else:
            m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.41))
            clear_info ()
            k.type_string (right_name)
            k.tap_key (k.return_key)
            m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.48))
            clear_info ()
            k.type_string (right_passwd)
            k.tap_key (k.return_key)
            if self.get_client_remember_password () == 'FALSE' or self.get_client_remember_password () is None:
                m.click (int (a[0] + size[0] * 0.35), int (a[1] + size[1] * 0.54))
            else:
                logging.exception ("已开启记住密码")
            m.click (int (a[0] + size[0] * 0.49), int (a[1] + size[1] * 0.62))
        client_lvdi_close()
        with open ('C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
            p = f.read ()
            info = re.findall (r'.*UserPass=([a-zA-Z0-9]+).*', p)
            if info == []:
                return None
            else:
                return info[0]

    # 不勾选记住密码框
    def unremember_password(self):
        """  输入用户名，密码，不勾选记住密码，登入利旧，重启利旧
        :return: 返回配置文件里保存的用户密码
        """
        a = get_client_winds_siaze ()
        time.sleep (2)
        size = (a[2] - a[0], a[3] - a[1])
        m = PyMouse ()
        k = PyKeyboard ()
        time.sleep (0.5)
        if get_client_guest_info () == 'FALSE' or get_client_guest_info () is None:
            m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.46))
            clear_info ()
            k.type_string (right_name)
            k.tap_key (k.return_key)
            m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.52))
            clear_info ()
            k.type_string (right_passwd)
            k.tap_key (k.return_key)
            if self.get_client_remember_password () == 'FALSE' or self.get_client_remember_password () is None:
                logging.exception ("未开启记住密码")
            else:
                m.click (int (a[0] + size[0] * 0.35), int (a[1] + size[1] * 0.59))
            m.click (int (a[0] + size[0] * 0.49), int (a[1] + size[1] * 0.68))
        else:
            m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.41))
            clear_info ()
            k.type_string (right_name)
            k.tap_key (k.return_key)
            m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.48))
            clear_info ()
            k.type_string (right_passwd)
            k.tap_key (k.return_key)
            if self.get_client_remember_password () == 'FALSE' or self.get_client_remember_password () is None:
                logging.exception ("未开启记住密码")
            else:
                m.click (int (a[0] + size[0] * 0.35), int (a[1] + size[1] * 0.54))
            m.click (int (a[0] + size[0] * 0.49), int (a[1] + size[1] * 0.62))
        client_lvdi_close ()
        with open ('C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
            p = f.read ()
            info1 = re.findall (r'.*UserPass=([a-zA-Z0-9]+).*', p)
            if info1 == []:
                return None
            else:
                return info1[0]

    def client_clcik_other_set( self ):
        """利旧客户端点击设置"""
        a = get_client_winds_siaze ()
        size = (a[2] - a[0], a[3] - a[1])
        m = PyMouse ()
        time.sleep (1)
        m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.90))
        time.sleep (1)

    def client_Setting_click( self ):
        """当设置保存的提示框"""
        win = automation.PaneControl (ClassName='ErrorTipWnd')
        if win.Exists ():
            win.Click (0.5, 0.87)

    def basic_info_Setting_hostname( self ):
        with open ('C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
            p = f.read ()
            info = re.findall (r'.*hostname=([a-zA-Z0-9]+).*', p)
            if info == []:
                return None
            else:
                return info[0]

    def basic_info_Setting_mainserver( self ):
        flag_list = [0]
        a = get_client_winds_siaze ()
        time.sleep (2)
        size = (a[2] - a[0], a[3] - a[1])
        m = PyMouse ()
        k = PyKeyboard ()
        time.sleep (1)
        m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.90))
        time.sleep (1)
        m.click(int (a[0] + size[0] * 0.42), int (a[1] + size[1] * 0.28))
        clear_info ()
        k.type_string (main_server)
        k.tap_key (k.return_key)
        self.client_Setting_click()
        with open ('C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
            p = f.read ()
            info1 = re.findall (r'.*mainServer=([a-zA-Z0-9]+).*', p)
            if info1== []:
                return None
            else:
                return info1[0]

    def basic_info_Setting_mainserverip( self ):
        flag_list = [0,0]
        a = get_client_winds_siaze ()
        time.sleep (2)
        size = (a[2] - a[0], a[3] - a[1])
        m = PyMouse ()
        k = PyKeyboard ()
        time.sleep (1)
        m.click (int (a[0] + size[0] * 0.45), int (a[1] + size[1] * 0.90))
        time.sleep (1)
        m.click (int (a[0] + size[0] * 0.42), int (a[1] + size[1] * 0.28))
        clear_info ()
        k.type_string (illegal_ip)
        k.tap_key (k.return_key)
        try:
            self.client_Setting_click()
            flag_list[0] = 1
        except Exception as e:
                print(e)
        m.click (int (a[0] + size[0] * 0.42), int (a[1] + size[1] * 0.28))
        clear_info ()
        k.type_string (" ")
        k.tap_key (k.return_key)
        try:
            self.client_Setting_click ()
            flag_list[1] = 1
        except Exception as e:
            print(e)

    def network_configuration_ip( self ):
        with open ('C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
            p = f.read ()
            info1 = re.findall (r'.*ip=([a-zA-Z0-9]+).*', p)
            if info1== []:
                return None
            else:
                return info1[0]

    def network_configuration_netmask( self ):
        with open ('C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
            p = f.read ()
            info2 = re.findall (r'.*netmask=([a-zA-Z0-9]+).*', p)
            if info2 == []:
                return None
            else:
                return info2[0]

    def network_configuration_gateway( self ):
        with open ('C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
            p = f.read ()
            info3 = re.findall (r'.*gateway=([a-zA-Z0-9]+).*', p)
            if info3 == []:
                return None
            else:
                return info3[0]

    def get_client_auto_login( self ):
        """查看利旧客户端是否开启自启动"""
        with open ('C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
            p = f.read ()
            info = re.findall (r'.*login=([a-zA-Z]+).*', p)
            if info == []:
                return None
            else:
                return info[0]

    def get_client_winds( self ):
        """
        获取自启动后的利旧客户端的大小
        :return: 有自启动则返回大小，无则返回为空
        """
        try:
            dialog = win32gui.FindWindow ("RCD_WINDOW_CLIENT_MAIN_WND", "RCC-Client")
            win32gui.SetForegroundWindow (dialog)
            a = win32gui.GetWindowRect (dialog)
            return a
        except:
            logging.info("利旧客户端未开启")
            return None


    def other_seting_autoloin( self ):
        client_clcik_other_set()
        a = get_client_winds_siaze ()
        time.sleep (2)
        size = (a[2] - a[0], a[3] - a[1])
        m = PyMouse ()
        time.sleep (1)
        if get_client_guest_info () == 'FALSE' or get_client_guest_info () is None:
            m.click (int (a[0] + size[0] * 0.34), int (a[1] + size[1] * 0.30))
        else:
            logging.exception ("已开启自启动")
        system('reboot')
        info1=self.get_client_winds()
        return info1

    def other_seting_unautoloin( self ):
         client_clcik_other_set()
         a = get_client_winds_siaze ()
         time.sleep (2)
         size = (a[2] - a[0], a[3] - a[1])
         m = PyMouse ()
         time.sleep (1)
         if get_client_guest_info () == 'FALSE' or get_client_guest_info () is None:
             logging.exception ("未开启自启动")
         else:
             m.click (int (a[0] + size[0] * 0.34), int (a[1] + size[1] * 0.30))
         system('reboot')
         info2=self.get_client_winds()
         return info2

