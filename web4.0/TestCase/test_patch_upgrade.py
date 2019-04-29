#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@software: PyCharm
@time: 2019/03/07 14:24
"""

import pytest
from TestData.patchUpgradedata import *
from TestData.Logindata import *

from WebPages.LoginPage import Login
from WebPages.patchUpgradePage import *

# url列表
master_url = patch_upgradePage.get_master_url()
reserve_url = patch_upgradePage.get_reserve_url()
url_list = ["".join(master_url), "".join(reserve_url)]


class Test_PatchUpgrade:

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('url', master_url)
    def test_colony_master_patchUpgrade_btn_isExist(self, url_fixture, url):
        """
        测试点：集群主控补丁升级按钮呈现
        步骤：1、使用管理员帐户登录RCD集群主控HA或物理地址，进入高级配置->云主机升级界面；
             2、使用管理员帐户登录RCM集群主控HA或物理地址，进入高级配置->云主机升级界面;
        校验点：存在补丁包升级按钮
        """
        logging.info("-----------------------------补丁包升级A1.1用例开始-----------------------------")
        patch = patch_upgradePage(url_fixture)
        patch.goto_cloud_host_upgrade()
        time.sleep(com_slp)
        assert patch.is_exist_patch_upgrade_btn() == 0
        logging.info("-----------------------------补丁包升级A1.1用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('url', reserve_url)
    def test_colony_reserve_patchUpgrade_btn_isExist(self, url_fixture, url):
        """
        测试点：集群非主控补丁升级按钮不呈现
        步骤：使用管理员帐户登录RCD/RCM集群备控、拓展主存、拓展备存、计算节点物理地址，进入高级配置->云主机升级界面；
        校验点：无补丁包升级按钮
        """
        logging.info("-----------------------------补丁包升级A1.2用例开始-----------------------------")
        patch = patch_upgradePage(url_fixture)
        patch.goto_cloud_host_upgrade()
        time.sleep(com_slp)
        assert patch.is_exist_patch_upgrade_btn() == 1
        logging.info("-----------------------------补丁包升级A1.2用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_patchUpgrade_btn_isExist(self, com_fixture):
        """
        测试点：单机RCM/RCD环境补丁升级按钮呈现
        步骤：1、RCD/RCM单机环境
             2、上传成功可用升级补丁包PT目录）
        校验点：1、单机RCM/RCD环境所有类型云主机均呈现补丁包升级按钮
        """
        logging.info("-----------------------------补丁包升级A1.3  1.4用例开始-----------------------------")
        patch = patch_upgradePage(com_fixture)
        patch.goto_cloud_host_upgrade()
        time.sleep(com_slp)
        assert patch.is_exist_patch_upgrade_btn() == 0
        logging.info("-----------------------------补丁包升级A1.3 1.4用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_ordinary_admin_login(self, login_fixture):
        """
        测试点：普通管理员登录无补丁升级按钮呈现
        步骤：1、创建或导入的普通管理员帐户登录RCD/RCM集群HA地址，进入高级配置->云主机升级界面；
        校验点：1、无补丁包升级按钮
        """
        logging.info("-----------------------------补丁包升级A1.5用例开始-----------------------------")
        t = Login(login_fixture)
        patch = patch_upgradePage(login_fixture)
        t.login(Commanage,Commanage_pwd)
        assert patch.is_exist_deployment_and_upgrade_btn() == 1
        logging.info("-----------------------------补丁包升级A1.5用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_not_enough_memory(self,com_fixture):
        """
        测试点：单机环境下，补丁包升级所需目录空间不足
        步骤：1、RCD/RCM环境出现云主机（任意角色主控/备控/存储节点/计算节点）/OPT目录容量不足4.5G（可以使用fallocate命令占用/OPT目录）
        校验点：1、告警管理中提示告警，并提示用户删除共享目录或补丁包释放空间，否则影响补丁包升级；
               2、点击补丁包升级时，同样给出告警提示，不允许升级；
        """
        logging.info("-----------------------------补丁包升级A1.33用例开始-----------------------------")
        patch = patch_upgradePage(com_fixture)
        patch.goto_cloud_host_upgrade()
        patch.goto_upload_patch_page()
        patch.upload_patch(patch_path, upgrade_patch_name)
        time.sleep(60)
        file = server_conn(host_ip,'df -h /opt')
        list = file.split()
        optsize = patch.translate_size(list[10])
        size = str(int(optsize - 1))+'G'
        server_conn(host_ip, 'fallocate -l %s /opt/bigfile ' % size)
        time.sleep(120)
        patch.click_warning_btn()
        time.sleep(2)
        '''升级时内存空间不足信息提示'''
        assert patch.get_all_warning_info().find(not_enough_memory) >= 0
        patch.back_current_page()
        patch.click_cloud_host_upgrade_btn()
        patch.click_patch_upgrade_btn()
        patch.click_next()
        patch.start_update()
        patch.send_passwd_confirm()
        assert patch.isExist_tip(not_enough_upgrade_tip) == 0
        """升级失败，还原环境  删除大文件和升级包"""
        server_conn(host_ip, 'rm -rf /opt/bigfile')
        patch.click_pre()
        patch.patch_deleted(upgrade_patch_name)
        time.sleep(3)
        logging.info("-----------------------------补丁包升级A1.33用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_delete_patch(self, com_fixture):
        """
        19
        测试点：RCM单机环境补丁包删除
        步骤：1、RCM单机环境
             2、存在多个补丁包
        校验点：1、可删除成功
        14
        测试点：补丁包上传完成后手动刷新显示
        步骤：1、使用管理员帐户登录RCD/RCM主控的HA或物理地址，进入高级配置->云主机升级界面；
             2、点击上传->WEB补丁包
             3、完成后快速手动点击刷新按钮
        校验点：补丁包上传完成后手动刷新显示正常
        """
        logging.info("----------------------------------补丁包升级A1.14用例开始------------------------------")
        p = patch_upgradePage(com_fixture)
        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.goto_upload_patch_page()
        p.upload_patch(upload_patch_path, upload_patch_name_list[0])
        p.upload_patch(upload_patch_path, upload_patch_name)
        time.sleep(2)
        p.refresh_patch()
        text = p.get_all_patch_info()
        logging.info('上传补丁包成功')
        assert text.__contains__(upload_patch_name)
        logging.info("----------------------------------补丁包升级A1.14用例结束------------------------------")

        logging.info('还原环境，删除补丁包')
        logging.info("----------------------------------补丁包升级A1.18.19用例开始------------------------------")
        logging.info('删除补丁包成功')
        assert p.patch_deleted(upload_patch_name) == 0
        time.sleep(3)
        p.patch_deleted(upload_patch_name_list[0])
        logging.info("----------------------------------补丁包升级A1.18.19用例结束------------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_upload_patch(self, com_fixture):
        """
        测试点：可上传补丁包
        步骤：1、使用管理员帐户登录云主机的物理地址，进入高级配置->云主机升级界面；
             2、点击上传->WEB补丁包
        校验点：1、补丁包上传成功且五秒后自动刷新
        """
        logging.info("----------------------------------补丁包升级A1.9.11.12用例开始------------------------------")
        p = patch_upgradePage(com_fixture)
        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.goto_upload_patch_page()
        p.upload_patch(upload_patch_path, upload_patch_name)
        time.sleep(6)

        text = p.get_all_patch_info()
        logging.info('上传补丁包成功且五秒后自动刷新')
        assert text.__contains__(upload_patch_name)
        logging.info('还原环境，删除补丁包')
        time.sleep(60)
        p.patch_deleted(upload_patch_name)
        time.sleep(3)
        logging.info("----------------------------------补丁包升级A1.9.11.12用例结束------------------------------")

    @pytest.mark.patch_upgrade1
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_firefox_upload_patch(self, firefox_login_fixture):
        """
        测试点：补丁包上传完成后5秒内自动刷新显示
        步骤：1、使用谷歌浏览器，点击补丁包上传
             2、使用火狐浏览器，点击补丁包上传
        校验点：1、补丁包上传完成后5秒内自动刷新显示
        """
        logging.info("----------------------------------补丁包升级A1.13用例开始------------------------------")
        p = patch_upgradePage(firefox_login_fixture)
        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.goto_upload_patch_page()
        p.upload_patch_firefox(upload_patch_path, upload_patch_name)
        time.sleep(6)

        text = p.get_all_patch_info()
        logging.info('上传补丁包成功且五秒后自动刷新')
        assert text.__contains__(upload_patch_name)
        logging.info('还原环境，删除补丁包')
        time.sleep(60)
        p.patch_deleted(upload_patch_name)
        time.sleep(3)
        logging.info("----------------------------------补丁包升级A1.13用例结束------------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_ftp_upload_file_format(self, com_fixture):
        """
        测试点：FTP工具补丁包上传格式校验
        步骤：1、点击上传->WEB补丁包
             2、弹出FTP工具后，将合法的ZIP补丁包进行上传
             3、将非ZIP格式的文件上传
        校验点：1、ZIP后缀的合法补丁包上传成功
               2、非ZIP格式的文件上传失败，并给出错误提示：“上传的补丁包不合法，只允许上传格式为.zip的补丁包”
        """
        logging.info("-----------------------------补丁包升级A1.15用例开始-----------------------------")
        patch = patch_upgradePage(com_fixture)
        patch.goto_cloud_host_upgrade()
        patch.goto_upload_patch_page()
        patch.upload_patch(patch_path, zip_patch)
        logging.info("等待校验结束")
        time.sleep(50)
        assert patch.get_all_patch_info().__contains__(zip_patch)
        time.sleep(5)
        logging.info("还原环境，删除上传的包")
        assert patch.patch_deleted(zip_patch) == 0
        time.sleep(3)
        text = patch.get_warning_info(patch_path, iso_patch, upload_patch_format_error_info)
        assert text.find(upload_patch_format_error_info) >= 0
        logging.info("-----------------------------补丁包升级A1.15用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_0
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_colony_patch_list_isExist(self,com_fixture):
        """
        测试点：RCD/RCM集群环境主控均展现补丁包列表
        步骤：使用管理员帐户登录RCD/RCM集群主控HA或物理地址，进入高级配置->云主机升级界面；
        校验点：呈现补丁包列表，并且未升级的补丁包均呈现升级按钮
        """
        logging.info("-----------------------------补丁包升级A1.6,A1.8用例开始-----------------------------")
        patch = patch_upgradePage(com_fixture)
        patch.goto_cloud_host_upgrade()
        patch.click_patch_upgrade_btn()
        patch.upload_patch(patch_path,upgrade_patch_name)
        assert patch.is_exist_check_patch() == 0
        logging.info("验证未升级补丁包呈现升级按钮")
        time.sleep(com_slp)
        patch.click_next()
        time.sleep(3)
        assert patch.not_Upgrade() == 0
        assert patch.isExist_begin_upgrade_btn() == 0
        patch.click_begin_upgrade()
        assert patch.isExist_tip(tip_info) == 0
        logging.info("-----------------------------补丁包升级A1.6,A1.8用例结束-----------------------------")
        logging.info('还原环境，删除补丁包')
        time.sleep(30)
        patch.click_pre()
        time.sleep(3)
        patch.patch_deleted(upgrade_patch_name)
        time.sleep(3)

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_error_admin_pwd(self,com_fixture):
        """
        测试点：输入错误的二次密码 升级失败
        步骤：1、RCM集群环境选择补丁包并确认云主机后点击升级
             2、输入错误超级管理员密码
        校验点：不进入升级流程
        """
        logging.info("-----------------------------补丁包升级A1.27用例开始-----------------------------")
        patch = patch_upgradePage(com_fixture)
        patch.goto_cloud_host_upgrade()
        patch.goto_upload_patch_page()
        patch.upload_patch(patch_path, upgrade_patch_name)
        time.sleep(60)
        patch.select_patch(upgrade_patch_name)
        patch.click_next()
        patch.click_begin_upgrade()
        logging.info("二次密码输入框")
        patch.click_confire()
        patch.send_pwd(error_passwd)
        patch.close_confirm_pwd()
        assert patch.isExist_tip(tip_pwd_error_info) == 0
        logging.info("-----------------------------补丁包升级A1.27用例结束-----------------------------")
        logging.info('还原环境，删除补丁包')
        time.sleep(30)
        patch.click_pre()
        time.sleep(3)
        patch.patch_deleted(upgrade_patch_name)
        time.sleep(3)

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_zip_bigger_than_3_5G(self,com_fixture):
        """
        步骤：1、将大文件拖拽到补丁包ZIP中，使补丁包大于3.5G
             2、上传第一步生成ZIP的补丁包
        校验点：1、可拖拽大文件到ZIP包成功
               2、FTP工具判断大于3.5G，不允许上传
        """
        logging.info("-----------------------------补丁包升级A1.34用例开始-----------------------------")
        patch = patch_upgradePage(com_fixture)
        patch.goto_cloud_host_upgrade()
        patch.click_patch_upgrade_btn()
        text = patch.get_warning_info(patch_path,bigger_than_3_5_zip,bigger_35_info)
        assert text.find(bigger_35_info)>=0
        logging.info("-----------------------------补丁包升级A1.34用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_update_patch(self, com_fixture):
        """
        步骤：1、RCD集群环境选择补丁包并确认云主机后点击升级
        校验点：需二次密码确认，确认通过后弹出升级提示：云主机升级，将开启维护模式，关闭所有VDI云桌面！sunny服务将禁用！终端用户和普通管理员将禁止登录！
        """
        logging.info("-----------------------------补丁包升级A1.25/26用例开始-----------------------------")
        p = patch_upgradePage(com_fixture)
        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.goto_upload_patch_page()
        # p.delete_upload_patch()
        p.upload_patch(upload_patch_path, patch_name)
        p.click_next()
        p.start_update()
        try:
            p.send_passwd_confirm()
        except:
            assert '无二次密码确认'
        time.sleep(30)
        logging.info('弹出升级提示：云主机升级，将开启维护模式，关闭所有VDI云桌面！sunny服务将禁用！终端用户和普通管理员将禁止登录')
        assert p.get_upload_msg() != ''
        p.check_update_success(vm_ip)
        # 降版本
        # TODO:降版本
        logging.info("-----------------------------补丁包升级A1.25/26用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('special_patch_name', upload_patch_name_list)
    def test_patch_special_name(self, com_fixture,special_patch_name):
        """
        步骤：1、修改补丁包名中带中文后，通过FTP工具上传
             2、修改补丁包名中带特殊字符后，通过FTP工具上传
        校验点：可上传成功，并且可正常升级
        """
        logging.info("-----------------------------补丁包升级A1.89用例开始-----------------------------")
        p = patch_upgradePage(com_fixture)
        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.goto_upload_patch_page()
        #上传补丁包
        p.upload_patch(upload_patch_path, special_patch_name)
        time.sleep(2)

        text = p.get_all_info_patch()
        logging.info('补丁包名中带中文或特殊字符可上传成功')
        assert text.__contains__(special_patch_name)
        time.sleep(40)
        p.click_next()
        p.start_update()
        p.send_passwd_confirm()
        succ = p.check_update_success(vm_ip)
        logging.info('升级完成')
        assert succ == 1
        flag = p.login_Reserve_control(vm_ip)
        logging.info('升级成功，可正常登录')
        assert flag == 1
        # 降版本
        # TODO:降版本
        logging.info("-----------------------------补丁包升级A1.89用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_patch_update_time(self, com_fixture):
        """
        步骤：1、单机情况下RCD/RCM进行补丁包升级
        校验点：升级成功不超过20分钟
        """
        logging.info("-----------------------------补丁包升级A1.113用例开始-----------------------------")
        p = patch_upgradePage(com_fixture)
        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.goto_upload_patch_page()
        # 删除之前上传过的包
        # p.delete_upload_patch()
        # 上传补丁包
        p.upload_patch(upload_patch_path, patch_name)
        time.sleep(2)
        text = p.get_all_info_patch()
        assert text.__contains__(patch_name)
        time.sleep(40)
        p.click_next()
        p.start_update()
        p.send_passwd_confirm()
        time_start = time.time()
        succ = p.check_update_success(vm_ip)
        assert succ == 1
        # 间隔秒数
        time_end = time.time() - time_start
        # 间隔分钟数
        assert time_end < 1200
        # 降版本
        # TODO:降版本

    @pytest.mark.patch_upgrade1
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_group_patch_update_time(self, com_fixture):
        """
        前置步骤:1、RCD/RCM集群环境
        步骤：主备计算情况下RCD/RCM进行补丁包升级
        校验点：升级成功不超过40分钟
        """
        logging.info("-----------------------------补丁包升级A1.115用例开始-----------------------------")
        p = patch_upgradePage(com_fixture)
        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.goto_upload_patch_page()
        # 删除之前上传过的包
        p.delete_upload_patch()
        # 上传补丁包
        p.upload_patch(upload_patch_path, patch_name)
        time.sleep(2)
        text = p.get_all_info_patch()
        assert text.__contains__(patch_name)
        time.sleep(40)
        p.click_next()
        p.start_update()
        p.send_passwd_confirm()
        time_start = time.time()
        succ = p.check_update_success(vm_ip)
        assert succ == 1
        # 间隔秒数
        time_end = time.time() - time_start
        # 间隔分钟数
        assert time_end < 2400
        # 降版本
        # TODO:降版本


    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_upgrade_refresh(self, com_fixture):
        """
        步骤：1、补丁包升级过程，刷新浏览器
        校验点：仍显示升级进展界面
        """
        logging.info("-----------------------------补丁包升级A1.52用例开始-----------------------------")
        patch = patch_upgradePage(com_fixture)
        patch.goto_cloud_host_upgrade()
        patch.goto_upload_patch_page()
        patch.upload_patch(patch_path, upgrade_patch_name)
        time.sleep(60)
        patch.select_patch(upgrade_patch_name)
        patch.click_next()
        patch.click_begin_upgrade()
        patch.click_confire()
        patch.send_passwd_confirm(passwd)
        logging.info("开始升级")
        time.sleep(120)
        text = patch.get_upload_msg()
        patch.refresh_webdriver()
        time.sleep(5)
        assert patch.get_upload_msg() == text
        time.sleep(120)
        time_start = time.time()
        succ = patch.check_update_success(vm_ip)
        assert succ == 1
        # 间隔秒数
        time_end = time.time() - time_start
        # 间隔分钟数
        assert time_end < 2400
        # 降版本
        # TODO:降版本
        logging.info("-----------------------------补丁包升级A1.52用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_default_all_host(self, com_fixture):
        """
        前置步骤：
                1、RCD/RCM集群环境（主控/备控/拓展主存/拓展备存/计算节点版本一致）
                2、主控上传补丁包a成功
        执行步骤：1、主控上选择补丁包a，进行升级
        校验点：1、确认需要补丁包升级的云主机时默认勾选全部云主机

        """
        logging.info("----------------------------------补丁包升级A1.23用例开始------------------------------")
        p = patch_upgradePage(com_fixture)

        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.goto_upload_patch_page()
        p.upload_patch(upload_patch_path, upload_patch_name)
        time.sleep(2)
        p.goto_cloud_desk()
        ip_num = p.get_ip_num()
        p.click_cloud_desk_update()
        time.sleep(35)
        p.click_next()
        host_num = p.get_Cloud_Hosting()
        time.sleep(5)
        logging.info('要升级的云主机默认勾选全部云主机')
        assert ip_num == host_num
        p.click_pre()
        logging.info('还原环境，删除补丁包')
        assert p.patch_deleted(upload_patch_name)
        logging.info("----------------------------------补丁包升级A1.23用例结束------------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_patch_update_time(self, com_fixture):
        """
        步骤：1、单机情况下RCD/RCM进行补丁包升级
        校验点：升级成功不超过20分钟
        """
        logging.info("-----------------------------补丁包升级A1.113用例开始-----------------------------")
        p = patch_upgradePage(com_fixture)
        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.goto_upload_patch_page()
        # 删除之前上传过的包
        p.delete_upload_patch()
        # 上传补丁包
        p.upload_patch(upload_patch_path, patch_name)
        time.sleep(2)
        text = p.get_all_info_patch()
        assert text.__contains__(patch_name)
        time.sleep(40)
        p.click_next()
        p.start_update()
        p.send_passwd_confirm()
        time_start = time.time()
        succ = p.check_update_success(vm_ip)
        # 间隔秒数
        time_end = time.time() - time_start
        # 间隔分钟数
        assert time_end < 1200
        # 降版本
        # TODO:降版本
        logging.info("-----------------------------补丁包升级A1.113用例结束-----------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    @pytest.mark.parametrize('url', url_list)
    def test_master_del_patch(self, url_fixture, url):
        """
        执行步骤：1、使用管理员帐户登录RCD/RCM主控的HA或物理地址，进入高级配置->云主机升级界面；
                2、删除主控多余的补丁包
        预期结果：1、主控上补丁包删除成功
                2、非主控无补丁包删除入口
        """
        logging.info("----------------------------------补丁包升级A1.16用例开始------------------------------")
        patch = patch_upgradePage(url_fixture)
        patch.goto_cloud_host_upgrade()
        if url in reserve_url:
            assert patch.is_exist_patch_upgrade_btn() == 1
            return
        time.sleep(2)
        patch.click_patch_upgrade_btn()
        for patchName in patch_list:
            print patchName
            patch.upload_patch(patch_path, patchName)
            time.sleep(10)
        assert patch.is_exist_check_patch() == 0
        unselected_list = patch.get_unselected_patch_list()
        for patchName in unselected_list:
            patch.patch_deleted(patchName)
            time.sleep(10)
        logging.info('还原环境，删除补丁包')
        time.sleep(10)
        patch.patch_deleted(patch_list[-1])
        time.sleep(3)
        logging.info("----------------------------------补丁包升级A1.16用例结束------------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_ha_switch(self, com_fixture):
        """
        执行步骤：1、触发业务网HA切换后，云主机B成为当前主控
                2、点击补丁包升级
                3、在当前主控B重新上传补丁包a，上传成功后再点击补丁包升级
        预期结果：1、业务网HA切换后，重新上传相同补丁包可正常升级
        """
        logging.info("----------------------------------补丁包升级A1.39用例开始------------------------------")
        patch = patch_upgradePage(com_fixture)
        t = Login(com_fixture)
        patch.goto_cloud_host_upgrade()
        patch.click_patch_upgrade_btn()
        patch.upload_patch(patch_path, upgrade_patch_name)
        time.sleep(60)
        server_conn(vm_ip, "service rcd_ha restart")
        time.sleep(180)
        patch.refresh_webdriver()
        t.login(username, passwd)
        patch.goto_cloud_host_upgrade()
        patch.click_patch_upgrade_btn()
        patch.upload_patch(patch_path, upgrade_patch_name)
        patch.select_patch(upgrade_patch_name)
        patch.click_next()
        patch.click_begin_upgrade()
        patch.click_confire()
        patch.send_pwd(passwd)
        logging.info("开始升级")
        time.sleep(120)
        succ = patch.check_update_success(vm_ip)
        logging.info('升级完成')
        assert succ == 1
        # 降版本
        # TODO:降版本

        logging.info("----------------------------------补丁包升级A1.39用例结束------------------------------")

    @pytest.mark.patch_upgrade2
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_HA_exchange(self, com_fixture):
        """
        前置步骤：1、RCD/RCM集群
                2、云主机A（当前主控）上传补丁包a和b，云主机B（当前备控）
        执行步骤：1、触发存储网HA切换（拔插主控A的光纤线），云主机A仍为当前业务主控
        校验点：1、补丁包列表中依旧显示切换前的补丁包列表存在a和b补丁包（5433数据库未发生变化）

        """
        logging.info("----------------------------------补丁包升级A1.36用例开始------------------------------")
        p = patch_upgradePage(com_fixture)

        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.goto_upload_patch_page()
        p.upload_patch(upload_patch_path, upload_patch_name)
        p.upload_patch(upload_patch_path, upload_patch_name_list[0])
        time.sleep(100)
        text_old = p.get_all_patch_info()
        text_new = ''
        # 存储主备切换
        server_conn(vm_ip, "ifdown bond1 && sleep 60 && ifup bond1")
        time.sleep(100)
        try:
            text_new = p.get_all_patch_info()
        except:
            pass
        logging.info('触发HA切换后补丁包列表中依旧显示切换前的补丁包列表存在a和b补丁包')
        assert text_old == text_new

        hostip = server_conn(mainip, r"SELECT * FROM lb_server_host where is_master='Y'")
        backupip = server_conn(mainip, r"SELECT * FROM lb_server_host where is_master='N'")
        patch = server_conn(mainip, r"SELECT * FROM fusion_fix_pack_info where del_flag='N'")
        logging.info('数据库业务主备控未发生变化')
        assert hostip == mainip
        assert backupip == vm_ip
        logging.info('数据库补丁包依然存在')
        assert upload_patch_name in patch
        assert upload_patch_name_list[0] in patch
        logging.info('还原环境，删除补丁包')
        p.patch_deleted(upload_patch_name)
        p.patch_deleted(upload_patch_name_list[0])

        logging.info("----------------------------------补丁包升级A1.36用例结束------------------------------")

    @pytest.mark.patch_upgrade
    @pytest.mark.case_lever_2
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_clock_task(self, com_fixture):
        """
        前置步骤：RCD集群
        执行步骤：1、设置定时重启云主机任务
                2、设置定时关闭云主机任务
                3、在定时任务触发时间内，进行补丁包升级

        校验点：1、在补丁包升级过程中定时任务不触发启动，不生效

        """
        logging.info("----------------------------------补丁包升级A1.51用例开始------------------------------")
        p = patch_upgradePage(com_fixture)
        p.goto_cloud_host_upgrade()
        time.sleep(2)
        p.create_clock_task(u'关闭云主机', u'指定时间点任务', 4)
        p.click_cloud_desk_update()
        p.goto_upload_patch_page()
        p.upload_patch(upload_patch_path, patch_name)
        p.create_clock_task(u'重启云主机', u'指定时间点任务', 4)
        p.click_cloud_host_upgrade_btn()
        p.goto_upload_patch_page()

        p.click_next()
        p.start_update()
        time.sleep(2)
        try:
            p.send_passwd_confirm()
        except:
            assert '无二次密码确认'
        # 等待升级
        p.check_update_success(vm_ip)
        flag = p.login_Reserve_control(vm_ip)
        logging.info('升级成功，可正常登录')
        assert flag == 1
        # 降版本
        # TODO:降版本

        logging.info("----------------------------------补丁包升级A1.51用例结束------------------------------")

    if __name__ == "__main__":
        t = time.strftime("%Y-%m-%d")
        pytest.main(["-m", "patch_upgrade1","--html",report_dir + "//{0}_testweb4.0_htmlreport.html".format(t)])
