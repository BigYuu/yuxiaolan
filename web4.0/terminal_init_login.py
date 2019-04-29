#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/12/7 13:54
"""
from Common.terminal_action import *
from configparser import ConfigParser
from selenium import webdriver
from WebPages.LoginPage import Login
from Common.Mylog import *
from WebPages.Idvpage import IdvPage
from WebPages.adnroid_vdi_page import AndroidVdi


# 点击初始化终端
class TerminalInit:
    def __init__(self):
        pass

    # 初始化vdi,连接服务器
    def vdi_terminal_init(self):
        cp = ConfigParser()
        cp.read(os.getcwd() + "\\terminal.cfg")
        p = AndroidVdi()
        android_ip_list = eval(cp.get('ip_list', 'vdi_android_ip_list'))
        linux_ip_list = eval(cp.get('ip_list', 'vdi_linux_ip_list'))
        i = 0
        alist_fail = list()
        for ip in android_ip_list:
            try:
                os.system("adb connect {}".format(ip))
                i = i + 1
                p.vm_name_ip_set('VDI_0{0}'.format(i), cp.get('ip_list', 'vm_ip'))
            except Exception as error:
                alist_fail.append(ip)
                logging.error(error)
                logging.error('ip为{}的终端不可连接'.format(ip))
            logging.error("未连接成功IP列表为{}".format(alist_fail))
            os.system("adb disconnect {}".format(ip))
        llist_fail = list()
        for ip in linux_ip_list:
            try:
                i = i + 1
                vdi_name_ip_set(ip, 'VDI_0{0}'.format(i), cp.get('ip_list', 'vm_ip'))
            except Exception as error:
                llist_fail.append(ip)
                logging.error(error)
                logging.error('ip为{}的终端不可连接'.format(ip))
            logging.error("未连接成功IP列表为{}".format(llist_fail))

    # vdi登入
    def vdi_login(self):
        p = AndroidVdi()
        cp = ConfigParser()
        cp.read(os.getcwd() + "\\terminal.cfg")
        android_ip_list = eval(cp.get('ip_list', 'vdi_android_ip_list'))
        linux_ip_list = eval(cp.get('ip_list', 'vdi_linux_ip_list'))
        android_vdi_user = eval(cp.get('user_name', 'vdi_android_user'))
        linux_vdi_user = eval(cp.get('user_name', 'vdi_linux_user'))
        guest_ip = eval(cp.get('ip_list', 'vdi_guest_ip_list'))
        sleep_ip = eval(cp.get('ip_list', 'vdi_sleep_ip_list'))
        i = 0
        n = 0
        list_fail = list()
        for ip in android_ip_list:
            os.system("adb connect {}".format(ip))
            if ip in guest_ip:
                try:
                    p.guest_login_set(android_vdi_user[i], '123')
                    p.click_guest_login(ip)
                except Exception as e:
                    logging.error(e)
                    logging.error("{}的ip未登入成功".format(ip))
                    list_fail.append(ip)
            elif ip in sleep_ip:
                try:
                    p.set_sleep_time(10)
                    p.login(android_vdi_user[i], ip, '123')
                except Exception as e:
                    logging.error(e)
                    logging.error("{}的ip未登入成功".format(ip))
                    list_fail.append(ip)
            else:
                try:
                    p.login(android_vdi_user[i], ip, '123')
                except Exception as e:
                    logging.error(e)
                    logging.error("{}的ip未登入成功".format(ip))
                    list_fail.append(ip)
            os.system("adb disconnect {}".format(ip))
            i = i + 1
            for ip in linux_ip_list:
                try:
                    vdi_login(ip, linux_vdi_user[n], '123')
                    n = n + 1
                except Exception as error:
                    logging.error(error)
                    logging.error("ip为{}的终端为登入失败".format(ip))
                    list_fail.append(ip)
        logging.error("未连接成功IP列表为{}".format(list_fail))

    # 初始化idv
    def idv_terminal_init(self):
        # cp = ConfigParser()
        # cp.read(os.getcwd() + "\\terminal.cfg")
        # idv_ip_list = eval(cp.get('ip_list', 'idv_ip_list'))
        # idv_single_ip_list = eval(cp.get('ip_list', 'idv_single_ip_list'))
        # idv_public_ip_list = eval(cp.get('ip_list', 'idv_public_ip_list'))
        # idv_common_ip_list = eval(cp.get('ip_list', 'idv_common_ip_list'))
        single_user = cp.get('user_name', 'idv_single_user')
        i = 0
        for ip in idv_ip_list:
            try:
                idv_set_name_host_ip(ip, 'IDV_0{}'.format(i),host_ip)
                i = i+1
            except Exception as error:
                logging.exception(error)
                logging.error("IP为{}的终端未连接入集群，请检查是否输入的ip有误，或终端电源未开启".format(ip))
        time.sleep(10)
        for ip in idv_ip_list:
            try:
                driver = webdriver.Chrome()
                driver.maximize_window()
                driver.get("http://{}/main.html#/login".format(vm_ip))
                l = Login(driver)
                p = IdvPage(driver)
                l.login(c_user, c_pwd)
                p.terminal_init(ip)
                p.reboot_terminal(ip)
            except Exception as error:
                logging.error(error)
                logging.error("IP为{}的终端不可点击，请检查是否输入的ip有误，或终端电源未开启".format(ip))
        time.sleep(10)
        for ip in idv_ip_list:
            idv_initialization_click(ip)
        i = 0
        for ip in idv_single_ip_list:
            idv_pattern_chose(ip, 'single', name=single_user[i])
            i = i + 1
        for ip in idv_public_ip_list:
            idv_pattern_chose(ip, 'public')
        for ip in idv_common_ip_list:
            idv_pattern_chose(ip, 'common')

    def idv_bach_user_login(self, ip_list, name_list, pwd=123, login_type=0):
        """用户批量登入方法
         :ip_list,终端IP列表
         :name_list,登入用户名列表
         :pwd 用户密码默认为123
        :login_type用户登入模式0为正常用户登入，1为访客登入"""
        i = 0
        for ip in ip_list:
            try:
                if login_type == 0:
                    idv_login(ip, name_list[i], pwd)
                    i = i + 1
                else:
                    idv_guest_login(ip)
            except Exception as error:
                logging.exception(error)
                logging.error('ip为{}的终端未登入成功'.format(ip))

    # idv 登入
    def idv_user_login(self):
        """idv终端登入"""
        cp = ConfigParser()
        cp.read(os.getcwd() + "\\terminal.cfg")
        single_user = eval(cp.get('user_name', 'idv_single_user'))
        public_user = eval(cp.get('user_name', 'idv_public_user'))
        idv_single_ip_list = eval(cp.get('ip_list', 'idv_single_ip_list'))
        idv_public_ip_list = eval(cp.get('ip_list', 'idv_public_ip_list'))
        idv_guest_ip_list = eval(cp.get('ip_list', 'idv_guest_ip_list'))
        self.idv_bach_user_login(idv_single_ip_list, single_user)
        self.idv_bach_user_login(idv_public_ip_list,  public_user)
        self.idv_bach_user_login(idv_guest_ip_list, None)


if __name__ == "__main__":
    from Common.terminal_action import *
    t = TerminalInit()
    # t.vdi_terminal_init()
    # t.vdi_login()
    t.idv_terminal_init()
    # time.sleep(10)
    # idv_set_name_host_ip('172.21.204.18', 'IDV_01', host_ip)
    # t.idv_user_login()
    pass
