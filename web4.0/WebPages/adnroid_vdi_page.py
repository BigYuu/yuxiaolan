#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/12/11 14:46
"""
from Common.parse_dump_file import *
from Common.terminal_action import *
from Common.serverconn import *
from TestData.basicdata import *
import logging
import os
import time


class AndroidVdi:
    def __init__(self):
        pass

    # 保存按钮id
    save_burttion_id = "com.ruijie.rccstu:id/btn_save"
    # 点击设置
    set_button_id = "com.ruijie.rccstu:id/imgbtn_setting"
    # 用户名输入框
    user_name_id = "com.ruijie.rccstu:id/et_name"
    # 密码输入框
    paswd_input_id = "com.ruijie.rccstu:id/et_password"
    # 登入按钮
    login_button_id = "com.ruijie.rccstu:id/btn_login"
    # 点击断开连接按钮
    off_connect_id = "com.ruijie.rccstu:id/btn_disconnect"
    # 判断连接次数
    connect_times_id = "com.ruijie.rccstu:id/tv_prompt_title"
    # 终端名称输入框
    terminal_name_id = "com.ruijie.rccstu:id/et_host_name"
    # ip地址输入框
    host_ip_id = "com.ruijie.rccstu:id/et_host_address"
    # 自动获取ip信息
    dynamic_get_ip_id = "com.ruijie.rccstu:id/rdoBtn_auto_ip"
    # 使用静态ip
    static_get_ip_id = "com.ruijie.rccstu:id/rdoBtn_manual_ip"
    # 使用静态ip，ip输入框
    static_ip_input_ip_id = "com.ruijie.rccstu:id/et_ip_address"
    # 子网掩码
    mask_id = "com.ruijie.rccstu:id/et_netmask"
    # 网关
    gateway_id = "com.ruijie.rccstu:id/et_gateway"
    # 其他设置按钮
    other_set_id = "com.ruijie.rccstu:id/btn_other_set"
    # 电源设置id
    power_set_id = "com.ruijie.rccstu:id/btn_power"
    # 点击休眠时间框
    sleep_time_set_id = "com.ruijie.rccstu:id/spn_sleep"
    # 关闭窗口按钮
    close_window_button_id = "com.ruijie.rccstu:id/btn_close"
    # 修改密码
    change_passwd_id = "com.ruijie.rccstu:id/tv_change_password"
    # 修改密码输入用户名
    chang_passwd_user_id = "com.ruijie.rccstu:id/et_user_name"
    # 修改密码保存按钮
    change_passwd_save_id = "com.ruijie.rccstu:id/btn_change_password"
    # 初始化输入密码
    init_passwd_input_id = "com.ruijie.rccstu:id/et_super_password"
    # s输入初始化密码点击确定
    confirm_button_id = "com.ruijie.rccstu:id/btn_ok"
    # 基本设置按钮
    basic_button_id = "com.ruijie.rccstu:id/btn_basic"
    # 访客设置id
    guest_set_id = "com.ruijie.rccstu:id/btn_visitor"
    # 访客登入开关
    guest_button_id = "com.ruijie.rccstu:id/toggle_visitor_function"
    # 访客用户
    guest_user_id = "com.ruijie.rccstu:id/et_visitor_name"
    # 访客密码
    guest_passwd_id = "com.ruijie.rccstu:id/et_visitor_password"
    # 点击访客登入
    guest_login_button_id = "com.ruijie.rccstu:id/imgbtn_login_visitor"
    # 锁屏按钮
    close_screen_id = "com.ruijie.rccstu:id/btn_float_bar_lock"
    # 确认锁屏
    close_confirm_id = "com.ruijie.rccstu:id/btn_ok"
    # 终端关机
    terminal_close_id = "com.ruijie.rccstu:id/btn_float_bar_force_shutdown"
    # 用户名密码输入错误提示
    no_user_id = "com.ruijie.rccstu:id/tv_error_title"
    # 重新连接
    reconnect_id = "com.ruijie.rccstu:id/btn_reconnect"
    # 登入系统页面输入密码
    sys_pwd_input_id = "com.ruijie.rccstu:id/canvas"
    # 有键盘弹出的登入页面
    keyboard_exist_id = 'com.ruijie.rccstu:id/rl_bg'
    # 输入服务器ip
    host_ip_set_id = 'com.ruijie.rccstu:id/et_host_address'
    # 系统更新id
    android_update_id = 'android:id/title_container'
    # 终端下线页面
    terminal_out_id = 'com.ruijie.rccstu:id/tv_prompt_account_content'
    # 进入到设置页面id
    terminal_set_id = 'com.ruijie.rccstu:id/rl_dlg_title'
    # 被迫下线信息通知
    user_offline_id = "com.ruijie.rccstu:id/ll_account_content"
    # 未开启特性提示
    unopen_vdi_id = "com.ruijie.rccstu:id/imgv_error"
    # 管理员密码错误提示
    error_passwd_info_id = "com.ruijie.rccstu:id/tv_prompt_content"

    def vdi_connect(self, ip):
        """连接设备，ip为终端ip"""
        # list1 = os.popen('adb devices')
        # list_info = list1.read().splitlines()
        # if list_info[1] != '':
        #     list_info.remove(list_info[0])
        #     list_info.remove(list_info[-1])
        #     for item in list_info:
        #         devices = re.findall('(.*):5555', item)[0]
        #         os.system("adb disconnect {}".format(devices))
        os.system("adb kill-server")
        os.system("adb devices")
        conn_info = ''
        n = 0
        while n < 5:
            conn = os.popen("adb connect {}".format(ip))
            conn_info = conn.read()
            if conn_info.__contains__('unable to connect to :5555'):
                os.system('adb kill-server ')
                time.sleep(1)
                os.system('adb connect {}'.format(ip))
                if n == 5:
                    logging.error('终端连接失败')
            else:
                break
            n = n + 1
        time.sleep(1)
        logging.info(conn_info)
        return conn_info

    def connect_check(self, ip):
        """"确认终端是否可连接，不可连接返回1可连接返回0"""
        result = os.popen('adb connect {} '.format(ip))
        s = result.read()
        if s.__contains__('unable to connect to'):
            return 1
        else:
            return 0

    def vdi_disconnect(self, ip=None):
        """ 断开设备，ip为终端ip"""
        if ip is None:
            os.system('adb kill-server')
        else:
            os.system("adb disconnect {}".format(ip))

    def clear_info(self, elem_id):
        """清除信息"""
        p = get_element_msg(elem_id)
        if p is not None:
            i = 0
            while i <= len(p):
                os.system("adb shell input keyevent 'KEYCODE_MOVE_END'&adb shell input keyevent 'KEYCODE_DEL'")
                i = i + 1

    def pwd_clear(self, n=8):
        """清除密码"""
        i = 0
        while i <= n:
            os.system("adb shell input keyevent 'KEYCODE_MOVE_END'&adb shell input keyevent 'KEYCODE_DEL'")
            i = i + 1

    def get_winsize(self):  # 将屏幕亮起
        """ 获取屏幕大小"""
        os.system("adb shell input keyevent 26&adb shell input tap 800 600")
        os.system("adb shell input tap 800 600")
        result = os.popen("adb shell wm size").read()
        a = re.findall(r'.*?size: (.*)\r', result)[0]
        return a.split('x')

    def screen_lock(self):
        """终端锁屏"""
        a = self.get_winsize()
        os.system('adb shell input tap {0} {1}&adb shell input tap {0} {1}'.format(int(int(a[0]) / 2), 0))
        x, y = get_element_point(self.close_screen_id)
        click(x, y)
        x, y = get_element_point(self.close_confirm_id)
        click(x, y)

    def terminal_close(self):
        """终端强制关机"""
        if get_element_point(self.user_name_id) is None:
            a = self.get_winsize()
            os.system('adb shell input tap {0} {1}&adb shell input tap {0} {1}'.format(int(int(a[0]) / 2), 0))
            if get_element_point(self.terminal_close_id) is not None:
                x, y = get_element_point(self.terminal_close_id)
                click(x, y)
            x, y = get_element_point(self.close_confirm_id)
            click(x, y)
            n = 0
            while n < 30:
                try:
                    if get_element_point(self.user_name_id) is not None:
                        print(get_element_point(self.user_name_id))
                        break
                except:
                    logging.error('未知错误')
                n = n + 1
            if n >= 30:
                logging.error("关机失败")
        else:
            logging.info("已经在登录页面")

    def terminal_vm_close(self, ip, name, pwd):
        """winds系统虚机，关机,ip是云桌面ip"""
        get_win_conn_info(ip, name, pwd, "shutdown -s -t 00 -f")
        n = 0
        while n < 30:
            try:
                if get_element_point(self.user_name_id) is not None:
                    print(get_element_point(self.user_name_id))
                    break
                else:
                    time.sleep(3)
            except:
                time.sleep(3)
                logging.error('未知错误')
            n = n + 1
        if n >= 30:
            logging.error("关机失败")

    def login_init(self):
        """将用户设置到登入页面"""
        os.system("adb shell input keyevent 26&adb shell input tap 800 600")
        os.system("adb shell input tap 800 600")
        if get_current_activity() == "com.undatech.opaque.RemoteCanvasActivity":
            self.terminal_close()
        elif get_element_point(self.init_passwd_input_id) is not None:
            x, y = get_element_point(self.init_passwd_input_id)
            click(x, y)
            self.pwd_clear(3)
            os.system("adb shell input text 'ruijie.com'")
            time.sleep(0.5)
            x, y = get_element_point(self.confirm_button_id)
            click(x, y)
            self.click_close_button()
        elif get_element_msg(self.no_user_id) == "用户不存在或密码错误" or \
                get_element_msg(self.no_user_id) == "指定的域不存在，或无法联系":
            x, y = get_element_point(self.reconnect_id)
            click(x, y)
        elif get_element_point(self.user_offline_id) is not None:
            x, y = get_element_point(self.confirm_button_id)
            click(x, y)
        elif get_element_point(self.basic_button_id) is not None:
            self.click_close_button()
        elif get_element_point(self.connect_times_id) is not None:
            self.off_connect()
        elif get_element_point(self.terminal_out_id) is not None:
            x, y = get_element_point(self.confirm_button_id)
            click(x, y)
        elif get_element_point(self.terminal_set_id) is not None:
            x, y = get_element_point(self.terminal_set_id)
            click(x, y)
        if get_element_point(self.error_passwd_info_id) is not None:
            logging.info("输入的管理员账号错误")
            x, y = get_element_point(self.confirm_button_id)
            click(x, y)
            time.sleep(1)
            x, y = get_element_point(self.click_close_button)
            click(x, y)
        if get_element_point(self.unopen_vdi_id) is not None:
            x, y = get_element_point(self.reconnect_id)
            click(x, y)
        if get_element_point(self.keyboard_exist_id) is not None:
            os.system("adb shell input tap 800 100")

    def click_set(self):
        """点击设置"""
        self.login_init()
        x, y = get_element_point(self.set_button_id)
        click(x, y)
        if get_element_point(self.init_passwd_input_id) is not None:
            x, y = get_element_point(self.init_passwd_input_id)
            click(x, y)
            self.pwd_clear(3)
            os.system("adb shell input text 'ruijie.com'")
            x, y = get_element_point(self.confirm_button_id)
            click(x, y)

    def click_save(self):
        """点击保存"""
        x, y = get_element_point(self.save_burttion_id)
        click(x, y)

    def click_close_button(self):
        """点击关闭"""
        x, y = get_element_point(self.close_window_button_id)
        click(x, y)

    def sys_pwd_input(self, pwd='rcd'):
        """判断用户是否要输入密码"""
        if get_element_point(self.sys_pwd_input_id) is not None:
            os.system("adb shell input text {0}&adb shell input keyevent 'KEYCODE_ENTER'".format(pwd))

    def vm_name_ip_set(self, name, host_ip, ip):
        """Android vdi设置终端名称和服务器ip"""
        self.click_set()
        cm_version = self.judge_terminal_update()
        x, y = get_element_point(self.terminal_name_id)
        click(x, y)
        self.clear_info(self.terminal_name_id)
        os.system("adb shell input text '{0}'&adb shell input keyevent 'KEYCODE_ENTER'".format(name))
        x, y = get_element_point(self.host_ip_set_id)
        click(x, y)
        self.clear_info(self.host_ip_id)
        os.system("adb shell input text '{0}'&adb shell input keyevent 4".format(host_ip))
        self.click_save()
        if cm_version == 0:
            n = 0
            while n < 30:
                if self.connect_check(ip) == 0 and get_element_point(self.user_name_id) is not None:
                    logging.info("设置完成，升级完成")
                    break
                else:
                    time.sleep(6)
                n = n + 1
        else:
            logging.info("设置完成")

    def input_username_passwd(self, name, pwd):
        """输入账号密码点击登录"""
        x, y = get_element_point(self.user_name_id)
        click(x, y)
        self.clear_info(self.user_name_id)
        os.system(u"adb shell input text '{0}'&adb shell input keyevent 'KEYCODE_ENTER'".format(name))
        self.pwd_clear()
        os.system(u"adb shell input text '{0}'&adb shell input keyevent 4".format(pwd))
        x, y = get_element_point(self.login_button_id)
        click(x, y)

    def login(self, name, ip, pwd='123', wait_times=10):
        """android vdi登入终端"""
        self.login_init()
        cm_version = self.judge_terminal_update()
        self.input_username_passwd(name, pwd)
        time.sleep(wait_times)
        try:
            if cm_version == 0:
                n = 0
                while n < 30:
                    if self.connect_check(ip) == 0 and get_element_point(self.user_name_id) is not None:
                        self.input_username_passwd(name, pwd)
                        break
                    else:
                        time.sleep(6)
                    n = n + 1
            elif get_element_point(self.connect_times_id) is not None:
                time.sleep(50)
                a = get_element_msg(self.connect_times_id)
                times = int(re.findall('.*(\d+).*', a)[0])
                if times > 20:
                    print("连接超时，请检查服务器ip是否正确，服务器是否正常")
                    self.off_connect()
                else:
                    print("连接成功")
            else:
                time.sleep(25)
                if get_current_activity() == 'com.undatech.opaque.RemoteCanvasActivity':
                    print("登入虚机成功")
            if get_element_msg(self.no_user_id) == "用户不存在或密码错误" or \
                    get_element_msg(self.no_user_id) == "指定的域不存在，或无法联系":
                x, y = get_element_point(self.reconnect_id)
                click(x, y)
                logging.error("输入的用户密码错误")
            return cm_version
        except Exception as e:
            logging.error(e)
            logging.error("未知错误")

    def ipstate_set(self, ipstate='dynamic', ip=None, mask=None, gateway=None):
        """选择静态获取ip还是动态"""
        self.click_set()
        if ipstate == 'static':
            x, y = get_element_point(self.static_get_ip_id)
            click(x, y)
            if ip is not None:
                x, y = get_element_point(self.static_ip_input_ip_id)
                click(x, y)
                self.clear_info(self.static_ip_input_ip_id)
                os.system("adb shell input text {0}&adb shell input keyevent 4".format(ip))
            if mask is not None:
                x, y = get_element_point(self.mask_id)
                click(x, y)
                self.clear_info(self.mask_id)
                os.system("adb shell input text {0}&adb shell input keyevent 4".format(mask))
            if gateway is not None:
                x, y = get_element_point(self.gateway_id)
                click(x, y)
                self.clear_info(self.gateway_id)
                os.system("adb shell input text {0}&adb shell input keyevent 4".format(gateway))
        elif ipstate == 'dynamic':
            x, y = get_element_point(self.dynamic_get_ip_id)
            click(x, y)
        else:
            print("你输入的ip获取形式有误")
        self.click_save()

    def off_connect(self):
        """超时连接点击断开"""
        x, y = get_element_point(self.off_connect_id)
        click(x, y)

    def set_sleep_time(self, sleep_time):
        """设置休眠时间,其中sleep_time只能10/30分钟，1/3/5/8小时和从不"""
        self.click_set()
        x, y = get_element_point(self.power_set_id)
        click(x, y)
        x, y = get_element_point(self.sleep_time_set_id)
        click(x, y)
        x, y = get_element_point_by_msg("{}".format(sleep_time))
        click(x, y)
        self.click_save()

    def set_passwd(self, name, oldpasswd='123', newpasswd='1'):
        """修改密码"""
        self.login_init()
        x, y = get_element_point(self.change_passwd_id)
        click(x, y)
        x, y = get_element_point(self.chang_passwd_user_id)
        click(x, y)
        self.clear_info(self.chang_passwd_user_id)
        os.system("adb shell input text {0}&adb shell input keyevent 'TAB'&adb shell input text {1}"
                  "&adb shell input keyevent 'TAB'&adb shell input text {2}&adb shell input keyevent 'TAB'"
                  "&adb shell input text {2}&adb shell input keyevent 4".format(name, oldpasswd, newpasswd))

        x, y = get_element_point(self.change_passwd_save_id)
        click(x, y)

    def guest_login_set(self, name, passwd):
        """访客登入"""
        self.click_set()
        x, y = get_element_point(self.guest_set_id)
        click(x, y)
        if get_element_msg(self.guest_button_id) != "开启":
            x, y = get_element_point(self.guest_button_id)
            click(x, y)
        x, y = get_element_point(self.guest_user_id)
        click(x, y)
        self.clear_info(self.guest_user_id)
        os.system("adb shell input text {0}".format(name))
        x, y = get_element_point(self.guest_passwd_id)
        click(x, y)
        self.pwd_clear()
        os.system("adb shell input text {0}&adb shell input keyevent 4".format(passwd))
        self.click_save()

    def click_guest_login(self, ip):
        """点击访客登入按钮"""
        cm_version = self.judge_terminal_update()
        if get_element_point(self.keyboard_exist_id) is not None:
            os.system("adb shell input tap 800 100")
            time.sleep(1)
        x, y = get_element_point(self.guest_login_button_id)
        click(x, y)
        time.sleep(5)
        try:
            if cm_version == 0:
                n = 0
                while n < 30:
                    if self.connect_check(ip) == 0 and get_element_point(self.guest_login_button_id) is not None:
                        x, y = get_element_point(self.guest_login_button_id)
                        click(x, y)
                        break
                    else:
                        time.sleep(5)
                    n = n + 1
            elif get_element_point(self.connect_times_id) is not None:
                a = get_element_msg(self.connect_times_id)
                times = int(re.findall('.*(\d+).*', a)[0])
                if times > 15:
                    print("连接超时，请检查服务器ip是否正确，服务器是否正常")
                    self.off_connect()
                else:
                    print("连接成功")
            else:
                time.sleep(25)
                if get_current_activity() == 'com.undatech.opaque.RemoteCanvasActivity':
                    self.sys_pwd_input()
                    print("登入虚机成功")
            if get_element_msg(self.no_user_id) == "用户不存在或密码错误" or \
                    get_element_msg(self.no_user_id) == "指定的域不存在，或无法联系":
                x, y = get_element_point(self.reconnect_id)
                click(x, y)
                logging.error("输入的用户密码错误,请重新登入")
        except Exception as e:
            logging.error(e)
            logging.error("未知错误")

    def is_win_activity(self):
        """判断是否登入到windows系统,成功登入虚机后返回com.undatech.opaque.RemoteCanvasActivity，
        在登入界面为.LoginActivity"""
        return get_current_activity()

    def system_android_version(self):
        """获取Android终端系统最新版本信息"""
        version_list = list()
        v1 = server_conn(host_ip, "ls /opt/ftpshare/upgrade/OTA/packages/Rain100S")
        v2 = server_conn(host_ip, "ls /opt/ftpshare/upgrade/OTA/packages/Rain200S")
        temp1 = v1.replace('.zip\r\n', '')
        temp2 = v2.replace('.zip\r\n', '')
        version_list.append(temp1)
        version_list.append(temp2)
        return version_list

    def termianl_system_version(self):
        """获取android终端系统版本信息"""
        result = os.popen('adb shell cat /system/build.prop')
        info = result.read()
        temp_version = re.findall('.*?ro.product.version=(.*).*', info)[0]
        version = temp_version[0:-1]
        return version

    def termianl_user_info(self):
        """获取android终端登入用户信息"""
        result = os.popen('adb shell cat /data/data/com.ruijie.rccstu/shared_prefs/rcc_pref.xml |findstr "username"')
        r = result.read()
        return re.findall(r'.*?\">(.*)<.*', r)[0]

    def termianl_name_info(self):
        """获取android终端登入用户信息"""
        result = os.popen('adb shell cat /data/data/com.ruijie.rccstu/shared_prefs/rcc_pref.xml |findstr "hostname"')
        r = result.read()
        return re.findall(r'.*?\">(.*)<.*', r)[0]

    def get_android_ip_mac(self):
        """获取终端的ip和mac"""
        result = os.popen('adb shell netcfg | findstr "eth0"')
        r = result.read().split()
        dict01 = {}
        ip = r[2][0:-3]
        mac = r[-1].upper()
        dict01['ip'] = ip
        dict01['mac'] = mac
        return dict01

    def judge_terminal_update(self):
        """验证android终端是否要升级，要升级返回0 ，不升级返回1"""
        version = self.termianl_system_version()
        if version in self.system_android_version():
            return 1
        else:
            return 0

    def disconnect_all_devices_and_connect(self, ip):
        """断开adb所有连接，重新连接ip"""
        os.system("adb kill-server")
        os.system("adb devices")
        self.vdi_connect(ip)


if __name__ == "__main__":
    t = AndroidVdi()

    # t.input_username_passwd('expire_user', 'ad@2008')
    # t.vdi_connect('172.21.204.10')
    t.login('18_group1', "172.21.204.11", "123456")
    # t.click_guest_login(vdi_android_ip_list[0])
    # t.pwd_clear(20)
    # t.guest_login_set('idv2_02',t_pwd)
    # t.vdi_connect('172.21.204.10')
    # t.login('vdi1_03','172.21.204.11','123')
    # print t.termianl_system_version()
    # os.system('adb connect "172.21.3.204"')
    # t.vm_name_ip_set('vdi9', '172.21.195.78', '172.21.204.14')
    # t.vdi_connect('172.21.3.39')
    # t.screen_lock()
    # t.login('it_user_a2_1', '172.21.3.43', '123456')
    # t.vdi_disconnect('172.21.3.204')
    # t.guest_login_set('vdi3_01', '12322')
    # t.click_guest_login('172.21.3.204')
    # t.login('vdi3_01', '172.21.3.204')
    # t.sys_pwd_input()
    pass
