#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll / zhouxihong / houjinqi
@contact: chengll@ruijie.com / zhouxihong@ruijie.com.cn
@software: PyCharm
@time: 2018/12/xx xx:xx / 2018/12/03 14:09
"""
import pytest
from WebPages.LoginPage import Login
from WebPages.AuthenmanagePage import AuthenManage
from Common.serverconn import *
from TestData.Logindata import *


class Test_AD:
    """
        web已连接上AD域
        AD域中需要运行ad_domain_action.exe。
        AD域中需要1000users，1users，hjq组织。
        其中hjq组织中需要h1，time_limit，expire_user用户。
        time_limit用户有登录时间限制，expire_user用户设置为过期的用户
    """

    # @pytest.mark.webadm
    # def test_ad_domain_before_test(self, com_fixture):
    #     logging.info("-----------------------------------认证管理HJQ前制条件开始执行-------------------------------")
    #     p = AuthenManage(com_fixture)
    #     p.goto_adm()
    #     p.input_all_info()
    #     p.choose_ou('hjq')
    #     p.choose_ou('AD域认证测试')

    @pytest.mark.webadm
    def test_ad_enable(self, login_fixture):
        logging.info("----------------------------------认证管理A1.1测试用例开始执行---------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_enable()
        logging.info("校验不填任何项保存")
        assert flag_list[0] == 1
        logging.info("校验不填满带*号的项后点击保存")
        assert flag_list[1] == 1
        logging.info("校验服务器断网后的情况点击保存")
        assert flag_list[2] == 1
        logging.info("校验填入非法IP情况点击保存")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_enable_success(self, login_fixture):
        logging.info("----------------------------------认证管理A1.2测试用例开始执行--------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_enable_success()
        logging.info("校验填写正确参数后点击连接")
        assert flag_list[0] == 1
        logging.info("校验填写正确参数后点击保存")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_domain_server_name_check(self, login_fixture):
        logging.info("----------------------------------认证管理A1.3测试用例开始执行--------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_domain_server_name_check()
        logging.info("校验能否正确连接成功")
        assert flag_list[0] == 1
        logging.info("校验填写正确参数后点击保存")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_domain_server_ip_check(self, login_fixture):
        logging.info("----------------------------------认证管理A1.4测试用例开始执行--------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_domain_server_ip_check()
        logging.info("校验输入合法可达的AD域服务器IP，点击“连接”并保存")
        assert flag_list[0] == 1
        logging.info("校验输入合法不可达的域名服务器IP，点击“连接”并保存")
        assert flag_list[1] == 1
        logging.info("校验输入非法的AD域名服务器IP，点击“连接”并保存")
        assert flag_list[2] == 1
        logging.info("校验输入空的服务器IP地址，点击“连接”并保存")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_domain_server_port_check(self, login_fixture):
        logging.info("----------------------------------认证管理A1.5测试用例开始执行--------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_domain_server_port_check()
        logging.info("校验输入合法的服务器端口（1-65535）后，点击”连接“并保存")
        assert flag_list[0] == 1
        logging.info("校验输入已被占用的服务器端口后，点击”连接“并保存")
        assert flag_list[1] == 1
        logging.info("校验输入不合法的端口（中文），点击”连接“并保存")
        assert flag_list[2] == 1
        logging.info("校验输入不合法的端口（字母），点击”连接“并保存")
        assert flag_list[3] == 1
        logging.info("校验输入不合法的端口（数字），点击”连接“并保存")
        assert flag_list[4] == 1
        logging.info("校验输入不合法的端口（字符），点击”连接“并保存")
        assert flag_list[5] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_auto_join_ad_check_1(self, login_fixture):
        logging.info("----------------------------------认证管理A1.17测试用例开始执行--------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).auto_join_ad_check_1()
        logging.info("校验AD域服务器连接失败时,勾选自动加入AD域,点击'连接'按钮")
        assert flag_list[0] == 1
        logging.info("校验AD域服务器连接失败时,勾选自动加入AD域,点击'保存'按钮")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_mapping_config_add_1(self, login_fixture):
        logging.info("----------------------------------认证管理A1.25测试用例开始执行--------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).mapping_config_add_1()
        logging.info("校验配置正确的情况下,未配置映射关系，勾选'保存'进行同步账号")
        assert flag_list[0] == 1
        logging.info("校验配置正确的情况下,未配置映射关系，点击'同步账号'按钮同步账号")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_case_sensitive_check(self, login_fixture):
        logging.info("----------------------------------认证管理A1.92测试用例开始执行--------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).case_sensitive_check()
        logging.info("校验连接AD域服务器时使用小写字母,能否连接成功")
        assert flag_list[0] == 1
        logging.info("校验连接AD域服务器时使用大写字母,能否连接成功")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.webadm
    # def test_normal_account_login_check(self, login_fixture):
    #     logging.info("----------------------------------认证管理A1.93测试用例开始执行--------------------------------")
    #     tt = Login(login_fixture)
    #     tt.login(login_user_succ["name"], login_user_succ["passwd"])
    #     flag_list = AuthenManage(login_fixture).normal_account_login_check()
    #     logging.info("校验使用普通管理员账号（非Admin账号）登录Web查看认证管理界面")
    #     assert flag_list[0] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.webadm
    # def test_sync_account_double_check(self, login_fixture):
    #     logging.info("----------------------------------认证管理A1.10测试用例开始执行--------------------------------")
    #     tt = Login(login_fixture)
    #     tt.login(login_user_succ["name"], login_user_succ["passwd"])
    #     flag_list = AuthenManage(login_fixture).sync_account_double_check()
    #     logging.info("校验连续同步账号时是否有冲突提示")
    #     assert flag_list[0] == 1
    #     logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webadm
    def test_ad_domain_close_check_1(self, login_fixture):
        logging.info("----------------------------------认证管理A1.14测试用例开始执行--------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_domain_close_check_1()
        logging.info("校验同步账号时关闭AD域是否有冲突提示")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束------------------------------------------")

    @pytest.mark.webadm1
    def test_ad_domain_close_check_2(self, login_fixture):
        logging.info("----------------------------------认证管理A1.15测试用例开始执行--------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_domain_close_check_2()
        logging.info("校验关闭AD域是否有二次确认提示及密码确认框")
        assert flag_list[0] == 1
        logging.info("校验关闭AD域后用户管理账号是否被禁用")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_mapping_config_add_2(self, login_fixture):
        logging.info("----------------------------------认证管理A1.26、27、28测试用例开始执行------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).mapping_config_add_2()
        logging.info("校验点击添加按钮，是否出现添加映射组弹窗")
        assert flag_list[0] == 1
        logging.info("校验不选中分组直接点击下一步，是否有'请选择组织机构'提示")
        assert flag_list[1] == 1
        logging.info("校验已映射的用户组是否无法选择")
        assert flag_list[2] == 1
        logging.info("校验未被选中的用户组是否可以直接勾选")
        assert flag_list[3] == 1
        logging.info("校验搜索时是否可搜索出内容")
        assert flag_list[4] == 1
        logging.info("校验不选中点击下一步是否提示请选择本地用户组")
        assert flag_list[5] == 1
        logging.info("校验能否返回上一步")
        assert flag_list[6] == 1
        logging.info("校验能否选中本地用户组")
        assert flag_list[7] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_mapping_config_modify_1(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.32、33测试用例开始执行----------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).mapping_config_modify_1()
        logging.info("校验点击编辑按钮，是否出现编辑映射组弹窗")
        assert flag_list[0] == 1
        logging.info("校验能否编辑弹出的映射组弹窗")
        assert flag_list[1] == 1
        logging.info("校验点击上一步后编辑配置是否保存")
        assert flag_list[2] == 1
        logging.info("校验能否成功保存")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_local_group_ad_domain_switch(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.45、46测试用例开始执行----------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).local_group_ad_domain_switch()
        logging.info("校验点击本地切换按钮，取消后是否保存")
        assert flag_list[0] == 1
        logging.info("校验点击本地切换按钮，确定后是否保存")
        assert flag_list[1] == 1
        logging.info("校验AD域切换按钮，取消后是否保存")
        assert flag_list[2] == 1
        logging.info("校验AD域切换按钮，确定后是否保存")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_mapping_config_modify_2(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.34测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).mapping_config_modify_2()
        logging.info("校验断网或服务器异常时，修改映射关系")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm1
    def test_local_group_portion_user_sync(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.35测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).local_group_portion_user_sync()
        logging.info("校验是否完成账号同步")
        assert flag_list[0] == 1
        logging.info("校验勾选的用户成功同步至组A下")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm1
    def test_mapping_config_delete_1(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.36测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).mapping_config_delete_1()
        logging.info("校验点击映射配置删除按钮")
        assert flag_list[0] == 1
        logging.info("校验修改完后点击保存")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.webadm
    # def test_mapping_config_delete_2(self, login_fixture):
    #     logging.info("-----------------------------------认证管理A1.37测试用例开始执行-------------------------------")
    #     tt = Login(login_fixture)
    #     tt.login(login_user_succ["name"], login_user_succ["passwd"])
    #     flag_list = AuthenManage(login_fixture).mapping_config_delete_2()
    #     logging.info("校验断网后点击删除映射关系")
    #     assert flag_list[0] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_local_user_group_delete_1(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.38测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).local_user_group_delete_1()
        logging.info("校验删除本地映射的用户组能否成功")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.webadm
    # def test_mapping_config_crud(self, login_fixture):
    #     logging.info("-----------------------------------认证管理A1.39测试用例开始执行-------------------------------")
    #     tt = Login(login_fixture)
    #     tt.login(login_user_succ["name"], login_user_succ["passwd"])
    #     flag_list = AuthenManage(login_fixture).mapping_config_crud()
    #     logging.info("校验在同步过程中点击删除映射关系能否成功")
    #     assert flag_list[0] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_mapping_config_add_3(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.29测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).mapping_config_add_3()
        logging.info("校验新增映射时，选中的本地组已在列表中存在，能否成功")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_mapping_config_add_4(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.30测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).mapping_config_add_4()
        logging.info("校验连不上域控服务器时，添加域控映射能否成功")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.webadm5
    # def test_mapping_config_add_5(self, login_fixture):
    #     logging.info("-----------------------------------认证管理A1.31测试用例开始执行-------------------------------")
    #     tt = Login(login_fixture)
    #     tt.login(login_user_succ["name"], login_user_succ["passwd"])
    #     flag_list = AuthenManage(login_fixture).mapping_config_add_5()
    #     logging.info("校验添加100个用户映射列表能否正常显示")
    #     assert flag_list[0] == 1
    #     # logging.info("校验添加5000个用户映射列表能否正常显示")
    #     # assert flag_list[1] == 1
    #     logging.info("校验页面能否正常和滚动映射关系")
    #     assert flag_list[2] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_arch_mode_mapping_edit_1(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.40测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_arch_mode_mapping_edit_1()
        logging.info("校验点击取消后映射是否生效")
        assert flag_list[0] == 1
        logging.info("校验多次点击编辑后，编辑是否保存")
        assert flag_list[1] == 1
        logging.info("校验搜索框输入字符后能否生效")
        assert flag_list[2] == 1
        logging.info("校验编辑后，右侧是否存在映射")
        assert flag_list[3] == 1
        logging.info("校验点击保存按钮后，映射是否保存")
        assert flag_list[4] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.webadm
    # def test_ad_arch_mode_mapping_edit_2(self, login_fixture):
    #     logging.info("-----------------------------------认证管理A1.41测试用例开始执行-------------------------------")
    #     tt = Login(login_fixture)
    #     tt.login(login_user_succ["name"], login_user_succ["passwd"])
    #     flag_list = AuthenManage(login_fixture).ad_arch_mode_mapping_edit_2()
    #     logging.info("校验账号同步过程中，点击“编辑”按钮")
    #     assert flag_list[0] == 1
    #     logging.info("校验断网、服务器异常时点击“编辑”按钮")
    #     assert flag_list[1] == 1
    #     #ad域恢复
    #     time.sleep(60)
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_arch_mode_data_sync(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.42测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_arch_mode_data_sync()
        logging.info("校验同步是否成功")
        assert flag_list[0] == 1
        logging.info("校验在用户管理里是否存在同步后的组")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_arch_mode_local_group_crud_1(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.43测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_arch_mode_local_group_crud_1()
        logging.info("校验在AD域本地组下新增用户组")
        assert flag_list[0] == 1
        logging.info("校验在AD域本地组下删除用户组")
        assert flag_list[1] == 1
        logging.info("校验在AD域本地组下修改用户组名称或上级组织")
        assert flag_list[2] == 1
        logging.info("校验在AD域本地组下修改用户组其他配置信息")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_arch_mode_local_group_crud_2(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.44测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_arch_mode_local_group_crud_2()
        logging.info("校验在AD域本地组下新增用户")
        assert flag_list[0] == 1
        logging.info("校验在AD域本地组下删除用户")
        assert flag_list[1] == 1
        logging.info("校验在AD域本地组下修改用户姓名、所属组")
        assert flag_list[2] == 1
        logging.info("校验在AD域本地组下修改用户其他配置信息")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_user_change_password(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.65测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).ad_user_change_password()
        logging.info("校验修改密码能否成功")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_save_config_info(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.47测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).save_config_info()
        logging.info("校验密码不对时保存是否有错误提示")
        assert flag_list[0] == 1
        logging.info("校验账号不对时保存是否有错误提示")
        assert flag_list[1] == 1
        logging.info("校验端口号不对时保存是否有错误提示")
        assert flag_list[2] == 1
        logging.info("校验保存时是否有二次密码确认")
        assert flag_list[3] == 1
        logging.info("校验保存后用户是否开始同步")
        assert flag_list[4] == 1
        logging.info("校验连续同步时是否有错误提示")
        assert flag_list[5] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_sync_log_search(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.86测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).sync_log_search()
        logging.info("校验是否有<同步日志>按钮")
        assert flag_list[0] == 1
        logging.info("校验能否点击时间选择")
        assert flag_list[1] == 1
        logging.info("校验同步后是否有日志")
        assert flag_list[2] == 1
        logging.info("校验同步后是否有同步结果")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_sync_log_views(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.87测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).sync_log_views()
        logging.info("校验<同步日志>是否支持分页查看")
        assert flag_list[0] == 1
        logging.info("校验<同步日志>是否支持失败原因查看")
        assert flag_list[1] == 1
        logging.info("校验<同步日志>是否支持同步方式查看")
        assert flag_list[2] == 1
        logging.info("校验<同步日志>是否支持同步日期查看")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.webadm
    # def test_user_account_retain_item(self, login_fixture):
    #     logging.info("-----------------------------------认证管理A1.95测试用例开始执行-------------------------------")
    #     tt = Login(login_fixture)
    #     tt.login(login_user_succ["name"], login_user_succ["passwd"])
    #     flag_list = AuthenManage(login_fixture).user_account_retain_item()
    #     logging.info("校验同步后是否有日志")
    #     assert flag_list[0] == 1
    #     logging.info("校验同步后失败原因能否是保留字段")
    #     assert flag_list[1] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_user_account_delete(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.53测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).user_account_delete()
        logging.info("校验在AD域本地组下新增用户组")
        assert flag_list[0] == 1
        logging.info("校验在AD域本地组下删除用户组")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.webadm
    # def test_sync_ad_ten_group(self, login_fixture):
    #     logging.info("-----------------------------------认证管理A1.94测试用例开始执行-------------------------------")
    #     tt = Login(login_fixture)
    #     tt.login(login_user_succ["name"], login_user_succ["passwd"])
    #     flag_list = AuthenManage(login_fixture).sync_ad_ten_group()
    #     logging.info("校验同步是否成功")
    #     assert flag_list[0] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_sync_ad_warnning(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.96测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).sync_ad_warnning()
        logging.info("校验是否出现告警")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_sync_ad_warnning_recovery(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.97测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).sync_ad_warnning_recovery()
        logging.info("校验是否恢复告警")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_create_ad_user_ad(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.48测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).create_ad_user_ad()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验能否找到同步后的用户")
        assert flag_list[1] == 1
        logging.info("校验数据库密码是否有加密过")
        assert flag_list[2] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_create_ad_user_local(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.49测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).create_ad_user_local()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验能否找到同步后的用户")
        assert flag_list[1] == 1
        logging.info("校验数据库密码是否有加密过")
        assert flag_list[2] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_create_user_exist_ad_mode(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.50测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).create_user_exist_ad_mode()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验能否找到同步后的用户")
        assert flag_list[1] == 1
        logging.info("校验数据库密码是否有加密过")
        assert flag_list[2] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_create_user_exist_local_mode(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.51测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).create_user_exist_local_mode()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验能否找到同步后的用户")
        assert flag_list[1] == 1
        logging.info("校验数据库密码是否有加密过")
        assert flag_list[2] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_create_same_user_name(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.52测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).create_same_user_name()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验是否存在同名用户提示")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_user_delete_1(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.54测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).user_delete_1()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验数据库，用户是否已禁用")
        assert flag_list[1] == 1
        AuthenManage(login_fixture).connect_ad_domain_1()
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm1
    def test_user_delete_2(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.55测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).user_delete_2()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验数据库，用户是否已被删除")
        assert flag_list[1] == 1
        AuthenManage(login_fixture).connect_ad_domain_1()
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm1
    def test_new_ad_domain_user_1(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.81测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).new_ad_domain_user_1()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验以WindowsAD域为准，WEB新建该架构未同步的用户情况")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_new_ad_domain_user_2(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.82测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).new_ad_domain_user_2()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验以本地信息为准，WEB新建该架构未同步的用户情况")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_new_ad_domain_user_3(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.83测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).new_ad_domain_user_3()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验以WindowsAD域为准，导入该架构未同步的用户情况")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm1
    def test_new_ad_domain_user_4(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.84测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).new_ad_domain_user_4()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验以本地信息为准，导入该架构未同步的用户情况")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_new_ad_domain_user_5(self, login_fixture):
        logging.info("-----------------------------------认证管理A1.85测试用例开始执行-------------------------------")
        tt = Login(login_fixture)
        tt.login(login_user_succ["name"], login_user_succ["passwd"])
        flag_list = AuthenManage(login_fixture).new_ad_domain_user_5()
        logging.info("校验是否同步成功")
        assert flag_list[0] == 1
        logging.info("校验导入不存在映射关系的架构，未同步的用户情况")
        assert flag_list[1] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    ############################################

    @pytest.mark.webadm1
    def test_ad_domain_manager_name(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.6测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.ad_domain_manager_name_check()
        logging.info("AD域管理员账号修改位3位字符后，校验输入3位字符管理员账号，正常连接")
        assert flag_list[0] == 1
        # logging.info("AD域管理员账号修改位100位字符后，校验输入100位管理员账号，正常连接") # AD域用户名无法修改为100位
        # assert flag_list[1] == 1
        logging.info("校验输入错误的管理员账号，提示错误")
        assert flag_list[2] == 1
        logging.info("校验输入空的管理员账号，提示错误")
        assert flag_list[3] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_domain_manager_pwd(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.7测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.ad_domain_manager_passwd_check()
        logging.info("校验输入错误的管理员密码，提示错误")
        assert flag_list[0] == 1
        logging.info("校验输入空的管理员密码，提示错误")
        assert flag_list[1] == 1
        logging.info("AD域管理员密码修改为32位后，校验输入32位的管理员密码，提示错误")
        assert flag_list[2] == 1
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    # @pytest.mark.webadm
    # def test_ad_domain_network_off(self, com_fixture):
    #     logging.info("----------------------------认证管理A1.8 A1.16测试用例开始执行-------------------------------")
    #     p = AuthenManage(com_fixture)
    #     flag_list = p.ad_domain_network_off_sync_account()
    #     logging.info("A1.8 校验同步账号时，域控断网会提示错误")
    #     assert flag_list[0] == 1
    #     logging.info("A1.8 校验域控断网情况下，同步账号会提示错误")
    #     assert flag_list[1] == 1
    #     logging.info("A1.16 校验域控断网情况下，AD域认证能正常关闭")
    #     assert flag_list[2] == 1
    #     logging.info("--------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webadm
    def test_close_auto_user_join_ad(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.19测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.close_auto_user_join_ad_check()
        logging.info("校验关闭自动加入AD域时，新建域用户不会进行加域")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webadm
    def test_error_dns_auto_join_ad(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.20测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.error_dns_auto_join_ad_check()
        logging.info("校验开启自动加入AD域时，未配置用户的DNS为域控时不能加域")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webadm1
    def test_ad_domain_android_vdi(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.18 A1.11测试用例开始执行-------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.auto_join_ad_check_2()
        logging.info("校验自动加入AD域时，已配置用户的DNS为域控，用户登录能加域")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webadm
    def test_restore_user_join_ad_domain(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.21测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.restore_user_join_ad_domain()
        logging.info("校验AD域用户设置为还原桌面类型时，不会进行加域")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    @pytest.mark.webadm
    def test_ad_domain_desktop_check(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.23测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.ad_domain_desktop_check()
        logging.info("#校验用户加域后D盘桌面数据不会丢失")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    @pytest.mark.webadm1
    def test_ad_user_login_method(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.67测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.ad_user_login_method()
        logging.info("校验使用三种登录方式，用户均能登录")
        assert flag_list[0] == 1
        assert flag_list[1] == 1
        # assert flag_list[2] == 1  #虚机登录用户名有限制
        logging.info("----------------------------------------测试用例结束-------------------------------------------")

    # @pytest.mark.webadm
    # def test_ad_user_login_wrong_method(self, com_fixture):
    #     logging.info("-----------------------------------认证管理A1.69测试用例开始执行-------------------------------")
    #     p = AuthenManage(com_fixture)
    #     flag_list = p.ad_user_login_wrong_method()
    #     logging.info("校验使用三种异常登录方式，用户登录失败")
    #     assert flag_list[0] == 1
    #     assert flag_list[1] == 1
    #     assert flag_list[2] == 1
    #     logging.info(
    #         "----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_user_disable_check1(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.71测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.ad_user_disable_check1()
        logging.info("校验在AD域服务器上禁用已加域用户后，用户再次登录提示'您的账号已被停用'")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束--------------------------------------------")

    # @pytest.mark.webadm
    # # 用例错误，可以正常登录，虚机无法联网
    # def ad_net_off_user_login(self, login_fixture):
    #     logging.info("-----------------------------------认证管理A1.72测试用例开始执行-------------------------------")
    #     p = AuthenManage(login_fixture)
    #     flag_list = p.ad_user_disable_check1()
    #     logging.info("校验域服务器断网或异常时，使用已加域用户登录终端，提示您的账号已被停用")
    #     assert flag_list[0] == 1
    #     logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_net_off_user_first_login(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.88测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.ad_net_off_user_first_login()
        logging.info("校验创建用户后，首次登录时AD域断网，登录提示指定的域不存在，或无法联系")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_ad_user_disable_check2(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.89测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.ad_user_disable_check2()
        logging.info("校验在AD域服务器上禁用用户后，该用户首次登录失败")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_expire_user_login(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.90测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.expire_user_login()
        logging.info("校验一个已过期的账户登陆，终端提示：用户账户已过期")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    @pytest.mark.webadm
    def test_time_limit_user_login(self, com_fixture):
        logging.info("-----------------------------------认证管理A1.91测试用例开始执行-------------------------------")
        p = AuthenManage(com_fixture)
        flag_list = p.time_limit_user_login()
        logging.info("校验在可登陆时间外的时间登陆用户，提示：您的账户有时间限制，您当前无法登录。请稍后再试")
        assert flag_list[0] == 1
        logging.info("----------------------------------------测试用例结束---------------------------------------------")

    # @pytest.mark.webadm
    # # 时间较久，先不执行
    # def test_add_thousand_users(self, com_fixture):
    #     logging.info("--------------------------------认证管理A1.9 A1.13测试用例开始执行----------------------------")
    #     p = AuthenManage(com_fixture)
    #     flag_list = p.add_thousand_users()
    #     logging.info("校验在AD域控中添加1000个用户，重启tomcat能自动同步，且用户登录能自动加域")
    #     assert flag_list[0] == 1
    #     logging.info("---------------------------------------测试用例结束-------------------------------------------")

if __name__ == "__main__":
    t = time.strftime("%Y-%m-%d %H%M")
    # pytest.main(['-vv',"-m", "webadm", "--html", report_dir + "//{0}_testwebAD_htmlreport.html".format(t)])
    pytest.main(['-v',"-m", "webadm1","--html", report_dir + "//{0}_testwebADerror_htmlreport.html".format(t)])
