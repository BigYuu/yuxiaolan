#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pytest
from Common.serverconn import *
from TestData.clientdata import *
from WebPages.clientPage import *
import socket



class Test_Client:


    @pytest.mark.client1
    @pytest.mark.case_level_0
    @pytest.mark.case_type_fun
    def test_client_abnormal_login ( self, ):
        logging.info ("----------------------------------利旧客户端A1.5,1.6用例开始执行------------------------------")
        cl = Client(BasicFun)
        flag_list=cl.client_abnormal_login()
        logging.info ("密码错误，校验客户端是否有提示")
        assert flag_list[0] == 1
        logging.info ("用户名错误，校验客户端是否有提示")
        assert flag_list[1] == 1
        logging.info ("输入32位用户名，校验客户端是否有提示")
        assert flag_list[2] == 1
        logging.info ("输入32位密码，校验客户端是否有提示")
        assert flag_list[3] == 1
        logging.info ("----------------------------------利旧客户端A1.5,1.6用例结束执行------------------------------")

    @pytest.mark.client
    @pytest.mark.case_level_0
    @pytest.mark.case_type_fun
    def test_client_install ( self,  ):
        logging.info ("----------------------------------利旧客户端A1.4,1.7用例开始执行------------------------------")
        cl = Client (BasicFun)
        flag_list = cl.client_login ()
        logging.info ("修改密码，校验用户是否修改密码成功")
        assert flag_list[0] == 1
        logging.info ("输入正确用户名密码，校验用户是否正常登录")
        assert flag_list[1] == 1
        logging.info ("----------------------------------利旧客户端A1.4,1.7用例结束执行------------------------------")


    @pytest.mark.client
    @pytest.mark.case_level_0
    @pytest.mark.case_type_fun
    def test_client_install ( self,  ):
        logging.info ("----------------------------------利旧客户端A1.10,1.11用例开始执行------------------------------")
        cl = Client (BasicFun)
        info = cl.remember_password ()
        logging.info ("重启终端，校验是否能记住密码")
        assert info [0] == "123456"
        info1 = cl.unremember_password ()
        logging.info ("重启终端，校验是否没有记住密码")
        assert info1 is None
        logging.info ("----------------------------------利旧客户端A1.10,1.11用例结束执行------------------------------")


    @pytest.mark.client
    @pytest.mark.case_level_0
    @pytest.mark.case_type_fun
    def test_client_install ( self):
        logging.info ("----------------------------------利旧客户端A1.12,A1.13,A1.14,A1.15用例开始执行------------------------------")
        cl = Client (BasicFun)
        info = cl.basic_info_Setting_hostname ()
        logging.info ("校验利旧客户端计算名写死，直接读取的是本机计算机名")
        hostname = socket.gethostname ()
        print "Host Name:%s" % hostname
        assert info [0] == hostname
        logging.info ("校验主服务器/备用服务器地址为合法IP能够修改，并且保存成功")
        info1= cl.basic_info_Setting_mainserver()
        assert info1 [0] == main_server
        flag_list = cl.basic_info_Setting_mainserverip ()
        logging.info ("校验主服务器/备用服务器地址为非法IP，无法保存")
        assert flag_list[0] == 1
        logging.info ("校验主服务器/备用服务器地址为空，无法保存")
        assert flag_list[1] == 1
        logging.info ("----------------------------------利旧客户端A1.12,A1.13,A1.14,A1.15用例结束执行------------------------------")

    @pytest.mark.client
    @pytest.mark.case_level_0
    @pytest.mark.case_type_fun
    def test_client_install ( self):
        logging.info ("----------------------------------利旧客户端A1.16用例开始执行------------------------------")
        cl = Client (BasicFun)
        logging.info ("校验利旧客户端读取本机IP信息")
        info1 = cl.network_configuration_ip ()
        hostname = socket.gethostname ()
        ip = socket.gethostbyname (hostname)
        assert info1[0] == ip
        logging.info ("校验没有dhcp场景")
        info2 = cl.network_configuration_netmask ()
        assert info2 is None
        info3 = cl.network_configuration_gateway ()
        assert info3 is None
        logging.info ("----------------------------------利旧客户端A1.16用例结束执行------------------------------")

    @pytest.mark.client
    @pytest.mark.case_level_0
    @pytest.mark.case_type_fun
    def test_client_install ( self):
        logging.info ("----------------------------------利旧客户端A1.18用例开始执行------------------------------")
        cl = Client (BasicFun)
        logging.info ("校验本地PC重启后，利旧客户端是否自动启动并且变为全屏")
        info1 = cl.other_seting_autoloin ()
        assert info1 == [0,0,1600,900]
        logging.info ("校验本地PC重启后，利旧客户端还是需要双击才能打开，不会开机自启动")
        info2 = cl.other_seting_unautoloin ()
        assert info2 is None
        logging.info ("----------------------------------利旧客户端A1.18用例结束执行------------------------------")



if __name__ == "__main__":
    t = time.strftime("%Y-%m-%d %H%M")
    pytest.main(["-m", "client1"])