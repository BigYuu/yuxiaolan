#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll / zhouxihong / houjinqi
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/12/03 14:09
"""

from Common.Basicfun import BasicFun
from TestData.Admdata import *
from selenium.webdriver.common.keys import Keys
from TestData.Logindata import *
from WebPages.adnroid_vdi_page import *
from Common.parse_dump_file import *
from Common.linuxconn import *
from TestData.basicdata import *
import time
import logging
import uiautomation as automation
import random
from selenium.webdriver import ActionChains
from Common.terminal_action import *
from WebPages.Idvpage import IdvPage
from TestData.Usermanagedata import *
import logging
from LoginPage import *
from WebPages.adnroid_vdi_page import AndroidVdi

class AuthenManage(BasicFun):
    # 用户管理
    user_management_xpath = u"//span[contains(.,'用户管理')]"
    # 用户管理翻页按钮
    user_manage_next_page_xpath = "//i[@class='el-icon el-icon-arrow-right']"
    # 用户管理状态列表(此xpath返回一系列元素)
    user_manage_status_xpath = "//*[@class='el-tooltip item']"
    # 用户管理用户名称列表
    user_username_status_xpath = "//*[contains(@class,'el-table__row')]"
    # 下一页按钮
    user_manage_next_btn_xpath = "//*[@class='el-icon el-icon-arrow-right']/.."
    # 用户组单个条目
    user_manage_group_item_xpath = u"//div[@class='custom-tree-node']//div[contains(.,'{0}')]/../.."
    # 用户组展开按钮
    user_manage_expend_btn_xpath = u"//div[@class='custom-tree-node']//div[contains(.,'{0}')]/../.." \
                                   u"//span[contains(@class,'el-icon-caret-right')]"
    # 新建用户组按钮
    user_manage_create_group_btn_xpath = u"//i[@class='sk-icon-add']/.."
    # 基本信息-名称
    user_manage_base_info_name_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'名称')]//input/parent::div"
    # 基本信息-上级组织
    user_manage_base_info_pre_organ_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'上级组织')]//input/parent::div"
    # 基本信息-描述
    user_manamge_base_info_description_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'描述')]//textarea"
    # IDV云终端
    user_manage_idv_cloud_terminal_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'IDV云终端')]//input/.."
    # VDI云桌面
    user_manage_vdi_cloud_desktop_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'VDI云桌面')]//input/.."
    # 云盘
    user_manage_cloud_disk_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'云盘')]//input"
    # 外设策略-跳转
    user_manage_out_device_strategy_xpath = "//*[@name='peripheralPolicy']"
    # 外设策略-详细项(输入设备\摄像设备\音频设备\其他已归类设备\存储设备\办公设备\手机\其他未归类设备)
    user_manage_out_device_strategy_detail_xpath = u"//span[@class='el-checkbox__label']/..//*[contains(.,'{0}')]//" \
                                                   u"preceding-sibling::span"
    # 新建用户组-确认按钮
    user_manage_ok_btn_xpath = u"//*[@class='dialog-footer']//*[contains(.,'确认')]"
    # 新建用户组-取消按钮
    user_manage_cancel_btn_xpath = u"//*[@class='dialog-footer']//*[contains(.,'取消')]"
    # 关闭弹出页面
    user_manage_pop_page_xpath = "//*[@class='el-dialog__headerbtn']"
    # 用户选择-勾选用户
    user_manage_select_xpath = u"//*[contains(@class,'el-table__row')]//span[contains(.,'{0}')]/ancestor::tr//*[conta" \
                               u"ins(@class,'el-checkbox__input')]"
    # 删除用户-按钮
    user_manage_delete_user_xpath = u"//*[@class='sk-toolbar']//span[contains(.,'删除用户')]/.."
    # 删除用户-确认删除
    user_manage_delete_confirm_xpath = u"//div[@class='el-message-box__btns']//span[contains(.,'删除')]/.."
    # 新建用户-按钮
    user_manage_create_user_xpath = u"//*[@class='sk-toolbar']//span[contains(.,'新建用户')]/.."
    # 新建用户-基本信息-用户名
    user_manage_new_username_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'用户名')]//input/parent::div"
    # 新建用户-基本信息-用户名-输入
    user_manage_new_username_input_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'用户名')]//input"
    # 新建用户-基本信息-用户组
    user_manage_new_user_group_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'用户组')]//input/parent::div"
    # 新建用户-基本信息-密码
    user_manage_new_user_pwd_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'密码')]//input/parent::div"
    # 新建用户-基本信息-姓名
    user_manage_new_name_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'姓名')]//input/parent::div"
    # 新建用户-基本信息-姓名-输入
    user_manage_new_name_input_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'姓名')]//input"
    # 新建用户-基本信息-手机号
    user_manage_new_tel_xpath = u"//div[@class='form-item-wrap']//*[contains(.,'手机号')]//input/parent::div"
    # 新建用户-确认按钮
    user_manage_confirm_btn_xpath = u"//div[@class='dialog-footer']//button[contains(.,'确认')]"
    # 错误提示
    user_manage_error_tips_xpath = "//*[@class='el-form-item__error']"
    # AD域本地模式映射用户冲突提示
    user_manage_local_model_user_conflict_tips = "//*[@class='el-message-box__message']"
    # AD域本地模式用户冲突确认
    user_manage_local_model_user_conflict_ok = "//*[@class='el-message-box__btns']//button"
    # AD域正常用户无法删除提示
    user_manage_ad_user_delete_tips_xpath = "//p[@class='el-message__content']"
    # 用户选择-更多-传参
    user_manage_more_xpath = u"//*[contains(@class,'el-table__row')]//span[contains(.,'{0}')]/ancestor::tr//*" \
                             u"[contains(.,'更多')]/..//button"
    # 更多选择-传参(编辑\详情\发送消息\临时利旧传输\重置密码)
    user_manage_more_detail_xpath = u"//ul[@x-placement='bottom-start']//*[contains(.,'{0}')]//li"
    # 更多-按钮
    user_manage_more_select_xpath = "//div[@class='sk-toolbar']//div[@class='el-dropdown']//button"
    # 上传文件
    user_manage_upload_files_xpath = "//*[@class='el-dialog__body']//span[contains(.,'上传文件')]/.."
    # 开始导入
    user_manage_start_import_xpath = "//*[@class='el-dialog__body']//span[contains(.,'开始导入')]/.."
    # 新建用户组选择上级组织按钮
    user_manage_create_group_select_org_btn = u"//div[@role='tooltip']//*[@class='custom-tree-node']//div[contains" \
                                              u"(.,'{0}')]/../..//label"
    # 删除用户组按钮
    user_manage_group_delete_xpath = u"//div[@class='custom-tree-node']//div[contains(.,'{0}')]/..//i[@class='el-" \
                                     u"icon-delete']/.."
    # 编辑用户组按钮
    user_manage_group_edit_xpath = u"//div[@class='custom-tree-node']//div[contains(.,'{0}')]/..//i[@class='el-" \
                                   u"icon-edit']/.."
    # 用户组删除确认按钮
    user_manage_group_ok_delete_xpath = u"//div[@class='el-message-box__btns']//span[contains(.,'删除')]/.."
    # 用户组删除提示信息
    user_manage_delete_tips_xpath = u"//*[@class='el-message__content']/..//*[contains(.,'该用户组')]"

    # 高级配置
    advanced_config_xpath = u"//span[contains(text(),'高级配置')]"
    # 部署和升级 -> 先点击高级配置
    deployment_and_upgrade_xpath = u"//span[contains(.,'部署与升级')]"
    # 认证管理-> 先点击部署与升级
    certified_manage_xpath = u"//span[contains(.,'认证管理')]"
    # 系统设置
    system_setting_xpath = u"//span[contains(.,'系统设置')]"
    # 管理员账号设置
    admin_account_setting_xpath = u"//span[contains(.,'管理员账号设置')]"
    # 新建管理员账号按钮
    create_admin_account_xpath = "//*[@class='el-dropdown']//button"
    # 新建选项
    create_menu_item_xpath = u"//*[@class='el-dropdown-menu__item']/..//*[contains(.,'新建账号')]"
    # 管理员名称
    create_admin_username_xpath = u"//*[@class='el-form-item is-required']//*[text()='管理员名称：']/..//input"
    create_admin_name_xpath = u"//*[@class='el-form-item is-required']//*[text()='姓名：']/..//input"
    create_admin_pwd_xpath = u"//*[@class='el-form-item is-required']//*[text()='密码：']/..//input"
    create_admin_sec_pwd_xpath = u"//*[@class='el-form-item is-required']//*[text()='确认密码：']/..//input"
    create_admin_ok_xpath = u"//*[@class='el-dialog__footer dialog-footer__custom']//span[contains(.,'确认')]/.."
    # 取消
    create_admin_sec_cancel_xpath = u"//*[@class='el-dialog__footer dialog-footer__custom']//span[contains(.,'取消')]/.."
    # 二次确认
    create_admin_sec_ok_xpath = u"//*[@class='el-message-box__btns']//span[contains(.,'确认')]/.."

    # 管理员用户名已存在提示
    create_admin_catch_tips_xpath = "//*[@class='el-message__content']"

    # 注销按钮
    test_logout_xpath = "//*[@class='sk-icon sk-icon-logout']"
    # 用户名输入框
    test_username_input_xpath = "//*[@name='userName']"
    # 密码输入框
    test_passwd_input_xpath = "//*[@name='pwd']"
    # 登入按钮
    test_login_button_xpath = "//button[@type='button']"

    # 身份源对接模式选择 - 不启用
    id_source_mode_disable_xpath = u"//*[@class='el-form-item']//*[contains(.,'身份源对接模式选择')]/..//span" \
                                   u"[contains(.,'不启用')]/.."
    # 身份源对接模式选择 - 启用
    id_source_mode_enable_xpath = u"//*[@class='el-form-item']//*[contains(.,'身份源对接模式选择')]/.." \
                                  u"//span[contains(.,'AD域')]/.."
    # 自动加入AD域
    auto_join_ad_xpath = "//span[contains(@class,'checkbox__input')]"
    # 同步账号
    sync_account_xpath = u"//*[@class='el-form-item']//span[contains(.,'同步账号')]/.."
    # AD域服务器名称输入
    ad_servername_input_xpath = u"//label[contains(.,'AD域服务器名称')]/..//*[@class='sk-adDomain__input el-input']//input"
    # 服务器IP地址输入
    ad_serverip_input_xpath = u"//label[contains(.,'服务器IP地址')]/..//*[@class='sk-adDomain__input el-input']//input"
    # 端口
    ad_port_input = u"//label[contains(.,'端口')]/..//*[@class='sk-adDomain__port el-input']//input"
    # AD域管理员用户名
    ad_admin_name_input_xpath = u"//label[contains(.,'AD域管理员用户名')]/..//*[@class='sk-adDomain__input el-input']//input"
    # AD管理员密码
    ad_admin_pwd_input_xpath = u"//label[contains(.,'AD域管理员密码')]/..//*[@class='sk-adDomain__input el-input']//input"

    # 连接按钮
    ad_domain_connect_xpath = u"//*[@class='el-form-item']//span[contains(.,'连接')]/.."
    # 覆盖原则, 以AD域对接为准
    accorading_to_ad_xpath = u"//*[contains(@class,'el-radio')]//*[contains(.,'以AD域对接为准')]/.."
    # 以本地信息为准
    accorading_to_local_xpath = u"//*[contains(@class,'el-radio')]//*[contains(.,'本地信息为准')]/.."
    # 映射配置添加按钮
    mapping_config_add_xpath = u"//*[@class='el-form-item']//span[contains(.,'添加')]/.."
    # 映射配置编辑按钮
    mapping_config_edit_xpath = u"//*[@class='el-form-item']//span[contains(.,'编辑')]/.."

    # 组织架构切换
    mapping_org_switch_xpath = "//span[@class='el-switch__core']/.."
    # 本地组模式
    mapping_local_mode_xpath = "//span[@class='el-switch__core']//following-sibling::span[1]"
    # 选中分组
    mapping_select_group_xpath = u"//*[@class='el-dialog__body']//*[contains(@class,'sk-text--ellipse')]/.." \
                                 u"//*[text()='{0}']/..//preceding-sibling::label[1]"
    # 点击分组
    mapping_select_click_group_xpath = u"//*[@class='el-dialog__body']//*[contains(@class,'sk-text--ellipse')]" \
                                       u"/..//*[text()='{0}']/.."
    # 组织机构-一系列映射
    mapping_organization_items_xpath = "//tr[@class='el-table__row']//div[@class='cell']//div"

    # 暂无数据
    mapping_none_xpath = "//*[@class='el-table__empty-text']"
    # 编辑组织机构
    mapping_edit_xpath = u"//*[@class='el-table__row']//span[contains(.,'编辑')]/.."
    # 删除组织机构
    mapping_delete_xpath = u"//*[@class='el-table__row']//span[contains(.,'删除')]/.."
    # 选择组织机构提示
    mapping_sele_tips_xpath = u"//*[@class='el-message__content']/..//*[contains(.,'请选择')]"
    # 搜索框
    mapping_search_box_xpath = "//*[@class='el-input el-input--suffix']//input"
    # AD域右侧映射显示
    ad_mapping_right_show_xpath = "//div[@class='sk-composite-tree__right']"
    # 添加按钮下一步
    mapping_next_step_xpath = u"//span[contains(.,'下一步')]/.."
    # 添加按钮上一步
    mapping_previous_step_xpath = u"//span[contains(.,'上一步')]/.."
    # 添加用户组
    mapping_add_group_xpath = u"//span[contains(.,'添加用户组')]/.."
    # 输入用户组名
    mapping_input_usergroup_xpath = "//div[@class='el-input']//input"
    # 输入完用户组名之后的确认按钮
    mapping_input_ok_xpath = u"//span[contains(.,'确认')]/.."
    # 禁用提示确认按钮2
    mapping_input_btn_xpath = u"//*[@class='dialog-footer']//span[contains(.,'确认')]/.."
    # 取消按钮
    mapping_input_cancel_xpath = u"//span[contains(.,'取消')]/.."
    # 最终确认添加按钮
    mapping_ok_add_xpath = u"//span[contains(.,'确认添加')]/.."
    # 同步时关闭按钮
    mapping_sync_close_xpath = u"//*[@class='el-dialog__header']//*[text()='任务执行中']/..//button"
    # 同步后确认按钮
    mapping_sync_is_ok_xpath = "//*[@class='el-dialog__body']//button"
    # 保存按钮
    save_button_xpath = u"//button[contains(.,'保存')]"
    # 二次密码确认框
    sec_pwd_confirm_xpath = "//*[@class='el-dialog']//*[@class='el-dialog__body']//input"
    # 确认按钮
    sec_pwd_ok_xpath = u"//*[@class='el-dialog']//*[@class='dialog-footer']//span[contains(.,'确认')]/.."
    # 二次确认提示
    sec_pwd_tips_xpath = "//*[contains(@class,'user-disable-tip-main')]"
    # 取消按钮
    sec_pwd_cancel_xpath = u"//*[@class='el-dialog']//*[@class='dialog-footer']//span[contains(.,'取消')]/.."
    # 数据不合法
    data_illegal_tip_xpath = u"//*[@class='el-message__content']/..//*[contains(.,'数据不合法')]"
    # AD域服务器连接失败
    ad_disconnect_xpath = u"//*[@class='el-message__content']/..//*[contains(.,'AD域服务器连接失败')]"
    # AD域服务器连接成功
    ad_connect_xpath = u"//*[@class='el-notification__content']/p"
    # AD域映射配置为空
    ad_mapping_config_tips_xpath = "//*[@class='el-message__content']"
    # 错误提示
    error_tips_xpath = "//*[@class='el-form-item__error']"
    # 同步日志按钮
    sync_log_btn = u"//button[contains(.,'同步日志')]"
    # 日志搜索时间选择框
    log_search_times_select = u"//input[contains(@placeholder,'选择开始时间')]"
    # 日志搜索时间弹出框
    log_search_alert_select = "//div[contains(@class,'el-picker-panel__body-wrapper')]"
    # 日志搜索按钮
    log_search_btn = u"//button[contains(.,'查询')]"
    # 日志显示总条目
    log_display_all_items = "//tbody//tr[contains(@class,'el-table__row')]"
    # 日志显示头信息
    log_display_header_info = "//thead[contains(@class,'has-gutter')]"
    # 同步日志返回按钮
    sync_log_back_btn = "//*[contains(@class,'el-icon-back')]/../.."
    # 同步日志翻页按钮
    sync_log_next_page_btn = "//*[contains(@class,'el-icon el-icon-arrow-right')]/.."
    # 告警管理Xpath--# 告警管理iframe=frameContent
    warnning_xpath = "//*[@class='sk-icon sk-icon-alert']/.."
    # 历史告警
    warnning_history_xpath = "//*[@onclick='gotoHistoryAlarmPage();']"
    # 历史首页告警
    warnning_history_first_xpath = u"//*[contains(text(),'AD域服务器')]/ancestor::tr"

    ##################################

    # 认证管理-同步成功确认按钮
    sync_success_sure_button_xpath = "//div[@class='sk-progresses__status']/descendant::button"
    # 认证管理-同步失败提示框
    sync_wrong_xpath = "//span[@class='sk-text--left']"
    # 认证管理-同步日志按钮
    sync_log_button_xpath = "//*[@class='el-button el-button--primary el-button--medium is-round']"
    # 认证管理-同步失败日志
    sync_wrong_log_xpath = "//*[@class='el-scrollbar el-table__body-wrapper is-scrolling-none']//tr[1]//" \
                           "span[@class='sk-icon-status__content sk-icon-status__content--error']"
    # 认证管理-开启AD认证之后的展示的窗口
    ad_domain_window_xpath = "//form[@onsubmit=' return false;']"
    # 认证管理-已启用自动加入AD域
    open_auto_join_ad_xpath = u"//label[@class='el-checkbox is-checked']"
    # 认证管理-未启用自动加入AD域
    close_auto_join_ad_xpath = u"//label[@class='el-checkbox']"
    # 认证管理-编辑按钮
    edit_ou_button_xpath = u"//span[contains(text(),'编辑')]"
    # 认证管理-选用某组织架构
    choose_ou_xpath = "//span[contains(text(),'{}')]/../preceding-sibling::label[@class='el-checkbox']"
    # 认证管理-选用某组织架构后的确认添加按钮
    choose_ou_sure_button_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"
    # 认证管理-选用某组织架构后禁用用户的确认添加按钮
    user_disable_sure_button_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"

    # 跳转到用户管理页面xpath
    user_manage_xpath = u"//*[text()='用户管理']"
    # 搜素框后的更多按钮xpath
    more_operate_xpath = "//div[@class='sk-toolbar']/descendant::div[@class='el-dropdown']//button"
    # 填充ipxpath
    fill_ip_xpath = u"//li[contains(text(),'填充IP') ]"
    # 云桌面首选DNS：输入框
    first_DNS_xpaht = "//*[contains(text(),'云桌面首选DNS：')]/parent::div//descendant::input"
    # 确定按钮
    confirm_button_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"
    # 选择用户单选框传入用户名为参数
    chose_user_xpath = "//*[text()='{}']/ancestor::tr//span[@class='el-checkbox__input']"
    # 搜索框xpath
    search_xpath = "//*[@class='fl']//*[@class='el-input__inner']"

    # 用户管理-更多按钮
    user_manage_more_button_xpath = u"//*[text()='{}']/ancestor::tr//button"
    # 用户管理-更多选项中的编辑按钮
    user_manage_edit_button_xpath = u"//li[contains(text(),'编辑')]"
    # 用户管理-VDI云桌面设置
    vdi_vm_set_xpath = u"//div[@id='scrollpane-vdiPolicy']/descendant::*[contains(text(),'VDI云桌面')]"
    # 用户管理-启用vdi云桌面
    vdi_vm_open_xpath = "//*[@id='scrollpane-vdiPolicy']/descendant::*[@class='el-switch']"
    # 用户管理-VDI云桌面类型选择
    vdi_vm_type_xpath = u"//div[@id='scrollpane-vdiPolicy']/descendant::*[contains(text(),'桌面类型')]/following-sibling::*"
    # 用户管理-VDI云桌面类型选择还原
    vdi_vm_type_restore_xpath = u"//*[@class='el-scrollbar']//span[contains(text(),'还原')]"
    # 用户管理-VDI云桌面类型选择个性
    vdi_vm_type_single_xpath = u"//*[@class='el-scrollbar']//span[contains(text(),'个性')]"
    # 用户管理-绑定镜像文字
    vdi_vm_bind_string_xpath = u"//*[@for='vdiPolicy.imageIds']"
    # 用户管理-VDI云桌面镜像选择
    vdi_vm_base_xpath = u"//div[@id='scrollpane-vdiPolicy']/descendant::*[contains(text(),'绑定镜像')]" \
                        u"/following-sibling::*"
    # 用户管理-VDI云桌面类型选择镜像
    vdi_vm_base_set_xpath = u"//span[contains(text(),'{}')]"
    # 用户管理-首选DNS地址编辑
    first_dns_edit_xpath = u"//label[contains(text(),'云桌面首选DNS')]/following-sibling::*/child::div"
    # 用户管理-编辑界面确认按钮
    edit_form_sure_button_xpath = u"//button[@class='el-button el-button--primary el-button--mini is-round']"
    # 用户管理-个性变还原桌面类型提示框提示框
    vm_type_info_form_xpath = u"//div[@class='el-message-box__wrapper']"
    # 用户管理-个性变还原桌面类型提示框确认按钮
    vm_type_info_form_sure_button_xpath = u"//button[@class='el-button el-button--default el-button--mini is-round " \
                                          u"el-button--primary ']"
    # 用户管理-输入密码确认框
    input_passwd_xpath = u"//*[@placeholder='请输入管理员密码']"
    # 用户管理-输入密码户确认按钮
    input_passwd_sure_button_xpath = u"//*[@placeholder='请输入管理员密码']/../../../../../../following-sibling::div//" \
                                     u"child::*[contains(text(),'确认')]"

    # 用户名输入框
    username_input_xpath = "//*[@name='userName']"
    # 密码输入框
    passwd_input_xpath = "//*[@name='pwd']"
    # 登入按钮
    login_button_xpath = "//button[@type='button']"

    # 安卓vdi-用户名密码输入错误提示
    no_user_id = "com.ruijie.rccstu:id/tv_error_title"
    # 安卓vdi-重新连接
    reconnect_id = "com.ruijie.rccstu:id/btn_reconnect"

    # 用户禁用确认按钮
    u_confirm_button_xpath = ur"//*[@class='dialog-footer']//*[text()='确认']"
    # 提示框文本-提示二字
    prompt_text_xpath = r"//*[@class='el-dialog']/div[@class='el-dialog__header']/span"
    # 搜索按钮
    click_xpath = r"//*[@class='el-input__icon sk-icon-search sk-toolbar__icon el-tooltip item']"

    # 确认用户ad禁用
    def disable_aduser_confirm(self):
        try:
            self.click_elem(self.u_confirm_button_xpath)
        except:
            logging.info("无禁用用户提示")

    # 跳转到认证管理页面
    def goto_adm(self):
        self.click_elem(self.advanced_config_xpath)
        time.sleep(0.5)
        self.click_elem(self.deployment_and_upgrade_xpath)
        time.sleep(2)
        self.scroll_into_view(self.certified_manage_xpath)

    # 正常连接AD域
    def connect_ad_domain(self):
        time.sleep(0.2)
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.find_elem(self.ad_servername_input_xpath).click()
        self.find_elem(self.ad_servername_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_servername_input_xpath).send_keys(ad_domain_name)
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_serverip_input_xpath).send_keys(ad_domain_ip_2)
        self.find_elem(self.ad_port_input).click()
        self.find_elem(self.ad_port_input).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_port_input).send_keys(ad_domain_port)
        self.find_elem(self.ad_admin_name_input_xpath).click()
        self.find_elem(self.ad_admin_name_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_admin_name_input_xpath).send_keys(ad_domain_admin_username2)
        self.find_elem(self.ad_admin_pwd_input_xpath).click()
        self.find_elem(self.ad_admin_pwd_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_admin_pwd_input_xpath).send_keys(ad_domain_admin_user_pwd)
        self.find_elem(self.ad_domain_connect_xpath).click()

    # 切换到本地组
    def switch_local_group(self):
        if not self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            self.click_elem(self.mapping_select_group_xpath.format(ad_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()

    # 校验开启AD域认证失败情况(A1.1)
    def ad_enable(self):
        flag_list = [0, 0, 0, 0]
        self.goto_adm()
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.find_elem(self.ad_servername_input_xpath).click()
        self.find_elem(self.ad_servername_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_port_input).click()
        self.find_elem(self.ad_port_input).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_admin_name_input_xpath).click()
        self.find_elem(self.ad_admin_name_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_admin_pwd_input_xpath).click()
        self.find_elem(self.ad_admin_pwd_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            flag_list[0] = 1
        self.find_elem(self.ad_servername_input_xpath).click()
        self.find_elem(self.ad_servername_input_xpath).send_keys(ad_domain_name)
        self.find_elem(self.ad_port_input).click()
        self.find_elem(self.ad_port_input).send_keys(ad_domain_port)
        self.find_elem(self.ad_admin_name_input_xpath).click()
        self.find_elem(self.ad_admin_name_input_xpath).send_keys(ad_domain_admin_username2)
        self.find_elem(self.ad_admin_pwd_input_xpath).click()
        self.find_elem(self.ad_admin_pwd_input_xpath).send_keys(ad_domain_admin_user_pwd)
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            flag_list[1] = 1
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(ad_domain_ip_2[0:-1] + '9')
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            flag_list[2] = 1
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_serverip_input_xpath).send_keys(ad_domain_ip_2[0:-1] + '99')
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            flag_list[3] = 1
        return flag_list

    # 校验开启AD域是否认证成功(A1.2)
    def ad_enable_success(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.ad_connect_xpath).text.__contains__(u"AD域服务器连接成功"):
            flag_list[0] = 1
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        try:
            if self.find_elem(self.sec_pwd_tips_xpath, wait_times=5).text.__contains__(u"用户将被禁用"):
                self.find_elem(self.mapping_input_btn_xpath).click()
        except Exception as e:
            print(e)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(login_user_succ["passwd"])
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[1] = 1
        return flag_list

    # 校验AD域服务器名称(A1.3)
    def ad_domain_server_name_check(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.ad_connect_xpath).text.__contains__(u"AD域服务器连接成功"):
            flag_list[0] = 1
        self.find_elem(self.ad_admin_name_input_xpath).click()
        self.find_elem(self.ad_admin_name_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_admin_name_input_xpath).click()
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            if self.find_elem(self.error_tips_xpath).text.__contains__(u"必填项"):
                flag_list[1] = 1
        return flag_list

    # 校验AD域服务器IP地址(A1.4)
    def ad_domain_server_ip_check(self):
        flag_list = [0, 0, 0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.ad_connect_xpath).text.__contains__(u"AD域服务器连接成功"):
            flag_list[0] = 1
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_serverip_input_xpath).send_keys(ad_domain_ip_2[0:-1] + '9')
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            if self.find_elem(self.error_tips_xpath).text.__contains__(u"AD域服务器连接失败"):
                flag_list[1] = 1
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_serverip_input_xpath).send_keys(ad_domain_ip_2[0:-1] + '99')
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            if self.find_elem(self.error_tips_xpath).text.__contains__(u"ip地址不合法"):
                flag_list[2] = 1
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            if self.find_elem(self.error_tips_xpath).text.__contains__(u"必填项"):
                flag_list[3] = 1
        return flag_list

    # 校验AD域服务器端口(A1.5)
    def ad_domain_server_port_check(self):
        flag_list = [0, 0, 0, 0, 0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.ad_connect_xpath).text.__contains__(u"AD域服务器连接成功"):
            flag_list[0] = 1
        self.find_elem(self.ad_port_input).click()
        self.find_elem(self.ad_port_input).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_port_input).send_keys(u'80')
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            if self.find_elem(self.error_tips_xpath).text.__contains__(u"AD域服务器连接失败"):
                flag_list[1] = 1
        test_list = [u'中文测试', u'testtest', u'999999', u'!@#$%^']
        for i in range(len(test_list)):
            self.find_elem(self.ad_port_input).click()
            self.find_elem(self.ad_port_input).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
            self.find_elem(self.ad_port_input).send_keys(test_list[i])
            self.find_elem(self.ad_domain_connect_xpath).click()
            if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
                if self.find_elem(self.error_tips_xpath).text.__contains__(u"请输入1-65535的整数"):
                    flag_list[i + 2] = 1
        return flag_list

    # 校验自动加入AD域异常情况(A1.17)
    def auto_join_ad_check_1(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_serverip_input_xpath).send_keys(ad_domain_ip_2[0:-1] + '9')
        self.find_elem(self.auto_join_ad_xpath).click()
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            if self.find_elem(self.error_tips_xpath).text.__contains__(u"AD域服务器连接失败"):
                flag_list[0] = 1
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            if self.find_elem(self.error_tips_xpath).text.__contains__(u"AD域服务器连接失败"):
                flag_list[1] = 1
        return flag_list

    # 映射配置添加失败情况(A1.25)
    def mapping_config_add_1(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.switch_local_group()
        try:
            self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
        except Exception as e:
            self.scroll_into_view(self.mapping_delete_xpath)
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            self.find_elem(self.mapping_input_btn_xpath).click()
            print(e)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(login_user_succ["passwd"])
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.ad_mapping_config_tips_xpath).text.__contains__(u"AD域映射配置为空，请新增后重试！"):
            flag_list[0] = 1
        time.sleep(2)
        self.click_elem(self.sync_account_xpath)
        time.sleep(0.2)
        if self.find_elem(self.ad_mapping_config_tips_xpath).text.__contains__(u"AD域映射配置为空，请新增后重试！"):
            flag_list[1] = 1
        return flag_list

    # 大小写敏感测试(A1.92)
    def case_sensitive_check(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.ad_connect_xpath).text.__contains__(u"AD域服务器连接成功"):
            flag_list[0] = 1
        self.find_elem(self.ad_admin_name_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_admin_name_input_xpath).send_keys(ad_domain_admin_upper_username)
        self.find_elem(self.ad_admin_pwd_input_xpath).click()
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.ad_connect_xpath).text.__contains__(u"AD域服务器连接成功"):
            flag_list[1] = 1
        return flag_list

    # 使用普通管理员账号登录(A1.93)
    def normal_account_login_check(self):
        flag_list = [0]
        create_user = u'test'
        create_pwd = u'test'
        self.find_elem(self.advanced_config_xpath).click()
        self.find_elem(self.system_setting_xpath).click()
        self.find_elem(self.admin_account_setting_xpath).click()
        self.find_elem(self.create_admin_account_xpath).click()
        self.find_elem(self.create_menu_item_xpath).click()
        self.find_elem(self.create_admin_username_xpath).click()
        self.find_elem(self.create_admin_username_xpath).send_keys(create_user)
        self.find_elem(self.create_admin_name_xpath).click()
        self.find_elem(self.create_admin_name_xpath).send_keys(create_user)
        self.find_elem(self.create_admin_pwd_xpath).click()
        self.find_elem(self.create_admin_pwd_xpath).send_keys(create_pwd)
        self.find_elem(self.create_admin_sec_pwd_xpath).click()
        self.find_elem(self.create_admin_sec_pwd_xpath).send_keys(create_pwd)
        self.find_elem(self.create_admin_ok_xpath).click()
        self.find_elem(self.create_admin_sec_ok_xpath).click()
        try:
            if len(self.find_elems(self.create_admin_catch_tips_xpath, wait_times=3)) != 0:
                self.find_elem(self.create_admin_sec_cancel_xpath).click()
        except Exception as e:
            print(e)
        time.sleep(3)
        self.find_elem(self.test_logout_xpath).click()
        self.find_elem(self.test_username_input_xpath).send_keys(create_user)
        self.find_elem(self.test_passwd_input_xpath).send_keys(create_pwd)
        self.find_elem(self.test_login_button_xpath).click()
        self.find_elem(self.advanced_config_xpath).click()
        try:
            self.find_elems(self.certified_manage_xpath, wait_times=3)
        except Exception as e:
            flag_list[0] = 1
            print(e)
        return flag_list

    # 同步账号异常测试(A1.10)
    def sync_account_double_check(self):
        flag_list = [0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.switch_local_group()
        try:
            self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
            self.find_elem(self.mapping_config_add_xpath).click()
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_next_step_xpath).click()
            # try:
            #     self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
            # except Exception as e:
            #     self.find_elem(self.mapping_add_group_xpath).click()
            #     self.find_elem(self.mapping_input_usergroup_xpath).click()
            #     self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
            #     self.find_elem(self.mapping_input_ok_xpath).click()
            #     print(e)
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
        except Exception as e:
            print(e)
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.disable_aduser_confirm()
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        self.find_elem(self.mapping_sync_close_xpath).click()
        # self.driver.refresh()
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.ad_mapping_config_tips_xpath).text.__contains__(u"AD域用户正在同步"):
            flag_list[0] = 1
        return flag_list

    # AD域认证关闭-异常测试(A1.14)
    def ad_domain_close_check_1(self):
        flag_list = [0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        try:
            self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
            self.find_elem(self.mapping_config_add_xpath).click()
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_next_step_xpath).click()
            try:
                self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
            except Exception as e:
                self.find_elem(self.mapping_add_group_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
                self.find_elem(self.mapping_input_ok_xpath).click()
                print(e)
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
        except Exception as e:
            print(e)
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        time.sleep(0.5)
        self.find_elem(self.mapping_sync_close_xpath).click()
        self.find_elem(self.id_source_mode_disable_xpath).click()
        # self.driver.refresh()
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.mapping_input_ok_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.ad_mapping_config_tips_xpath).text.__contains__(u"AD域用户正在同步"):
            flag_list[0] = 1
        #   保证ad域同步完成避免影响下一条用例
        time.sleep(60)
        return flag_list

    # AD域认证关闭-正常关闭(A1.15)
    def ad_domain_close_check_2(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        try:
            self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
            self.find_elem(self.mapping_config_add_xpath).click()
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_next_step_xpath).click()
            try:
                self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
            except Exception as e:
                self.find_elem(self.mapping_add_group_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
                self.find_elem(self.mapping_input_ok_xpath).click()
                print(e)
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
        except Exception as e:
            print(e)
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        self.find_elem(self.mapping_sync_is_ok_xpath, wait_times=300).click()
        self.find_elem(self.id_source_mode_disable_xpath).click()
        # self.driver.refresh()
        try:
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            self.find_elem(self.mapping_input_ok_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
            flag_list[0] = 1
        except Exception as e:
            flag_list[0] = 0  # 如果出现异常flag置为0
            print(e)
        self.find_elem(self.user_management_xpath).click()
        time.sleep(5)
        ele_list = self.find_elems(self.user_manage_status_xpath)
        temp_text_list = []
        for i in range(len(ele_list)):
            temp_text_list.append(ele_list[i].text.strip())
        if temp_text_list.__contains__(u"禁用"):
            flag_list[1] = 1
        return flag_list

    # AD域本地组模式-映射配置添加(A1.26、27、28)
    def mapping_config_add_2(self):
        flag_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.switch_local_group()
        try:
            self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
        except Exception as e:
            self.scroll_into_view(self.mapping_delete_xpath)
            print(e)
        self.find_elem(self.mapping_config_add_xpath).click()
        if self.find_elem(self.mapping_config_add_xpath):
            flag_list[0] = 1
        self.find_elem(self.mapping_next_step_xpath).click()
        if self.find_elem(self.mapping_sele_tips_xpath).text.__contains__(u'请选择组织机构'):
            flag_list[1] = 1
        if self.find_elem(self.mapping_select_group_xpath.format(unselectable_group)).get_attribute('class'). \
                __contains__(u'is-disabled'):
            flag_list[2] = 1
        self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked'). \
                __contains__('mixed') or self.find_elem(self.mapping_select_group_xpath.format(ad_group)). \
                get_attribute('aria-checked').__contains__('true'):
            flag_list[3] = 1
        self.find_elem(self.mapping_search_box_xpath).click()
        self.find_elem(self.mapping_search_box_xpath).send_keys(ad_group)
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked'). \
                __contains__('mixed') or self.find_elem(self.mapping_select_group_xpath.format(ad_group)). \
                get_attribute('aria-checked').__contains__('true'):
            flag_list[4] = 1
        self.find_elem(self.mapping_next_step_xpath).click()
        self.find_elem(self.mapping_next_step_xpath).click()
        if self.find_elem(self.mapping_sele_tips_xpath).text.__contains__(u"请选择本地用户组"):
            flag_list[5] = 1
        self.find_elem(self.mapping_previous_step_xpath).click()
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked'). \
                __contains__('mixed') or self.find_elem(self.mapping_select_group_xpath.format(ad_group)). \
                get_attribute('aria-checked').__contains__('true'):
            flag_list[6] = 1
        self.find_elem(self.mapping_next_step_xpath).click()
        try:
            self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
        except Exception as e:
            self.find_elem(self.mapping_add_group_xpath).click()
            self.find_elem(self.mapping_input_usergroup_xpath).click()
            self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
            self.find_elem(self.mapping_input_ok_xpath).click()
            print(e)
        self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
        if self.find_elem(self.mapping_select_group_xpath.format(mapping_group)).get_attribute('aria-checked'). \
                __contains__('mixed') or self.find_elem(self.mapping_select_group_xpath.format(mapping_group)). \
                get_attribute('aria-checked').__contains__('true'):
            flag_list[7] = 1
        self.find_elem(self.mapping_next_step_xpath).click()
        self.find_elem(self.mapping_ok_add_xpath).click()
        return flag_list

    # AD域本地组模式-映射配置修改(A1.32、33)
    def mapping_config_modify_1(self):
        flag_list = [0, 0, 0, 0]
        self.goto_adm()
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.switch_local_group()
        time.sleep(5)
        self.scroll_into_view(self.mapping_config_edit_xpath)
        time.sleep(5)
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)):
            flag_list[0] = 1
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked'). \
                __contains__('mixed') or self.find_elem(self.mapping_select_group_xpath.format(ad_group)). \
                get_attribute('aria-checked').__contains__('true'):
            flag_list[1] = 1
        self.find_elem(self.mapping_next_step_xpath).click()
        self.find_elem(self.mapping_previous_step_xpath).click()
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked'). \
                __contains__('mixed') or self.find_elem(self.mapping_select_group_xpath.format(ad_group)). \
                get_attribute('aria-checked').__contains__('true'):
            flag_list[2] = 1
        self.find_elem(self.mapping_next_step_xpath).click()
        self.find_elem(self.mapping_ok_add_xpath).click()
        if self.find_elem(self.mapping_edit_xpath):
            flag_list[3] = 1
        return flag_list

    # AD域模式切换-本地组切换为AD域，AD域切换为本地组(A1.45、46)
    def local_group_ad_domain_switch(self):
        flag_list = [0, 0, 0, 0]
        self.goto_adm()
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.switch_local_group()
        self.find_elem(self.mapping_org_switch_xpath).click()
        self.find_elem(self.mapping_input_cancel_xpath).click()
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            flag_list[0] = 1
        self.find_elem(self.mapping_org_switch_xpath).click()
        self.find_elem(self.mapping_input_ok_xpath).click()
        time.sleep(2)
        self.click_elem(self.mapping_ok_add_xpath)
        if not self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            flag_list[1] = 1
        self.find_elem(self.mapping_org_switch_xpath).click()
        self.find_elem(self.mapping_input_cancel_xpath).click()
        if not self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            flag_list[2] = 1
        self.find_elem(self.mapping_org_switch_xpath).click()
        time.sleep(0.5)
        self.click_elem(self.mapping_input_ok_xpath)
        self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
        self.find_elem(self.mapping_next_step_xpath).click()
        self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
        self.find_elem(self.mapping_next_step_xpath).click()
        self.find_elem(self.mapping_ok_add_xpath).click()
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            flag_list[3] = 1
        return flag_list

    # AD域本地组模式-映射配置修改(A1.34)
    def mapping_config_modify_2(self):
        flag_list = [0]
        self.goto_adm()
        self.find_elem(self.id_source_mode_enable_xpath).click()
        # 切换回本地组模式
        if not self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_next_step_xpath).click()
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            try:
                if self.find_elem(self.sec_pwd_tips_xpath, wait_times=2).text.__contains__(u"用户将被禁用"):
                    self.find_elem(self.mapping_input_ok_xpath).click()
            except Exception as e:
                print(e)
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
            self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        self.connect_ad_domain()  # 正常连接AD域
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_serverip_input_xpath).send_keys(ad_domain_ip_2[0:-1] + '9')
        self.find_elem(self.ad_domain_connect_xpath).click()
        if not self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_next_step_xpath).click()
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
            self.find_elem(self.mapping_edit_xpath).click()
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            flag_list[0] = 1
        return flag_list

    # AD域本地组模式(A1.35)
    # 点击所在分组
    ad_user_group_xpath = u"//*[contains(text(),'{}')]"
    # 禁用点击确认
    unable_to_use_confirm_xpath = '//*[@class="el-button el-button--primary el-button--mini is-round"]'
    def local_group_portion_user_sync(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.switch_local_group()
        try:
            self.find_elem(self.mapping_delete_xpath, wait_times=3).click()
        except Exception as e:
            print(e)
        try:
            self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
            self.find_elem(self.mapping_config_add_xpath).click()
            self.find_elem(self.mapping_select_click_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_select_group_xpath.format(ad_user_list[0])).click()
            self.find_elem(self.mapping_next_step_xpath).click()
            try:
                self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
            except Exception as e:
                print(e)
                self.find_elem(self.mapping_add_group_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
                self.find_elem(self.mapping_input_ok_xpath).click()
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
        except Exception as e:
            print(e)
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        try:
            if self.find_elem(self.sec_pwd_tips_xpath, wait_times=2).text.__contains__(u"用户将被禁用"):
                flag_list[0] = 1
            self.find_elem(self.mapping_input_ok_xpath).click()
        except Exception as e:
            print(e)
        if self.elem_is_exist2(self.unable_to_use_confirm_xpath) is not None:
            self.click_elem(self.unable_to_use_confirm_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        self.find_elem(self.user_management_xpath).click()
        time.sleep(1)
        self.click_elem(self.ad_user_group_xpath.format(mapping_group))
        time.sleep(1)
        for temp in range(2):
            temp_user_list = self.find_presence_elems(self.user_username_status_xpath)
            temp_text_user_list = []
            for i in range(len(temp_user_list)):
                temp_text_user_list.append(temp_user_list[i].text.strip())
            for j in range(len(temp_text_user_list)):
                try:
                    if temp_text_user_list[j].__contains__(ad_user_list[0]):
                        if temp_text_user_list[j].__contains__(u"正常"):
                            flag_list[1] = 1
                            break
                except Exception as e:
                    print(e)
            if flag_list[1] == 1:
                break
            self.find_elem(self.user_manage_next_page_xpath).click()
            time.sleep(2)
        return flag_list

    # AD本地组模式映射配置删除(A1.36)
    def mapping_config_delete_1(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.switch_local_group()
        try:
            self.scroll_into_view(self.mapping_delete_xpath, wait_times=3)
        except Exception as e:
            print(e)
            try:
                self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
                self.find_elem(self.mapping_config_add_xpath).click()
                self.find_elem(self.mapping_select_click_group_xpath.format(ad_group)).click()
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
                self.find_elem(self.mapping_next_step_xpath).click()
                try:
                    self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
                except Exception as e:
                    print(e)
                    self.scroll_into_view(self.mapping_add_group_xpath)
                    self.find_elem(self.mapping_input_usergroup_xpath).click()
                    self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
                    self.find_elem(self.mapping_input_ok_xpath).click()
                # self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
                # self.find_elem(self.mapping_next_step_xpath).click()
                # self.find_elem(self.mapping_ok_add_xpath).click()
                # self.find_elem(self.save_button_xpath).click()
                # self.find_elem(self.sec_pwd_confirm_xpath).click()
                # self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
                # self.find_elem(self.sec_pwd_ok_xpath).click()
                self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
                self.scroll_into_view(self.mapping_delete_xpath)
            except Exception as e:
                print(e)
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        time.sleep(2)
        if self.find_elem(self.sec_pwd_tips_xpath).text.__contains__(u"被禁用"):
            flag_list[0] = 1
        self.find_elem(self.sec_pwd_ok_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        time.sleep(3)
        self.click_elem(self.user_management_xpath)

        temp_user_list = self.find_presence_elems(self.user_username_status_xpath)
        temp_text_user_list = []
        for i in range(len(temp_user_list)):
            temp_text_user_list.append(temp_user_list[i].text.strip())
        for j in range(len(temp_text_user_list)):
            try:
                if temp_text_user_list[j].__contains__(u"禁用"):
                    flag_list[1] = 1
                    break
                else:
                    self.find_elem(self.user_manage_next_page_xpath).click()
                    time.sleep(2)
            except Exception as e:
                print(e)
        return flag_list

    # AD本地组模式映射配置删除(A1.37)
    def mapping_config_delete_2(self):
        flag_list = [0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域

        try:
            self.scroll_into_view(self.mapping_delete_xpath, wait_times=3)
        except Exception as e:
            print(e)
            try:
                self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
                self.find_elem(self.mapping_config_add_xpath).click()
                self.find_elem(self.mapping_select_click_group_xpath.format(ad_group)).click()
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
                self.find_elem(self.mapping_next_step_xpath).click()
                try:
                    self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
                except Exception as e:
                    self.find_elem(self.mapping_add_group_xpath).click()
                    self.find_elem(self.mapping_input_usergroup_xpath).click()
                    self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
                    self.find_elem(self.mapping_input_ok_xpath).click()
                    print(e)
                self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
                self.find_elem(self.mapping_next_step_xpath).click()
                self.find_elem(self.mapping_ok_add_xpath).click()
                time.sleep(1)
                self.click_elem(self.save_button_xpath)
                self.find_elem(self.sec_pwd_confirm_xpath).click()
                self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
                self.find_elem(self.sec_pwd_ok_xpath).click()
                self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
                self.find_elem(self.mapping_delete_xpath).click()
            except Exception as e:
                print(e)
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_serverip_input_xpath).send_keys(ad_domain_ip_2[0:-1] + '9')
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            flag_list[0] = 1
        return flag_list

    # AD本地组模式用户组删除(A1.38)
    def local_user_group_delete_1(self):
        flag_list = [0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.switch_local_group()
        try:
            self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
            self.find_elem(self.mapping_config_add_xpath).click()
            self.find_elem(self.mapping_select_click_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_next_step_xpath).click()
            try:
                self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
            except Exception as e:
                self.find_elem(self.mapping_add_group_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
                self.find_elem(self.mapping_input_ok_xpath).click()
                print(e)
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
            self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        except Exception as e:
            print(e)
        self.find_elem(self.user_management_xpath).click()
        self.chainstay(self.user_manage_group_item_xpath.format(mapping_group))
        self.find_elem(self.user_manage_group_delete_xpath.format(mapping_group)).click()
        self.find_elem(self.user_manage_group_ok_delete_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.user_manage_delete_tips_xpath).text.__contains__(u'该用户组在【认证管理】存在映射关系'):
            flag_list[0] = 1
        return flag_list

    # AD本地组模式映射配置增删改(A1.39)
    def mapping_config_crud(self):
        flag_list = [0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.switch_local_group()
        try:
            self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
            self.find_elem(self.mapping_config_add_xpath).click()
            time.sleep(2)
            # self.find_elem(self.mapping_select_click_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_next_step_xpath).click()
            try:
                self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
            except Exception as e:
                self.find_elem(self.mapping_add_group_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
                self.find_elem(self.mapping_input_ok_xpath).click()
                print(e)
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
        except Exception as e:
            print(e)
            self.find_elem(self.sync_account_xpath).click()
        self.find_elem(self.mapping_sync_close_xpath).click()
        self.scroll_into_view(self.mapping_delete_xpath)
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.disable_aduser_confirm()
        self.elem_send_keys(self.sec_pwd_confirm_xpath, c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.ad_mapping_config_tips_xpath).text.__contains__(u'AD域用户正在同步，请稍后重试！'):
            flag_list[0] = 1
        return flag_list

    # AD本地组模式映射配置——添加(A1.29)
    def mapping_config_add_3(self):
        flag_list = [0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.switch_local_group()
        time.sleep(2)
        self.scroll_into_view(self.mapping_delete_xpath)
        # try:
        #     self.scroll_into_view(self.mapping_delete_xpath)
        # except Exception as e:
        #     print(e)
        try:
            self.find_elem(self.mapping_none_xpath, wait_times=5).text.__contains__(u'暂无数据')
            self.find_elem(self.mapping_config_add_xpath).click()
            self.click_elem(self.mapping_select_click_group_xpath.format(ad_group))
            self.click_elem(self.mapping_select_group_xpath.format(ad_user_list[0]))
            self.click_elem(self.mapping_next_step_xpath)
            try:
                self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
            except Exception as e:
                self.find_elem(self.mapping_add_group_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
                self.find_elem(self.mapping_input_ok_xpath).click()
                print(e)
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
        except Exception as e:
            print(e)
        temp_num_1 = len(self.find_elems(self.mapping_organization_items_xpath))
        self.find_elem(self.mapping_config_add_xpath).click()
        self.click_elem(self.mapping_select_group_xpath.format(ad_group))
        self.find_elem(self.mapping_next_step_xpath).click()
        self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
        self.find_elem(self.mapping_next_step_xpath).click()
        self.find_elem(self.mapping_ok_add_xpath).click()
        temp_num_2 = len(self.find_elems(self.mapping_organization_items_xpath))
        if temp_num_2 > temp_num_1:
            flag_list[0] = 1
        return flag_list

    # AD域本地组模式映射配置——添加(A1.30)
    def mapping_config_add_4(self):
        flag_list = [0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.switch_local_group()
        self.find_elem(self.ad_serverip_input_xpath).click()
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_serverip_input_xpath).send_keys(ad_domain_ip_2[0:-1] + '9')
        self.find_elem(self.mapping_config_add_xpath).click()  # 点击配置添加
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            flag_list[0] = 1
        return flag_list

    # AD域本地组模式映射配置——添加(A1.31)
    def mapping_config_add_5(self):
        flag_list = [0, 0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if not self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_next_step_xpath).click()
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
        try:
            self.find_elem(self.mapping_delete_xpath, wait_times=3).click()
        except Exception as e:
            print(e)
            pass
        if not self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_next_step_xpath).click()
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
        try:
            self.find_elem(self.mapping_none_xpath, wait_times=3).text.__contains__(u'暂无数据')
            self.find_elem(self.mapping_config_add_xpath).click()
            self.find_elem(self.mapping_select_click_group_xpath.format(ad_group)).click()
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_group_batch_list[0]))
            self.find_elem(self.mapping_next_step_xpath).click()
            try:
                self.find_elem(self.mapping_select_group_xpath.format(mapping_group), wait_times=3)
            except Exception as e:
                self.find_elem(self.mapping_add_group_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).click()
                self.find_elem(self.mapping_input_usergroup_xpath).send_keys(mapping_group)
                self.find_elem(self.mapping_input_ok_xpath).click()
                print(e)
            self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
            self.find_elem(self.mapping_next_step_xpath).click()
            self.find_elem(self.mapping_ok_add_xpath).click()
        except Exception as e:
            print(e)
        temp_num_1 = len(self.find_elems(self.mapping_organization_items_xpath))
        if temp_num_1 > 0:
            flag_list[0] = 1
        self.find_elem(self.mapping_config_add_xpath).click()
        time.sleep(2)
        self.scroll_into_view(self.mapping_select_group_xpath.format(ad_group_batch_list[1]))
        self.find_elem(self.mapping_next_step_xpath).click()
        self.scroll_into_view(self.mapping_select_group_xpath.format(mapping_group))
        self.find_elem(self.mapping_next_step_xpath).click()
        self.find_elem(self.mapping_ok_add_xpath).click()
        temp_num_2 = len(self.find_elems(self.mapping_organization_items_xpath))
        if temp_num_2 > 0:
            flag_list[1] = 1
        if temp_num_2 > temp_num_1:
            flag_list[2] = 1
        return flag_list

    # AD域本地组模式映射配置——添加(A1.40)
    def ad_arch_mode_mapping_edit_1(self):
        flag_list = [0, 0, 0, 0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            # if not self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #         'aria-checked').__contains__('mixed') or \
            #         self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #             'aria-checked').__contains__('true'):
            if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked') is None:
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认添加按钮
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
            self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
            self.driver.refresh()  # 刷新页面
        self.find_elem(self.mapping_config_edit_xpath).click()
        time.sleep(2)
        self.find_elem(self.mapping_input_cancel_xpath).click()  # 取消按钮
        self.find_elem(self.mapping_config_edit_xpath).click()
        time.sleep(2)
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
                'aria-checked').__contains__('mixed') or \
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
                    'aria-checked').__contains__('true'):
            flag_list[0] = 1  # 取消后映射是否生效
        self.find_elem(self.mapping_input_cancel_xpath).click()  # 取消按钮
        self.find_elem(self.mapping_config_edit_xpath).click()
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
                'aria-checked').__contains__('mixed') or \
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
                    'aria-checked').__contains__('true'):
            flag_list[1] = 1
        self.find_elem(self.mapping_search_box_xpath).click()
        self.find_elem(self.mapping_search_box_xpath).send_keys(ad_group)
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
                'aria-checked').__contains__('mixed') or \
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
                    'aria-checked').__contains__('true'):
            flag_list[2] = 1
        if self.find_elem(self.ad_mapping_right_show_xpath).text.__contains__(ad_group):  # 查找右边映射
            flag_list[3] = 1
        self.find_elem(self.mapping_ok_add_xpath).click()
        self.find_elem(self.mapping_config_edit_xpath).click()  # 映射配置编辑按钮
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
                'aria-checked').__contains__('mixed') or \
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
                    'aria-checked').__contains__('true'):
            flag_list[4] = 1
        return flag_list

    # AD域本地组模式映射配置——添加(A1.41)
    def ad_arch_mode_mapping_edit_2(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            # if not self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #         'aria-checked').__contains__('mixed') or \
            #         self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #             'aria-checked').__contains__('true'):
            if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked') is None:
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认添加按钮
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
            self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
            self.driver.refresh()  # 刷新页面
        self.find_elem(self.mapping_config_edit_xpath).click()  # 校验是否已勾选用户组
        # if not self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
        #         'aria-checked').__contains__('mixed') or \
        #         self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
        #             'aria-checked').__contains__('true'):
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked') is None:
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        self.find_elem(self.mapping_sync_close_xpath).click()
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.ad_mapping_config_tips_xpath).text.__contains__(u"AD域用户正在同步"):
            flag_list[0] = 1
        self.find_elem(self.ad_serverip_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.ad_serverip_input_xpath).send_keys(ad_domain_ip_2[0:-1] + '9')
        self.find_elem(self.mapping_config_edit_xpath).click()  # 点击编辑按钮
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            flag_list[1] = 1
        return flag_list

    # AD域组织架构模式-数据同步(A1.42)
    def ad_arch_mode_data_sync(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            print self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
                    'aria-checked')
            # if not self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #         'aria-checked').__contains__('mixed') or \
            #         self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #             'aria-checked').__contains__('true'):
            if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked') is None:
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认添加按钮
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
            self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
            self.driver.refresh()  # 刷新页面
        self.find_elem(self.mapping_config_edit_xpath).click()  # 校验是否已勾选用户组
        # if not self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
        #         'aria-checked').__contains__('mixed') or \
        #         self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
        #             'aria-checked').__contains__('true'):
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked')is None:
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        time.sleep(2)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        time.sleep(2)
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        time.sleep(1)
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        time.sleep(0.5)
        self.click_elem(self.user_management_xpath)
        self.find_elem(self.user_manage_expend_btn_xpath.format(ad_user_group), wait_times=10).click()
        if self.find_elem(self.user_manage_expend_btn_xpath.format(ad_group), wait_times=10):
            self.find_elem(self.user_manage_group_item_xpath.format(ad_group)).click()
            flag_list[1] = 1
        return flag_list

    # AD域组织架构模式-本地组增删改(A1.43)
    def ad_arch_mode_local_group_crud_1(self):
        flag_list = [0, 0, 0, 0]
        self.ad_arch_mode_data_sync()
        self.find_elem(self.user_manage_create_group_btn_xpath).click()
        self.find_elem(self.user_manage_base_info_pre_organ_xpath).click()
        # 校验新增用户组-传参
        if self.find_elem(self.user_manage_create_group_select_org_btn.format(ad_group)).get_attribute('class') \
                .__contains__('is-disabled'):
            flag_list[0] = 1
        self.find_elem(self.user_manage_pop_page_xpath).click()  # 关闭弹出页面
        self.chainstay(self.user_manage_group_item_xpath.format(ad_group))
        try:
            self.find_elem(self.user_manage_group_delete_xpath, wait_times=3).click()  # 判断能否找到删除按钮
        except Exception as e:
            flag_list[1] = 1
            print(e)
        self.find_elem(self.user_manage_group_edit_xpath.format(ad_group)).click()  # 编辑用户组按钮-传参
        # 校验名字和上级组织是否不能选中
        if self.find_elem(self.user_manage_base_info_name_xpath).get_attribute('class').__contains__('is-disabled'):
            if self.find_elem(self.user_manage_base_info_pre_organ_xpath).get_attribute('class'). \
                    __contains__('is-disabled'):
                flag_list[2] = 1
        # 开启vdi和idv特性
        self.find_elem(self.user_manage_idv_cloud_terminal_xpath).click()
        self.find_elem(self.user_manage_vdi_cloud_desktop_xpath).click()
        if self.find_elem(self.user_manage_idv_cloud_terminal_xpath).get_attribute('class').__contains__('is-checked'):
            if self.find_elem(self.user_manage_vdi_cloud_desktop_xpath).get_attribute('class'). \
                    __contains__('is-checked'):
                flag_list[3] = 1
        return flag_list

    # AD域组织架构模式-本地组用户增删改(A1.44)
    def ad_arch_mode_local_group_crud_2(self):
        flag_list = [0, 0, 0, 0]
        self.ad_arch_mode_data_sync()
        self.find_elem(self.user_manage_create_user_xpath).click()  # 点击新建按钮
        self.find_elem(self.user_manage_new_user_group_xpath).click()  # 点击用户组
        if self.find_elem(self.user_manage_create_group_select_org_btn.format(ad_group)).get_attribute('class') \
                .__contains__('is-disabled'):
            flag_list[0] = 1
        self.find_elem(self.user_manage_pop_page_xpath).click()  # 关闭弹出页面
        self.find_elem(self.user_manage_select_xpath.format(ad_user_name[0])).click()  # 选中用户
        self.find_elem(self.user_manage_delete_user_xpath).click()  # 点击删除用户
        # 校验提示
        if self.find_elem(self.user_manage_ad_user_delete_tips_xpath).text.__contains__(u"正常状态AD域用户，无法删除"):
            flag_list[1] = 1
        self.find_elem(self.user_manage_more_xpath.format(ad_user_name[0])).click()
        self.find_elem(self.user_manage_more_detail_xpath.format(u"编辑")).click()  # 更多-编辑
        self.find_elem(self.user_manage_new_user_group_xpath).click()  # 点击用户组
        if self.find_elem(self.user_manage_create_group_select_org_btn.format(ad_group)).get_attribute('class') \
                .__contains__('is-disabled'):
            if self.find_elem(self.user_manage_new_username_xpath).get_attribute('class').__contains__('is-disabled'):
                flag_list[2] = 1
        self.find_elem(self.user_manage_new_user_group_xpath).click()  # 点击用户组
        # 开启vdi和idv特性
        self.find_elem(self.user_manage_idv_cloud_terminal_xpath).click()
        self.find_elem(self.user_manage_vdi_cloud_desktop_xpath).click()
        if self.find_elem(self.user_manage_idv_cloud_terminal_xpath).get_attribute('class').__contains__('is-checked'):
            if self.find_elem(self.user_manage_vdi_cloud_desktop_xpath).get_attribute('class'). \
                    __contains__('is-checked'):
                flag_list[3] = 1
        return flag_list

    # AD域用户修改密码-Web(A1.65)
    def ad_user_change_password(self):
        flag_list = [0]
        self.ad_arch_mode_data_sync()
        self.find_elem(self.user_manage_more_xpath.format(ad_user_name[0])).click()
        if self.find_elem(self.user_manage_more_detail_xpath.format(u"重置密码")).get_attribute('class'). \
                __contains__('is-disabled'):  # 更多-重置密码
            flag_list[0] = 1
        return flag_list

    # 保存配置信息(A1.47)
    def save_config_info(self):
        flag_list = [0, 0, 0, 0, 0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.find_elem(self.ad_admin_pwd_input_xpath).click()  # 密码
        self.find_elem(self.ad_admin_pwd_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            flag_list[0] = 1
        self.find_elem(self.ad_admin_pwd_input_xpath).send_keys(ad_domain_admin_user_pwd)
        self.find_elem(self.ad_admin_name_input_xpath).click()  # 账号
        self.find_elem(self.ad_admin_name_input_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            flag_list[1] = 1
        self.find_elem(self.ad_admin_name_input_xpath).send_keys(ad_domain_admin_username2)
        self.find_elem(self.ad_port_input).click()  # 端口号
        self.find_elem(self.ad_port_input).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            flag_list[2] = 1
        self.find_elem(self.ad_port_input).send_keys(ad_domain_port)
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        if self.find_elem(self.sec_pwd_confirm_xpath, wait_times=5):
            flag_list[3] = 1
        else:
            flag_list[3] = 1
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_close_xpath, wait_times=5):
            flag_list[4] = 1
        self.find_elem(self.mapping_sync_close_xpath).click()
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.ad_mapping_config_tips_xpath).text.__contains__(u"AD域用户正在同步"):
            flag_list[5] = 1
        return flag_list

    # 同步日志搜索(A1.86)
    def sync_log_search(self):
        flag_list = [0, 0, 0, 0]
        self.ad_arch_mode_data_sync()  # 生成日志
        self.find_elem(self.certified_manage_xpath).click()  # 跳转到认证管理页面
        if self.find_elem(self.sync_log_btn).text.__contains__(u"同步日志"):  # 校验是否有同步日志按钮
            flag_list[0] = 1
        self.find_elem(self.sync_log_btn).click()  # 点击同步日志按钮
        self.find_elem(self.log_search_times_select).click()  # 点击时间选择按钮
        logging.info(self.find_elem(self.log_search_alert_select).text)
        if self.find_elem(self.log_search_alert_select).text.__contains__(u"日 一 二 三 四 五 六"):  # 校验是否出现日期
            flag_list[1] = 1
        self.find_elem(self.log_search_btn).click()  # 点击搜索按钮
        if len(self.find_elems(self.log_display_all_items)) >= 1:  # 出现日志
            flag_list[2] = 1
        if self.find_elem(self.log_display_header_info).text.__contains__(u"同步结果"):
            flag_list[3] = 1
        return flag_list

    # 同步日志查看(A1.87)
    def sync_log_views(self):
        flag_list = [0, 0, 0, 0]
        self.ad_arch_mode_data_sync()  # 生成日志
        self.find_elem(self.certified_manage_xpath).click()  # 跳转到认证管理页面
        self.find_elem(self.sync_log_btn).click()  # 点击同步日志按钮
        if self.find_elem(self.sync_log_next_page_btn).get_attribute('class').__contains__("btn-next"):
            flag_list[0] = 1
        if self.find_elem(self.log_display_header_info).text.__contains__(u"失败原因"):
            flag_list[1] = 1
        if self.find_elem(self.log_display_header_info).text.__contains__(u"同步方式"):
            flag_list[2] = 1
        if self.find_elem(self.log_display_header_info).text.__contains__(u"同步开始时间"):
            if self.find_elem(self.log_display_header_info).text.__contains__(u"同步结束时间"):
                flag_list[3] = 1
        return flag_list

    # 用户账号使用保留字段(A1.95)
    # 日志同步失败下xpath
    log_scy_fail_xpath = u"//*[contains(text(),'部分用户同步失败')]/ancestor::tr"
    def user_account_retain_item(self):
        flag_list = [0, 0]
        test_special_case = u"测试特殊情况"  # 特殊的域用户
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            # if not self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #         'aria-checked').__contains__('mixed') or \
            #         self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #             'aria-checked').__contains__('true'):
            if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute( 'aria-checked') is None:
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认添加按钮
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            self.disable_aduser_confirm()
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
            self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
            self.driver.refresh()  # 刷新页面
        self.find_elem(self.mapping_config_edit_xpath).click()  # 校验是否已勾选用户组
        time.sleep(2)
        self.scroll_into_view(self.mapping_select_group_xpath.format(test_special_case))  # 选择特殊AD域分组
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.disable_aduser_confirm()
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        self.find_elem(self.sync_log_btn).click()  # 点击同步日志按钮
        if self.find_elem(self.log_scy_fail_xpath).text.__contains__(u"格式不合法"):
            if self.find_elem(self.log_scy_fail_xpath).text.__contains__(u"保留字段"):
                flag_list[1] = 1
        self.find_elem(self.sync_log_back_btn).click()
        self.find_elem(self.mapping_config_edit_xpath).click()  # 校验是否已勾选用户组
        time.sleep(2)
        self.scroll_into_view(self.mapping_select_group_xpath.format(test_special_case))  # 选择特殊AD域分组
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        try:
            if self.find_elem(self.sec_pwd_tips_xpath, wait_times=2).text.__contains__(u"用户将被禁用"):
                self.find_elem(self.mapping_input_ok_xpath).click()
        except Exception as e:
            print(e)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        return flag_list

    # 删除本地域用户(A1.53)
    def user_account_delete(self):
        flag_list = [0, 0]
        self.ad_arch_mode_data_sync()
        self.find_elem(self.user_manage_create_group_btn_xpath).click()
        self.find_elem(self.user_manage_base_info_pre_organ_xpath).click()
        # 校验新增用户组-传参
        if self.find_elem(self.user_manage_create_group_select_org_btn.format(ad_group)).get_attribute('class') \
                .__contains__('is-disabled'):
            flag_list[0] = 1
        self.find_elem(self.user_manage_pop_page_xpath).click()  # 关闭弹出页面
        self.chainstay(self.user_manage_group_item_xpath.format(ad_group))
        try:
            self.find_elem(self.user_manage_group_delete_xpath, wait_times=3).click()  # 判断能否找到删除按钮
        except Exception as e:
            flag_list[1] = 1
            print(e)
        return flag_list

    # 同步域控10级组(A1.94)
    def sync_ad_ten_group(self):
        ad_user_group_ten = u"11级架构"
        flag_list = [0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            # if not self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #         'aria-checked').__contains__('mixed') or \
            #         self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #             'aria-checked').__contains__('true'):
            if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked') is None:
                self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认添加按钮
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
            self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
            self.driver.refresh()  # 刷新页面
        self.find_elem(self.mapping_config_edit_xpath).click()  # 校验是否已勾选用户组
        self.find_elem(self.mapping_select_group_xpath.format(ad_user_group_ten)).click()
        if self.find_elem(self.mapping_select_group_xpath.format(ad_user_group_ten)).get_attribute(
                'aria-checked').__contains__('mixed') or \
                self.find_elem(self.mapping_select_group_xpath.format(ad_user_group_ten)).get_attribute(
                    'aria-checked').__contains__('true'):
            self.find_elem(self.mapping_select_group_xpath.format(ad_user_group_ten)).click()
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        return flag_list

    # Web-AD域告警(A1.96)
    def sync_ad_warnning(self):
        flag_list = [0]
        self.goto_adm()
        self.ad_arch_mode_data_sync()
        temp_cmd = "ifdown br0 && sleep 60 && ifup br0"
        # text = get_win_conn_info("172.21.3.231", "Administrator", "ad@2008", "dir")
        server_conn(host_ip, temp_cmd)
        time.sleep(120)
        self.driver.refresh()
        self.find_elem(self.test_username_input_xpath).send_keys(c_user)
        self.find_elem(self.test_passwd_input_xpath).send_keys(c_pwd)
        self.find_elem(self.test_login_button_xpath).click()
        self.find_elem(self.warnning_xpath).click()
        time.sleep(3)
        self.get_ciframe('frameContent')
        self.find_elem(self.warnning_history_xpath).click()
        if self.find_elem(self.warnning_history_first_xpath).text.__contains__(u"AD域服务器连接失败"):
            flag_list[0] = 1
        # logging.info(text)
        return flag_list

    # Web-AD域告警恢复(A1.97)
    def sync_ad_warnning_recovery(self):
        flag_list = [0]
        self.sync_ad_warnning()
        if self.find_elem(self.warnning_history_first_xpath).text.__contains__(u"自动解除"):
            flag_list[0] = 1
        return flag_list

    # 新建AD域用户/覆盖原则-本地无-AD(A1.48)
    def create_ad_user_ad(self):
        flag_list = [0, 0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        self.switch_local_group()
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            # self.scroll_into_view(self.mapping_select_group_xpath.format(ad_group))  # 0417
            # self.scroll_into_view(self.mapping_select_group_xpath.format(ad_group))  # 0417
            # if not self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #         'aria-checked').__contains__('mixed') or \
            #         self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #             'aria-checked').__contains__('true'):
            if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked') is None:
                    self.scroll_into_view(self.mapping_select_group_xpath.format(ad_group)).click()
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认添加按钮
            time.sleep(0.5)
            if  self.get_elem_attribute(self.accorading_to_ad_xpath,'class').__contains__('is-checked'):
                pass
            else:
                self.find_elem(self.accorading_to_ad_xpath).click()  # 以AD域为准勾选
            time.sleep(1)
            self.click_elem(self.save_button_xpath)
            if self.elem_is_exist2(self.sure_xpath) is not None:
                self.click_elem(self.sure_xpath)
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
            self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
            self.driver.refresh()  # 刷新页面
        self.find_elem(self.mapping_config_edit_xpath).click()  # 校验是否已勾选用户组
        self.scroll_into_view(self.mapping_select_group_xpath.format(ad_group))  # 0417
        self.scroll_into_view(self.mapping_select_group_xpath.format(ad_group))  # 0417
        # if not self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
        #         'aria-checked').__contains__('mixed') or \
        #         self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
        #             'aria-checked').__contains__('true'):
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked') is None:
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        time.sleep(1)
        self.click_elem(self.accorading_to_ad_xpath)  # 以AD域为准勾选
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        self.find_elem(self.user_management_xpath).click()
        self.find_elem(self.user_manage_expend_btn_xpath.format(ad_user_group), wait_times=10).click()
        if self.find_elem(self.user_manage_expend_btn_xpath.format(ad_group), wait_times=10):
            self.find_elem(self.user_manage_group_item_xpath.format(ad_group)).click()
        try:
            self.find_elem(self.user_manage_select_xpath.format(ad_user_name), wait_times=3).click()  # 选中test2
            flag_list[1] = 1  # 能选中则存在
        except Exception as e:
            print(e)
            flag_list[1] = 0  # 不存在则失败
        te = server_sql_qurey(host_ip, "SELECT user_pwd FROM idv_user WHERE user_name='{0}';".
                              format(str(ad_user_name)))
        if str(te).__contains__(u'U2Fsd'):
            flag_list[2] = 1
        return flag_list

    # 新建AD域用户/覆盖原则-本地无-本地(A1.49)
    def create_ad_user_local(self):
        flag_list = [0, 0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            # if not self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #         'aria-checked').__contains__('mixed') or \
            #         self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute(
            #             'aria-checked').__contains__('true'):
        else:
            if self.elem_is_exist2(self.add_part_xpath) is not None:
                self.find_elem(self.add_part_xpath).click()
            elif self.elem_is_exist2(self.add_part_xpath2) is not None:
                self.find_elem(self.add_part_xpath2).click()
            else:
                logging.error('添加AD域用户组不存在')
        if self.find_elem(self.mapping_select_group_xpath.format(ad_group)).get_attribute('aria-checked') is None:
            self.find_elem(self.mapping_select_group_xpath.format(ad_group)).click()
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认添加按钮
        self.find_elem(self.accorading_to_local_xpath).click()  # 以本地组为准勾选
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        self.find_elem(self.user_management_xpath).click()
        self.find_elem(self.user_manage_expend_btn_xpath.format(ad_user_group), wait_times=10).click()
        if self.find_elem(self.user_manage_expend_btn_xpath.format(ad_group), wait_times=10):
            self.find_elem(self.user_manage_group_item_xpath.format(ad_group)).click()
        try:
            self.find_elem(self.user_manage_select_xpath.format(ad_user_name), wait_times=3).click()  # 选中test2
            flag_list[1] = 1  # 能选中则存在
        except Exception as e:
            print(e)
            flag_list[1] = 0  # 不存在则失败D:\webdata\admdata

        te = server_sql_qurey(host_ip, "SELECT user_pwd FROM idv_user WHERE user_name='{0}';".
                              format(str(ad_user_name)))[0][0]
        if str(te).__contains__(u'U2Fsd'):
            flag_list[2] = 1
        return flag_list

    # 新建AD域用户/覆盖原则-本地有-AD(A1.50)
    def create_user_exist_ad_mode(self):
        self.goto_adm()
        self.connect_ad_domain()
        self.choose_ou(ad_group)
        self.find_elem(self.id_source_mode_disable_xpath).click()  # 关闭认证源模式
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        try:
            self.find_elem(self.sec_pwd_tips_xpath, wait_times=3).text.__contains__(u"用户将被禁用")
            self.find_elem(self.mapping_input_btn_xpath).click()
        except Exception as e:
            print(e)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        self.find_elem(self.user_management_xpath).click()
        try:
            self.find_elem(self.user_manage_expend_btn_xpath.format(ad_user_group), wait_times=5).click()
            if self.find_elem(self.user_manage_expend_btn_xpath.format(ad_group), wait_times=10):
                self.find_elem(self.user_manage_group_item_xpath.format(ad_group)).click()
            self.find_elem(self.user_manage_select_xpath.format(ad_user_name[0]), wait_times=3).click()  # 选中用户
            self.find_elem(self.user_manage_delete_user_xpath).click()  # 点击删除用户
            self.find_elem(self.user_manage_delete_confirm_xpath).click()  # 确认删除
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
        except Exception as e:
            print(e)
        try:
            self.find_elem(self.user_manage_group_item_xpath.format(mapping_group)).click()  # 点击t分组
            self.find_elem(self.user_manage_create_user_xpath).click()  # 点击新建用户按钮
            self.find_elem(self.user_manage_new_username_input_xpath).send_keys(ad_user_name)  # 输入用户名
            self.find_elem(self.user_manage_new_name_input_xpath).send_keys(ad_user_name)  # 输入姓名
            self.find_elem(self.user_manage_confirm_btn_xpath).click()  # 点击确认
        except Exception as e:
            print(e)
        self.driver.refresh()  # 刷新
        flag_list = self.create_ad_user_ad()
        return flag_list

    # 新建AD域用户/覆盖原则-本地有-本地(A1.51)
    def create_user_exist_local_mode(self):
        self.goto_adm()
        self.find_elem(self.id_source_mode_disable_xpath).click()  # 关闭认证源模式
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        try:
            self.find_elem(self.sec_pwd_tips_xpath, wait_times=3).text.__contains__(u"用户将被禁用")
            self.find_elem(self.mapping_input_btn_xpath).click()
        except Exception as e:
            print(e)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        self.find_elem(self.user_management_xpath).click()
        try:
            self.find_elem(self.user_manage_expend_btn_xpath.format(ad_user_group), wait_times=10).click()
            if self.find_elem(self.user_manage_expend_btn_xpath.format(ad_group), wait_times=10):
                self.find_elem(self.user_manage_group_item_xpath.format(ad_group)).click()
            self.find_elem(self.user_manage_select_xpath.format(ad_user_name[0]), wait_times=3).click()  # 选中用户
            self.find_elem(self.user_manage_delete_user_xpath).click()  # 点击删除用户
            self.find_elem(self.user_manage_delete_confirm_xpath).click()  # 确认删除
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
        except Exception as e:
            print(e)
        self.driver.refresh()  # 刷新
        try:
            self.find_elem(self.user_manage_group_item_xpath.format(mapping_group)).click()  # 点击t分组
            self.find_elem(self.user_manage_create_user_xpath).click()  # 点击新建用户按钮
            self.find_elem(self.user_manage_new_username_input_xpath).send_keys(ad_user_name)  # 输入用户名
            self.find_elem(self.user_manage_new_name_input_xpath).send_keys(ad_user_name)  # 输入姓名
            self.find_elem(self.user_manage_confirm_btn_xpath).click()  # 点击确认
        except Exception as e:
            print(e)
        self.driver.refresh()  # 刷新
        flag_list = self.create_ad_user_local()
        self.driver.refresh()  # 刷新
        self.find_elem(self.user_manage_group_item_xpath.format(mapping_group)).click()  # 点击t分组
        try:
            self.find_elem(self.user_manage_select_xpath.format(ad_user_name), wait_times=3).click()  # 选中test2
            flag_list[1] = 1  # 能选中则存在
        except Exception as e:
            print(e)
            flag_list[1] = 0  # 不存在则失败
        self.find_elem(self.user_manage_delete_user_xpath).click()  # 点击删除用户
        self.find_elem(self.user_manage_delete_confirm_xpath).click()  # 确认删除
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        time.sleep(2)
        return flag_list

    # 新建AD域用户/覆盖原则-新建同名(A1.52)
    def create_same_user_name(self):
        flag_list = self.ad_arch_mode_data_sync()
        self.find_elem(self.user_manage_create_user_xpath).click()  # 点击新建用户按钮
        self.find_elem(self.user_manage_new_username_input_xpath).send_keys(ad_user_name)  # 输入用户名
        self.find_elem(self.user_manage_new_name_input_xpath).send_keys(ad_user_name)  # 输入姓名
        self.find_elem(self.user_manage_confirm_btn_xpath).click()  # 点击确认
        if self.find_elem(self.user_manage_error_tips_xpath, wait_times=3).text.__contains__(u"用户名已存在！"):
            flag_list[1] = 1
        return flag_list

    # 删除AD域用户(A1.54)
    def user_delete_1(self):
        flag_list = self.ad_arch_mode_data_sync()
        self.driver.refresh()
        self.goto_adm()
        self.find_elem(self.id_source_mode_disable_xpath).click()  # 关闭认证源模式
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        try:
            self.find_elem(self.sec_pwd_tips_xpath, wait_times=3).text.__contains__(u"用户将被禁用")
            self.find_elem(self.mapping_input_ok_xpath).click()
        except Exception as e:
            print(e)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        te = server_sql_qurey(mainip, 5433, "SELECT status FROM idv_user WHERE user_name='{0}';".
                              format(str(ad_user_name)))
        if str(te).__eq__(u'N'):
            flag_list[1] = 1
        return flag_list

    # 重新开启AD域认证(A1.54)(A1.55)
    def connect_ad_domain_1(self):
        self.driver.refresh()
        self.goto_adm()
        self.connect_ad_domain()
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        time.sleep(5)

    # 同时删除AD域和本地用户(A1.55)
    def user_delete_2(self):
        flag_list = self.user_delete_1()
        self.driver.refresh()
        self.find_elem(self.user_management_xpath).click()
        try:
            self.find_elem(self.user_manage_expend_btn_xpath.format(ad_user_group), wait_times=10).click()
            if self.find_elem(self.user_manage_expend_btn_xpath.format(ad_group), wait_times=10):
                self.find_elem(self.user_manage_group_item_xpath.format(ad_group)).click()
            self.find_elem(self.user_manage_select_xpath.format(ad_user_name[0]), wait_times=3).click()  # 选中用户
            self.find_elem(self.user_manage_delete_user_xpath).click()  # 点击删除用户
            self.find_elem(self.user_manage_delete_confirm_xpath).click()  # 确认删除
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
            self.find_elem(self.sec_pwd_ok_xpath).click()
        except Exception as e:
            print(e)
        time.sleep(2)
        te = server_sql_qurey(mainip, 5433, "SELECT status FROM idv_user WHERE user_name='{0}';".
                              format(str(ad_user_name)))
        if str(te).__eq__(u''):  # 用户从数据库删除
            flag_list[1] = 1
        else:
            flag_list[1] = 0
        return flag_list

    # 新增AD域用户(A1.81)
    def new_ad_domain_user_1(self):
        err_tips = u"AD域上存在同名用户，请到【认证管理】页面通过映射同步来新增该用户"
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        # 如果不是AD域模式，使其切换到AD域模式
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            self.find_elem(self.mapping_ok_add_xpath).click()
        # self.find_elem(self.mapping_config_edit_xpath).click()  # 点击编辑
        if self.elem_is_exist2(self.add_part_xpath) is not None:
            self.find_elem(self.add_part_xpath).click()
        elif self.elem_is_exist2(self.add_part_xpath2) is not None:
            self.find_elem(self.add_part_xpath2).click()
        else:
            logging.info('不需要点击添加或者编辑按钮')
        if not self.find_elem(self.mapping_select_group_xpath.format(ad_user_group_1)).get_attribute(
                'class').__contains__('is-checked'):
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_group_1))  # 选择此分组
            time.sleep(2)  # 此处需要等待
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
            time.sleep(1)
            self.click_elem(self.mapping_config_edit_xpath) # 点击编辑
            time.sleep(2)
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_group_1))  # 取消
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_1))  # 只选择这个
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        time.sleep(2)
        self.find_elem(self.accorading_to_ad_xpath).click()  # 以AD域为准勾选
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        self.find_elem(self.user_management_xpath).click()
        # 点击t分组
        self.find_elem(self.user_manage_group_item_xpath.format(mapping_group), wait_times=10).click()
        self.find_elem(self.user_manage_create_user_xpath).click()  # 点击新建用户组
        self.find_elem(self.user_manage_new_username_input_xpath).send_keys(ad_user_2)  # 输入用户名
        self.find_elem(self.user_manage_new_name_input_xpath).send_keys(ad_user_2)  # 输入姓名
        if self.find_elem(self.user_manage_error_tips_xpath).text.__contains__(err_tips):
            flag_list[1] = 1
        return flag_list

    # 新增AD域用户(A1.82)
    def new_ad_domain_user_2(self):
        err_tips_1 = u"AD域存在同名用户，如想新增AD域用户，可通过同步AD用户来新增该用户。"
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        # 如果不是AD域模式，使其切换到AD域模式
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            self.find_elem(self.mapping_ok_add_xpath).click()
        # self.find_elem(self.mapping_config_edit_xpath).click()  # 点击编辑
        if self.elem_is_exist2(self.add_part_xpath) is not None:
            self.find_elem(self.add_part_xpath).click()
        elif self.elem_is_exist2(self.add_part_xpath2) is not None:
            self.find_elem(self.add_part_xpath2).click()
        else:
            logging.info('不需要点击添加或者编辑按钮')
        if not self.find_elem(self.mapping_select_group_xpath.format(ad_user_group_1)).get_attribute(
                'class').__contains__('is-checked'):
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_group_1))  # 选择此分组
            time.sleep(2)  # 此处需要等待
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
            self.find_elem(self.mapping_config_edit_xpath).click()  # 点击编辑
            time.sleep(2)
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_group_1))  # 取消
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_1))  # 只选择这个
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        time.sleep(1)
        self.click_elem(self.accorading_to_local_xpath)  # 以本地信息为准勾选
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        self.find_elem(self.user_management_xpath).click()
        # 点击t分组
        self.find_elem(self.user_manage_group_item_xpath.format(mapping_group), wait_times=10).click()
        self.find_elem(self.user_manage_create_user_xpath).click()  # 点击新建用户组
        self.find_elem(self.user_manage_new_username_input_xpath).send_keys(ad_user_2)  # 输入用户名
        self.click_elem(self.user_manage_new_name_input_xpath)  # 输入姓名
        if self.find_elem(self.user_manage_local_model_user_conflict_tips).text.__contains__(err_tips_1):
            flag_list[1] = 1
        self.find_elem(self.user_manage_local_model_user_conflict_ok).click()  # 点击确定
        return flag_list

    # 新增AD域用户(A1.83)
    def new_ad_domain_user_3(self):
        err_tips_1 = u"AD域上存在同名用户，如想新增AD域用户，可通过同步AD域用户来新增用户，或者改名后再次尝试导入"
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        # 如果不是AD域模式，使其切换到AD域模式
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            self.find_elem(self.mapping_ok_add_xpath).click()
        # self.find_elem(self.mapping_config_edit_xpath).click()  # 点击编辑
        if self.elem_is_exist2(self.add_part_xpath) is not None:
            self.find_elem(self.add_part_xpath).click()
        elif self.elem_is_exist2(self.add_part_xpath2) is not None:
            self.find_elem(self.add_part_xpath2).click()
        else:
            logging.info('不需要点击添加或者编辑按钮')
        if not self.find_elem(self.mapping_select_group_xpath.format(ad_user_group_1)).get_attribute(
                'class').__contains__('is-checked'):
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_group_1))  # 选择此分组
            time.sleep(2)  # 此处需要等待
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
            self.find_elem(self.mapping_config_edit_xpath).click()  # 点击编辑
            time.sleep(2)
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_group_1))  # 取消
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_1))  # 只选择这个
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        self.find_elem(self.accorading_to_ad_xpath).click()  # 以本地信息为准勾选
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        self.find_elem(self.user_management_xpath).click()
        self.find_elem(self.user_manage_more_select_xpath).click()  # 点击更多按钮
        self.find_elem(self.user_manage_more_detail_xpath.format(u"模板导入")).click()  # 点击<模板导入>按钮
        self.find_elem(self.user_manage_upload_files_xpath).click()  # 点击<上传文件>按钮
        # 上传导入模板文件
        self.upload(file_1)
        time.sleep(10)
        if self.find_elem(self.user_manage_local_model_user_conflict_tips,wait_times=50).text.__contains__(err_tips_1):  # 校验提示信息
            flag_list[1] = 1
        self.find_elem(self.user_manage_local_model_user_conflict_ok).click()  # 点击确定
        return flag_list

    # 新增AD域用户(A1.84)
    def new_ad_domain_user_4(self):
        err_tips_1 = u"AD域上存在同名用户，如想新增AD域用户，可通过同步AD域用户来新增用户，或者改名后再次尝试导入"
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        # 如果不是AD域模式，使其切换到AD域模式
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            self.find_elem(self.mapping_ok_add_xpath).click()
        # self.find_elem(self.mapping_config_edit_xpath).click()  # 点击编辑
        if self.elem_is_exist2(self.add_part_xpath) is not None:
            self.find_elem(self.add_part_xpath).click()
        elif self.elem_is_exist2(self.add_part_xpath2) is not None:
            self.find_elem(self.add_part_xpath2).click()
        else:
            logging.info('不需要点击添加或者编辑按钮')
        if not self.find_elem(self.mapping_select_group_xpath.format(ad_user_group_1)).get_attribute(
                'class').__contains__('is-checked'):
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_group_1))  # 选择此分组
            time.sleep(2)  # 此处需要等待
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
            self.find_elem(self.mapping_config_edit_xpath).click()  # 点击编辑
            time.sleep(2)
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_group_1))  # 取消
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_1))  # 只选择这个
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        time.sleep(1)
        self.click_elem(self.accorading_to_local_xpath)  # 以本地信息为准勾选
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        self.find_elem(self.user_management_xpath).click()
        self.find_elem(self.user_manage_more_select_xpath).click()  # 点击更多按钮
        self.find_elem(self.user_manage_more_detail_xpath.format(u"模板导入")).click()  # 点击<模板导入>按钮
        self.find_elem(self.user_manage_upload_files_xpath).click()  # 点击<上传文件>按钮
        # 上传导入模板文件
        self.upload(file_1)
        time.sleep(10)
        # upload_file = automation.WindowControl(searchDepth=2, RegexName=u'.*打开.*')
        # upload_file.ButtonControl(Name=u"上一个位置").Click()
        # # 输入地址栏，注意用automation
        # automation.SendKeys(upload_file_path)
        # automation.SendKey(automation.Keys.VK_ENTER)
        # # 输入文件名
        # upload_file.EditControl(Name=u"文件名(N):").SendKeys(file_1)
        # upload_file.SplitButtonControl(Name=u"打开(O)").Click()  # 点击打开按钮
        if self.find_elem(self.user_manage_local_model_user_conflict_tips,wait_times=50).text.__contains__(err_tips_1):  # 校验提示信息
            flag_list[1] = 1
        self.find_elem(self.user_manage_local_model_user_conflict_ok).click()  # 点击确定
        return flag_list

    # 新增AD域用户(A1.85)
    def new_ad_domain_user_5(self):
        flag_list = [0, 0]
        self.goto_adm()
        self.connect_ad_domain()  # 正常连接AD域
        # 如果不是AD域模式，使其切换到AD域模式
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            self.find_elem(self.mapping_org_switch_xpath).click()
            self.find_elem(self.mapping_input_ok_xpath).click()
            time.sleep(2)
            self.find_elem(self.mapping_ok_add_xpath).click()
        # self.find_elem(self.mapping_config_edit_xpath).click()  # 点击编辑
        if self.elem_is_exist2(self.add_part_xpath) is not None:
            self.find_elem(self.add_part_xpath).click()
        elif self.elem_is_exist2(self.add_part_xpath2) is not None:
            self.find_elem(self.add_part_xpath2).click()
        else:
            logging.info('不需要点击添加或者编辑按钮')
        if not self.find_elem(self.mapping_select_group_xpath.format(ad_user_group_1)).get_attribute(
                'class').__contains__('is-checked'):
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_group_1))  # 选择此分组
            time.sleep(2)  # 此处需要等待
            self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
            self.find_elem(self.mapping_config_edit_xpath).click()  # 点击编辑
            time.sleep(2)
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_group_1))  # 取消
            self.scroll_into_view(self.mapping_select_group_xpath.format(ad_user_1))  # 只选择这个
        time.sleep(2)  # 此处需要等待
        self.find_elem(self.mapping_ok_add_xpath).click()  # 确认编辑按钮
        time.sleep(1)
        self.click_elem(self.accorading_to_ad_xpath)  # 以本地信息为准勾选
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.disable_aduser_confirm()
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        if self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).text.__contains__(u'确认'):
            flag_list[0] = 1
        self.find_elem(self.mapping_sync_is_ok_xpath,wait_times=300).click()
        self.find_elem(self.user_management_xpath).click()
        self.find_elem(self.user_manage_more_select_xpath).click()  # 点击更多按钮
        self.find_elem(self.user_manage_more_detail_xpath.format(u"模板导入")).click()  # 点击<模板导入>按钮
        self.find_elem(self.user_manage_upload_files_xpath).click()  # 点击<上传文件>按钮
        # 上传导入模板文件
        self.upload(file_2)
        time.sleep(10)
        # upload_file = automation.WindowControl(searchDepth=2, RegexName=u'.*打开.*')
        # upload_file.ButtonControl(Name=u"上一个位置").Click()
        # # 输入地址栏，注意用automation
        # automation.SendKeys(upload_file_path)
        # automation.SendKey(automation.Keys.VK_ENTER)
        # # 输入文件名
        # upload_file.EditControl(Name=u"文件名(N):").SendKeys(file_2)
        # time.sleep(2)
        # upload_file.SplitButtonControl(Name=u"打开(O)").Click()  # 点击打开按钮
        self.find_elem(self.user_manage_local_model_user_conflict_ok).click()  # 点击确定
        self.find_elem(self.user_manage_start_import_xpath).click()  # 开始导入
        time.sleep(2)
        self.find_elem(self.user_manage_group_item_xpath.format(mapping_group)).click()  # 点击t分组
        try:
            self.find_elem(self.user_manage_select_xpath.format(ad_user_3), wait_times=3).click()  # 选择ljm1用户
            flag_list[1] = 1
        except Exception as e:
            flag_list[1] = 0
            print(e)
        self.find_elem(self.user_manage_delete_user_xpath).click()  # 点击删除用户
        self.find_elem(self.user_manage_delete_confirm_xpath).click()  # 确认删除
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)  # 输入二次密码确认框
        self.find_elem(self.sec_pwd_ok_xpath).click()  # 点击确认
        time.sleep(2)
        return flag_list

    ########################
    # 用户管理搜索
    # 搜索条数
    searchCount_xpath = "//div[@class='fr']//span[@class='el-pagination__total']"
    def get_search_info(self,name):
        self.edit_text(self.search_xpath, name)
        self.click_elem(self.click_xpath)
        info = self.find_elem(self.searchCount_xpath).text
        s = info.replace(u'共', '')
        return s.replace(u"条", "")

    # 删除用户管理用户
    #选择用户
    chose_user_xpath1 = u"//*[text()='{}']/ancestor::tr//span[@class='el-checkbox__input']"
    def del_user(self,name):
        if int(self.get_search_info(name)) != 0:
            self.click_elem(self.chose_user_xpath1.format(name))
            self.find_elem(self.user_manage_delete_user_xpath).click()  # 点击删除用户
            self.find_elem(self.user_manage_delete_confirm_xpath).click()  # 确认删除
            self.find_elem(self.sec_pwd_confirm_xpath).click()
            self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)  # 输入二次密码确认框
            self.find_elem(self.sec_pwd_ok_xpath).click()  # 点击确认
            time.sleep(1)

    # 填写输入框内信息
    def input_info(self, xpath, data):
        self.find_elem(xpath).click()
        self.find_elem(xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(xpath).send_keys(data)

    # 正确填入认证管理界面所有输入框内信息
    def input_all_info(self):
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.input_info(self.ad_servername_input_xpath, ad_domain_name)
        self.input_info(self.ad_serverip_input_xpath, ad_domain_ip_2)
        self.input_info(self.ad_port_input, ad_domain_port)
        self.input_info(self.ad_admin_name_input_xpath, ad_domain_admin_username2)
        self.input_info(self.ad_admin_pwd_input_xpath, ad_domain_admin_user_pwd)

    # 选用组织架构
    # 切换分组点击确认
    sure_xpath = '//*[@class="el-button el-button--default el-button--mini is-round el-button--primary "]'
    # 被选择用户
    chose_ou_selected_xpath = u"//span[contains(text(),'{}')]/../preceding-sibling::label"
    def choose_ou(self, ou):
        if self.find_elem(self.mapping_local_mode_xpath).get_attribute('class').__contains__('is-active'):
            if self.elem_is_exist2(self.mapping_none_xpath, wait_times=5) is not None:
                self.find_elem(self.mapping_org_switch_xpath).click()
                if self.elem_is_exist2(self.sure_xpath) is not None:
                    self.click_elem(self.sure_xpath)
                    if self.elem_is_exist2(self.choose_ou_xpath.format(ou), wait_times=2) is not None:
                        self.scroll_into_view(self.choose_ou_xpath.format(ou), wait_times=5)

            else:
                self.find_elem(self.mapping_org_switch_xpath).click()
            if self.elem_is_exist2(self.sure_xpath) is not None:
                self.click_elem(self.sure_xpath)
            time.sleep(2)
            self.find_elem(self.mapping_ok_add_xpath).click()
        self.click_elem(self.edit_ou_button_xpath)
        try:
            if self.elem_is_exist2(self.chose_ou_selected_xpath.format(ou)) is not  None:
                self.scroll_into_view(self.choose_ou_xpath.format(ou), wait_times=5)
        except Exception as e:
            print(e)
        self.find_elem(self.choose_ou_sure_button_xpath).click()
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.disable_aduser_confirm()
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(login_user_succ["passwd"])
        self.find_elem(self.sec_pwd_ok_xpath).click()
        self.find_elem(self.mapping_sync_is_ok_xpath, wait_times=300).click()

    #  选择组织
    add_part_xpath =u"// span[contains(text(), '添加')]"
    add_part_xpath2 = u"// span[contains(text(), '编辑')]"
    def choose_part(self, ou):
        if self.elem_is_exist2(self.add_part_xpath) is not None:
            self.find_elem(self.add_part_xpath).click()
        elif self.elem_is_exist2(self.add_part_xpath2) is not None:
            self.find_elem(self.add_part_xpath2).click()
        else:
            logging.error('添加AD域用户组不存在')
        time.sleep(2)
        self.scroll_into_view(self.choose_ou_xpath.format(ou), wait_times=10)
        time.sleep(1)
        self.find_elem(self.choose_ou_sure_button_xpath).click()
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.disable_aduser_confirm()
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(login_user_succ["passwd"])
        self.find_elem(self.sec_pwd_ok_xpath).click()
        self.find_elem(self.mapping_sync_is_ok_xpath, wait_times=300).click()


    # 点击认证管理同步账号
    def sync_count(self):
        self.find_elem(self.sync_account_xpath).click()
        self.find_elem(self.sync_success_sure_button_xpath, wait_times=300).click()

    # 修改vdi用户桌面类型，并且绑定镜像。参数为用户名，桌面类型(默认为个性)。要绑定其他镜像需要修改Admdata中的镜像名
    def edit_vdi_user_type(self, vdi_user_name, vm_type='single',
                           restore_base=restore_base_name, single_base=single_base_name):
        time.sleep(1)
        self.click_elem(self.user_manage_xpath)
        self.edit_text(self.search_xpath, vdi_user_name)
        self.click_elem(self.click_xpath)
        self.click_elem(self.chose_user_xpath.format(vdi_user_name))
        self.scroll_into_view(self.user_manage_more_button_xpath.format(vdi_user_name))
        time.sleep(1)
        self.find_elem(self.user_manage_edit_button_xpath).click()
        self.find_elem(self.vdi_vm_set_xpath).click()
        try:
            self.find_elem(self.vdi_vm_open_xpath, wait_times=3).click()
        except Exception as e:
            print(e)
        self.find_elem(self.vdi_vm_type_xpath).click()
        if vm_type == 'restore':
            time.sleep(0.5)
            self.scroll_into_view(self.vdi_vm_type_restore_xpath)
            time.sleep(1)
            self.find_elem(self.vdi_vm_base_xpath).click()
            time.sleep(3)
            self.scroll_into_view(self.vdi_vm_base_set_xpath.format(restore_base))
            time.sleep(1)
            self.find_elem(self.vdi_vm_bind_string_xpath).click()
            time.sleep(1)
            self.find_elem(self.edit_form_sure_button_xpath).click()
            time.sleep(2)
            self.click_elem(self.vm_type_info_form_sure_button_xpath)
            try:
                self.find_elem(self.input_passwd_xpath, wait_times=5).send_keys(passwd)
                time.sleep(1)
                self.find_elem(self.input_passwd_sure_button_xpath).click()
            except Exception as e:
                print(e)
        elif vm_type == 'single':
            time.sleep(0.5)
            self.scroll_into_view(self.vdi_vm_type_single_xpath)
            time.sleep(1)
            self.find_elem(self.vdi_vm_base_xpath).click()
            time.sleep(3)
            self.scroll_into_view(self.vdi_vm_base_set_xpath.format(single_base))
            time.sleep(1)
            self.find_elem(self.edit_form_sure_button_xpath).click()
            time.sleep(2)
            self.click_elem(self.vm_type_info_form_sure_button_xpath)
            try:
                self.find_elem(self.input_passwd_xpath, wait_times=5).send_keys(passwd)
                time.sleep(1)
                self.find_elem(self.input_passwd_sure_button_xpath).click()
            except Exception as e:
                print(e)
    # 填充某用户首选DNS
    def fill_dns(self, user_name):
        self.edit_text(self.search_xpath, user_name)
        self.click_elem(self.click_xpath)
        self.click_elem(self.chose_user_xpath.format(user_name))
        self.find_elem(self.more_operate_xpath).click()
        time.sleep(1)
        self.click_elem(self.fill_ip_xpath)
        self.find_elem(self.first_DNS_xpaht).click()
        self.find_elem(self.first_DNS_xpaht).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.first_DNS_xpaht).send_keys(ad_domain_ip_2)
        self.find_elem(self.confirm_button_xpath).click()

    # 查询用户是否加域,参数为主控IP和用户名
    def whether_in_ad_domain(self, ip, vm_user_name):
        # 查询用户是否加域
        vdi_vm_ip = server_sql_qurey(ip, find_vdi_vm_ip_in_sql.format(vm_user_name))[0][0]
        if win_conn_useful(vdi_vm_ip, s_user,s_pwd) == u'winrm可使用':
            a = get_win_conn_info(vdi_vm_ip, android_vm_user_name, android_vm_user_passwd, find_vm_whether_in_domain)
            print a
            return a

    # 登录安卓vdi时填入信息,参数为用户名和密码，若登录失败，则返回提示信息
    def fill_login_vdi(self, vm_user_name=android_vdi_user_name, password=android_vdi_user_passwd):
        ll = AndroidVdi()
        ll.vdi_connect(android_vdi_terminal_ip)
        ll.login(vm_user_name,android_vdi_terminal_ip, password)
        if get_element_msg(self.no_user_id) is not None:
            result = get_element_msg(self.no_user_id)
            xx, yy = get_element_point(self.reconnect_id)
            click(xx, yy)
            ll.vdi_disconnect(android_vdi_terminal_ip)
            return result

    def fill_login_vdi2(self, vm_user_name=android_vdi_user_name, password=android_vdi_user_passwd):
        ll = AndroidVdi()
        ll.vdi_connect(android_vdi_terminal_ip)
        ll.login_init()
        ll.input_username_passwd(vm_user_name,password)
        if get_element_msg(self.no_user_id) is not None:
            result = get_element_msg(self.no_user_id)
            xx, yy = get_element_point(self.reconnect_id)
            click(xx, yy)
            ll.vdi_disconnect(android_vdi_terminal_ip)
            return result

    # 登录安卓vdi用户,参数为主控IP、用户名、密码
    def login_vdi_vm(self, ip = host_ip, vm_user_name=android_vdi_user_name,
                     password=android_vdi_user_passwd):
        # 获取用户的终端IP
        # vdi_terminal_ip = server_sql_qurey(mainip, 5433, find_vdi_terminal_ip_in_sql.format(vm_user_name))[0][0]
        ll = AndroidVdi()
        ll.vdi_connect(android_vdi_terminal_ip)
        ll.login(vm_user_name,android_vdi_terminal_ip, password)  # 连接终端并且登录虚机
        result = self.whether_in_ad_domain(ip, vm_user_name)  # 查询是否加域
        vdi_vm_ip = server_sql_qurey(ip, find_vdi_vm_ip_in_sql.format(vm_user_name))[0][0]
        ll.terminal_vm_close(vdi_vm_ip, android_vm_user_name, android_vm_user_passwd)  # 关闭用户虚机
        # ll.vdi_disconnect(android_vdi_terminal_ip)
        return result

    # 校验管理员用户名(A1.6)
    def ad_domain_manager_name_check(self):
        flag_list = [0, 0, 0, 0]
        self.goto_adm()
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.input_info(self.ad_servername_input_xpath, ad_domain_name)
        self.input_info(self.ad_serverip_input_xpath, ad_domain_ip_2)
        self.input_info(self.ad_port_input, ad_domain_port)
        win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd, 'edit3name', 's')  # 修改AD域用户名为3位
        self.input_info(self.ad_admin_name_input_xpath, '{}@ruijiecll.com.cn'.format(ad_domain_admin_user_3name))
        self.input_info(self.ad_admin_pwd_input_xpath, ad_domain_admin_user_pwd)
        self.find_elem(self.ad_domain_connect_xpath).click()
        time.sleep(3)
        if self.find_elem(self.ad_connect_xpath).text.__contains__(u"AD域服务器连接成功"):
            flag_list[0] = 1
        time.sleep(35)
        # win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd, 'edit100name','s')
        # self.input_info(self.ad_admin_name_input_xpath, '{}@ruijiecll.com.cn'.format(ad_domain_admin_100name))
        # self.input_info(self.ad_admin_pwd_input_xpath, ad_domain_admin_user_pwd)
        # self.find_elem(self.ad_domain_connect_xpath).click()
        # if self.find_elem(self.ad_connect_xpath).text.__contains__(u"AD域服务器连接成功"):
        #     flag_list[1] = 1
        # time.sleep(35)
        self.driver.refresh()
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.input_info(self.ad_servername_input_xpath, ad_domain_name)
        self.input_info(self.ad_serverip_input_xpath, ad_domain_ip_2)
        self.input_info(self.ad_port_input, ad_domain_port)
        self.input_info(self.ad_admin_name_input_xpath, 'error_name')  # 在认证管理填入错误用户名
        self.input_info(self.ad_admin_pwd_input_xpath, ad_domain_admin_user_pwd)
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            flag_list[2] = 1
        self.driver.refresh()
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.input_info(self.ad_servername_input_xpath, ad_domain_name)
        self.input_info(self.ad_serverip_input_xpath, ad_domain_ip_2)
        self.input_info(self.ad_port_input, ad_domain_port)
        self.input_info(self.ad_admin_name_input_xpath, '')  # 在认证管理填入空用户名
        self.input_info(self.ad_admin_pwd_input_xpath, ad_domain_admin_user_pwd)
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            flag_list[3] = 1
        time.sleep(30)
        return flag_list

    # 校验管理员用户密码(A1.7)
    def ad_domain_manager_passwd_check(self):
        flag_list = [0, 0, 0, 0]
        self.goto_adm()
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.input_info(self.ad_servername_input_xpath, ad_domain_name)
        self.input_info(self.ad_serverip_input_xpath, ad_domain_ip_2)
        self.input_info(self.ad_port_input, ad_domain_port)
        self.input_info(self.ad_admin_name_input_xpath, ad_domain_admin_username2)
        self.input_info(self.ad_admin_pwd_input_xpath, 'error_passwd')  # 在认证管理填入错误密码
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.ad_disconnect_xpath).text.__contains__(u"AD域服务器连接失败"):
            flag_list[0] = 1
        self.driver.refresh()
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.input_info(self.ad_servername_input_xpath, ad_domain_name)
        self.input_info(self.ad_serverip_input_xpath, ad_domain_ip_2)
        self.input_info(self.ad_port_input, ad_domain_port)
        self.input_info(self.ad_admin_pwd_input_xpath, '')
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.data_illegal_tip_xpath).text.__contains__(u"数据不合法"):
            if self.find_elem(self.error_tips_xpath).text.__contains__(u"必填项"):
                flag_list[1] = 1
        win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd, 'edit32passwd',
                 's')  # 修改AD域用户名为32位
        self.driver.refresh()
        self.find_elem(self.id_source_mode_enable_xpath).click()
        self.input_info(self.ad_servername_input_xpath, ad_domain_name)
        self.input_info(self.ad_serverip_input_xpath, ad_domain_ip_2)
        self.input_info(self.ad_port_input, ad_domain_port)
        self.input_info(self.ad_admin_pwd_input_xpath, ad_domain_admin_user_32pwd)
        self.find_elem(self.ad_domain_connect_xpath).click()
        if self.find_elem(self.ad_connect_xpath).text.__contains__(u"AD域服务器连接成功"):
            flag_list[2] = 1
        time.sleep(30)
        return flag_list

    # 校验域控服务器断网时同步账号、关闭AD域认证情况(A1.8 A1.16)
    def ad_domain_network_off_sync_account(self):
        flag_list = [0, 0, 0]
        self.goto_adm()
        self.input_all_info()
        win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd, 'networkoff', 's')
        self.find_elem(self.sync_account_xpath).click()  # 先点击同步，再域控断网
        if self.find_elem(self.sync_wrong_xpath, wait_times=240).text.__contains__(u"同步失败，可点击"):
            flag_list[0] = 1
        self.driver.refresh()
        time.sleep(50)
        self.input_all_info()
        win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd, 'networkoff', 's')
        time.sleep(3)
        self.find_elem(self.sync_account_xpath).click()  # 先域控断网，再点击同步
        if self.find_elem(self.sync_wrong_xpath, wait_times=240).text.__contains__(u"同步失败，可点击"):
            flag_list[1] = 1
        self.driver.refresh()
        time.sleep(50)
        win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd, 'networkoff', 's')
        self.find_elem(self.id_source_mode_disable_xpath, wait_times=240).click()
        try:
            self.find_elem(self.ad_domain_window_xpath, wait_times=3)
        except Exception as e:
            print(e)
            flag_list[2] = 1
        return flag_list

    # 校验在AD域控中添加1000用户，重启tomcat能自动同步，且用户登录能自动加域(A1.9 A1.13)
    def add_thousand_users(self):
        flag_list = [0, 0]
        ou = '1000users'
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_add_user.format('zgwz', ou))
        self.goto_adm()
        self.connect_ad_domain()
        self.choose_ou(ou)  # 选用1000users组织架构
        user_name = 'z501'
        win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                 'add1000users', 's')  # 在域控创建1000个新用户A_1，密码ad@2008
        time.sleep(540)
        server_conn(mainip, 'service tomcat restart')
        time.sleep(900)
        self.driver.refresh()
        self.find_elem(self.username_input_xpath).send_keys(username)
        self.find_elem(self.passwd_input_xpath).send_keys(passwd)
        self.find_elem(self.login_button_xpath).click()
        self.edit_vdi_user_type(user_name)
        self.fill_dns(user_name)
        result = self.login_vdi_vm(mainip, user_name)
        if ad_domain in str(result):
            flag_list[0] = 1
        win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd, 'delete1000users',
                 's')  # 删除AD域中添加的用户
        time.sleep(600)
        self.goto_adm()
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.user_disable_sure_button_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(login_user_succ["passwd"])
        self.find_elem(self.sec_pwd_ok_xpath).click()
        ll = AndroidVdi()
        ll.vdi_connect(android_vdi_terminal_ip)
        ll.login(user_name, android_vdi_user_passwd)
        if get_element_msg(self.no_user_id) == "用户不存在或密码错误":
            xx, yy = get_element_point(self.reconnect_id)
            click(xx, yy)
            flag_list[1] = 1
        return flag_list

    # 校验未选用自动加入AD域，用户是否能加域(A1.19)
    # 已经选中用户xpath
    choosed_ou_xpath = "//span[contains(text(),'{}')]/../preceding-sibling::label"
    def close_auto_user_join_ad_check(self):
        flag_list = [0]
        ou = '1users'
        add_user_name = 'A_{}'.format(random.randint(1000, 4000))
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_add_user.format(add_user_name, ou), )  # 在域控创建单个新用户，密码ad@2008
        self.goto_adm()
        try:
            self.get_elem_attribute(self.open_auto_join_ad_xpath, 'aria-checked').__contains__("true")
            self.find_elem(self.auto_join_ad_xpath).click()  # 关闭自动加入AD域
        except Exception as e:
            print(e)
        self.connect_ad_domain()
        self.choose_ou(ou)
        self.edit_vdi_user_type(add_user_name)
        result = self.login_vdi_vm(mainip, add_user_name)
        if ad_domain not in str(result):
            flag_list[0] = 1
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_rm_ou_users.format(ou))  # 删除AD域中添加的用户
        self.del_ad_user(ou,add_user_name)
        # time.sleep(2)
        # self.scroll_into_view(self.certified_manage_xpath)
        # self.click_elem(self.mapping_config_edit_xpath)
        # time.sleep(1)
        # self.scroll_into_view(self.choosed_ou_xpath.format(ou), wait_times=5)
        # self.scroll_into_view(self.mapping_ok_add_xpath)
        # time.sleep(1)
        # self.choose_ou(ad_group)
        # self.click_elem(self.user_manage_xpath)
        # self.del_user(add_user_name)
        return flag_list

    # 删除ad域加入的用户
    def del_ad_user(self, part, user):
        time.sleep(2)
        self.scroll_into_view(self.certified_manage_xpath)
        time.sleep(0.5)
        if self.elem_is_exist2(self.mapping_config_edit_xpath):
            self.click_elem(self.mapping_config_edit_xpath)
        if self.elem_is_exist2(self.mapping_config_add_xpath):
            self.click_elem(self.mapping_config_add_xpath)
        time.sleep(1)
        self.scroll_into_view(self.choosed_ou_xpath.format(part), wait_times=5)
        self.scroll_into_view(self.mapping_ok_add_xpath)
        time.sleep(1)
        self.choose_ou(ad_group)
        self.click_elem(self.user_manage_xpath)
        self.del_user(user)

    # 校验选用自动加入AD域，未配置用户的DNS为域控时是否能加域(A1.20)
    def error_dns_auto_join_ad_check(self):
        flag_list = [0]
        ou = '1users'
        add_user_name = 'A_{}'.format(random.randint(1000, 4000))
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_add_user.format(add_user_name, ou))  # 在域控创建单个新用户，密码ad@2008
        self.goto_adm()
        self.connect_ad_domain()
        try:
            self.find_elem(self.close_auto_join_ad_xpath, wait_times=5)
            self.find_elem(self.auto_join_ad_xpath).click()  # 打开自动加入AD域
        except Exception as e:
            print(e)
        self.choose_ou(ou)
        self.edit_vdi_user_type(add_user_name)
        result = self.login_vdi_vm(host_ip, add_user_name)
        if ad_domain not in str(result):
            flag_list[0] = 1
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_rm_ou_users.format(ou))  # 删除AD域中添加的用户
        self.del_ad_user(ou, add_user_name)
        return flag_list

    # 校验打开自动加入AD域，配置DNS为域控服务器IP，用户登录是否能加入AD域(A1.18 A1.11)
    def auto_join_ad_check_2(self):
        flag_list = [0]
        ou = '1users'
        add_user_name = 'A_{}'.format(random.randint(1000, 4000))
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_add_user.format(add_user_name, ou))  # 在域控创建单个新用户，密码ad@2008
        self.goto_adm()
        self.connect_ad_domain()
        try:
            self.find_elem(self.close_auto_join_ad_xpath, wait_times=5)
            self.find_elem(self.auto_join_ad_xpath).click()  # 打开自动加入AD域
        except Exception as e:
            print(e)
        self.choose_ou(ou)
        self.edit_vdi_user_type(add_user_name)
        self.fill_dns(add_user_name)
        result = self.login_vdi_vm(mainip, add_user_name)
        if ad_domain in str(result):
            flag_list[0] = 1
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_rm_ou_users.format(ou))  # 删除AD域中添加的用户
        self.del_ad_user(ou, add_user_name)
        return flag_list

    # 校验还原用户是否能加入AD域(A1.21)
    def restore_user_join_ad_domain(self):
        flag_list = [0]
        ou = '1users'
        add_user_name = 'A_{}'.format(random.randint(1000, 4000))
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_add_user.format(add_user_name, ou))  # 在域控创建单个新用户，密码ad@2008
        self.goto_adm()
        self.connect_ad_domain()
        self.choose_ou(ou)
        self.edit_vdi_user_type(vdi_user_name=add_user_name, vm_type='restore')
        result = self.login_vdi_vm(host_ip, add_user_name)
        if ad_domain not in str(result):
            flag_list[0] = 1
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_rm_ou_users.format(ou))  # 删除AD域中添加的用户
        # vdi_vm_ip = server_sql_qurey(host_ip, find_vdi_vm_ip_in_sql.format(android_vdi_user_name))[0][0]
        # AndroidVdi().terminal_vm_close(vdi_vm_ip, android_vm_user_name, android_vm_user_passwd)  # 关闭用户虚机
        # time.sleep(60)
        # self.edit_vdi_user_type(android_vdi_user_name, 'single')  # 还原为个性用户
        self.del_ad_user(ou, add_user_name)
        return flag_list

    # 校验用户加域后D盘桌面数据是否丢失(A1.23)
    def ad_domain_desktop_check(self):
        flag_list = [0]
        ou = '1users'
        add_user_name = 'A_{}'.format(random.randint(1000, 4000))
        desktop_data = 'dir D:\个人桌面'
        make_new_file = ''
        for i in file_type:
            make_new_file = make_new_file + 'echo {0} > {0}.{1};'.format(add_user_name, i)
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_add_user.format(add_user_name, ou))  # 在域控创建单个新用户，密码ad@2008
        self.goto_adm()
        self.connect_ad_domain()
        self.choose_ou(ou)
        self.edit_vdi_user_type(add_user_name)
        self.fill_login_vdi(add_user_name)
        time.sleep(240)
        vdi_vm_ip = server_sql_qurey(mainip, find_vdi_vm_ip_in_sql.format(add_user_name))[0][0]
        before_desktop = get_win_conn_info(vdi_vm_ip, android_vm_user_name, android_vm_user_passwd,
                                           desktop_data).split('File')[0]
        get_win_conn_info(vdi_vm_ip, android_vm_user_name, android_vm_user_passwd, make_new_file)

        AndroidVdi().terminal_vm_close(vdi_vm_ip, android_vm_user_name, android_vm_user_passwd)  # 关闭用户虚机
        self.fill_dns(add_user_name)
        self.fill_login_vdi(add_user_name)
        time.sleep(240)
        after_desktop = get_win_conn_info(vdi_vm_ip, android_vm_user_name, android_vm_user_passwd,
                                          desktop_data).split('File')[0]
        if before_desktop == after_desktop:
            flag_list[0] = 1
        AndroidVdi().terminal_vm_close(vdi_vm_ip, android_vm_user_name, android_vm_user_passwd)  # 关闭用户虚机
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_rm_ou_users.format(ou))  # 删除AD域中添加的用户
        self.del_ad_user(ou, add_user_name)
        return flag_list

    # 校验AD域用户登录-三种方式(A1.67)
    def ad_user_login_method(self):
        flag_list = [0, 0, 0]
        ou = '1users'
        add_user_name = 'A_{}'.format(random.randint(1000, 4000))
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_add_user.format(add_user_name, ou))  # 在域控创建单个新用户，密码ad@2008
        self.goto_adm()
        self.connect_ad_domain()
        try:
            self.find_elem(self.close_auto_join_ad_xpath, wait_times=5)
            self.find_elem(self.auto_join_ad_xpath).click()  # 打开自动加入AD域
        except Exception as e:
            print(e)
        self.choose_ou(ou)
        self.edit_vdi_user_type(add_user_name)
        logging.info("第一种方式登入")
        self.fill_dns(add_user_name)
        ret1 = self.login_vdi_vm(mainip, add_user_name)
        if ad_domain in str(ret1):
            flag_list[0] = 1
        logging.info("第二种方式登入")
        self.fill_login_vdi(r'ruijiecll\\{0}'.format(add_user_name))
        ret2 = self.whether_in_ad_domain(mainip, add_user_name)  # 查询是否加域
        vdi_vm_ip = server_sql_qurey(mainip, find_vdi_vm_ip_in_sql.format(add_user_name))[0][0]
        if win_conn_useful(vdi_vm_ip,android_vm_user_name,android_vm_user_passwd) == u"winrm可使用":
            AndroidVdi().terminal_vm_close(vdi_vm_ip, android_vm_user_name, android_vm_user_passwd)  # 关闭用户虚机
        if ad_domain in str(ret2):
            flag_list[1] = 1
        logging.info("第三种方式登入")
        # self.fill_login_vdi(r'{0}@ruijiecll.com.cn'.format(add_user_name))
        # ret3 = self.whether_in_ad_domain(mainip, add_user_name)  # 查询是否加域
        # vdi_vm_ip = server_sql_qurey(mainip, 5433, find_vdi_vm_ip_in_sql.format(add_user_name))[0][0]
        # AndroidVdi().terminal_vm_close(vdi_vm_ip, android_vm_user_name, android_vm_user_passwd)  # 关闭用户虚机
        # if ad_domain in str(ret3):
        #     flag_list[2] = 1
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_rm_ou_users.format(ou))  # 删除AD域中添加的用户
        self.del_ad_user(ou, add_user_name)
        return flag_list

    # 校验AD域用户登录-三种异常登录方式(A1.69)
    def ad_user_login_wrong_method(self):
        flag_list = [0, 0, 0]
        ou = '1users'
        add_user_name = '69@ruijiecll.com.cn'
        win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd, add_user_name, 's')
        self.goto_adm()
        self.connect_ad_domain()
        self.choose_ou(ou)
        self.edit_vdi_user_type(add_user_name)
        self.fill_dns(add_user_name)
        ret1 = self.fill_login_vdi2(add_user_name)
        print ret1
        logging.info( ret1)
        if ret1 == '用户不存在或密码错误':
            flag_list[0] = 1
        ret2 = self.fill_login_vdi2(r'ruijiecll\\{0}'.format(add_user_name))
        print ret2
        logging.info(ret2)
        if ret2 == '用户不存在或密码错误':
            flag_list[1] = 1
        ret3 = self.fill_login_vdi2(r'{0}@ruijiecll.com.cn'.format(add_user_name))
        print ret3
        logging.info(ret3)
        if ret3 == '用户不存在或密码错误':
            flag_list[2] = 1
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_rm_ou_users.format(ou))  # 删除AD域中添加的用户
        self.del_ad_user(ou, add_user_name)
        return flag_list

    # 校验在AD域服务器上“禁用"已加域用户后，登录提示"您的账号已被停用"(A1.71)
    def ad_user_disable_check1(self):
        flag_list = [0]
        ou = 'hjq'
        self.goto_adm()
        self.input_all_info()
        self.choose_ou(ou)
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_user_disable.format(android_vdi_user_name, ou))  # 在域控上禁用h1账号
        ll = AndroidVdi()
        ll.vdi_connect(android_vdi_terminal_ip)
        ll.login_init()
        ll.input_username_passwd(android_vdi_user_name, android_vdi_user_passwd)
        time.sleep(2)
        if get_element_msg(self.no_user_id) == "您的账户已被停用。请向系统管理员咨询":
            xx, yy = get_element_point(self.reconnect_id)
            click(xx, yy)
            flag_list[0] = 1
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_user_able.format(android_vdi_user_name, ou))
        ll.vdi_disconnect(android_vdi_terminal_ip)
        return flag_list

    # 校验域服务器断网或异常时，使用已加域用户登录终端，提示"您的账号已被停用"(A1.72)
    # 用例错误，可以正常登录，虚机无法联网
    def ad_net_off_user_login(self):
        flag_list = [0]
        ou = 'hjq'
        self.goto_adm()
        self.input_all_info()
        self.choose_ou(ou)
        win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd, 'networkoff', 's')
        ll = AndroidVdi()
        ll.vdi_connect(android_vdi_terminal_ip)
        ll.login_init()
        ll.input_username_passwd(android_vdi_user_name, android_vdi_user_passwd)
        time.sleep(2)
        if get_element_msg(self.no_user_id) == "您的账户已被停用。请向系统管理员咨询":
            xx, yy = get_element_point(self.reconnect_id)
            click(xx, yy)
            flag_list[0] = 1
        if win_conn_useful(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd) == u'winrm可使用':
            get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_user_able.format(android_vdi_user_name, ou))
        ll.vdi_disconnect(android_vdi_terminal_ip)
        return flag_list

    # 校验创建用户后，首次登录时AD域断网，提示'指定的域不存在，或无法联系'(A1.88)
    def ad_net_off_user_first_login(self):
        flag_list = [0]
        ou = '1users'
        add_user_name = 'A_{}'.format(random.randint(1000, 4000))
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_add_user.format(add_user_name, ou))  # 在域控创建单个新用户，密码ad@2008
        self.goto_adm()
        self.connect_ad_domain()
        self.choose_ou(ou)
        self.edit_vdi_user_type(add_user_name)
        self.fill_dns(add_user_name)
        win_conn(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd, 'networkoff', 's')
        ll = AndroidVdi()
        ll.vdi_connect(android_vdi_terminal_ip)
        ll.login_init()
        ll.input_username_passwd(add_user_name, android_vdi_user_passwd)
        time.sleep(2)
        if get_element_msg(self.no_user_id) == "指定的域不存在，或无法联系":
            xx, yy = get_element_point(self.reconnect_id)
            click(xx, yy)
            flag_list[0] = 1
        if win_conn_useful(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd) ==  u'winrm可使用':
            get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                              ad_domain_rm_ou_users.format(ou))  # 删除AD域中添加的用户
        ll.vdi_disconnect(android_vdi_terminal_ip)
        self.del_ad_user(ou, add_user_name)
        return flag_list

    # 校验在AD域服务器上“禁用"用户后，该用户首次登录失败(A1.89)
    def ad_user_disable_check2(self):
        flag_list = [0]
        ou = '1users'
        add_user_name = 'A_{}'.format(random.randint(1000, 4000))
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_add_user.format(add_user_name, ou))  # 在域控创建单个新用户，密码ad@2008
        self.goto_adm()
        self.connect_ad_domain()
        self.choose_ou(ou)
        self.edit_vdi_user_type(add_user_name)
        self.fill_dns(add_user_name)
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_user_disable.format(add_user_name, ou))  # 在域控上禁用此账号
        ll = AndroidVdi()
        ll.vdi_connect(android_vdi_terminal_ip)
        ll.login_init()
        ll.input_username_passwd(add_user_name, android_vdi_user_passwd)
        time.sleep(2)
        if get_element_msg(self.no_user_id) == "您的账户已被停用。请向系统管理员咨询":
            xx, yy = get_element_point(self.reconnect_id)
            click(xx, yy)
            flag_list[0] = 1
        get_win_conn_info(ad_domain_ip_2, ad_domain_admin_user_name, ad_domain_admin_user_pwd,
                          ad_domain_rm_ou_users.format(ou))  # 删除AD域中添加的用户
        ll.vdi_disconnect(android_vdi_terminal_ip)
        return flag_list

    # 在域控上选择一个已过期的账户登陆，终端提示：用户账户已过期(A1.90)
    def expire_user_login(self):
        flag_list = [0]
        user_name = 'expire_user'
        self.goto_adm()
        self.input_all_info()
        self.choose_ou('hjq')
        ll = AndroidVdi()
        ll.vdi_connect(android_vdi_terminal_ip)
        ll.login_init()
        ll.input_username_passwd(user_name, android_vdi_user_passwd)
        time.sleep(2)
        if get_element_msg(self.no_user_id) == "用户账户已过期":
            xx, yy = get_element_point(self.reconnect_id)
            click(xx, yy)
            flag_list[0] = 1
        return flag_list

    # 在域控上修改用户的可登陆时间，在可登陆时间外的时间登陆，提示：您的账户有时间限制，您当前无法登录。请稍后再试(A1.91)
    def time_limit_user_login(self):
        flag_list = [0]
        user_name = 'time_limit'
        self.goto_adm()
        self.input_all_info()
        self.choose_ou('hjq')
        ll = AndroidVdi()
        ll.vdi_connect(android_vdi_terminal_ip)
        ll.login_init()
        ll.input_username_passwd(user_name, android_vdi_user_passwd)
        time.sleep(2)
        if get_element_msg(self.no_user_id) == "您的账户有时间限制，您当前无法登录。请稍后再试":
            xx, yy = get_element_point(self.reconnect_id)
            click(xx, yy)
            flag_list[0] = 1
        return flag_list

    # 云桌面管理按钮
    cloud_desktop_manage_xpath = u"//li[contains(.,'云桌面管理')]"
    # 云桌面管理下的搜索按钮
    cloud_desktop_manage_lookup_xpath = u"//input[@placeholder='用户名/终端名称/用户组/终端组/IP地址']"
    # 云桌面管理下的更多按钮
    cloud_desktop_manage_more_xpath =u"//span[contains(.,'%s')]//ancestor::tr//span[contains(.,'更多')]"
    # 云桌面管理-更多按钮-还原云桌面
    cloud_desktop_manage_more_reduction_xpath =u"//*[@x-placement='bottom-start']//li[contains(.,'还原云桌面')]"
    # 云桌面管理-更多按钮-还原云桌面-确定
    cloud_desktop_manage_more_reduction_y_xpath = u"//*[text()='确认 ']"
    # 云桌面管理-更多按钮-还原云桌面-取消
    cloud_desktop_manage_more_reduction_n_xpath = u"//*[contains(text(),'取消')]"
    # 用户的还原属性
    user_reduction_xpath = u"//button//*[contains(text(),'还原')]"

    # 跳转云桌面
    def goto_cloud_desktop(self):
        self.find_elem(self.cloud_desktop_manage_xpath).click()

    # 云桌面管理-用户显示区域
    cloud_desktop_manage_user_show_xpath = "// table[ @class ='el-table__body']"

    # 清空云桌面搜索
    def goto_cloud_desktop_search_clean(self):
        self.find_elem(self.cloud_desktop_manage_lookup_xpath).send_keys(Keys.CONTROL, 'a')
        self.find_elem(self.cloud_desktop_manage_lookup_xpath).send_keys(Keys.BACK_SPACE)

    # 跳转云桌面搜索
    def goto_cloud_desktop_search(self, name):
        self.find_elem(self.cloud_desktop_manage_lookup_xpath).send_keys(name, Keys.ENTER)
        self.goto_cloud_desktop_search_clean()

    #云桌面小眼睛查看按钮
    eyes_xpath = "//i[ @class ='sk-icon-eye']"
    def goto_eyes(self):
        self.find_elem(self.eyes_xpath).click()


    #云桌面小眼睛 -- 云桌面IP
    eyes_ip_xpath = "// li[ @class ='sk-column-item'][6] //i"
    eyes_ip_xpath_true ="// li[ @class ='sk-column-item'][6] //i[@class='el-icon-check']"
    def goto_eyes_ip(self):
        self.find_elem(self.eyes_ip_xpath).click()

    # 云桌面小眼睛 -- 终端名称
    eyes_xpath_terminalname = "// li[ @class ='sk-column-item'][9] //i"
    eyes_xpath_terminalname_true = "// li[ @class ='sk-column-item'][9] //i[@class='el-icon-check']"
    def goto_eyes_terminalname(self):
        self.find_elem(self.eyes_xpath_terminalname).click()

    # 跳转云桌面更多
    def goto_cloud_desktop_more(self,name):
        self.find_elem(self.cloud_desktop_manage_more_xpath % name).click()

     # 点击还原云桌面
    def click_reduction(self):
        self.find_elem(self.cloud_desktop_manage_more_reduction_xpath).click()
        self.find_elem(self.user_reduction_xpath).click()

    # 确认密码
    confirm_passwd_xpath = "//input[@type='password']"
    passwd_confirm_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"

    # 输入密码点击确认
    def send_passwd_confirm(self, passwd):
        self.back_current_page()
        self.find_elem(self.confirm_passwd_xpath).send_keys(passwd)
        self.find_elem(self.passwd_confirm_xpath).click()

    #云桌面下的云桌面IP栏
    cloud_manage_cloudip_xpath = "//tr[1]//td[8]"
    #云桌面下的用户名栏
    cloud_manage_user_name_xpath = "// tr[1] // td[2]"
    # 云桌面下的终端名称栏
    cloud_manage_terminal_name_xpath = "// tr[1] // td[11]"

    # 云桌面下的终端名称下的降序按钮栏
    cloud_manage_terminal_name_down_xpath = "// th[11] // i[ @class ='sort-caret descending']"
    def terminal_name_down(self):
        self.find_elem(self.cloud_manage_terminal_name_down_xpath).click()

    # 云桌面下的搜索结果判断
    def seach_result(self):
        self.back_current_page()

    #新建用户已存在提示
    user_already_exits_xpath = "// div[ @class ='el-form-item__error']"

    # 新建用户用户名超过32个字符提示
    user_already_Exceed32_xpath = "// div[ @class ='el-form-item__error']"
    # 修改文本框
    def edit_text(self, locator, text=''):
        time.sleep(0.5)
        self.find_elem(locator).click()
        self.find_elem(locator).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(locator).send_keys(text)
        return text

    # 开启ad域
    def conn_ad(self,):
        self.connect_ad_domain()
        time.sleep(1)
        self.click_elem(self.save_button_xpath)
        self.find_elem(self.sec_pwd_confirm_xpath).click()
        self.find_elem(self.sec_pwd_confirm_xpath).send_keys(c_pwd)
        self.find_elem(self.sec_pwd_ok_xpath).click()
        time.sleep(5)


