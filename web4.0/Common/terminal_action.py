#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/11/12 11:04
"""
from Common.serverconn import *
import win32gui
from pymouse import PyMouse
from pykeyboard import PyKeyboard
from PIL import Image
import uiautomation as automation
from TestData.basicdata import *
import win32api
import win32com.client
import win32con
import math
import operator
import logging
import time
import sys
import re
import os


#     比较图片不同
def compare_picture(path_one, path_two):
    image1 = Image.open(path_one)
    image2 = Image.open(path_two)
    histogram1 = image1.histogram()
    histogram2 = image2.histogram()
    try:
        diff = math.sqrt(
            reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, histogram1, histogram2))) / len(histogram1))
        return diff
    except Exception as e:
        logging.exception(e)
        logging.info("两张图片不同无法比较")


def idv_get_picture(ip):
    """idv裁剪图片并保存"""
    terminal_conn(ip, 'export DISPLAY=:0;sleep 0.15;rm Pictures/set.png;sleep 0.15;scrot ~/Pictures/set.png')
    terminal_download_conn(ip, 'Pictures/')
    im = Image.open(os.path.join(picture_dir, "set.png"))
    x, y = im.size
    region = im.crop((int(x / 2) - 426, int(y / 2) - 290, int(x / 2) + 426, int(y / 2) - 190))
    region.save(os.path.join(picture_dir, "set1.png"))
    return os.path.join(picture_dir, "set1.png")


def idv_get_size_picture(ip, x1, y1, x2, y2):
    """idv裁剪图片并保存,传入参数为裁剪图片位置"""
    terminal_conn(ip, 'export DISPLAY=:0;sleep 0.15;rm Pictures/set.png;sleep 0.15;scrot ~/Pictures/set.png')
    terminal_download_conn(ip, 'Pictures/')
    im = Image.open(os.path.join(picture_dir, "set.png"))
    region = im.crop((x1, y1, x2, y2))
    region.save(os.path.join(picture_dir, "set.png"))
    return os.path.join(picture_dir, "set.png")


def idv_get_login_picture(ip):
    """idv裁剪图片并保存(保存设置的图片默认截取全部)"""
    idv_screan_siz_set(ip)
    terminal_conn(ip, 'export DISPLAY=:0;sleep 0.15;rm Pictures/set.png;sleep 0.15;scrot ~/Pictures/set.png')
    terminal_download_conn(ip, 'Pictures/')
    return os.path.join(picture_dir, "set.png")


def vdi_get_picture(ip, x1, y1, x2, y2):
    """vdi 裁剪图片并保存 """
    terminal_conn(ip,
                  'export DISPLAY=:0;mkdir Pictures;sleep 0.15;rm Pictures/lset.png;sleep 0.15;'
                  'scrot ~/Pictures/lset.png')
    terminal_download_conn(ip, 'Pictures/')
    im = Image.open(os.path.join(picture_dir, "lset.png"))
    x, y = im.size
    region = im.crop((int(x / 2) - int('{}'.format(x1)), int(y / 2) - int('{}'.format(y1)),
                      int(x / 2) + int('{}'.format(x2)), int(y / 2) + int('{}'.format(y2))))
    region.save(os.path.join(picture_dir, "lset.png"))
    return os.path.join(picture_dir, "lset.png")


def get_scren_size(ip):
    """获取屏幕分辨率"""
    try:
        size_info = terminal_conn(ip, 'export DISPLAY=:0;xrandr --current | head -n 1')
        if size_info.__contains__("Can't open display :0"):
            return None
        else:
            size = re.findall('.*current (.*?),.*', size_info)
            a = size[0].split(' x ')
            return a
    except Exception as e:
        logging.error(e)
        logging.info("不能连接上终端，查看终端是否断网或关机")


def get_current_win(ip):
    """获取当前鼠标所在窗口名称"""
    result = terminal_conn(ip, "export DISPLAY=:0;xdotool getmouselocation")
    if re.match(r'.*?window:(\d+)', result) is not None:
        return re.findall(r'.*?window:(\d+)', result)[0]
    else:
        print("虚机不在登入界面")
        return None


def idv_screan_siz_set(ip):
    """设置idv终端分辨率"""
    a = get_scren_size(ip)
    if a is not None:
        if a[0] != '1024' and a[1] != '768':
            terminal_conn(ip, "export DISPLAY=:0;xrandr -s 1024x768_60.00;sleep 1;pkill IDV_Client;sleep 10")
    else:
        logging.error("终端不再未连接或已登录无法设置分辨率")


def idv_in_login_page(ip):
    """判断终端是否在用户登入界面"""
    flag = ''
    try:
        size_info = terminal_conn(ip, 'export DISPLAY=:0;xrandr --current | head -n 1')
        if size_info.__contains__("Can't open display :0"):
            flag = 0
        else:
            try:
                idv_screan_siz_set(ip)
                path = idv_get_login_picture(ip)
                if compare_picture(os.path.join(picture_dir, "idv_login.png"), path) <= 200:
                    flag = 1
                    time.sleep(3)
            except Exception as err:
                logging.error(err)
                logging.info("终端截图失败")
    except:
        logging.error("未知错误")
    return flag


def idv_in_login_page2(ip):
    """判断终端是否在用户登入界面"""
    flag = 0
    n = 0
    while n < 300:
        try:
            size_info = terminal_conn(ip, 'export DISPLAY=:0;xrandr --current | head -n 1')
            if size_info.__contains__("Can't open display :0"):
                time.sleep(3)
            else:
                try:
                    idv_screan_siz_set(ip)
                    path = idv_get_login_picture(ip)
                    if compare_picture(os.path.join(picture_dir, "idv_login.png"), path) <= 200:
                        flag = 1
                        time.sleep(3)
                except Exception as err:
                    logging.error(err)
                    logging.info("终端截图失败")
                break
        except:
            time.sleep(3)
        n = n + 1
    return flag


def idv_set_init(ip, u_name=None):
    """idv登入页面初始化"""
    if judje_idv_vm_is_running(ip) == 0:
        cd_ip = server_sql_qurey(host_ip, "SELECT vm_ip from idv_terminal where ip='{}'".format(ip))
        if cd_ip is not None and len(cd_ip) > 0:
            print(cd_ip)
            cd_ip = cd_ip[0][0]
        else:
            cd_ip = None
        if cd_ip is not None:
            if win_conn_useful(cd_ip, s_user, s_pwd) == u'winrm可使用':
                win_conn(cd_ip, s_user, s_pwd, "login")
                time.sleep(2)
                win_conn(cd_ip, s_user, s_pwd, "logout")
                time.sleep(50)
        else:
            logging.error("终端未连接")
    else:
        pass
    idv_screan_siz_set(ip)
    s = (1024 / 2 - 426, 768 / 2 - 290,)
    size = (852, 580)
    path1 = idv_get_picture(ip)
    path2 = idv_get_login_picture(ip)
    if compare_picture(os.path.join(picture_dir, "rujie_input.png"), path1) <= 100:
        terminal_conn(ip,
                      "export DISPLAY=:0;xdotool type 'ruijie.com';sleep 1;xdotool mousemove {0} {1} click 1"
                      .format(s[0] + size[0] * 0.45, s[1] + size[1] * 0.95))

    elif compare_picture(os.path.join(picture_dir, "set_head.png"), path1) <= 100:
        terminal_conn(ip, "export DISPLAY=:0;sleep 0.15;xdotool mousemove 575 638 click 1")

    elif compare_picture(os.path.join(picture_dir, "unbind_image.png"), path2) <= 200:
        terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 780 280 click 1;sleep 2")
        if u_name is not None:
            idv_pattern_chose(ip, name=u_name)
        else:
            idv_pattern_chose(ip, pattern='public')

    elif compare_picture(os.path.join(picture_dir, "pattern_chose.png"), path2) <= 360:
        if u_name is not None:
            idv_pattern_chose(ip, name=u_name)
        else:
            idv_pattern_chose(ip, pattern='public')
    if compare_picture(os.path.join(picture_dir, "idv_login.png"), path2) <= 350:
        pass
    else:
        logging.error("未知页面")


def click_idv_set(ip):
    """ 点击设置"""
    a = get_scren_size(ip)
    terminal_conn(ip, "export DISPLAY=:0;sleep 0.15;xdotool mousemove {0} {1} click 1"
                  .format(int(a[0]) * 0.42, int(a[1]) * 0.92))
    s = (int(a[0]) / 2 - 426, int(a[1]) / 2 - 290,)
    size = (852, 580)
    path1 = idv_get_picture(ip)
    if compare_picture(os.path.join(picture_dir, "rujie_input.png"), path1) <= 100:
        terminal_conn(ip,
                      "export DISPLAY=:0;sleep 0.15;xdotool type 'ruijie.com';sleep 1;xdotool mousemove {0} {1} click 1"
                      .format(s[0] + size[0] * 0.45, s[1] + size[1] * 0.95))
        time.sleep(1)


def idv_initialization_click(ip):
    """idv用户初始化,点击下载镜像"""
    idv_screan_siz_set(ip)
    terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 823 272 click 1")


def idv_pattern_chose(ip, pattern='single', name=None, times=300):
    """idv选择用户模式下载镜像"""
    if pattern == 'single':
        if name is not None:
            terminal_conn(ip,
                          "export DISPLAY=:0;xdotool mousemove 307 236 click 1;sleep 0.15;xdotool type {}".format(name))
    elif pattern == 'public':
        terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 487 239 click 1")
    elif pattern == 'common':
        terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 720 239 click 1")
    terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 499 580 click 1")
    n = 0
    while n < times:
        path = idv_get_login_picture(ip)
        if compare_picture(os.path.join(picture_dir, "idv_login.png"), path) <= 360:
            break
        else:
            time.sleep(6)
        n = n + 1


def mirror_dowload(ip):
    """检验镜像是否下载完成"""
    i = 0
    winds = get_current_win(ip)
    while i <= 40:
        temp = get_current_win(ip)
        if winds != temp:
            break
        else:
            winds = temp
            time.sleep(30)
        i = i + 1
    if i >= 41:
        raise NotImplementedError("下载镜像失败")
    else:
        logging.info("镜像下载完成可登入")


def idv_init_to_login(ip, pattern='single', name=None):
    """终端初始化完成到登录界面"""
    idv_initialization_click(ip)
    time.sleep(10)
    idv_pattern_chose(ip, pattern, name)
    mirror_dowload(ip)


def idv_is_bind_image(ip):
    """判断终端是否绑定镜像,"""
    flag = 0
    try:
        path = idv_get_login_picture(ip)
        if compare_picture(os.path.join(picture_dir, "unbind_image.png"), path) <= 100:
            flag = 1
    except:
        logging.error("未知错误")
    return flag


def idv_change_pwd(ip, name, pwd, oldpwd='123456'):
    """修改密码"""
    idv_set_init(ip)
    terminal_conn(ip,
                  "export DISPLAY=:0;xdotool mousemove 618 388 click 1;sleep 0.3;xdotool type '{0}';sleep 0.15;"
                  "xdotool key 'Tab';xdotool type {2};sleep 0.15;xdotool key 'Tab';sleep 0.15;xdotool type {1};sleep 1;"
                  "xdotool key 'Tab';sleep 0.15;xdotool type {1};sleep 0.15;xdotool mousemove 430 545 click 1"
                  .format(name, pwd, oldpwd))


def idv_is_enter_sys(ip):
    """判断是否在登录到windows系统"""
    n = 0
    flag = 0
    while n < 40:
        a = get_scren_size(ip)
        if a is None:
            flag = 1
            break
        else:
            time.sleep(30)
        n = n + 1
    return flag


def idv_login(ip, user_name=None, pwd='123'):
    """idv 登入"""
    idv_set_init(ip, u_name=user_name)
    terminal_conn(ip,
                  "export DISPLAY=:0;xdotool mousemove 522 297 click 1;sleep 0.15;xdotool key 'ctrl+a' 'BackSpace';"
                  "sleep 0.15;xdotool type '{0}';sleep 0.15;xdotool key 'Return';"
                  "sleep 0.15;xdotool key 'Tab';sleep 0.15;"
                  "xdotool type '{1}';sleep 0.2;xdotool key 'Return';"
                  .format(user_name, pwd))


def idv_guest_login(ip):
    """idv访客登入"""
    idv_set_init(ip)
    sql1 = "SELECT t.guest_login_status FROM idv_terminal t  where t.ip='{}'".format(ip)
    state_info = server_sql_qurey(host_ip, sql1)[0][0]
    if state_info != 0:
        sql2 = "update idv_terminal set guest_login_status='0' where ip='{}'".format(ip)
        server_sql_qurey(host_ip, sql2, qureresult=0)
        server_conn(host_ip, 'service tomcat restart')
        time.sleep(30)
        terminal_reboot(ip)
        time.sleep(2)
    terminal_conn(ip, "export DISPLAY=:0;sleep 0.15;xdotool mousemove 502 552 click 1")


def idv_set_name_host_ip(ip, name, h_ip):
    """ 点击设置配置终端名称和服务器ip"""
    click_idv_set(ip)
    terminal_conn(ip,
                  "export DISPLAY=:0;xdotool key 'BackSpace';sleep 0.2;xdotool type '{0}';sleep 0.15;"
                  "xdotool key 'Return';sleep 0.15;xdotool key 'Tab';sleep 0.15;xdotool key 'ctrl+a' 'BackSpace';"
                  "xdotool type '{1}';sleep 0.3;xdotool mousemove 417 636 click 1"
                  .format(name, h_ip))


def idv_vm_ip_set(ip, ipstate, userip=None, mask=None, gateway=None, dns=None):
    """idv虚机ip获取方式设置 dynamic为动态，static指定ip"""
    a = get_scren_size(ip)
    click_idv_set(ip)
    terminal_conn(ip, "export DISPLAY=:0;sleep 0.15;sleep 0.3;xdotool mousemove {0} {1} click 1"
                  .format(int(a[0]) * 0.41, int(a[1]) * 0.28))
    if ipstate == 'dynamic':
        terminal_conn(ip,
                      "export DISPLAY=:0;sleep 0.15;sleep 0.3;xdotool mousemove 279 363 click 1;sleep 0.15;"
                      "xdotool mousemove 282 563 click 1;sleep 0.15;xdotool mousemove 412 633 click 1")
    elif ipstate == 'static':
        terminal_conn(ip, "export DISPLAY=:0;sleep 0.15;sleep 0.3;xdotool mousemove 279 399 click 1")
        if userip is not None:
            terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 480 421 click 1;sleep 0.15;"
                              "xdotool key 'ctrl+a' 'BackSpace';sleep 0.15;xdotool type{0}"
                              ";sleep 0.15;".format(userip))
        if mask is not None:
            terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 480 466 click 1;sleep 0.15;"
                              "xdotool key 'ctrl+a' 'BackSpace';sleep 0.15;xdotool type{0}"
                              ";sleep 0.15;".format(mask))
        if gateway is not None:
            terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 497 511 click 1;sleep 0.15;"
                              "xdotool key 'ctrl+a' 'BackSpace';sleep 0.15;xdotool type{0}"
                              ";sleep 0.15;".format(gateway))
        if dns is not None:
            terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 923 557 click 1;sleep 0.15;"
                              "xdotool mousemove 446 577 click 1;sleep 0.15;"
                              "xdotool key 'ctrl+a' 'BackSpace';sleep 0.15;xdotool type{0}"
                              ";sleep 0.15;".format(dns))
    else:
        logging.info("输入的虚机ip设置方式不正确，只有static静态和dynamic动态两种方式")


def vdi_input_pwd_judge(ip):
    """vdi 判断是否在初始输入密码到设置界面，是则输入密码点击确认"""
    path1 = vdi_get_picture(ip, 200, 100, 200, 100)
    if compare_picture(path1, os.path.join(picture_dir, 'vdi_ruijie.png')) <= 30:
        terminal_conn(ip, "export DISPLAY=:0;xdotool type 'ruijie.com';sleep 1;xdotool mousemove 474 457 click 1")


def vdi_set_judge(ip):
    """vdi判断是否在设置页面,是则点击关闭出口"""
    path1 = vdi_get_picture(ip, 310, 325, 310, -275)
    if compare_picture(path1, os.path.join(picture_dir, 'vdi_set_head.png')) <= 30:
        terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 806 71 click 1")


def vdi_change_pwd_judeg(ip):
    """判断是否在修改密码页面是，则点击关闭按钮"""
    path1 = vdi_get_picture(ip, 231, 115, 231, -65)
    if compare_picture(path1, os.path.join(picture_dir, 'vdi_cpasswd.png')) <= 30:
        terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 596 470 click 1")


def vdi_set_init(ip):
    """vdi终端初始化到登入输入账号密码的页面"""
    terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 596 470")
    if get_current_win(ip) is not None:
        vdi_lock_scren(ip)
    else:
        vdi_input_pwd_judge(ip)
        vdi_set_judge(ip)
        vdi_change_pwd_judeg(ip)


def vdi_lock_scren(ip):
    """vdi终端锁屏"""
    terminal_conn(ip, "export DISPLAY=:0;sleep 0.15; xdotool key 'super+l'")


def vdi_terminal_close(ip, name='Administrator', pwd='rcd'):
    """vdi终端关机"""
    get_win_conn_info(ip, name, pwd, "shutdown -s -t 00 -f")
    # terminal_conn(ip, "export DISPLAY=:0;xdotool key 'super';sleep 1;xdotool mousemove {0} {1} click 1;".format(
    #     int(a[0]) * 0.19, int(a[1]) * 0.92))


def vdi_close(ip):
    """vdi点击强制关机"""
    a = get_scren_size(ip)
    terminal_conn(ip,
                  'export DISPLAY=:0;xdotool mousemove {0} 0 click 1;sleep 0.15;xdotool mousemove {1} 10 click 1;'
                  'sleep 0.15;xdotool mousemove {2} {3} click 1'.format(int(a[0]) * 0.5, int(a[0]) * 0.52,
                                                                        int(a[0]) * 0.48, int(a[1]) * 0.58))


def vdi_login(ip, user_name, pwd, spwd='rcd'):
    """vdi 输入用户名密码点击登入"""
    vdi_set_init(ip)
    terminal_conn(ip,
                  "export DISPLAY=:0;xdotool mousemove 468 226 click 1;sleep 0.15;xdotool key 'ctrl+a' 'BackSpace';"
                  "sleep 0.2;xdotool type '{0}';sleep 0.5;xdotool key 'Tab';sleep 0.5;xdotool key 'ctrl+a' 'BackSpace';"
                  "xdotool type '{1}';sleep 0.5;xdotool mousemove 509 406 click 1;sleep 45;xdotool type {2};"
                  "sleep 0.5;xdotool key 'Return'"
                  .format(user_name, pwd, spwd))


def sys_passed_input(ip, spwd='rcd'):
    """windows系统密码输入"""
    terminal_conn(ip, "export DISPLAY=:0;xdotool type {0};sleep 0.5;xdotool key 'Return'".format(spwd))


def click_vdi_set(ip):
    """vdi 终端点击设置"""
    vdi_set_init(ip)
    terminal_conn(ip, "export DISPLAY=:0;sleep 0.15;xdotool mousemove 472 624 click 1")
    vdi_input_pwd_judge(ip)


def vdi_sleep_time_set(ip, n=10):
    """vdi终端休眠时间设置"""
    click_vdi_set(ip)
    terminal_conn(ip, "export DISPLAY=:0;sleep 0.15;xdotool mousemove 472 624 click 1")
    if n == 10:
        terminal_conn(ip, "sed -i '5cid=0' /etc/RCC-Client/x_idle.ini")
    elif n == 30:
        terminal_conn(ip, "sed -i '5cid=1' /etc/RCC-Client/x_idle.ini")
    elif n == 1:
        terminal_conn(ip, "sed -i '5cid=2' /etc/RCC-Client/x_idle.ini")
    elif n == 3:
        terminal_conn(ip, "sed -i '5cid=3' /etc/RCC-Client/x_idle.ini")
    elif n == 5:
        terminal_conn(ip, "sed -i '5cid=4' /etc/RCC-Client/x_idle.ini")
    elif n == 8:
        terminal_conn(ip, "sed -i '5cid=5' /etc/RCC-Client/x_idle.ini")
    else:
        terminal_conn(ip, "sed -i '5cid=6' /etc/RCC-Client/x_idle.ini")


def vdi_name_ip_set(ip, name, hip):
    """设置服务器ip和终端名称"""
    click_vdi_set(ip)
    terminal_conn(ip,
                  "export DISPLAY=:0;xdotool mousemove 389 160 click 1;sleep 0.5;xdotool key 'ctrl+a' 'BackSpace';"
                  "xdotool type {0};sleep 1.5;xdotool key 'Tab';sleep 0.15;xdotool key 'ctrl+a' 'BackSpace';"
                  "sleep 1;xdotool type {1};sleep 0.15;xdotool mousemove 509 682 click 1"
                  .format(name, hip))


def vdi_ipstate_set(ip, state="dynamic", userip=None, mask=None, gateway=None, dns=None):
    """设置vdi终端的ip获取方式， dynamic为动态，static指定ip"""
    click_vdi_set(ip)
    if state == "dynamic":
        terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 250 316 click 1;sleep 0.15;"
                          "xdotool mousemove 250,520 click 1;sleep 0.15;")
    elif state == "static":
        terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 419 397 click 1;")
        if userip is not None:
            terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 432,376 click 1;sleep 0.15;"
                              "xdotool key 'ctrl+a' 'BackSpace';sleep 0.15;xdotool type{0}"
                              ";sleep 0.15;".format(userip))
        if mask is not None:
            terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 436 416 click 1;sleep 0.15;"
                              "xdotool key 'ctrl+a' 'BackSpace';sleep 0.15;xdotool type{0}"
                              ";sleep 0.15;".format(mask))
        if gateway is not None:
            terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 436 456 click 1;sleep 0.15;"
                              "xdotool key 'ctrl+a' 'BackSpace';sleep 0.15;xdotool type{0}"
                              ";sleep 0.15;".format(gateway))
        if dns is not None:
            terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 446 577 click 1;sleep 0.15;"
                              "xdotool key 'ctrl+a' 'BackSpace';sleep 0.15;xdotool type{0}"
                              ";sleep 0.15;".format(dns))
    else:
        logging.info("输入的虚机ip设置方式不正确，只有static静态和dynamic动态两种方式")


def vdi_set_passwd(ip, name, oldpasswd='123', newpasswd='1'):
    """修改密码"""
    terminal_conn(ip, "export DISPLAY=:0;sleep 0.15;sleep 1;xdotool mousemove 633 325 click 1;sleep 0.5;"
                      "xdotool key 'BackSpace';xdotool type {0};sleep 1.5;xdotool key 'Tab';sleep 0.15;"
                      "xdotool type {1};sleep 0.15;sleep 1.5;xdotool key 'Tab';xdotool type {2};"
                      "sleep 0.15;xdotool key 'Tab';sleep 0.15;xdotool type {2};sleep0.15;"
                      "xdotool mousemove 433 473 click 1"
                  .format(name, oldpasswd, newpasswd))


def vdi_guest_login(ip, user_name, pwd):
    """vdi访客登入"""
    flag = get_vdi_visitor_info(ip)
    click_vdi_set(ip)
    terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 580 77 click 1")
    if flag == 0:
        terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 442 164 click 1")
    else:
        terminal_conn(ip, "export DISPLAY=:0;xdotool key 'Tab'")
    terminal_conn(ip,
                  "export DISPLAY=:0;xdotool key 'Tab';sleep 0.15;xdotool key 'ctrl+a' 'BackSpace';xdotool type '{0}';"
                  "sleep 1.5;xdotool key 'Tab';sleep 0.15;xdotool key 'ctrl+a' 'BackSpace';sleep 1;xdotool type {1};"
                  "sleep 0.1;xdotool mousemove 801 73 click 1;sleep 0.15;xdotool mousemove 518 544 click 1"
                  .format(user_name, pwd))


def click_vdi_guest_login(ip):
    """vdi终端点击访客登入按钮"""
    vdi_set_init(ip)
    terminal_conn(ip, "export DISPLAY=:0;sleep 0.15;xdotool mousemove 801 73 click 1")


def get_vdi_visitor_info(ip):
    """获取访客登入开启否信息"""
    info = terminal_conn(ip, 'cat /etc/RCC-Client/visitor_mode.ini')  # vdi的命令
    return re.findall(r'.*enable=(\d).*', info)[0]


def get_client_winds_siaze():
    """获取利旧客户端窗口位置"""
    rcc_client_host_ip_set()
    try:
        dialog = win32gui.FindWindow("RCD_WINDOW_CLIENT_MAIN_WND", "RCC-Client")
        print
        if dialog == 0:
            win32api.ShellExecute(0, 'open', "C:\\Program Files (x86)\\RCC-Client\\RCC-Client.exe", '', '', 0)
            time.sleep(2)
            dialog = win32gui.FindWindow("RCD_WINDOW_CLIENT_MAIN_WND", "RCC-Client")
        time.sleep(2)
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys('%')
        win32gui.SetForegroundWindow(dialog)
        time.sleep(2)
        a = win32gui.GetWindowRect(dialog)
        return a
    except Exception as error:
        logging.exception("未找到窗口查看是否开启利旧客户端")
        raise error


def close_client_winds(name='RCC-Client.exe'):
    """关闭利旧客户端窗口"""
    os.system("taskkill /im {} /f".format(name))


def get_client_guest_info():
    """查看利旧客户端设置"""
    with open('C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
        p = f.read()
        info = re.findall(r'.*Visitor=([A-Z]+).*', p)
        if info == []:
            return None
        else:
            return info[0]


def clear_info():
    """利旧清除信息"""
    k = PyKeyboard()
    k.press_keys([k.control_key, 'a'])
    time.sleep(0.5)
    k.tap_key(k.delete_key)


def client_login(name, pwd):
    """利旧客户端登入"""
    close_client_winds()
    a = get_client_winds_siaze()
    time.sleep(3)
    size = (a[2] - a[0], a[3] - a[1])
    m = PyMouse()
    k = PyKeyboard()
    time.sleep(1)
    if get_client_guest_info() == 'FALSE' or get_client_guest_info() is None:
        m.click(int(a[0] + size[0] * 0.45), int(a[1] + size[1] * 0.46))
        time.sleep(1)
        clear_info()
        time.sleep(2)
        k.tap_key(k.shift_key)
        time.sleep(2)
        k.type_string(name)
        k.tap_key(k.return_key)
        m.click(int(a[0] + size[0] * 0.45), int(a[1] + size[1] * 0.52))
    else:
        m.click(int(a[0] + size[0] * 0.45), int(a[1] + size[1] * 0.41))
        time.sleep(1)
        clear_info()
        time.sleep(2)
        k.tap_key(k.shift_key)
        time.sleep(2)
        k.type_string(name)
        time.sleep(2)
        k.tap_key(k.return_key)
        time.sleep(2)
        m.click(int(a[0] + size[0] * 0.45), int(a[1] + size[1] * 0.48))
    clear_info()
    k.type_string(pwd)
    time.sleep(1)
    k.tap_key(k.return_key)
    m.click(int(a[0] + size[0] * 0.5), int(a[1] + size[1] * 0.62))


def client_kill():
    """杀掉利旧客户端进程"""
    os.system("taskkill /F /IM RCC-Client.exe 1>nul 2>nul")


def client_error_passwd_click():
    """当输入的密码错误时，点击关闭密码错误输入框"""
    win = automation.PaneControl(ClassName='ErrorTipWnd')
    if win.Exists():
        win.Click(0.5, 0.87)


def client_clcik_other_set():
    """利旧客户端点击设置其他设置"""
    a = get_client_winds_siaze()
    size = (a[2] - a[0], a[3] - a[1])
    m = PyMouse()
    time.sleep(1)
    m.click(int(a[0] + size[0] * 0.45), int(a[1] + size[1] * 0.90))
    time.sleep(1)
    m.click(int(a[0] + size[0] * 0.32), int(a[1] + size[1] * 0.12))


def client_click_save():
    """点击保存"""
    a = get_client_winds_siaze()
    size = (a[2] - a[0], a[3] - a[1])
    m = PyMouse()
    time.sleep(1)
    m.click(int(a[0] + size[0] * 0.5), int(a[1] + size[1] * 0.92))
    time.sleep(1)
    m.click(int(a[0] + size[0] * 0.5), int(a[1] + size[1] * 0.61))


def client_sleep_time_set(n):
    """利旧客户端设置休眠时间"""
    a = get_client_winds_siaze()
    time.sleep(3)
    size = (a[2] - a[0], a[3] - a[1])
    m = PyMouse()
    client_clcik_other_set()
    time.sleep(0.5)
    m.click(int(a[0] + size[0] * 0.40), int(a[1] + size[1] * 0.21))
    time.sleep(0.5)
    if n == '10':
        m.click(int(a[0] + size[0] * 0.34), int(a[1] + size[1] * 0.25))
        time.sleep(0.5)
    else:
        m.click(int(a[0] + size[0] * 0.34), int(a[1] + size[1] * 0.43))
        time.sleep(0.5)
    client_click_save()


def client_guest_login(name, pwd):
    """利旧客户端访客登入"""
    close_client_winds()
    time.sleep(3)
    a = get_client_winds_siaze()
    size = (a[2] - a[0], a[3] - a[1])
    m = PyMouse()
    k = PyKeyboard()
    time.sleep(0.5)
    client_clcik_other_set()
    time.sleep(0.5)
    k.tap_key(k.shift_key)
    if get_client_guest_info() == 'FALSE':
        m.click(int(a[0] + size[0] * 0.32), int(a[1] + size[1] * 0.50))
        time.sleep(0.5)
    m.click(int(a[0] + size[0] * 0.35), int(a[1] + size[1] * 0.56))
    time.sleep(0.5)
    clear_info()
    time.sleep(2)
    k.type_string(name)
    time.sleep(0.5)
    k.tap_key(k.enter_key)
    time.sleep(0.3)
    m.click(int(a[0] + size[0] * 0.35), int(a[1] + size[1] * 0.63))
    time.sleep(0.5)
    k.tap_key(k.tab_key)
    clear_info()
    k.type_string(pwd)
    time.sleep(0.5)
    k.tap_key(k.enter_key)
    time.sleep(0.5)
    client_click_save()
    time.sleep(1)
    m.click(int(a[0] + size[0] * 0.52), int(a[1] + size[1] * 0.75))


def click_client_guest_login():
    """点击访客登入按钮"""
    a = get_client_winds_siaze()
    size = (a[2] - a[0], a[3] - a[1])
    m = PyMouse()
    m.click(int(a[0] + size[0] * 0.52), int(a[1] + size[1] * 0.75))


def client_logout():
    """利旧客户端锁屏"""
    try:
        time.sleep(3)
        dialog = win32gui.FindWindow("gdkWindowToplevel", "RCD-OA")
        win32gui.SetForegroundWindow(dialog)
        a = win32gui.GetWindowRect(dialog)
        size = (a[2] - a[0], a[3] - a[1])
        m = PyMouse()
        m.move(int(a[0] + size[0] * 0.54), int(a[1] + size[1] * 0.043))
        time.sleep(0.5)
        m.click(int(a[0] + size[0] * 0.54), int(a[1] + size[1] * 0.043))
        time.sleep(0.2)
        m.click(int(a[0] + size[0] * 0.57), int(a[1] + size[1] * 0.10))
    except Exception as error:
        logging.exception("未找到窗口查看是否开启利旧客户端")
        raise error


def client_lvdi_close():
    """利旧客户端关机"""
    time.sleep(3)
    dialog = win32gui.FindWindow("gdkWindowToplevel", "RCD-OA")
    win32gui.SetForegroundWindow(dialog)
    a = win32gui.GetWindowRect(dialog)
    size = (a[2] - a[0], a[3] - a[1])
    m = PyMouse()
    k = PyKeyboard()
    time.sleep(0.5)
    m.move(int(a[0] + size[0] * 0.54), int(a[1] + size[1] * 0.043))
    time.sleep(1)
    m.click(int(a[0] + size[0] * 0.54), int(a[1] + size[1] * 0.043))
    time.sleep(0.5)
    m.click(int(a[0] + size[0] * 0.65), int(a[1] + size[1] * 0.10))
    time.sleep(0.5)
    m.click(int(a[0] + size[0] * 0.45), int(a[1] + size[1] * 0.58))


def get_ip_mac(ip):
    """获取终端的ip和mac"""
    info = terminal_conn(ip, 'ifconfig')  # vdi的命令
    dict01 = {}
    mac = re.findall(r'.*?HWaddr (.*?) ', info)[0]
    ip = re.findall(r'.*inet addr:(.*?)  Bcast.* ', info)[0]
    dict01['ip'] = ip
    dict01['mac'] = mac.upper()
    return dict01


def get_vdi_terminal_name(ip):
    """获取vdi终端名称"""
    info = terminal_conn(ip, 'cat /etc/RCC-Client/RCC_Client_Config.ini')
    list01 = info.splitlines()
    return list01[5].split('=')[1]


def get_idv_terminal_name(ip):
    """获取idv终端名称"""
    info = terminal_conn(ip, 'cat /opt/lessons/RCC_Client/logic_configured.ini')
    return info.split()[-1]


def get_vdi_user_name(ip):
    """获取终端绑定用户"""
    info = terminal_conn(ip, 'cat /etc/RCC-Client/remember_password.ini')
    list01 = info.splitlines()
    return list01[4].split('=')[1]


def get_idv_user_name(ip):
    """获取idv终端用户名"""
    info = terminal_conn(ip, 'cat /opt/lessons/RCC_Client/logic.ini')
    if info.split()[-1] == '=':
        return None
    else:
        return info.split()[-1]


def get_idv_last_user_name(ip):
    """获取idv终端最后一次登入的用户名"""
    info = terminal_conn(ip, 'cat /opt/lessons/RCC_Client/last_logined_user.ini')
    list1 = info.splitlines()
    if list1[3] is None:
        return None
    else:
        return list1[3].split('=')[-1]


def get_terminal_system_info(ip, name, pwd):
    """获取idv终端系统信息"""
    info = get_win_conn_info(ip, name, pwd, 'systeminfo | find "OS"')
    first_line = info.splitlines()[0]
    return first_line.split(re.findall(':.*    ', first_line)[0])[1]


def get_terminal_mode(ip):
    """获取终端模式，0为单用户，1为多用户，2为公用户"""
    info = terminal_conn(ip, 'cat /opt/lessons/RCC_Client/logic.ini|grep mode')
    mode = info.split('=')[1]
    return mode


def get_terminal_info(ip):
    """获取终端信息，传入终端ip"""
    terminal_info = dict()
    info = terminal_conn(ip, 'ifconfig')
    terminal_info['ip'] = re.findall(r'.*inet addr:(.*?)  Bcast.* ', info)[0]
    terminal_info['mac'] = re.findall(r'.*?HWaddr (.*?) ', info)[0]
    terminal_info['mask'] = re.findall(r'.*?Mask:(.*)\r', info)[0]
    info2 = terminal_conn(ip, 'cat /opt/lessons/RCC_Client/logic.ini|grep mode')
    mode = info2.split('=')[1][1:2]
    if mode == '0':
        terminal_info['user_mode'] = u"单用户"
    elif mode == '1':
        terminal_info['user_mode'] = u"多用户"
    elif mode == '2':
        terminal_info['user_mode'] = u"公用户"
    else:
        terminal_info['user_mode'] = mode
        logging.info(u"终端用户模式有误")
    terminal_info['bind_user'] = get_idv_user_name(ip)
    terminal_info['terminal_name'] = get_idv_terminal_name(ip)
    info3 = terminal_conn(ip, 'cat /opt/lessons/acpitable.conf')
    terminal_info['product_name'] = re.findall('.*product_name=(.*)\r', info3)[0]
    terminal_info['sn'] = re.findall('.*sn=(.*)\r', info3)[0]
    terminal_info['version'] = re.findall('.*version=(.*)\r', info3)[0]
    terminal_info['soft_version'] = re.findall('.*version=(.*)\r', info3)[0]
    terminal_info['img'] = re.findall('.*img=(.*).base', info3)[0]
    terminal_info['hard_version'] = terminal_conn(ip, 'dmidecode -s system-version')[:-2]
    terminal_info['system_version'] = terminal_conn(ip, 'cat /etc/issue')[:-2]
    terminal_info['gateway'] = terminal_conn(ip, "ip route show |awk 'NR==1{print $3}'")[:-2]
    terminal_info['first_dns'] = terminal_conn(ip, "cat /etc/resolv.conf |grep nameserver|awk 'NR==1{print $2}'")[:-2]
    terminal_info['second_dns'] = terminal_conn(ip, "cat /etc/resolv.conf |grep nameserver|awk 'NR==2{print $2}'")[:-2]
    terminal_group_sql = "SELECT p.name FROM idv_user_group p where p.id " \
                         "in(select t.terminal_group_id from idv_terminal t  where host_name='{}')" \
        .format(terminal_info['terminal_name'])
    temp = server_sql_qurey(host_ip, terminal_group_sql)
    if temp != []:
        terminal_info['termian_group'] = server_sql_qurey(host_ip, terminal_group_sql)[0][0]
    else:
        terminal_info['termian_group'] = ''
    return terminal_info


def get_terminal_cloud_desk_info(ip):
    """获取终端云桌面信息，传入云桌面ip"""
    vm_info = dict()
    info = get_win_conn_info(ip, 'RCD', 'rcd', 'ipconfig/all')
    vm_info['vm_mac'] = re.findall(r'.*?Physical Address. . . . . . . . . : (.*)\r.*', info)[0]
    vm_info['vm_ip'] = re.findall(r'IPv4 Address. . . . . . . . . . . : (.*)\(Preferred\).*', info)[0]
    vm_info['vm_gatway'] = re.findall(r'.*?Default Gateway . . . . . . . . . : (.*)\r.*', info)[0]
    vm_info['vm_mask'] = re.findall(r'.*?Subnet Mask . . . . . . . . . . . : (.*)\r.*', info)[0]
    vm_info['vm_first_dns'] = re.findall(r'.*?DNS Servers . . . . . . . . . . . : (.*)\r.*', info)[0]
    vm_info['vm_second_dns'] = re.findall(r'.*?                                       (.*)\r.*', info)[0]
    vm_dhcp = re.findall(r'.*?DHCP Enabled. . . . . . . . . . . : (.*)\r.*', info)[0]
    if vm_dhcp == 'Yes':
        vm_info['vm_get_dhcp'] = u'手动'
        vm_info['vm_get_dns'] = u'手动'
    else:
        vm_info['vm_get_dhcp'] = u'自动'
        vm_info['vm_get_dns'] = u'自动'
    return vm_info


def terminal_reboot(ip):
    """终端在登录页面重启终端"""
    idv_screan_siz_set(ip)
    terminal_conn(ip, "export DISPLAY=:0;xdotool mousemove 584 696 click 1;sleep 0.5;"
                      "xdotool mousemove 573 366 click 1;sleep 0.5;xdotool mousemove 573 392 click 1;"
                      "sleep 1;xdotool mousemove 445 475 click 1")
    time.sleep(3)
    n = 0
    while n < 20:
        if judge_ip_is_used(ip) == u'ip可用':
            logging.info("重启成功")
            break
        else:
            time.sleep(3)
        n = n + 1


def judje_idv_vm_is_running(ip):
    """判断终端是否有虚机运行"""
    info = terminal_conn(ip, 'virsh list')
    if info.__contains__('running'):
        return 0
    else:
        return 1


def judge_ip_is_used(ip):
    """判断终端ip是否ping通过"""
    reload(sys)
    sys.setdefaultencoding('GBK')
    i = 0
    temp = ''
    while i < 50:
        info = os.popen('ping {0}'.format(ip))
        s1 = info.read()
        b = s1.splitlines()[2]
        if b.__contains__(u'的回复: 字节='):
            temp = u'ip可用'
            break
        else:
            time.sleep(3)
            temp = u'ip ping 不通'
        i = i + 1
    return temp


def win_conn_useful(ip, name, pwd, times=40):
    """判断登入虚机成功，winrm可使用"""
    n = 0
    temp = ''
    while n < times:
        try:
            info = get_win_conn_info(ip, name, pwd, 'ipconfig')
            if info.__contains__('Windows IP Configuration'):
                temp = u'winrm可使用'
                break
        except:
            time.sleep(6)
        n = n + 1
    return temp


def idv_guest_login_open(ip):
    """判断页面是否开启访客登入权限"""
    idv_screan_siz_set(ip)
    guest_path = idv_get_size_picture(ip, 467, 545, 568, 575)
    if compare_picture(os.path.join(picture_dir, 'idv_guest.png'), guest_path) < 10:
        temp = u'访客登入按钮开启'
    else:
        temp = u'访客登入按钮未开启'
    return temp


def get_guestool_info(ip):
    """获取guesttool版本信息ip为虚机ip"""
    info = get_win_conn_info(ip, s_user, s_pwd,
                             r'cd C:\Program Files (x86)\ && type RCC-Guest-Tool\version_guesttool.ini')
    return re.findall(r'.*?ruijie.rcc.guesttool.exefile=(.*?Setup.exe).*', info)[0]


def rcc_client_host_ip_set():
    """
    利旧客户端修改连接服务器虚ip
    :return:
    """
    d = ''
    with open(r'C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'r') as f:
        for line in f.readlines():
            if re.findall('.*mainServer=.*?\n', line) != list():
                line = 'mainServer={}\n'.format(vm_ip)
            d += line
    with open(r'C:\Program Files (x86)\RCC-Client\RCC-Client-Config.ini', 'w+') as f2:
        f2.write(d)


if __name__ == "__main__":
    rcc_client_host_ip_set()
    # idv_login('172.21.3.33','test_01','123')
    # idv_screan_siz_set('172.21.204.20')
    # idv_guest_login('172.21.204.22')
    # close_client_winds()
    # client_login('vdi3_01','123')
    # idv_login('172.21.204.23','idv2_01','123')
    # idv_get_login_picture('172.21.204.9')
    # get_guestool_info('172.21.204.30')
    pass
