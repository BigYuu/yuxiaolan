#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll / zhouxihong
@contact: chengll@ruijie.com / zhouxihong@ruijie.com.cn
@software: PyCharm / Pycharm
@time: 2018/8/24 9:13 / 2018/10/9
"""
from decimal import Decimal
from Common.DutGetShow import DutGetShow
from Common.serverconn import *
import re
from LoginPage import *
from Common import Mylog


class IndexPage(BasicFun):
    #     元素定位
    # 导航栏信息
    # 首页
    index_xpath = "//*[@class='fa fa-dashboard']/parent::li"
    # 告警按钮
    warning_button_xpath = "//*[@class='sk-icon sk-icon-alert']/parent::a"
    # 登入用户信息
    user_info_xpath = "//*[@class='el-menu-item is-not-action']/span"
    # 查看按钮
    check_button_xpath = u"//button/span[contains(text(),'查看')]"
    # 健康查看页面xpath定位
    # iframe窗口id
    iframeid = "serverDetailPanel"
    # ip地址获取定位
    ip_dress_xpath = "//*[@class='ip']"
    # 查看页面的使用率定位
    cpu_used_xpath = u"//*[@class='ip'and contains(text(),'{0}')]/ancestor::tr//div[@class='cpu']"
    # 内存利用率定位
    men_use_xpath = u"//*[@class='ip'and contains(text(),'{0}')]/ancestor::tr//div[@class='mem']"
    # 云桌面数量定位
    vdi_num_xpath = u"//*[@class='ip'and contains(text(),'{}')]/ancestor::tr//div[@class='mem']/ancestor::td/following-sibling::td[1]/div"
    # 状态定位
    status_xpath = u"//*[@class='ip'and contains(text(),'{}')]/ancestor::tr//div[@class='mem']/ancestor::td/following-sibling::td[2]/label"
    # 维护按钮定位
    fix_button_xpath = u"//*[@class='ip'and contains(text(),'{}')]/ancestor::tr//div[@class='mem']/ancestor::td/following-sibling::td[3]/div//a[text()='维护']"
    # 维护信息提示
    fix_info_xpath = "//*[@class='layui-layer-content layui-layer-padding']"
    # 维护确定关闭虚机成功提示
    close_virsh_info_xpath = "//*[@class='layui-layer-content layui-layer-padding']"
    # 关机按钮定位
    shutdown_button_xpath = u"//*[@class='ip'and contains(text(),'{}')]/ancestor::tr//div[@class='mem']/ancestor::td/following-sibling::td[3]/div//a[text()='关机']"
    # 重启按钮定位
    reboot_button_xpath = u"//*[@class='ip'and contains(text(),'{}')]/ancestor::tr//div[@class='mem']/ancestor::td/following-sibling::td[3]/div//a[text()='重启']"
    # 维护、关机、重启确定按钮
    confirm_button_xpath = "//*[@class='layui-layer-btn0']"
    # 维护、关机、重启取消按钮
    cancel_button_xpath = "//*[@class='layui-layer-btn1']"
    # 密码输入和确认框
    confirm_passwd_xpath = "//input[@type='password']"
    passwd_confirm_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"
    # 输入错误密码提示
    errot_passwd_info_xpath = "//*[@class='el-message__content']"
    # 密码确认取消
    passwd_cancle_xpath = "//*[@class='el-button el-button--default el-button--mini is-round']"
    # 关机、重启正确提示信息
    reboot_info_xpath = "//*[@class='layui-layer-content layui-layer-padding']"
    confirm_reboot_info_xpath = "//*[@class='messageServrity infoSeverityStyle']/label"
    reboot_confirm_button_xpath = "//*[@class='button']"
    # 关机重启提示页面iframe
    success_confirm_iframe_id = "messageDialog"
    # 关闭查看页面
    close_checkifeame_xpath = "//*[@class='close']"
    # 首页元素定位
    # 首页vdi云桌面数量显示
    vdi_numcount_xpath = u"//*[contains(text(),'云桌面VDI')]"
    # vdi运行中虚机数量
    vdi_running_num_xpath = u"//*[contains(text(),'云桌面VDI')]/parent::div//div[contains(text(),'运行中')]/preceding-sibling::div"
    # vdi休眠中虚机数量
    vdi_sleep_num_xpath = u"//*[contains(text(),'云桌面VDI')]/parent::div//div[contains(text(),'休眠')]/preceding-sibling::div"
    # vdi分组虚机数量显示（输入用户组名为参数）
    vdi_group_num_xpath = u"//*[contains(text(),'云桌面VDI')]/parent::div/following-sibling::div//div[text()='{}']/parent::td/following-sibling::td//span[@class='sk-link--normal']"
    # 获取vdi用户列表
    vdi_user_grouplist_xpath = u"//*[contains(text(),'云桌面VDI')]/parent::div/following-sibling::div//*[@class='cell el-tooltip showTooltip']"
    # vdi分组名称（输入用户组名为参数）
    vdi_group_name_xpath = u"//*[contains(text(),'云桌面VDI')]/parent::div/following-sibling::div//div[@class='cell el-tooltip showTooltip' and text()='{}']"
    # 云桌面vdi复选框
    vdi_checkbox_xpath = u"//*[contains(text(),'云桌面VDI')]/parent::div/following-sibling::div//div[contains(text(),'{}')]/parent::td/preceding-sibling::td//span[@class='el-checkbox__inner']"
    # vdi 分组全选按钮
    vdi_checkall_xpath = u"//*[contains(text(),'云桌面VDI')]/parent::div/following-sibling::div//div[text()='分组']/parent::th/preceding-sibling::th//span[@class='el-checkbox__inner']"
    # vdi批量关机
    vdi_close_button_xpath = u"//*[contains(text(),'云桌面VDI')]/parent::div/following-sibling::div[@class='sk-dashboard-terminal__footer']//button"
    # idv数量显示
    idv_numcount_xpath = u"//*[contains(text(),'胖终端IDV')]"
    # idv运行中虚机数量
    idv_running_num_xpath = u"//*[contains(text(),'胖终端IDV')]/parent::div//div[contains(text(),'运行中')]/preceding-sibling::div"
    # idv休眠中虚机数量
    idv_sleep_num_xpath = u"//*[contains(text(),'胖终端IDV')]/parent::div//div[contains(text(),'离线')]/preceding-sibling::div"
    # idv分组虚机数量显示（输入用户组名为参数）
    idv_group_num_xpath = u"//*[contains(text(),'胖终端IDV')]/parent::div/following-sibling::div//div[text()='{}']/parent::td/following-sibling::td//span[@class='sk-link--normal']"
    # 获取idv用户列表
    idv_user_grouplist_xpath = u"//*[contains(text(),'胖终端IDV')]/parent::div/following-sibling::div//*[@class='cell el-tooltip showTooltip']"
    # idv分组名称（输入用户组名为参数）
    idv_group_name_xpath = u"//*[contains(text(),'胖终端IDV')]/parent::div/following-sibling::div//div[@class='cell el-tooltip showTooltip'and text()='{}']"
    # idv胖终端复选框
    idv_checkbox_xpath = u"//*[contains(text(),'胖终端IDV')]/parent::div/following-sibling::div//div[contains(text(),'{}')]/parent::td/preceding-sibling::td//span[@class='el-checkbox__input']"
    # idv 分组全选按钮
    idv_checkall_xpath = u"//*[contains(text(),'胖终端IDV')]/parent::div/following-sibling::div//div[text()='分组']/parent::th/preceding-sibling::th//span[@class='el-checkbox__inner']"
    # idv批量关机
    idv_close_button_xpath = u"//*[contains(text(),'胖终端IDV')]/parent::div/following-sibling::div[@class='sk-dashboard-terminal__footer']//button"
    # 批量关闭虚机消息提示
    close_success_info_xpath = "//*[@class='el-message el-message--success']//p[@class='el-message__content']"
    # 告警气泡
    warming_xpath = "//*[contains(@class,'el-badge__content')]"
    # 告警信息
    warming_infoip_xpath = "//*[@class='el-alert__title is-bold']"
    warming_info_xpath = "//*[@class='el-alert__description']"
    # 关闭告警
    close_warning_xpath = "//*[@class='el-alert__closebtn el-icon-close']"

    '''by zhouxihong'''
    # 首页告警
    index_warning_xpath = u"//a[contains(.,'告警')]"
    # 初始化配置向导
    init_config_xpath = u"//a[contains(.,'初始化配置向导')]"
    # 在线客服
    online_service_xpath = u"//a[contains(.,'在线客服')]"
    # 注销
    logout_xpath = "//i[@class='sk-icon sk-icon-logout']"
    # 关于
    index_about_xpath = u"//li[contains(.,'关于')]"
    # 首页关于详情
    index_about_details_xpath = "//div[@class='el-col el-col-18']"
    # 关于页面二维码
    index_about_qrcode_xpath = "//img[@class='sk-about__card']"
    # 首页导航栏
    index_web_navigation_bar_xpath = "//span[contains(@class,'el-breadcrumb__item')]/.."

    # 查看按钮
    view_information_xpath = u"//button[contains(.,'查看')]"

    ## iframe窗口 ##
    ## 定位如下信息时，需要跳转到 http://服务器ip/index/panels/serverDetail.jsf (需要首页登录后访问)
    # 服务器ip
    use_server_xpath = "//a[@id='server_0']"  # 如果是多台服务器信息，修改 server_后面数字即可(012)
    use_server1_xpath = "//a[@id='server_1']"  # 如果是多台服务器信息，修改 server_后面数字即可(012)
    use_server2_xpath = "//a[@id='server_2']"  # 如果是多台服务器信息，修改 server_后面数字即可(012)
    # cpu占用
    use_cpu_xpath = ".//*[@id='cpu_0']"  # 如果是多台服务器信息，修改 cpu_后面数字即可(012)
    use_cpu1_xpath = ".//*[@id='cpu_1']"  # 如果是多台服务器信息，修改 cpu_后面数字即可(012)
    use_cpu2_xpath = ".//*[@id='cpu_2']"  # 如果是多台服务器信息，修改 cpu_后面数字即可(012)
    # mem占用
    use_mem_xpath = ".//*[@id='mem_0']"  # 返回的数值需处理！, 若多台，修改mem_后数字即可(012)
    use_mem1_xpath = ".//*[@id='mem_1']"  # 返回的数值需处理！, 若多台，修改mem_后数字即可(012)
    use_mem2_xpath = ".//*[@id='mem_2']"  # 返回的数值需处理!, 若多台，修改mem_后数字即可(012)
    # vdi个数
    use_vdi_xpath = ".//*[@id='serverDetailTable']/tbody/tr[1]/td[3]/div"  # 多台，修改 tr[1]其中的数字(012)
    use_vdi1_xpath = ".//*[@id='serverDetailTable']/tbody/tr[2]/td[3]/div"  # 多台，修改 tr[1]其中的数字(012)
    use_vdi2_xpath = ".//*[@id='serverDetailTable']/tbody/tr[3]/td[3]/div"  # 多台，修改 tr[1]其中的数字(012)
    # 服务器状态
    use_server_status_xpath = ".//*[@id='serverDetailTable']/tbody/tr[1]/td[4]/label"  # 多台,修改 tr[1]中的数字(012)
    use_server1_status_xpath = ".//*[@id='serverDetailTable']/tbody/tr[2]/td[4]/label"  # 多台,修改 tr[1]中的数字(012)
    use_server2_status_xpath = ".//*[@id='serverDetailTable']/tbody/tr[3]/td[4]/label"  # 多台,修改 tr[1]中的数字(012)
    # 关机操作
    use_poweroff_xpath = ".//*[@id='serverDetailTable']/tbody/tr[1]/td[5]/div/a[3]"  # 多台，修改tr[1]中数字(012)
    use_poweroff1_xpath = ".//*[@id='serverDetailTable']/tbody/tr[2]/td[5]/div/a[3]"  # 多台，修改tr[1]中数字(012)
    use_poweroff2_xpath = ".//*[@id='serverDetailTable']/tbody/tr[3]/td[5]/div/a[3]"  # 多台，修改tr[1]中数字(012)
    # 重启操作
    use_reboot_xpath = ".//*[@id='serverDetailTable']/tbody/tr[1]/td[5]/div/a[2]"  # 多台，修改tr[1]中的数字(012)
    use_reboot1_xpath = ".//*[@id='serverDetailTable']/tbody/tr[2]/td[5]/div/a[2]"  # 多台，修改tr[1]中的数字(012)
    use_reboot2_xpath = ".//*[@id='serverDetailTable']/tbody/tr[3]/td[5]/div/a[2]"  # 多台，修改tr[1]中的数字(012)
    # 维护操作
    use_maintain_xpath = ".//*[@id='serverDetailTable']/tbody/tr[1]/td[5]/div/a[1]"  # 多台，修改tr[1]中的数字(012)
    use_maintain1_xpath = ".//*[@id='serverDetailTable']/tbody/tr[2]/td[5]/div/a[1]"  # 多台，修改tr[1]中的数字(012)
    use_maintain2_xpath = ".//*[@id='serverDetailTable']/tbody/tr[3]/td[5]/div/a[1]"  # 多台，修改tr[1]中的数字(012)
    ## 确定按钮
    use_ok_button_xpath = "//*[contains(@id,'layui-layer')]/div[3]/a[1]"
    ## 取消按钮
    use_cancel_button_xpath = "//*[contains(@id,'layui-layer')]/div[3]/a[2]"

    # 关闭失败<返回的确定按钮>---当前服务器正有虚机运行，点击关机、重启、维护三种确定按钮
    use_running_back_xpath = "//*[contains(@id,'layui-layer')]/div[3]/a"

    # 使用情况 24小时
    usage_24_hours_xpath = "//button[contains(.,'24小时')]"
    # 使用情况 15天
    usage_15_days_xpath = "//button[contains(.,'15天')]"
    # 使用情况 60天
    usage_60_days_xpath = "//button[contains(.,'60天')]"

    # 搜索输入框
    search_input_box_xpath = "//input[contains(@type,'text')]"
    # 输入框输入后-无匹配元素
    search_result_empty_xpath = "//p[@class='el-autocomplete-suggestion__empty']"
    # 输入框输入后-有匹配元素
    search_result_xpath = "//*[contains(@class,'el-scrollbar__view el-autocomplete-suggestion__list')]"
    # 输入框中终端管理条目
    search_result_terminal_xpath = u"//*[contains(@class,'el-scrollbar__view el-autocomplete-suggestion__list')]" \
                                   u"//node()[contains(.,'终端管理')]"
    # 输入框中云桌面管理条目
    search_result_cloud_xpath = u"//*[contains(@class,'el-scrollbar__view el-autocomplete-suggestion__list')]" \
                                u"//node()[contains(.,'云桌面管理')]"

    # 云桌面管理搜索
    # 首页栏
    index_page_xpath = u"//li[contains(.,'首页')]"
    # 云桌面管理栏
    cloud_desktop_xpath = u"//span[contains(.,'云桌面管理')]"
    # 镜像管理栏
    image_manage_xpath = u"//span[contains(.,'镜像管理')]"
    # 高级配置管理栏
    set_manger_xpath = u"//span[contains(text(),'高级配置')]"
    # 存储管理栏
    storge_manger_xpath = u"//span[contains(text(),'存储管理')]"

    # 用户管理
    user_manage_xpath = u"//li[contains(.,'用户管理')]"
    # 终端管理
    terminal_manage_xpath = u"//span[contains(.,'终端管理')]"
    # 瘦终端(VDI) ->选择此元素前提->先点击终端管理
    terminal_manage_vdi_xpath = u"//span[contains(.,'瘦终端')]"
    # 胖终端(IDV) ->选择此元素前提->先点击终端管理
    terminal_manage_idv_xpath = u"//span[contains(.,'胖终端')]"

    # 高级配置
    advanced_config_xpath = u"//span[contains(.,'高级配置')]"
    # 部署和升级 -> 先点击高级配置
    deployment_and_upgrade_xpath = u"//span[contains(.,'部署与升级')]"
    # 云主机 ->先点击部署与升级
    cloud_host_xpath = u"//span[substring(., string-length(.) - string-length('云主机') +1) = '云主机']"
    # 云主机升级 -> 先点击部署与升级
    cloud_host_update_xpath = u"//span[contains(.,'云主机升级')]"
    # 终端升级-> 先点击部署与升级
    terminal_update_xpath = u"//span[contains(.,'终端升級')]"
    # CMS云空间管理-> 先点击部署与升级
    cms_cloud_space_xpath = u"//span[contains(.,'CMS云空间管理')]"
    # 定时任务-> 先点击部署与升级
    timed_task_xpath = u"//span[contains(.,'定时任务')]"
    # 云主机数据收集-> 先点击部署与升级
    cloud_host_data_xpath = u"//span[contains(.,'云主机数据收集')]"
    # 证书管理-> 先点击部署与升级
    certificate_manage_xpath = u"//span[contains(.,'证书管理')]"
    # 一键部署登录认证-> 先点击部署与升级
    oneclick_deployment_xpath = u"//span[contains(.,'一键部署登录认证')]"
    # 认证管理-> 先点击部署与升级
    certified_manage_xpath = u"//span[contains(.,'认证管理')]"
    # 调试工具-> 先点击部署与升级
    debug_tools_xpath = u"//span[contains(.,'调试工具')]"
    # OTA服务-> 先点击部署与升级
    ota_service_xpath = u"//span[contains(.,'OTA服务')]"

    # 存储管理-> 先点击高级配置
    storage_management_xpath = u"//span[contains(.,'存储管理')]"
    # USB外设管理-> 先点击高级配置
    usb_management_xpath = u"//span[contains(.,'USB外设管理')]"

    # 系统设置
    system_setting_xpath = u"//span[contains(.,'系统设置')]"
    # 网络配置 ->先点击系统设置
    network_setting_xpath = u"//span[contains(.,'网络配置')]"
    # 管理员账号设置 ->先点击系统设置
    admin_account_setting_xpath = u"//span[contains(.,'管理员账号设置')]"
    # 密码修改 ->先点击系统设置
    password_modify_xpath = u"//span[contains(.,'密码修改')]"
    # 系统时间 ->先点击系统设置
    system_time_xpath = u"//span[contains(.,'系统时间')]"
    # 离线登录时限设置 ->先点击系统设置
    offline_login_limit_xpath = u"//span[contains(.,'离线登录时限设置')]"
    # 云盘端口设置 ->先点击系统设置
    cloud_port_xpath = u"//span[contains(.,'云盘端口设置')]"
    # 客户信息 ->先点击系统设置
    customer_information_xpath = u"//span[contains(.,'客户信息')]"
    # 其他配置 ->先点击系统设置
    other_config_xpath = u"//span[contains(.,'其他配置')]"
    # 内存信息 ->先点击系统设置
    memory_information_xpath = u"//span[contains(.,'内存信息')]"
    # 云主机HA ->先点击系统设置
    cloud_host_ha_xpath = u"//span[contains(.,'云主机HA')]"

    # 云桌面VDI总数
    vdi_count_xpath = u"//div[contains(@class,'sk-dashboard-terminal__vdi-head')]/div[1]"
    # 云桌面IDV总数
    idv_count_xpath = "//div[contains(@class,'sk-dashboard-terminal__idv-head')]/div[1]"
    # VDI批量关机按钮
    vdi_batch_close_xpath = "//div[@class='sk-dashboard-terminal__vdi-head']/../div[3]/button"
    # IDV批量关机按钮
    idv_batch_close_xpath = "//div[@class='sk-dashboard-terminal__idv-head']/../div[3]/button"
    # 关机失败浮动按钮浮动条
    batch_close_tip_xpath = u"//p[contains(.,'请选择一条数据')]"
    # 批量关机后密码提示框
    batch_off_password_tip_xpath = "//*[contains(@placeholder,'请输入管理员密码')]"
    # 批量关机密码提示确认按钮
    batch_off_password_ok_xpath = "//*[contains(@class,'el-button el-button--primary el-button--mini is-round')]"
    # 批量关机密码提示取消按钮
    batch_off_password_cancel_xpath = "//*[contains(@class,'el-button el-button--default el-button--mini is-round')]"
    # 批量关机密码输入错误提示
    batch_off_password_error_xpath = "//*[contains(@class,'el-message el-message--error')]"
    # 批量关机后出现的成功提示
    batch_off_success_tip_xpath = "//*[contains(@class,'el-message el-message--success')]"
    # VDI全选分组按钮
    vdi_select_all_group_xpath = "//*[contains(@class,'sk-dashboard-terminal__vdi-head')]/..//node()[contains" \
                                 "(@class,'has-gutter')]//node()[contains(@class,'el-checkbox__inner')]"
    # IDV全选分组按钮
    idv_select_all_group_xpath = "//*[contains(@class,'sk-dashboard-terminal__idv-head')]/..//node()[contains" \
                                 "(@class,'has-gutter')]//node()[contains(@class,'el-checkbox__inner')]"
    # VDI <运行中> 选择
    vdi_running_xpath = "//*[contains(@class,'sk-dashboard-terminal__vdi-head')]//node()[contains" \
                        "(@class,'sk-dashboard-terminal__centent')]/div[1]/div[1]"
    # vdi <休眠> 选择
    vdi_sleep_xpath = "//*[contains(@class,'sk-dashboard-terminal__vdi-head')]//node()[contains" \
                      "(@class,'sk-dashboard-terminal__centent')]/div[2]/div[1]"
    # idv <运行中> 选择
    idv_running_xpath = "//*[contains(@class,'sk-dashboard-terminal__idv-head')]//node()[contains" \
                        "(@class,'sk-dashboard-terminal__centent')]/div[1]/div[1]"
    # idv <离线> 选择
    idv_offline_xpath = "//*[contains(@class,'sk-dashboard-terminal__idv-head')]//node()[contains" \
                        "(@class,'sk-dashboard-terminal__centent')]/div[2]/div[1]"
    # idv <终端使用情况>
    idv_terminal_usage_xpath = "//*[contains(@class,'el-card sk-dashboard-idv-card is-always-shadow')]" \
                               "//*[contains(@class,'primary-text')]"

    # 首页存储空间查看<四种全部>
    index_storage_view_xpath = "//*[contains(@class,'el-card sk-dashboard-storage-card is-always-shadow')]"

    # 云桌面系统盘已使用率
    index_cloud_sys_xpath = "//*[contains(@class,'sk-storage-progress__columnleft')]//node()" \
                            "[contains(.,'云桌面系统盘')]/../.."
    # 云桌面个人盘已使用率
    index_cloud_usr_xpath = "//*[contains(@class,'sk-storage-progress__columnleft')]//node()" \
                            "[contains(.,'云桌面用户数据盘')]/../.."
    # # 云盘已使用率
    # index_cloud_disk_xpath = "//*[contains(@class,'sk-storage-progress__columnleft')]//node()" \
    #                          "[contains(.,'云盘')]/../.."
    # 镜像已使用率
    index_image_xpath = u"//*[contains(@class,'sk-storage-progress__columnleft')]//node()" \
                        u"[contains(.,'镜像')]/../.."
    # vdi ad域图标
    vdi_ad_domain_ico_xpath = "//*[contains(@class,'sk-dashboard-terminal__vdi-head')]/following-sibling::*//node()" \
                              "[contains(@class,'sk-icon-terminal-ad is_single')]"
    # vdi ad域分组,使用时请使用 format传入参数
    vdi_ad_domain_group_xpath = "//*[contains(@class,'sk-dashboard-terminal__vdi-head')]/following-sibling::*//node()" \
                                "[contains(@class,'sk-icon-terminal-ad is_single')]/..//node()[contains(.,'{0}')]/.."
    # vdi 选中分组框,使用时请传入参数
    vdi_group_select_xpath = "//*[contains(@class,'sk-dashboard-terminal__vdi-head')]/following-sibling::*//node()" \
                             "[contains(@class,'cell el-tooltip showTooltip')]//node()[contains(.,'{0}')]/../../..//" \
                             "node()[contains(@class,'el-checkbox__inner')]"
    # vdi 分组框，使用时请传入参数
    vdi_group_xpath = "//*[contains(@class,'sk-dashboard-terminal__vdi-head')]/following-sibling::*//node()[contains" \
                      "(@class,'cell el-tooltip showTooltip')]//node()[contains(.,'{0}')]/.."
    # vdi 分组框内所有元素
    vdi_group_all_xpth = "//*[contains(@class,'sk-dashboard-terminal__vdi-head')]/following-sibling::*//node()" \
                         "[contains(@class,'cell el-tooltip showTooltip')]"

    # 云桌面系统盘已使用率浮动条
    index_cloud_sys_bar_xpath = "//*[contains(@class,'sk-storage-progress__columnleft')]//node()[contains" \
                                "(.,'云桌面系统盘')]/../../following-sibling::*"
    # 云桌面个人盘已使用率浮动条
    index_cloud_usr_bar_xpath = u"//*[contains(@class,'sk-storage-progress__columnleft')]//node()[contains(." \
                                u",'云桌面用户数据盘')]/../.."
    # # 云盘已使用率浮动条
    # index_cloud_disk_bar_xpath = "//*[contains(@class,'sk-storage-progress__columnleft')]//node()[contains" \
    #                              "(.,'云盘')]/../../following-sibling::*"
    # 镜像已使用率浮动条
    index_image_bar_xpath = "//*[contains(@class,'sk-storage-progress__columnleft')]//node()[contains" \
                            "(.,'镜像')]/../../following-sibling::*"

    #

    #
    #     点击首页
    def goto_indexpage(self):
        self.back_current_page()
        self.find_elem(self.index_xpath).click()

    #     获取用户信息
    def get_user_info1(self):
        return self.find_elem(self.user_info_xpath).text

    def logout(self):
        self.find_elem(IndexPage.logout_xpath).click()

    def index_about(self):
        self.find_elem(IndexPage.index_about_xpath).click()
        time.sleep(5)
        temp_text = self.find_elem(IndexPage.index_about_details_xpath).text
        temp_text = temp_text.split('\n')
        for i in range(len(temp_text)):
            temp_text1 = temp_text[i].strip()
            if temp_text1 == u'云办公主机' or temp_text1 == u'Ruijie Cloud Office' or temp_text1 == u'锐捷网络©2019':
                temp_text[i] = ''
                continue
        while '' in temp_text:
            temp_text.remove('')
        temp_text2 = {}
        for j in range(len(temp_text)):
            if re.match(u'^默认支持', temp_text[j].strip()):
                temp_text2[u'支持的分辨率'] = temp_text[j].strip()
            else:
                temp_text3 = temp_text[j].split(u'：')
                temp_text2[temp_text3[0].strip()] = temp_text3[1].strip()
        return temp_text2

    def search_jump_error(self):
        flag = 1
        time.sleep(com_slp)
        list_1 = ['!@#$%^&*', ' ', 'or 1=1#']
        for i in range(len(list_1)):
            self.find_elem(IndexPage.search_input_box_xpath).send_keys(list_1[i])
            time.sleep(2)
            if u'无匹配数据' != self.find_elem(IndexPage.search_result_empty_xpath).text:
                flag = 0
            self.find_elem(IndexPage.search_input_box_xpath).clear()
        return flag

    def cloud_vdi_jump(self):
        flag_1 = 0
        flag_2 = 0
        time.sleep(com_slp)
        self.find_elem(IndexPage.vdi_count_xpath).click()
        time.sleep(com_slp)
        if self.get_url() == url.rstrip('login') + 'cloud_desktop':
            flag_1 = 1
        time.sleep(com_slp)
        self.find_elem(IndexPage.index_page_xpath).click()
        time.sleep(com_slp)
        self.find_elem(IndexPage.idv_count_xpath).click()
        time.sleep(com_slp)
        if self.get_url() == url.rstrip('login') + 'terminal_manage/idv':
            flag_2 = 1
        return flag_1, flag_2

    def web_navigation_bar(self):
        flag_1 = 0
        flag_2 = 0
        flag_3 = 1
        time.sleep(com_slp)
        if self.find_elem(IndexPage.index_web_navigation_bar_xpath).text == u'首页':
            flag_1 = 1
        time.sleep(com_slp)
        self.find_elem(IndexPage.cloud_desktop_xpath).click()
        time.sleep(com_slp)
        if self.find_elem(IndexPage.index_web_navigation_bar_xpath).text == u'云桌面管理':
            flag_2 = 1
        self.find_elem(IndexPage.advanced_config_xpath).click()
        time.sleep(com_slp)
        self.find_elem(IndexPage.deployment_and_upgrade_xpath).click()
        time.sleep(com_slp)
        self.find_elem(IndexPage.ota_service_xpath).click()
        time.sleep(com_slp)
        if self.find_elem(IndexPage.index_web_navigation_bar_xpath).text == u'高级配置/\n部署与升级/\nOTA服务':
            flag_3 = 1
        return flag_1, flag_2, flag_3

    def view_server_health(self):
        flag_list = [0, 0, 0]  # ip,状态,总数
        time.sleep(com_slp)
        vdi_count = int(self.find_elem(IndexPage.vdi_running_xpath).text)
        self.find_elem(IndexPage.view_information_xpath).click()
        time.sleep(3)
        view_text = 0
        self.driver.get(url.rstrip('main.html#/login') + '/index/panels/serverDetail.jsf')
        status = u'正常'
        if server_count == 1:
            view_text = int(self.find_elem(IndexPage.use_vdi_xpath).text)
            view_ip = self.find_elem(IndexPage.use_server_xpath).text
            view_status = self.find_elem(IndexPage.use_server_status_xpath).text
            if view_ip == server_ip[0]:
                flag_list[0] = 1
            if view_status == status:
                flag_list[1] = 1
        elif server_count == 2:
            view_text = int(self.find_elem(self.use_vdi1_xpath).text) + int(self.find_elem(self.use_vdi1_xpath).text)
            view_ip = self.find_elem(IndexPage.use_server_xpath).text
            view_ip_1 = self.find_elem(IndexPage.use_server1_xpath).text
            view_status = self.find_elem(IndexPage.use_server_status_xpath).text
            view_status1 = self.find_elem(IndexPage.use_server1_status_xpath).text
            if view_ip == server_ip[0] or view_ip == server_ip[1]:
                flag_list[0] = 1
            if view_ip_1 == server_ip[1] or view_ip_1 == server_ip[0]:
                flag_list[0] = 1
            if view_status == status or view_status1 == status:
                flag_list[1] = 1
        elif server_count == 3:
            view_text = int(self.find_elem(IndexPage.use_vdi_xpath).text) + \
                        int(self.find_elem(IndexPage.use_vdi1_xpath).text) + \
                        int(self.find_elem(IndexPage.use_vdi2_xpath).text)
            view_ip = self.find_elem(IndexPage.use_server_xpath).text
            view_ip_1 = self.find_elem(IndexPage.use_server1_xpath).text
            view_ip_2 = self.find_elem(IndexPage.use_server2_xpath).text
            view_status = self.find_elem(IndexPage.use_server_status_xpath).text
            view_status1 = self.find_elem(IndexPage.use_server1_status_xpath).text
            view_status2 = self.find_elem(IndexPage.use_server2_status_xpath).text
            if view_ip == server_ip[0] or view_ip == server_ip[1] or view_ip == server_ip[2]:
                flag_list[0] = 1
            if view_ip_1 == server_ip[1] or view_ip_1 == server_ip[0] or view_ip_1 == server_ip[2]:
                flag_list[0] = 1
            if view_ip_2 == server_ip[2] or view_ip_2 == server_ip[0] or view_ip_2 == server_ip[1]:
                flag_list[0] = 1
            if view_status == status or view_status1 == status or view_status2 == status:
                flag_list[1] = 1
        if view_text == vdi_count:
            flag_list[2] = 1
        return flag_list

    def search_jump_smart(self):
        # 前提：需要导入selenium用户，然后才能进行操作
        flag_list = [0, 0, 0, 0]
        time.sleep(2)
        self.find_elem(IndexPage.search_input_box_xpath).send_keys(search_jump_smart_list[0])
        time.sleep(2)
        temp_text = self.find_elem(IndexPage.search_result_xpath).text
        if temp_text.find(u'终端管理'):
            flag_list[0] = 1
        if temp_text.find(u'用户管理'):
            flag_list[1] = 1
        if temp_text.find(u'云桌面管理'):
            flag_list[2] = 1
        self.find_elem(IndexPage.search_input_box_xpath).clear()
        self.find_elem(IndexPage.search_input_box_xpath).send_keys(search_jump_smart_list[1])
        time.sleep(com_slp)
        t1_text = self.find_elem(IndexPage.search_result_xpath).text
        self.find_elem(IndexPage.search_input_box_xpath).send_keys(search_jump_smart_list[2])
        time.sleep(com_slp)
        t2_text = self.find_elem(IndexPage.search_result_xpath).text
        self.find_elem(IndexPage.search_input_box_xpath).send_keys(search_jump_smart_list[3])
        time.sleep(com_slp)
        t3_text = self.find_elem(IndexPage.search_result_xpath).text
        if t1_text != t2_text and t2_text != t3_text and t1_text != t3_text:
            flag_list[3] = 1
        return flag_list

    def search_jump(self):
        flag_list = [0, 0, 0, 0, 0]
        time.sleep(1)
        self.find_elem(self.search_input_box_xpath).send_keys(search_jump_list[0])
        time.sleep(1)
        temp_text = self.find_elem(self.search_result_xpath).text
        if temp_text.find(search_jump_list[0][1:-1]) and temp_text.find(u'用户管理'):
            flag_list[0] = 1
        self.find_elem(self.search_input_box_xpath).clear()
        self.find_elem(self.search_input_box_xpath).send_keys(search_jump_list[1])
        time.sleep(0.5)
        temp_text = self.find_elem(self.search_result_xpath).text
        if temp_text.__contains__(search_jump_list[1]) and temp_text.__contains__(u'终端管理'):
            flag_list[1] = 1
        time.sleep(0.5)
        self.find_elem(self.search_input_box_xpath).clear()
        self.find_elem(self.search_input_box_xpath).send_keys(search_jump_list[2])
        time.sleep(1)
        temp_text = self.get_elem_text(self.search_result_xpath)
        if temp_text.__contains__(search_jump_list[2]) and temp_text.__contains__(u'云桌面管理'):
            flag_list[2] = 1
        time.sleep(1)
        self.find_elem(self.search_input_box_xpath).clear()
        self.find_elem(self.search_input_box_xpath).send_keys(search_jump_list[1])
        self.find_elem(self.search_result_terminal_xpath).click()
        time.sleep(1)
        print self.get_url()
        if self.get_url().__contains__('idv'):
            flag_list[3] = 1
        self.find_elem(IndexPage.index_page_xpath).click()
        time.sleep(com_slp)
        self.find_elem(IndexPage.search_input_box_xpath).clear()
        self.find_elem(IndexPage.search_input_box_xpath).send_keys(search_jump_list[2])
        time.sleep(1)
        self.find_elem(IndexPage.search_result_cloud_xpath).click()
        time.sleep(2)
        print self.get_url()
        if self.get_url().__contains__('cloud_desktop'):
            flag_list[4] = 1
        return flag_list
    # 云桌面使用率xpath
    storage_sys_use_xpath = u"//*[contains(text(),'云桌面系统盘')]/parent::div" \
                            u"//span[@class='sk-storage-progress__progress primary-text']"
    used_space_xpath = u"//*[contains(text(),'云桌面系统盘')]/parent::div//span[contains(text(),'(')]"
    def cloud_storage_sys_space_check(self):
        # time.sleep(300)
        flag_list = [0, 0]
        dut = DutGetShow()
        time.sleep(com_slp)
        bar_color = self.find_elem(IndexPage.index_cloud_sys_bar_xpath).get_attribute('class')
        a_list, b_list = [], []
        a, b = 0, 0
        for i in range(server_count):
            str_tmp = server_conn(server_ip[i], 'df')
            a_list.append(dut.dut_get_show_df(str_tmp, '/opt/cache', 'Used'))
            b_list.append(dut.dut_get_show_df(str_tmp, '/opt/cache', '1K-blocks'))
            a = a + Decimal(a_list[i])
            b = b + Decimal(b_list[i])
        c = Decimal('1024') * Decimal('1024')
        if bar_color.find('gradient'):
            flag_list[0] = 1
        used_rate = self.get_elem_text(self.storage_sys_use_xpath).replace('%','')
        print used_rate
        size =  self.get_elem_text(self.used_space_xpath)
        temp = size.replace('(','').replace(')','').split('/')
        a_size = temp[0].split('G')[0]
        b_size = temp[1].split('G')[0]
        print size,temp
        if float(used_rate) - float('{:.2%}'.format(a / b).strip('%')) <= 1 \
                and abs(float(a_size) - float('{:.2f}'.format(a / c))) <= 1 and \
                abs(float(b_size) - float('{:.2f}'.format(b / c))) <= 1:
            flag_list[1] = 1
        return flag_list
    # 云桌面使用率xpath
    user_sys_use_xpath = u"//*[contains(text(),'云桌面用户数据盘')]/parent::div" \
                            u"//span[@class='sk-storage-progress__progress primary-text']"
    used_user_space_xpath = u"//*[contains(text(),'云桌面用户数据盘')]/parent::div//span[contains(text(),'(')]"
    def cloud_storage_usr_space_check(self):
        flag_list = [0, 0]
        time.sleep(com_slp)
        bar_color = self.find_elem(IndexPage.index_cloud_usr_bar_xpath,wait_times=30).get_attribute('class')
        a_size = 0
        b_size = 0
        disk_size = server_conn(mainip,"df -h | grep drbd |awk '{print $3}'")
        disk_usde_size = server_conn(mainip,"df -h | grep drbd |awk '{print $2}'")
        for size in disk_size.split():
            if size[-1:] == 'T':
                size = Decimal(size[0:-1])*1024*1024
            elif size[-1:] == 'G':
                size = Decimal(size[0:-1]) * 1024
            elif size[-1:] == 'K':
                size = Decimal(size[0:-1]) / 1024
            else:
                size = Decimal(size[0:-1])
            a_size = a_size + size
        for size in disk_usde_size.split():
            if size[-1:] == 'T':
                size = Decimal(size[0:-1])*1024*1024
            elif size[-1:] == 'G':
                size = Decimal(size[0:-1]) * 1024
            elif size[-1:] == 'K':
                size = Decimal(size[0:-1]) / 1024
            else:
                size = Decimal(size[0:-1])
            b_size = b_size + size
        if bar_color.find('gradient'):
            flag_list[0] = 1
        used_rate = self.get_elem_text(self.user_sys_use_xpath).replace('%', '')
        print used_rate
        size = self.get_elem_text(self.used_user_space_xpath)
        temp = size.replace('(', '').replace(')', '').split('/')
        a = temp[0].split('G')[0]
        b = temp[1].split('G')[0]
        print a_size/b_size
        print float('{:.2%}'.format(a_size / b_size).strip('%'))
        print '页面获取的使用空间：%f'%float(a)
        print  '页面获取的总空间：%f'%float(b)
        print "数据库获取的使用空间：%f"%float('{:.2f}'.format(a_size / 1024))
        print "数据库获取的总使用空间：%f"%float('{:.2f}'.format(b_size / 1024))
        if float(used_rate) - float('{:.2%}'.format(a_size / b_size).strip('%')) <= 1 \
                and abs(float(a) - float('{:.2f}'.format(a_size / 1024))) <= 1 and \
                abs(float(b) - float('{:.2f}'.format(b_size / 1024))) <= 1:
            flag_list[1] = 1
        # if float(temp_text[0].strip("[u'").strip('%')) - float('{:.2%}'.format(a_size / b_size).strip('%')) <= 1:
        #     flag_list[1] = 1
        return flag_list

    # def cloud_storage_disk_space_check(self):
    #     flag_list = [0, 0]
    #     dut = DutGetShow()
    #     time.sleep(com_slp)
    #     bar_color = self.find_elem(IndexPage.index_cloud_disk_bar_xpath).get_attribute('class')
    #     str_tmp = serer_conn(server_ip[3],  'df')
    #     a = Decimal(dut.dut_get_show_df(str_tmp, '/user_disk/disk_space', 'Used'))
    #     b = Decimal(dut.dut_get_show_df(str_tmp, '/user_disk/disk_space', '1K-blocks'))
    #     c = Decimal('1024') * Decimal('1024')
    #     temp_text = self.find_elem(IndexPage.index_cloud_disk_xpath).text
    #     temp_text = temp_text.split('\n')
    #     if bar_color.find('gradient'):
    #         flag_list[0] = 1
    #     temp_text.remove(temp_text[0])
    #     temp_text = str(temp_text).split(' ')
    #     for j in range(len(temp_text)):
    #         temp_text[j] = temp_text[j].lstrip('(').rstrip('G/').rstrip(r"G)\\']")
    #     if float(temp_text[0].strip("[u'").strip('%')) - float('{:.2%}'.format(a / b).strip('%')) <= 1 \
    #             and abs(float(temp_text[1]) - float('{:.2f}'.format(a / c))) <= 1 and \
    #             abs(float(temp_text[2]) - float('{:.2f}'.format(b / c))) <= 1:
    #         flag_list[1] = 1
    #     return flag_list
    img_sys_use_xpath = u"//*[contains(text(),'镜像模板')]/parent::div" \
                         u"//span[@class='sk-storage-progress__progress primary-text']"
    used_img_space_xpath = u"//*[contains(text(),'镜像模板')]/parent::div//span[contains(text(),'(')]"
    def cloud_storage_image_space_check(self):
        flag_list = [0, 0]
        dut = DutGetShow()
        time.sleep(com_slp)
        bar_color = self.find_elem(IndexPage.index_image_bar_xpath,wait_times=30).get_attribute('class')
        str_tmp = server_conn(host_ip, 'df')
        a = Decimal(dut.dut_get_show_df(str_tmp, '/opt/lessons', 'Used'))
        b = Decimal(dut.dut_get_show_df(str_tmp, '/opt/lessons', '1K-blocks'))
        c = Decimal('1024') * Decimal('1024')
        time.sleep(5)
        if bar_color.find('gradient'):
            flag_list[0] = 1
        used_rate = self.get_elem_text(self.img_sys_use_xpath).replace('%', '')
        print used_rate
        size = self.get_elem_text(self.used_img_space_xpath)
        temp = size.replace('(', '').replace(')', '').split('/')
        a_size = temp[0].split('G')[0]
        b_size = temp[1].split('G')[0]
        print size, temp
        if float(used_rate) - float('{:.2%}'.format(a / b).strip('%')) <= 1 \
                and abs(float(a_size) - float('{:.2f}'.format(a / c))) <= 1 and \
                abs(float(b_size) - float('{:.2f}'.format(b / c))) <= 1:
            flag_list[1] = 1
        return flag_list

    def ad_domain_user_index_page(self):
        flag_list = [0, 0]
        ad_ico = self.find_elem(self.vdi_ad_domain_ico_xpath).get_attribute('class')
        if ad_ico.find('ad'):
            flag_list[0] = 1
        ad_group = self.find_elem(self.vdi_ad_domain_group_xpath.format(ad_vdi_list[0])).text
        if ad_group != '':
            flag_list[1] = 1
        return flag_list

    def batch_off_checked_vdi_group(self):
        flag_list = [0, 0, 0]
        time.sleep(com_slp)
        self.find_elem(self.vdi_group_select_xpath.format(vdi_group_list[0])).click()
        self.find_elem(self.vdi_batch_close_xpath).click()
        time.sleep(2 * com_slp)
        self.find_elem(self.batch_off_password_tip_xpath).send_keys('l')
        self.find_elem(self.batch_off_password_ok_xpath).click()
        time.sleep(com_slp)
        if self.find_elem(self.batch_off_password_error_xpath).text == u'管理员密码不正确！':
            flag_list[0] = 1
        self.find_elem(self.batch_off_password_tip_xpath).clear()
        self.find_elem(self.batch_off_password_tip_xpath).send_keys(login_user_succ["passwd"])
        self.find_elem(self.batch_off_password_cancel_xpath).click()
        if self.find_elem(self.vdi_group_xpath.format(vdi_group_list[0])).text == vdi_group_list[0]:
            flag_list[1] = 1
        time.sleep(2 * com_slp)
        self.find_elem(self.vdi_batch_close_xpath).click()
        self.find_elem(self.batch_off_password_tip_xpath).send_keys(login_user_succ["passwd"])
        self.find_elem(self.batch_off_password_ok_xpath).click()
        if self.find_elem(self.batch_off_success_tip_xpath).text == u'批量关机成功！':
            flag_list[2] = 1
        return flag_list

    ###########################################
    #     获取用户信息
    def get_user_info(self):
        return self.find_elem(self.user_info_xpath).text

    # 点击查看按钮
    def click_cheeck_button(self):
        time.sleep(1)
        self.find_elem(self.check_button_xpath).click()
        time.sleep(2)
        self.driver.switch_to.frame(self.iframeid)

    # 获取查看页面的所有主机ip
    def get_ip_info(self):
        time.sleep(1.5)
        self.find_elem(self.check_button_xpath).click()
        time.sleep(1)
        self.driver.switch_to.frame(self.iframeid)
        time.sleep(1)
        elems = self.find_elems(self.ip_dress_xpath)
        ip_list = []
        time.sleep(1)
        for i in range(len(elems)):
            temp = elems[i].text.replace(u"IP：", u'')
            ip_list.append(temp)
        return ip_list

    # 获取cpu利用率
    def get_cpuuse(self, ip):
        elems = self.find_elem(self.cpu_used_xpath.format(ip))
        data = float(elems.get_attribute("usage"))
        return round(data, 2)

    # 获取内存利用率
    def get_memuse(self, ip):
        elems = self.find_elem(self.men_use_xpath.format(ip))
        data = float(elems.get_attribute("usage"))
        return round(data, 2)

    # 获取服务器状态
    def get_status(self, ip):
        return self.find_elem(self.status_xpath.format(ip)).text
    # 跳转到iframe
    def go_frame_p(self):
        self.driver.switch_to.frame(self.iframeid)
    # 获取虚机台数
    def get_virsh_amount(self, ip):
        return self.find_elem(self.vdi_num_xpath.format(ip)).text

    # 点击关机按钮
    def close_server_click(self, ip):
        self.find_elem(self.shutdown_button_xpath.format(ip)).click()

    # 点击确定按钮
    def confirm_button_click(self):
        self.back_current_page()
        self.find_elem(self.confirm_button_xpath).click()
        self.driver.switch_to.frame(self.iframeid)

    # 点击取消按钮
    def cancel_button_click(self):
        self.back_current_page()
        self.find_elem(self.cancel_button_xpath).click()
        self.driver.switch_to.frame(self.iframeid)

    # 输入密码点击确定按钮
    def send_passwd_confirm(self, pd=c_pwd):
        self.back_current_page()
        self.find_elem(self.confirm_passwd_xpath).send_keys(pd)
        self.click_elem(self.passwd_confirm_xpath)

    #     输入密码错误提示消息
    def get_error_passwd_info(self):
        return self.find_elem(self.errot_passwd_info_xpath).text

    # 输入错误密码后清除再次输入正确的密码确定
    def send_passwd_again(self):
        self.find_elem(self.confirm_passwd_xpath).send_keys(Keys.CONTROL, 'a')
        self.find_elem(self.confirm_passwd_xpath).send_keys(Keys.BACK_SPACE)
        self.find_elem(self.confirm_passwd_xpath).send_keys(passwd)
        self.find_elem(self.passwd_confirm_xpath).click()

    # 输入密码后关机点击取消按钮
    def server_cancle(self):
        self.back_current_page()
        self.find_elem(self.passwd_cancle_xpath).click()

    #  点击重启按钮
    def restart_server_button_click(self, ip):
        self.find_elem(self.reboot_button_xpath.format(ip)).click()

    #     重启信息提示
    def get_reboot_info(self):
        time.sleep(1)
        self.back_current_page()
        return self.find_elem(self.reboot_info_xpath).text

    # 重启成功提示
    def get_reboot_confirm(self):
        time.sleep(1)
        self.get_ciframe(self.success_confirm_iframe_id)
        return self.find_elem(self.confirm_reboot_info_xpath).text

    # 重启成功确定
    def reboot_confirm(self):
        self.find_elem(self.reboot_confirm_button_xpath).click()

    # 点击维护
    def fix_server_click(self, ip):
        self.find_elem(self.fix_button_xpath.format(ip)).click()

    # 点击维护虚机时提示信息
    def get_fixinfo(self):
        self.back_current_page()
        return self.find_elem(self.fix_info_xpath).text

    # 关闭虚机后提示信息
    def close_virsh_info(self):
        time.sleep(1)
        self.back_current_page()
        return self.find_elem(self.close_virsh_info_xpath).text

    #     关闭查看页面
    def close_checkpage(self):
        self.back_current_page()
        self.find_elem(self.close_checkifeame_xpath).click()

    #     获取运行中vdi云桌面个数
    def get_running_num_vdi(self):
        return self.find_elem(self.vdi_running_num_xpath).text

    #     切换到ifream
    def getinto_iframe(self):
        time.sleep(3)
        self.get_ciframe(self.iframeid)

    # 页面刷新
    def refesh(self):
        self.driver.refresh()

    #     点击告警
    def warning_button_click(self):
        self.find_elem(self.warning_button_xpath).click()

    #         获取首页的vdi总数量
    def get_vdicount(self):
        p = self.find_elem(self.vdi_numcount_xpath).text
        return p.split(u"：", 1)[1]

    # 获取运行中虚机vdi个数
    def get_running_vdi(self):
        return self.find_elem(self.vdi_running_num_xpath).text

    # 点击跳转到运行中虚机页面
    def click_running_vdi(self):
        self.find_elem(self.vdi_running_num_xpath).click()

    # 获取休眠中虚机vdi个数
    def get_sleep_vdi(self):
        return self.find_elem(self.vdi_sleep_num_xpath).text

    #    点击休眠中虚机个数
    def click_sleep_vdi(self):
        self.click_elem(self.vdi_sleep_num_xpath)
    #         获取首页的idv总数量
    def get_idvcount(self):
        p = self.find_elem(self.idv_numcount_xpath).text
        return p.split(u"：", 1)[1]

    # 获取运行中虚机idv个数
    def get_running_idv(self):
        return self.find_elem(self.idv_running_num_xpath).text

    # 点击运行的idv数量
    def click_running_idv(self):
        self.find_elem(self.idv_running_num_xpath).click()

    # 获取离线虚机idv个数
    def get_sleep_idv(self):
        return self.find_elem(self.idv_sleep_num_xpath).text

    # 点击休眠idv个数
    def click_sleep_idv(self):
        self.find_elem(self.idv_sleep_num_xpath).click()

    #     获取vdi用户组
    def get_vdi_grop_name(self, name):
        return self.find_elem(self.vdi_group_name_xpath.format(name)).text

    #     获取idv用户组
    def get_idv_group_name(self, name):
        return self.find_elem(self.idv_group_name_xpath.format(name)).text

    # 获取vdi用户组虚机数量
    def get_vdi_group_num(self, name):
        return self.find_elem(self.vdi_group_num_xpath.format(name)).text

    #     获取idv用户组虚机数量
    def get_idv_group_num(self, name):
        return self.find_elem(self.idv_group_num_xpath.format(name)).text

    # 选择批量关机VDi用户组
    def close_vdi_terminal_chose(self, name):
        time.sleep(1)
        self.find_elem(self.vdi_checkbox_xpath.format(name)).click()

    # 点击批量关机VDi
    def close_vdi_terminal(self):
        time.sleep(1)
        self.find_elem(self.vdi_close_button_xpath).click()

    #        跳转到vdi终端管理页面
    def goto_vdi_terminal_page(self):
        self.find_elem(self.vdi_numcount_xpath).click()

    # 选择批量关机vdi用户组
    def close_idv_terminal_chose(self, name):
        self.find_elem(self.idv_checkbox_xpath.format(name)).click()

    #  点击批量关机idv
    def close_idv_terminal(self):
        self.find_elem(self.idv_close_button_xpath).click()

    #     批量关机所有vdi虚机
    def close_all_vdi_terminal(self):
        time.sleep(1)
        self.find_elem(self.vdi_checkall_xpath).click()
        self.find_elem(self.vdi_close_button_xpath).click()
        self.send_passwd_confirm()

    #     批量关机所有idv虚机
    def close_all_idv_terminal(self):
        self.find_elem(self.idv_checkall_xpath).click()
        self.find_elem(self.idv_close_button_xpath).click()
        self.send_passwd_confirm()

    #        跳转到idv组用户终端页面
    def goto_idv_terminal_page(self, name):
        time.sleep(1)
        self.find_elem(self.idv_group_num_xpath.format(name)).click()

    #         跳转到所选组vdi云桌面在线用户
    def goto_groupvdi_terminal_page(self, name):
        self.find_elem(self.vdi_group_num_xpath.format(name)).click()

    # 获取批量关机成功提示信息
    def get_close_success_info(self):
        return self.find_elem(self.close_success_info_xpath).text

    # 获取vdi用户管理列表
    def get_vdi_user_grouplist(self):
        elems = self.find_elems(self.vdi_user_grouplist_xpath)
        name_list = []
        for i in range(len(elems)):
            temp = elems[i].text
            name_list.append(temp)
        return name_list

    # 获取idv用户管理列表
    def get_idv_user_grouplist(self):
        elems = self.find_elems(self.idv_user_grouplist_xpath)
        name_list = []
        for i in range(len(elems)):
            temp = elems[i].text
            name_list.append(temp)
        return name_list

    # 获取告警气泡里的数量
    def get_warming_num(self):
        return self.find_elem(self.warming_xpath).text

    # 获取告警信息
    def get_warning_info(self):
        a = self.find_elem(self.warming_infoip_xpath).text
        b = self.find_elem(self.warming_info_xpath).text
        return a + b

    # 关闭告警内容
    def close_warning(self):
        self.find_elem(self.close_warning_xpath, wait_times=10).click()

    # 跳转到告警页面
    def goto_warming_info(self):
        self.find_elem(self.warming_xpath).click()

    # 跳转到用户管理页面
    def goto_usermange_button(self):
        self.find_elem(self.user_manage_xpath).click()

    # 跳转到镜像管理页面
    def goto_image_manage_button(self):
        self.find_elem(self.image_manage_xpath).click()

    # 跳转到存储管理页面
    def goto_storge_manage_page(self):
        self.find_elem(self.set_manger_xpath).click()
        time.sleep(0.5)
        self.find_elem(self.storage_management_xpath).click()

    # 获取用户数据盘
    frame_id = "frameContent"
    disk_flod_xpath = u'//*[@id="storage_user_data_disk_div"]//*[@class="toggle-div-btn-down"]'
    disk_name_xpath = '//*[@id="user_data_disk_body"]//tr/td[1]'
    def get_use_manger_disk(self):
        self.goto_storge_manage_page()
        time.sleep(1)
        name_list =list()
        elems  = self.find_presence_elem(self.disk_name_xpath)
        for ele in elems:
            name_list.append(ele.text)
        return name_list

