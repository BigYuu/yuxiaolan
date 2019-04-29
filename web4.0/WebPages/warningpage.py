#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll@houjinqi
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/10/16 15:21
"""
from Common.Basicfun import BasicFun
from Common.serverconn import *
from TestData.Logindata import *
from TestData.Warningdata import *
import time
from WebPages.LoginPage import Login

class WarningPage(BasicFun):
    #     元素定位
    # ifreme的id
    iframe_id = "frameContent"

    user_xpath = u"//*[text()='首页']"
    # 告警条数
    warming_count_xpath = "//*[@id='total_count']"
    # 告警内容
    warming__info_xpath = "//td[@class='rui-grid-body-td'][4]//*[@class='rui-grid-td-div table_common']"
    ##################################################
    # 告警按钮
    warning_button_xpath = "//*[@class = 'el-badge sk-navitem__badge']//ancestor::li"
    # 内存ECC告警内容
    warning_ram_xpath = u"//*[text()='主机:{} 告警内容: 内存ECC校验错误, 错误出现 1 次, 请联系售后:4008111000']"
    # CPU配置异常告警
    warning_cpu_xpath = u"//*[text()='主机:{} 告警内容: cpu 配置错误，错误出现 1 次, 请联系售后:4008111000']"

    # 镜像空间使用告警
    warning_lessons_xpath = u"//*[text()='主机:{} 告警内容: 镜像空间已满,请在web空间中删除不使用的镜像']"
    # 系统空间使用告警
    warning_system_xpath = u"//*[text()='主机:{} 告警内容: 操作系统空间已满,请联系售后4008111000']"

    # ssd cache目录变为只读告警
    warning_cache_xpath = u"//*[text()='主机:{} 告警内容: SSD文件系统不可访问, 请联系售后4008111000']"
    # 共享目录变为只读告警
    warning_share_xpath = u"//*[text()='主机:{} 告警内容: 共享目录文件系统变为只读, 请联系售后4008111000']"

    # 网卡连接异常告警
    warning_eth_xpath = u"//*[text()='主机:{} 告警内容: 网卡名称3: 第eth2 网卡未连接, 请检查端口,交换机,网线是否正常']"
    # 网卡速度变为百兆告警
    warning_netspeed_xpath = u"//*[contains(text(),'主机:{} 告警内容: 网卡名称{}: 第{} 网卡速度异常,网卡速度变为')]"
    # 业务网关不可达告警
    warning_gateway_xpath = u"//*[contains(text(),'主机:{} 告警内容: 业务网关1.1.1.1不可达, 请确认网关是否正常')]"
    # 存储网络冲突告警
    warning_storageip_xpath = u" //*[contains(text(),'主机:{} 告警内容: 存储网络10.14.195.{}与设备')]"

    def get_warming_count(self):
        time.sleep(3)
        self.get_ciframe(self.iframe_id)
        temp = self.find_elem(self.warming_count_xpath).text
        return temp

    def get_warming_info(self):
        return self.find_elem(self.warming__info_xpath).text
        # elems =self.find_elems(self.warming__info_xpath)
        # return elems[num-1].text

    def login_again(self):
        """
        重新登录
        """
        Login.login(c_user, c_pwd)




    ###############################################
    # 进入告警页面
    def goto_warning_page(self):
        time.sleep(1)
        self.find_elem(self.warning_button_xpath).click()

    # 进入告警内容的iframe
    def goto_warning_iframe(self):
        time.sleep(1)
        self.get_ciframe(self.iframe_id)

    def get_warning_count(self):
        time.sleep(3)
        self.get_ciframe(self.iframe_id)
        temp = self.find_elem(self.warming_count_xpath).text
        return temp

    def get_warning_info(self, xpath, wait_times=60):
        return self.find_elem(xpath, wait_times=wait_times).text
        # elems =self.find_elems(self.warming__info_xpath)
        # return elems[num-1].text

    def get_warning_is_show(self, xpath, timeout=450):
        """
        循环刷新页面等待告警出现
        :param xpath:
        :param timeout:
        :return:
        """
        start = time.time()
        end = time.time()
        self.click_elem(self.user_xpath)
        self.click_elem(self.warning_button_xpath)
        time.sleep(2)
        while (end - start) < timeout:
            self.get_ciframe(self.iframe_id)
            final = self.elem_is_exist2(xpath)
            self.back_current_page()
            if final is None:
                end = time.time()
                time.sleep(60)
                self.driver.refresh()
                time.sleep(1)
            else:
                return 1
        return 0


# 返回服务器是RCD还是RCM
def host_info(ip):
    read = server_conn(ip, host_info_command)
    try:
        if 'RCD' in read.splitlines()[10]:
            return 'RCD'
        if 'RCM' in read.splitlines()[10]:
            return 'RCM'
    except:
        return ''


# 检测服务器中已连接上的网卡
def eth_check(ip):
    read_list = server_conn(ip, 'ifconfig').splitlines()
    for i in range(len(read_list)):
        if 'eth' in read_list[i]:
            if 'RUNNING' in read_list[i + 1]:
                eth_list.append(read_list[i].split()[0])
    return eth_list


# df查找目录使用情况，返回为一个列表
def document_used(ip, doc):
    read = server_conn(ip, 'df')
    dic = {}
    for i in read.splitlines():
        if doc in i:
            dic['total'] = i.split()[1]
            dic['used'] = i.split()[2]
            dic['percent'] = i.split()[4]
            return dic


# 使用falloc占用目录空间为90%以上
def doc_falloc(ip, doc, percent=1.00):
    dic = document_used(ip, doc)
    total = int(dic['total'])
    used = int(dic['used'])
    per = int(dic['percent'].split("%")[0])
    if per <= 90:
        add = int(((total * percent) - used) / 1048576)
        cmd = 'fallocate ' + doc + '/test_image -l ' + str(add) + 'G'
        server_conn(ip, str(cmd))


# 恢复被falloc占用的目录空间
def doc_free(ip, doc):
    cmd = 'rm -rf ' + doc + '/test_image'
    server_conn(ip, cmd)


# 修改已连接的第一块业务网卡速率为100
def netspeed_edit(ip):
    eth_check(ip)
    server_conn(ip, edit_netspeed_command.format(eth_list[0]))


# 修改已连接的第一块业务网卡速率为100
def netspeed_recover(ip):
    eth_check(ip)
    server_conn(ip, recover_netspeed_command.format(eth_list[0]))


# 连接虚拟服务器宿主机172.21.195.30,用于操作虚拟服务器重启，关闭
def reboot_virtual_hosts():
    time.sleep(1)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='172.21.195.30', username='root', password="ruijie!@#$%^")
    ssh.exec_command(command='virsh destroy 3.0.80.216', get_pty=True)
    time.sleep(3)
    ssh.exec_command(command='virsh start 3.0.80.216', get_pty=True)
    ssh.close()

# # 制造全部异常场景
# def trouble_maker(ip):
#     # 告警用例A1.1:制造内存ECC异常
#     server_conn(ip, edit_ram_command)
#     # 告警用例A1.2：制造CPU异常
#     server_conn(ip, edit_cpu_command)
#     # 告警用例A1.3：使镜像目录空间占用为90%以上
#     doc_falloc(ip, lessons_doc)
#     # 告警用例A1.4：使系统目录占用空间为90%以上
#     doc_falloc(ip, system_doc)
#     # 告警用例A1.5：使cache目录变为只读
#     server_conn(ip, edit_fstab)
#     server_conn(ip, ro_cache_rcd_command)
#     # 告警用例A1.6：使共享目录变为只读
#     if host_info(ip) == 'RCD':
#         server_conn(ip, ro_share_rcd_command)
#     elif host_info(ip) == 'RCM':
#         server_conn(ip, ro_share_rcm_command)
#     # 告警用例A1.7：使网卡断开连接
#     server_conn(ip, down_eth2_command)
#     # 告警用例A1.8：使网卡断开连接网卡速度变为百兆
#     netspeed_edit(ip)
#     # 告警用例A1.10：修改错误网关
#     server_conn(ip, edit_gateway_command)
#     # 告警用例A1.11：业务网络冲突告警
#     # server_conn('172.21.195.204', edit_wan0_command.format(mainip.split('.')[3]))
#     # 告警用例A1.12：存储网络冲突告警
#     server_conn('172.21.195.216', edit_bond1_command.format(int(mainip.split('.')[3])+1))
#     server_conn('172.21.195.216', restart_network)
#
#
# # 恢复正常场景
# def trouble_helper(ip):
#     server_conn(ip, recover_ram_cpu_command)
#     doc_free(ip, lessons_doc)
#     doc_free(ip, system_doc)
#     # A1.5
#     server_conn(ip, recover_cache_rcd_command)
#     # A1.6
#     server_conn(ip, recover_share_rcd_command)
#     # A1.7
#     server_conn(ip, up_eth2_command)
#     # A1.8
#     netspeed_recover(ip)
#     # A1.10
#     server_conn(ip, recover_gateway_command)
#     # A1.12
#     server_conn('172.21.195.216', recover_bond1_command.format(mainip.split('.')[3]))
#     server_conn('172.21.195.216', restart_network)
