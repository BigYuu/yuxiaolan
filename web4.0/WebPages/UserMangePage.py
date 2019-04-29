#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/11/14 20:15
"""

from selenium.webdriver import ActionChains
from Common.terminal_action import *
from WebPages.Idvpage import IdvPage
from TestData.Usermanagedata import *
import logging
from LoginPage import *


class UserMange(BasicFun):
    #     元素定位
    #   跳转到用户管理页面xpath
    user_manage_xpath = "//*[@class='fa fa-user-circle']"
    usermanage_xpath = u"//span[contains(text(),'用户管理')]"
    #     搜素框后的更多按钮xpath
    more_operate_xpath = "//*[@class='sk-toolbar']/descendant::div[@class='el-dropdown']//button"
    #    填充ipxpath
    fill_ip_xpath = u"//li[contains(text(),'填充IP')]"
    # 模板导入下path
    user_import_xpath = u'//li[contains(text(),"模板导入")]'
    # 上传文件下path
    upload_file_xpath = u'//*[@class="el-button el-button--primary el-button--small is-round"]'
    # 选择上传文件点击确定
    confirm_file_xpath = '//*[@class="el-button el-button--default el-button--mini is-round el-button--primary "]'
    # 点击开始导入
    start_import_xpath = '//*[@class="el-button el-button--primary el-button--small is-round"]'
    # ip填充页面xpath
    # 云桌面起始IP：输入框
    start_ip_input_xpath = "//*[contains(text(),'云桌面起始IP：')]/parent::div//descendant::input"
    # 云桌面子网掩码：输入框
    mask_input_xpath = "//*[contains(text(),'云桌面子网掩码：')]/parent::div//descendant::input"
    # 云桌面网关：输入框
    gateway_xpath = "//*[contains(text(),'云桌面网关：')]/parent::div//descendant::input"
    # 云桌面首选DNS：输入框
    first_DNS_xpaht = "//*[contains(text(),'云桌面首选DNS：')]/parent::div//descendant::input"
    # 云桌面备用DNS：输入框
    spare_DNS_xpath = "//*[contains(text(),'云桌面备用DNS：')]/parent::div//descendant::input"
    # 确定按钮
    confirm_button_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"
    # 清除ipxpath
    clear_ip_xparh = "//li[contains(text(),'清空IP')]"
    # 确定清空按钮
    confirm_clear_xpath = "//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']"
    # 选择用户单选框传入用户名为参数
    chose_user_xpath = u"//*[text()='{}']/ancestor::tr//span[@class='el-checkbox__input']"
    # 搜索框xpath
    search_xpath = "//*[@class='fl']//*[@class='el-input__inner']"
    # 为选择用户点击填充ip提示信息
    without_user_info = "//*[@class='el-message el-message--warning']//p"
    # ip填充成功提示
    ip_fill_successinfo_xpath = "//*[@class='el-notification__content']/p"
    # 用户管理全选单选框
    select_all_user_xpath = u"//div[text()='姓名']/ancestor::tr//input"
    # 新增用户组
    new_group_xpath = u"//*[@class='el-button add-group-btn el-button--primary el-button--mini is-round is-noLabel']"
    # 输入用户组名
    group_name_xpath = u"//*[@class='el-form-item is-required']//*[@class='el-input__inner']"
    # 开启vdi用户属性
    vdi_attribute_button_xpath = u"//*[text()='VDI云桌面：']/ancestor::div[@class='el-form-item']" \
                                 u"//span[@class='el-switch__core']"
    # 开启idv特性
    idv_attribute_button_xpath = u"//*[text()='IDV云终端：']/ancestor::div[@class='el-form-item']" \
                                 u"//span[@class='el-switch__core']"
    # 绑定镜像xpath
    chose_mirrori_xpath = u"//*[@id='scrollpane-vdiPolicy']//*[contains(text(),'绑定镜像：')]/parent::div//input"
    # 新建用户
    new_user_xpath = u"//*[contains(text(),'新建用户')]"
    # 编辑xpath
    edit_xpath = u"//*[@x-placement='bottom-start']//li[contains(text(),'编辑')]"
    # 详情页面xpath
    info_xpath = u"//*[@x-placement='bottom-start']//li[contains(text(),'详情')]"
    # idv用户镜像修改
    idv_change_mirror_xpath = u"//*[@class='el-select-group__wrap']/parent::ul//" \
                              u"li[@class='el-select-dropdown__item']/span"
    # vdi用户镜像修改 //li//*[contains(text(),'test_vdi_restore_win7_rcd')]
    change_mirror_xpath2 = "//li//*[contains(text(),'{}')]"
    change_mirror_xpath = '//*[contains(@x-placement,"-start")]//li[@class="el-select-dropdown__item"]/span'

    # 获取用户的绑定镜像信息
    mirror_info_xpath = u"//*[contains(text(),'绑定镜像：')]/parent::div//*[@class='el-form-item__content']/span"

    # 确认按钮xpath
    confirm_xpath = u"//*[text()='确认']"
    # 点击确定后点击确认
    sure_xpath = u"//*[contains(text(),'确定')]"
    # 用户的更多操作的按钮
    user_more_operate_xpath = "//*[text()='{}']/ancestor::tr//button"
    # 关闭详情按钮
    close_info_button_xpath = "//*[@class='el-dialog__close el-icon el-icon-close']"
    # 用户组所在div
    group_xpath = u'//div[contains(text(),"{}")]'
    # 用户组编辑按钮
    group_edit_xpath = u'//div[contains(text(),"{}")]/parent::div//i[@class="el-icon-edit"]/parent::button'
    # 用户组绑定镜象按钮
    idv_group_mirror_bind_xpath = u'//*[contains(text(),"IDV云终端：")]/ancestor::div[@class="form-item-wrap"]' \
                                  u'//*[contains(text(),"绑定镜像：")]/parent::div//input'
    # idv用户组绑定镜象
    vdi_group_mirror_bind_xpath = u'//*[contains(text(),"VDI云桌面：")]/ancestor::div[@class="form-item-wrap"]' \
                                  u'//*[contains(text(),"绑定镜像：")]/parent::div//input'
    # idv用户桌面类型选择
    idv_desk_type_xpath = u'//*[contains(text(),"IDV云终端：")]/ancestor::div[@class="form-item-wrap"]' \
                          u'//*[contains(text(),"桌面类型：")]/parent::div//input'
    # vdi用户桌面类型选择
    vdi_desk_type_xpath = u'//*[contains(text(),"VDI云桌面：")]/ancestor::div[@class="form-item-wrap"]' \
                          u'//*[contains(text(),"桌面类型：")]/parent::div//input'
    # 桌面类型选择
    desk_type_chose_xpath = u'//*[@x-placement="bottom-start"]//*[text()="{}"]'
    # 修改用户组点击确认
    confirm_group_change_xpath = '//*[@class="el-button el-button--primary el-button--mini is-round"]'
    #  idv用户组修改点击确定
    idv_confirm_group_change_xpath = \
        '//*[@class="el-button el-button--default el-button--mini is-round el-button--primary "]'
    # 云盘是否为开启状态
    is_x_disk_open = u"//*[contains(text(),'云盘：')]/..//div[@role='switch']"
    idvPolicy = "//*[@id='scrollpane-idvPolicy']"

    # 跳转到用户管理页面
    def __init__(self, driver):
        BasicFun.__init__(self, driver)
        self.collect_log_msg_xpath = None

    def goto_usermanage_page(self):
        self.find_elem(self.user_manage_xpath).click()

    # 搜索功能
    def search_info(self, name):
        self.clear_text_info(self.search_xpath)
        self.find_elem(self.search_xpath).send_keys(name, Keys.ENTER)

    # 搜索功能
    def search_num_info(self, name):
        self.search_info(name)
        info = self.find_elem(self.searchCount_xpath).text
        s = info.replace(u'共', '')
        return s.replace(u"条", "")

    # 选中用户点击单选框
    def chose_user(self, name):
        self.find_elem(self.chose_user_xpath.format(name)).click()

    # 点击跟多操作
    def all_more_operate(self):
        self.find_elem(self.more_operate_xpath).click()

    # 填充ip
    def click_fill_ip(self):
        self.find_elem(self.fill_ip_xpath).click()

    def fill_ip_allinfo(self, ip, mask, gateway, dns):
        self.all_more_operate()
        self.click_fill_ip()
        self.find_elem(self.start_ip_input_xpath).send_keys(ip)
        self.find_elem(self.mask_input_xpath).send_keys(mask)
        self.find_elem(self.gateway_xpath).send_keys(gateway)
        self.find_elem(self.first_DNS_xpaht).send_keys(dns)
        self.find_elem(self.confirm_button_xpath).click()

    # 未选择用户时填充ip提示
    def fill_ip_nouser_info(self):
        return self.find_elem(self.without_user_info).text

    # ip填充成功提示
    def fill_ip_successinfo(self):
        return self.find_elem(self.ip_fill_successinfo_xpath).text

    # 清除ip
    def clear_ip(self):
        self.all_more_operate()
        self.find_elem(self.clear_ip_xparh).click()
        self.find_elem(self.confirm_clear_xpath).click()

    #   选择用户时点击全选的单选框
    def chose_all_user(self):
        self.find_elem(self.all_box).click()

    # 点击新增用户组
    def create_group(self):
        time.sleep(1)
        self.find_elem(self.new_group_xpath).click()

    def click_more_operate(self, name):
        """点击更多操作"""
        self.search_info(name)
        self.click_elem(self.user_more_operate_xpath.format(name))

    def vdi_attribute_set(self, name):
        """开启用户vdi属性"""
        self.find_elem(self.group_name_xpath).send_keys('{}'.format(name))
        self.find_elem(self.vdi_attribute_button_xpath).click()
        time.sleep(1)
        self.scroll_into_view(self.chose_mirrori_xpath)

    def click_edit(self, name):
        """点击编辑"""
        self.click_more_operate(name)
        self.click_elem(self.edit_xpath)

    def mirror_info(self, name):
        """获取用户镜像信息"""
        self.search_info(name)
        self.click_more_operate(name)
        self.click_elem(self.info_xpath)
        return self.get_elem_text(self.mirror_info_xpath)

    def close_info(self):
        """关闭详情页面"""
        self.click_elem(self.close_info_button_xpath)

    def change_mirror(self, name, pd=c_pwd):
        """修改用户镜像"""
        self.click_edit(name)
        self.scroll_into_view(self.chose_mirrori_xpath)
        a = self.find_elem(self.change_mirror_xpath).text
        self.click_elem(self.change_mirror_xpath)
        self.click_save(pd)
        return a

    def click_save(self, pd=c_pwd):
        """修改用户信息后点击确认"""
        self.click_elem(self.confirm_xpath)
        self.click_elem(self.sure_xpath)
        a = Login(self.driver)
        a.send_pwd_confirm(pd)

    def import_user(self):
        """导入用户数据"""
        self.all_more_operate()
        self.click_elem(self.user_import_xpath)
        self.click_elem(self.upload_file_xpath)

    def start_import(self):
        """点击开始导入数据"""
        self.click_elem(self.confirm_file_xpath)
        self.click_elem(self.start_import_xpath)
        time.sleep(2)

    def edit_group1(self, name):
        """用户组编辑"""
        self.chainstay(self.group_xpath.format(name))
        time.sleep(0.5)
        self.find_elem(self.group_edit_xpath.format(name)).click()

    def idv_group_set(self, desk_type=u'个性'):
        """修改idv用户组idv特性"""
        self.click_elem(self.idv_attribute_button_xpath)
        self.click_elem(self.idv_desk_type_xpath)
        self.click_elem(self.desk_type_chose_xpath.format(desk_type))
        self.click_elem(self.idv_group_mirror_bind_xpath)
        self.click_elem(self.change_mirror_xpath)
        self.click_elem(self.confirm_group_change_xpath)
        self.click_elem(self.idv_confirm_group_change_xpath)

    def vdi_group_set(self, desk_type=u'个性', name=None):
        """修改vdi用户组vdi特性"""
        self.scroll_into_view(self.vdi_attribute_button_xpath)
        self.click_elem(self.vdi_desk_type_xpath)
        self.click_elem(self.desk_type_chose_xpath.format(desk_type))
        self.click_elem(self.vdi_group_mirror_bind_xpath)
        if name is None:
            self.scroll_into_view(self.change_mirror_xpath)
        else:
            self.scroll_into_view(self.change_mirror_xpath2.format(name))
        time.sleep(0.5)
        if desk_type == u'还原':
            self.click_elem(self.vdi_group_mirror_bind_xpath)
        self.click_elem(self.confirm_group_change_xpath)
        self.click_elem(self.idv_confirm_group_change_xpath)

    def del_chose_user(self, user_name, pwd):
        """选择正常用户并删除用户"""
        self.search_info(user_name)
        time.sleep(1)
        self.chose_user(user_name)
        self.click_elem(self.delete_user_xpath)
        self.find_elem(self.confirm_deleteuser).click()
        self.send_passwd_confirm(pwd)
        time.sleep(3)

    u"-----------------------------------yuxiaolan封装部分--------------------------------------"

    # 取消按钮
    cancle_btn = u"//*[contains(text(),'取消')]"
    cancel_button1 = u"//span[text()='取消']"

    # 获取元素内容
    def get_value(self, locator):
        return self.get_elem_text(locator=locator)

    # 一整个用户组
    all_group_xpath = "//div[contains(@class,'user-group-body el-row clearAroundPadding')]"
    # 输入密码点击确认
    confirm_passwd_xpath = "//input[@type='password']"
    passwd_confirm_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"

    # 输入密码点击确认
    def send_passwd_confirm(self, passwd):
        self.back_current_page()
        self.find_elem(self.confirm_passwd_xpath).send_keys(passwd)
        self.find_elem(self.passwd_confirm_xpath).click()

    # 桌面类型下拉框还原xpath
    restore_xpath = u"//span[contains(text(),'还原')]/.."
    # 点击左侧vdi设置
    vdi_policy = u"//a[text()='VDI云桌面设置']"
    # 开启vdi按钮
    vdi_open_button = u"//label[text()='VDI云桌面：']/following-sibling::div/div"
    # vdi 桌面类型选择
    cd_type_vdi = u"//*[@id='scrollpane-vdiPolicy']//*[contains(text(),'桌面类型：')]/parent::div//input"
    # 镜像选择
    img_name = u"//span[contains(text(),'{}')]"
    # 确认按钮xpath
    confirm_xpath1 = u"//*[@class='dialog-footer']//span[contains(text(),'确认')]"

    def create_group_openvdi(self, group_name, img_name, cd_type=u"个性"):
        """新增组,开启VDI特性，其他属性均为默认"""
        self.del_group_exist(group_name)
        time.sleep(3.5)
        self.find_elem(self.new_group_xpath).click()
        time.sleep(1)
        self.find_elem(self.group_name_xpath).send_keys(group_name)  # 输入用户组名称
        self.find_elem(self.vdi_policy).click()  # 点击左侧vdi设置
        self.find_elem(self.vdi_open_button).click()  # 开启VDI特性
        time.sleep(2)
        if cd_type == u"还原":
            self.find_elem(self.cd_type_vdi).click()  # 点击桌面类型
            self.find_elem(self.restore_xpath).click()  # 点击还原
        self.find_elem(self.chose_mirrori_xpath).click()  # 点击绑定镜像
        self.scroll_into_view(self.img_name.format(img_name), click_type=1)
        self.find_elem(self.img_name.format(img_name)).click()  # 绑定镜像
        time.sleep(2)
        # self.find_elem(self.cd_type_vdi).click()  # 点击桌面类型选择，收回镜像选择下拉框
        self.find_elem(self.vdi_policy).click()  # 点击左侧vdi设置
        time.sleep(1)
        self.find_elem(self.confirm_xpath1).click()

    # 点击左侧idv设置
    idv_policy = u"//a[text()='IDV云终端设置']"
    # 开启idv按钮
    idv_open_button = u"//label[text()='IDV云终端：']/following-sibling::div/div"
    # 点击选择桌面类型
    cd_type_idv = u"//label[contains(text(),'桌面类型：')]/..//input"
    # 绑定镜像xpath
    chose_idvmirrori_xpath = u"//*[@id='scrollpane-idvPolicy']//*[contains(text(),'绑定镜像：')]/parent::div//input"

    def create_group_openidv(self, group_name, cd_type, img_name, cloud_disk=0, cloud_size="5"):
        """新增组，开启IDV特性，是否为还原以传参为准"""
        self.del_group_exist(group_name)
        time.sleep(3.5)
        self.find_elem(self.new_group_xpath).click()  # 点击新增
        time.sleep(1)
        self.find_elem(self.group_name_xpath).send_keys(group_name)  # 输入用户组名称
        self.find_elem(self.idv_policy).click()  # 点击左侧idv设置
        self.find_elem(self.idv_open_button).click()  # 开启IDV特性
        time.sleep(1)
        if cd_type == u"还原":
            self.click_elem(self.cd_type_idv)  # 点击选择桌面类型
            time.sleep(0.5)
            self.click_elem(self.restore_xpath)  # 点击桌面类型为还原桌面
            # self.select_list_chose(u"//label[contains(text(),'桌面类型：')]/..//input", u"还原")  # 选择镜像类型为还原
        self.find_elem(self.chose_idvmirrori_xpath).click()  # 点击绑定镜像
        self.scroll_into_view(self.img_name.format(img_name), click_type=1)
        self.find_elem(self.img_name.format(img_name)).click()  # 绑定镜像
        time.sleep(1)
        if cloud_disk == 1:
            self.click_elem(self.vdi_per_net_disk_xpath)  # 点击左侧启用个人云盘
            self.click_elem(self.is_x_disk_open)
            self.clear_text_info(self.edit_xdisk_xpath)
            self.find_elem(self.edit_xdisk_xpath).send_keys(cloud_size)
        self.find_elem(self.confirm_xpath1).click()

    # 点击某个用户组
    click_group_xpath = u"//div[contains(text(),'{}')]"

    def click_group(self, name):
        """点击具体某个用户组"""
        self.find_elem(self.click_group_xpath.format(name)).click()  # 点击具体某个组

    # 新建用户
    new_user = u"//span[contains(text(),'新建用户')]"
    # 新建用户_用户名
    user_name_xpath = "//*[@for='userBaseInfo.userName']/following-sibling::div/div/input"
    # 新建用户_姓名
    real_name_xpath = "//*[@for='userBaseInfo.realName']/following-sibling::div/div/input"

    def create_user_in_group(self, group_name, user_name, real_name):
        """在具体某个用户组下创建非自定义用户"""
        self.search_info(user_name)
        if self.elem_is_exist("//*[@class='el-table__row '][1]") == 0:
            self.del_user(passwd)
            self.find_elem(u"//p[contains(text(), '删除用户成功')]")
            time.sleep(2)
        self.scroll_into_view(self.group_xpath.format(group_name), click_type=1)  # 鼠标滚动到用户组
        self.click_group(group_name)  # 点击某个用户组
        self.find_elem(self.new_user).click()  # 点击新建用户
        self.find_elem(self.user_name_xpath).send_keys(user_name)  # 输入用户名称
        self.find_elem(self.real_name_xpath).send_keys(real_name)  # 输入用户姓名
        self.find_elem(self.confirm_xpath1).click()  # 点击确认按钮
        try:
            self.find_elem(u"//p[contains(text(), '用户创建成功！')]")
            time.sleep(2)
        except Exception as e:
            time.sleep(3)

    # 选中所有
    all_box = u"//*[@class='has-gutter']//label[1]//span[@class='el-checkbox__inner']"
    # 删除用户
    del_user_button = u"//span[contains(text(),'删除用户')]"
    # 删除
    del_resure_button = u"//button[@class='el-button el-button--default el-button--mini is-round el-button--primary ']"

    def del_user(self, password):
        """删除用户"""
        self.click_elem(self.all_box)
        self.click_elem(self.del_user_button)  # 点击删除
        self.click_elem(self.del_resure_button)  # 确认删除
        self.send_passwd_confirm(password)  # 输入密码并点击确认
        time.sleep(2)

    # 具体组后的删除按钮
    del_group_button = u"//div[contains(text(),'{}')]/..//button[2]"

    def del_group(self, name, password=passwd):
        """删除用户组"""
        self.scroll_into_view(self.click_group_xpath.format(name), click_type=1)
        self.chainstay(self.click_group_xpath.format(name))
        self.find_elem(self.delete_a_group_xpath.format(name)).click()  # 点击具体组后的删除按钮
        self.click_elem(self.del_resure_button)  # 点击删除
        self.send_passwd_confirm(password)
        time.sleep(0.3)

    def del_group_exist(self, name):
        """删除已存在用户组"""
        if name in self.get_value(self.all_group_xpath):
            self.scroll_into_view(self.click_group_xpath.format(name), click_type=1)
            self.chainstay(self.click_group_xpath.format(name))
            self.find_elem(self.delete_a_group_xpath.format(name)).click()  # 点击具体组后的删除按钮
            self.click_elem(self.del_resure_button)  # 点击删除
            self.send_passwd_confirm(passwd)
            time.sleep(0.3)

    # 用户等多操作按钮
    user_more_xpath = u"//*[@class='el-table__body']//span[contains(text(),'更多')]"
    # 编辑操作
    editor_btns_xpath = u"//li[contains(text(),'编辑')]"
    # vdi 开启switch按钮
    vdi_isopen_switch = u"//label[contains(text(),'VDI云桌面：')]/..//div[contains(@role,'switch')]"
    # 个性下拉选择
    cus_select_xpath = u"//span[contains(text(),'个性')]/.."
    # 根据镜像名选择删除要删除的镜像
    del_img_icon = u"//span[contains(text(),'{}')]/..//i[contains(@class,'el-tag__close')]"
    # 修改用户再次确定
    resure_btns = u"//span[contains(text(),'确定')]"
    # 用户编辑下的 x 退出按钮
    back_btns = "// i[ @class ='el-dialog__close el-icon el-icon-close']"

    # idv-编辑用户-镜像下拉款
    img_input1 = u"//label[contains(text(),'绑定镜像：')]/..//div[@class='el-select']"

    # 编辑用户--更改vdi相应的属性
    def edit_user_vdi(self, user_name, cd_type=u"个性", delimg_name=None, add_img=None, isdel=False, isadd=False,
                      local_disk=None):
        self.search_info(name=user_name)  # 搜索用户
        time.sleep(0.5)
        self.click_elem(self.user_more_xpath)  # 点击更多操作
        self.click_elem(self.editor_btns_xpath)  # 点击编辑
        self.find_elem(self.vdi_policy).click()  # 点击左侧vdi设置
        time.sleep(2)
        if cd_type == u"还原":
            self.find_elem(self.cd_type_vdi).click()  # 点击桌面类型
            self.find_elem(self.restore_xpath).click()  # 点击还原
        if cd_type == u"个性":
            self.find_elem(self.cd_type_vdi).click()  # 点击桌面类型
            self.find_elem(self.cus_select_xpath).click()  # 点击个性
        if isdel == True:  # 是否选择删除镜像
            self.click_elem(self.del_img_icon.format(delimg_name))
            time.sleep(1)
        if isadd == True:  # 是否添加镜像
            self.find_elem(self.img_input1).click()  # 点击绑定镜像
            self.scroll_into_view(self.img_name.format(add_img), click_type=1)
            self.find_elem(self.img_name.format(add_img)).click()  # 绑定镜像
            self.find_elem(self.vdi_policy).click()  # 点击左侧收起下拉框
            time.sleep(1)
        if local_disk != None:  # 本地盘使用权限
            self.checkbox_set(checkbox_name=u"允许使用本地盘", is_open=local_disk)
        self.find_elem(self.confirm_xpath1).click()  # 点击确认
        self.find_elem(self.resure_btns).click()  # 点击确定
        if self.elem_is_exist(self.confirm_passwd_xpath) == 0:
            self.send_passwd_confirm(passwd=passwd)  # 输入用户名和密码

    internal_memory_xpath = "//*[contains(text(),'内存 ')]/..//input"
    sys_disk_xpath = "//*[contains(text(),'系统盘')]/..//input"
    d_disk_xpath = "//*[contains(text(),'个人盘')]/..//input"
    x_disk_xpath = "//*[contains(text(),'云盘大小')]/..//input"
    x_disk_is_open = "//label[contains(text(),'云盘')]/..//div[@role='switch']"

    def editor_user_disk(self, user_name, cpu=None, internal_memory=None, sys_disk=None, d_disk=None, x_disk=None,
                         send_password=0):
        """修改用户各种盘大小"""
        time.sleep(2)
        self.search_info(name=user_name)  # 搜索用户
        time.sleep(0.5)
        self.click_elem(self.user_more_xpath)  # 点击更多操作
        self.click_elem(self.editor_btns_xpath)  # 点击编辑
        self.find_elem(self.vdi_policy).click()  # 点击左侧vdi设置
        if cpu != None:
            self.click_elem(self.cpu_choose_xpath)
            time.sleep(0.5)
            self.click_elem(self.cpu_number_xpath.format(cpu))
        if internal_memory != None:
            self.clear_text_info(self.internal_memory_xpath)
            self.find_elem(self.internal_memory_xpath).send_keys(internal_memory)
        if sys_disk != None:
            self.clear_text_info(self.sys_disk_xpath)
            self.find_elem(self.sys_disk_xpath).send_keys(sys_disk)
        if d_disk != None:
            time.sleep(0.5)
            self.clear_text_info(self.d_disk_xpath)
            self.find_elem(self.d_disk_xpath).send_keys(d_disk)
        if x_disk != None:
            self.scroll_into_view(self.x_disk_is_open, click_type=1)
            info = self.get_elem_attribute(self.x_disk_is_open, 'class')
            if "is-checked" not in info:
                self.click_elem(self.x_disk_is_open)
            self.clear_text_info(self.x_disk_xpath)
            self.find_elem(self.x_disk_xpath).send_keys(x_disk)
        time.sleep(0.5)
        self.find_elem(self.confirm_xpath1).click()  # 点击确认
        self.find_elem(self.resure_btns).click()  # 点击确定
        if self.elem_is_exist(self.confirm_passwd_xpath) == 0 and send_password == 0:
            self.send_passwd_confirm(passwd=passwd)  # 输入用户名和密码

    def editor_group_vdi_disk(self, gp_name, internal_memory=None, sys_disk=None, d_disk=None, x_disk=None):
        """修改用户组各种盘属性"""
        self.edit_group(gp_name)
        self.find_elem(self.vdi_policy).click()  # 点击左侧vdi设置
        if internal_memory != None:
            self.clear_text_info(self.internal_memory_xpath)
            self.find_elem(self.internal_memory_xpath).send_keys(internal_memory)
        if sys_disk != None:
            self.clear_text_info(self.sys_disk_xpath)
            self.find_elem(self.sys_disk_xpath).send_keys(sys_disk)
        if d_disk != None:
            self.clear_text_info(self.d_disk_xpath)
            self.find_elem(self.d_disk_xpath).send_keys(d_disk)
        if x_disk != None:
            self.scroll_into_view(self.x_disk_is_open, click_type=1)
            info = self.get_elem_attribute(self.x_disk_is_open, 'class')
            if "is-checked" not in info:
                self.click_elem(self.x_disk_is_open)
            self.clear_text_info(self.x_disk_xpath)
            self.find_elem(self.x_disk_xpath).send_keys(x_disk)
        self.find_elem(self.confirm_xpath1).click()  # 点击确认
        self.find_elem(self.resure_btns).click()  # 点击确定
        if self.elem_is_exist(self.confirm_passwd_xpath) == 0:
            self.send_passwd_confirm(passwd=passwd)  # 输入用户名和密码

    # idv-编辑用户-镜像下拉款
    img_input = u"//*[@placeholder='请选择1个镜像']"

    # 编辑用户--更改idv相应的属性
    def edit_user_idv(self, user_name, cd_type=u"个性", delimg_name=None, add_img=None, isdel=False, isadd=False,
                      local_disk=None):
        self.search_info(name=user_name)  # 搜索用户
        time.sleep(0.5)
        self.click_elem(self.user_more_xpath)  # 点击更多操作
        self.click_elem(self.editor_btns_xpath)  # 点击编辑
        self.find_elem(self.idv_policy).click()  # 点击左侧idv设置
        time.sleep(2)
        self.find_elem(self.cd_type_idv).click()  # 点击桌面类型
        if cd_type == u"还原":
            self.find_elem(self.restore_xpath).click()  # 点击还原
        if cd_type == u"个性":
            self.find_elem(self.cus_select_xpath).click()  # 点击个性
        if isdel == True:  # 是否选择删除镜像
            self.click_elem(self.del_img_icon.format(delimg_name))
            time.sleep(1)
        if isadd == True:  # 是否添加镜像
            time.sleep(0.5)
            self.find_elem(self.img_input).click()  # 点击绑定镜像
            self.scroll_into_view(self.img_name.format(add_img), click_type=1)
            self.find_elem(self.img_name.format(add_img)).click()  # 绑定镜像
            time.sleep(1)
        if local_disk != None:  # 本地盘使用权限
            self.checkbox_set(checkbox_name=u"允许使用本地盘", is_open=local_disk)
        self.scroll_into_view(self.confirm_xpath1, click_type=1)
        self.find_elem(self.confirm_xpath1).click()  # 点击确认
        self.find_elem(self.resure_btns).click()  # 点击确定
        flag = 0
        if self.elem_is_exist(self.confirm_passwd_xpath) == 0:
            self.send_passwd_confirm(passwd=passwd)  # 输入用户名和密码
            flag = 1
            return flag
        time.sleep(3)

    vlan_xpath = "//*[text()='VLAN：']/..//div[@class='el-input']//input"

    # 编辑用户关于VLAN部分
    def editor_user_vlan(self, user_name, vlan):
        self.search_info(name=user_name)  # 搜索用户
        time.sleep(0.5)
        self.click_elem(self.user_more_xpath)  # 点击更多操作
        self.click_elem(self.editor_btns_xpath)  # 点击编辑
        self.find_elem(self.vdi_policy).click()  # 点击左侧vdi设置
        time.sleep(1)
        self.clear_text_info(self.vlan_xpath)
        self.find_elem(self.vlan_xpath).send_keys(vlan)
        self.find_elem(self.confirm_xpath1).click()  # 点击确认
        self.find_elem(self.resure_btns).click()  # 点击确定

    sys_feedback = "//*[@class='sk-IdvPolicy__terminal--spaceTip']"

    # 搜索用户并点击编辑
    def searc_click_edit(self, user_name):
        self.search_info(user_name)
        time.sleep(0.5)
        self.click_elem(self.user_more_xpath)  # 点击更多操作
        self.click_elem(self.editor_btns_xpath)  # 点击编辑

    # 关闭或开idv-vid特性(switch开关),后续有需要可补充到该方法中
    def switch_set(self, switch, is_open):
        if switch == "idv":
            class_info = self.get_elem_attribute(self.idv_open_button, 'class')
        elif switch == "vdi":
            class_info = self.get_elem_attribute(self.vdi_open_button, 'class')
        flag = 0
        if is_open == 'close':
            if class_info.__contains__("is-checked"):
                self.click_elem(self.idv_open_button)
                flag = 1
            else:
                pass
        elif is_open == 'open':
            if not class_info.__contains__("is-checked"):
                self.click_elem(self.idv_open_button)
                flag = 1
            else:
                pass
        else:
            print(u"输入的参数错误")
        return flag

    # checkbox,根据参数传进来确定是哪个checkbox
    checkbox_xpath = u"//span[contains(text(),'{}')]/.."
    click_check_box = u"//span[contains(text(),'{}')]/../span[1]"

    # CheckBox开启或关闭
    def checkbox_set(self, checkbox_name, is_open):
        class_info = self.get_elem_attribute(self.checkbox_xpath.format(checkbox_name), 'class')
        flag = 0
        if is_open == 'close':
            if class_info.__contains__("is-checked"):
                self.click_elem(self.click_check_box.format(checkbox_name))
                flag = 1
            else:
                pass
        elif is_open == 'open':
            if not class_info.__contains__("is-checked"):
                self.click_elem(self.click_check_box.format(checkbox_name))
                flag = 1
            else:
                pass
        else:
            print(u"传入的参数有误")
        return flag

    # 分组后的编辑按钮
    edit_group_button = u"//div[contains(text(),'{}')]/..//*[contains(@class,'el-icon-edit')]/.."
    confirm_xpath2 = u"//*[text()='确认']"

    # 编辑分组-idv部分
    def edit_gp_idv(self, gp_name, isopen_idv=None, idv_or_vdi=u"idv", cd_type=None, image=None, isopen_local_disk=None,
                    check_name=u"使用本地盘"):
        """
        :param gp_name: 需要修改的组的名称
        :param isopen_idv: 是否开启idv特性，参数为open,close,不传参为不做修改
        :param idv_or_vdi: 此处由于是编辑组的idv所以默认传参是idv，可修改
        :param cd_type:桌面类型，不传参跳过
        :param image:绑定镜像，不传参跳过
        :param isopen_local_disk:
        :param check_name:开启某个复选框，此处选择的是本地盘，可根据具体情况传参
        :return:
        """
        time.sleep(1)
        self.scroll_into_view(self.click_group_xpath.format(gp_name))
        self.find_elem(self.edit_group_button.format(gp_name)).click()  # 点击具体组后的编辑按钮
        self.find_elem(self.idv_policy).click()  # 点击左侧idv设置
        if isopen_idv is not None:  # 开启或关闭idv特性
            self.switch_set(idv_or_vdi, isopen_idv)
        if cd_type is not None:
            self.select_list_chose(u"//label[contains(text(),'桌面类型：')]/..//input", cd_type)  # 选择镜像类型
        if image is not None:
            time.sleep(0.5)
            self.click_elem(self.chose_idvmirrori_xpath)  # 点击绑定镜像
            self.scroll_into_view(self.img_name.format(image), click_type=1)
            self.find_elem(self.img_name.format(image)).click()  # 绑定镜像
            time.sleep(1)
        if isopen_local_disk is not None:
            self.checkbox_set(check_name, isopen_local_disk)  # 是否开启本地盘
        self.click_elem(self.confirm_xpath2)  # 点击确认
        self.click_elem(self.sure_xpath)  # 点击确定
        time.sleep(2)
        if self.elem_is_exist(self.confirm_passwd_xpath) == 0:
            self.send_passwd_confirm(passwd=passwd)  # 输入用户名和密码
            time.sleep(3)

    # 元素点击
    def click(self, locatotr):
        self.click_elem(locator=locatotr)

    # ---------------------------------------------------------------new---------------------------------------------------------------
    # 90

    # 报错信息
    ipdelete_errormsg_xpath = "//*[@class='el-message__content']"

    # 80
    # 云桌面管理
    table_manage_xpath = u"//*[contains(text(),'云桌面管理')]"
    # 更多操作
    desk_more_xpath = "//*[contains(text(),'{0}')]/ancestor::tr//button"
    # 点击云桌面日志
    desk_log_xpath = "//*[@x-placement='bottom-start']//*[contains(text(),'云桌面日志')]/ancestor::div"
    # 不能收集云桌面日志提示
    desklog_errormsg_xpath = "// *[contains(text(), '云桌面处于离线或休眠状态，不能实时收集日志')]"

    # 89
    # 将要查找的用户名填入text中
    find_username_xpath = "//*[@class='fl']//*[@class='el-input__inner']"
    # 查找按钮
    find_button_xpath = "// *[@class ='fl'] // *[@ class ='el-input__icon sk-icon-search sk-toolbar__icon el-tooltip item']"
    # 勾选用户
    check_auser_xpath = "//*[contains(text(),'{0}')]/ancestor::tr//*[@class='el-checkbox__inner']"
    # 清空成功信息
    clearip_successmsg_xpath = "//*[contains(text(),'清空IP操作成功！')]"

    # 94
    # 自定义列表按钮
    user_attributelist_button_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round is-noLabel el-dropdown-selfdefine']"
    # 自定义列表已勾选的列
    user_attributelist_selected_xpath = "//*[@class='el-icon-check']/../..//*[@class='sk-column-item']//*[@class='el-icon-check']"  # 自定义列表已勾选的列
    # 自定义列表未勾选的列
    user_attributelist_unselected_xpath = "//*[@class='icon-empty']"
    # 显示某属性
    show_attribute_xpath = u"//*[@class='el-dropdown-menu el-popper el-dropdown-menu--column']//*[text()='{}']"

    # 95
    # 用户管理单独选择列 format传参选择
    userattribute_select_xpath = u"//*[@class='el-table__header']//*[contains(text(),'{0}')]/parent::th"
    # 未被选择的列
    not_select_column = "//*[@class='has-gutter']//node()[contains(@class,'is-noshow')]"
    # 所有列
    all_column = "//*[@class='has-gutter']//node()[contains(@class,'el-table_')]"
    # 用户管理按列增序排列
    user_sort_add_xpath = u"//*[@class='caret-wrapper']/../..//*[contains(.,'{0}')]//node()[@class='sort-caret ascending']"
    # 返回的搜索的所有结果
    all_search_results_xpath = "//*[contains(@class,'el-table__row')]/.."
    # all_search_results_xpath2 = "//*[@class='el-table__row ']/.."
    # 云桌面管理单独选择列 format传参选择
    column_select_xpath = u"//*[contains(@class,'has-gutter')]//div[contains(.,'{0}')]/.."
    # 滚动
    roll_xpath = u"//*[@class='el-table__header']//*[contains(text(),'云盘')]"
    # 云盘属性
    clouddisk_attribute_xpath = u"//*[text()='云盘：']/ancestor::div[@class='el-form-item']//span[@class='el-switch__core']"
    # 84
    # 点击模板导入
    import_model_xpath = u"//*[contains(text(),'模板导入')]"
    # 点击模板下载
    download_model_xpath = u"//*[contains(text(),'模板下载')]"
    # 点击上传文件
    upload_usermodel = u"//*[contains(text(),'上传文件')]"

    # 开始导入
    start_importuser_xpath = u"//*[contains(text(),'开始导入')]"
    # 导入成功提醒
    import_usermodel_success_xpath = u"//*[contains(text(),'用户导入成功！')]"
    # 78
    # 选择用户后的更多
    choose_a_user = u"//*[contains(text(),'{0}')]/ancestor::tr//*[contains(text(),'更多')]"
    # 还原云桌面
    renew_cdesk_xpath = u"//*[@x-placement='bottom-start']//*[contains(text(),'还原云桌面')]/ancestor::div"
    # 还原按钮
    renew_button = u"//*[@class='el-message-box__btns']//*[contains(text(),'还原')]"
    # 输入密码
    pwd_input_xpath = "//*[@class='el-dialog__body']//*[@class='el-input__inner']"

    # 76
    # 删除用户
    delete_user_xpath = u"//span[contains(text(),'删除用户')]"
    # 重要操作告警提示
    import_prompt = u"//*[contains(text(),'删除用户以及用户下的所有数据包括系统盘数据、个人盘数据、云盘数据。')]"
    # 确认删除
    confirm_deleteuser = u"//*[@class='el-message-box__btns']//*[contains(text(),'删除')]"
    # 无法删除报错
    delete_errer_msg = "//*[@class='el-message__content']"
    # 删除成功提示
    delete_success_msg = "//*[@class='el-notification__content']"
    # 新建用户时填充用户名等
    user_info_xpath = u"//*[contains(text(),'{}')]/parent::div//descendant::input"
    # 64
    # 点击vdi菜单
    vdi_set_xpath = u"//*[contains(text(),'VDI云桌面设置')]"
    # 点击云盘菜单
    xdisk_set_xpath = u"//*[contains(text(),'启用个人云盘')]"
    # vdi点击绑定镜像
    chose_vdimirrori_xpath = u"//*[@id='scrollpane-vdiPolicy']//*[contains(text(),'绑定镜像：')]/parent::div//descendant::input"
    # vdi选择镜像

    # vdi_mirror_xpath = u"//*[@class='el-select-dropdown__item hover']//*[contains(text(),'{0}')]"
    vdi_mirror = "//*[contains(text(), '{0}')] / parent::li"
    # 更改失败提示
    edit_falsemsg_xpath = u"//*[@class='el-message__content']"
    # 输入密码框
    pwd_xpath = u"//*[contains(text(),'请确认密码')]/ancestor::div//*[@class='el-input__inner']"
    # 更改VLAN数量
    VLAN_num_increase = u"//*[contains(text(),'VLAN')]/parent::div//*[@class='el-input-number__increase']"
    VLAN_num_decrease = u"//*[contains(text(),'VLAN')]/parent::div//*[@class='el-input-number__decrease']"
    # 关闭编辑框
    close_xpath = "//*[@class='el-dialog__close el-icon el-icon-close']"
    # 更改内存
    internal_memory_increase = u"//*[contains(text(),'内存')]/parent::div//*[@class='el-input-number__increase']"
    internal_memory_decrease = u"//*[contains(text(),'内存')]/parent::div//*[@class='el-input-number__decrease']"
    # 修改系统盘
    cdesk_increase = u"//*[contains(text(),'系统盘')]/parent::div//*[@class='el-input-number__increase']"
    cdesk_decrease = u"//*[contains(text(),'系统盘')]/parent::div//*[@class='el-input-number__decrease']"
    # 修改个人盘
    ddesk_increase = u"//*[contains(text(),'个人盘')]/parent::div//*[@class='el-input-number__increase']"
    ddesk_decrease = u"//*[contains(text(),'个人盘')]/parent::div//*[@class='el-input-number__decrease']"
    # 修改CPU
    CPU_choose = u"//*[@x-placement='bottom-start']//*[@class='el-select-dropdown__item selected']"
    CPU_num = u"//*[contains(text(),'CPU')]/parent::div//*[@class='el-input__inner']"
    CPU_increase = u"//span[text()='8']"
    CPU_decrease = u"//span[text()='4']"
    # 利旧传输数据
    trans_info_xpath = u"//*[contains(text(),'利旧传输数据：')]/parent::div//descendant::input"
    choose_trans = u"//*[contains(text(),'{0}')]"
    # 双网身份验证
    check_identity = u"//*[contains(text(),'双网身份验证：')]/parent::div//*[@class='el-checkbox__inner']"
    # 云桌面IP
    ip_info_xpath = u"//*[contains(text(),'{0}')]/parent::div//descendant::input"

    # 备用DNS
    prepare_DNS_xpath = u"//*[contains(text(),'云桌面备用DNS：')]/parent::div//descendant::input"
    # 修改成功提示
    edit_succmsg_xpath = "//*[@class='el-notification__content']"
    # 14
    # VLAN后的输入框
    edit_VLAN_xpath = "//*[contains(text(),'VLAN')]/parent::div//*[@class='el-input__inner']"
    click_VLAN_xpath = "//*[contains(text(),'VLAN')]/parent::div//*[@class='el-input']"
    # 关闭确认框
    close_tag_xpath = "//*[@class='el-message-box__close el-icon-close']"
    # 选择用户组
    choose_a_group = u"//div[@class='custom-tree-node']/descendant::div[contains(text(),'{0}')]"
    # choose_a_group = u"//*[@class='user-group-body el-row clearAroundPadding']//*[contains(text(),'{0}')]"
    # 37
    # 内存
    internal_memory_text_xpath = u"//*[contains(text(),'内存 (GB)：')]/parent::div//*[@class='el-input__inner']"
    # 编辑用户组
    edit_a_group = u"//*[@class='user-group']//*[contains(text(),'{0}')]//parent::div//parent::div[@class='el-tree-node__content']//*[@class='el-button tree-node-btn el-button--text el-button--medium is-round is-noLabel']"
    # 34
    # 系统盘输入框
    cdesk_val_xpath = u"//*[contains(text(),'系统盘')]/parent::div//*[@class='el-input__inner']"
    # 个人盘输入框
    ddesk_val_xpath = u"//*[contains(text(),'个人盘')]/parent::div//*[@class='el-input__inner']"

    # 93
    drag_source = "//*[@class='sk-split-pane-resizer is-vertical ']"
    drag_target = u"//*[contains(text(),'共 ')]"

    # 84
    # 点击组
    parent_group_xpath = u"//*[contains(text(),'{0}')]"

    # 确认后报错
    confirm_error_xpath = u"//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']"
    # 关闭导入模板的界面
    close_import_xpath = "//*[@class='el-dialog__close el-icon el-icon-close']"
    # 报错信息
    error_msg_box_xpath = "//*[@class='el-message-box']"
    # 确认导入
    confirm_import_xpath = "//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']"
    # 用户管理全选单选框
    select_users_xpath = u"//div[contains(text(),'用户名')]/ancestor::tr//*[@class='el-checkbox__inner']"
    # 删除用户组
    delete_a_group_xpath = u"//*[@class='user-group']//*[contains(text(),'{0}')]//parent::div//parent::div[@class='el-tree-node__content']//i[@class='el-icon-delete']/parent::button"

    # 73
    # 云桌面关机
    close_vdi_xpath = u"//li[contains(text(),'关机')]"
    # 确认关机
    close_button_xpath = u"//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']//*[contains(text(),'关机')]"
    # 更多
    cdesk_more_operate = u"//*[contains(text(),'{0}')]/ancestor::tr//button"
    # 第一行更多
    cdesk_more_operate_first = u"//*[contains(text(),'更多')]/ancestor::tr//button"
    # 网盘后输入框
    edit_xdisk_xpath = "//*[contains(text(),'云盘大小(GB)：')]/parent::div//*[@class='el-input__inner']"
    click_xdisk_xpath = "//*[contains(text(),'云盘大小(GB)：')]/parent::div//*[@class='el-input']"
    # 获取云桌面ip
    user_desk_ip = "//*[@class='el-table_1_column_14  ']//div//span"
    # 71
    # 云桌面ip列
    vdi_desktop_ip_xpath = "//*[@class='el-table__header-wrapper']//*[contains(text(),'VDI桌面IP')]"

    # 72
    # 每个用户可分配的最大网盘空间
    max_xdisk_xpath = u"//span[contains(text(),'每个用户最大可分配')]"
    # 扩容云盘超过可分配的最大值报错提示
    increase_xdisk_xpath = u"//*[@class='el-form-item__error']"
    # 编辑页面
    edit_page = u"//*[@class='el-dialog']"
    # 50
    # 外设策略
    external_equipment_xpath = u"//*[contains(text(),'外设策略')]"
    # 点击存储设备前的选择框(关闭)
    close_usb_cc_ok_xpath = u"//*[contains(text(),'{0}')]/parent::label/span[@class='el-checkbox__input is-checked']"
    # 点击存储设备前的选择框(打开)
    open_usb_cc_ok_xpath = u"//*[contains(text(),'{0}')]/parent::label/span[@class='el-checkbox__input']"
    # 30
    # 跳转到镜像管理界面
    mirror_manage_xpath = u"//*[@class='sk-icon sk-icon-images1']"
    # 进入镜像框架
    frame_id_xpath = u"//*[@id='frameContent']"
    # 进入提示框ifream
    prompt_xpath = u"//*[@id='layui-layer-iframe1']"
    # 点击用户磁盘计算
    user_disk_val_xpath = u"//*[contains(text(),'用户磁盘计算')]"
    # 需要创建的用户数
    user_num_xpath = u"//*[@id='desk_top1_size']"
    # 用户最大可分配的磁盘大小
    max_disk_xpath = u"//*[@id='caluResult']"
    # 点击确认进行计算
    calcu_xpath = u"//*[@class='btn_sq_dark btn_left']"
    # 关闭计算框
    close_calsu_xpath = u"//*[@class='layui-layer-ico layui-layer-close layui-layer-close1']"
    # 20
    # 查看云盘状态
    xdisk_value_xpath = u"//*[@role='srollpanel']//*[contains(text(),'云盘')]"
    # 云桌面ip
    cloud_ip_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[8]//span"

    # ------------------------------------------------------------------------------------------------------------------------------
    # ---------------------------------------------------------new----------------------------------------------------

    def edit_text(self, locator, text=''):
        """修改文本框"""
        time.sleep(1)
        self.find_elem(locator).click()
        time.sleep(1)
        self.find_elem(locator).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(locator).send_keys(text)
        return text

    # 89.90

    def ip_delete(self):
        """清空ip"""
        self.find_elem(self.more_operate_xpath).click()
        self.find_elem(self.clear_ip_xparh).click()

    def deleteip_errormsg_get(self):
        """获取清空ip报错信息"""
        try:
            return self.find_elem(self.ipdelete_errormsg_xpath).text
        except:
            return ''

    # 79,80

    def goto_cdesk_page(self):
        """云桌面页面"""
        self.find_elem(self.table_manage_xpath).click()
        #     获取终端云桌面ip

    def get_cloud_desk_ip(self, name):
        return self.find_elem(self.cloud_ip_xpath.format(name)).text

    # 获取日志报错信息
    def desklog_errormsg_get(self):
        """云桌面页面"""
        try:
            return self.find_elem(self.desklog_errormsg_xpath).text
        except:
            return ''

    def desklog_errormsg_tips(self):
        """鼠标移动到日志收集按钮上确认日志报错提示存在"""
        try:
            self.click_elem(self.cdesk_more_operate_first)
            time.sleep(1)
            self.click_elem(self.desk_log_xpath)
            time.sleep(1)
            final = self.find_elem(self.desklog_errormsg_xpath).text
            self.back_current_page()
            return final
        except:
            return ''

    def collect_log(self, username):
        """收集日志"""
        time.sleep(2)
        self.find_elem(self.desk_more_xpath.format(username)).click()
        self.find_elem(self.desk_log_xpath).click()
        time.sleep(2)

    # def ensure_ascending_sort(self):
    # self.find_elem(self.status)

    def find_user(self, username):
        """查找用户"""
        self.find_elem(self.find_username_xpath).click()
        self.edit_text(self.find_username_xpath, username)
        self.find_elem(self.find_button_xpath).click()

    def clear_find_user(self):
        """清空查找用户框"""
        self.find_elem(self.find_username_xpath).click()
        self.find_elem(self.find_username_xpath).clear()

    def choose_user(self, username):
        """选择用户"""
        self.find_elem(self.check_auser_xpath.format(username)).click()

    def check_ipclear(self):
        """验证清空ip是否成功"""
        try:
            return self.find_elem(self.clearip_successmsg_xpath)
        except:
            return ''

    # 94

    def attribute_list_drag(self):
        """用户管理显示项拖动"""
        flag_list = [1, 0]
        time.sleep(1)
        self.find_elem(self.user_attributelist_button_xpath).click()
        while len(self.find_elems(self.user_attributelist_selected_xpath)) != 1:
            self.find_elem(self.user_attributelist_selected_xpath).click()
        while len(self.find_elems(self.user_attributelist_unselected_xpath)) != 2:
            self.find_elem(self.user_attributelist_unselected_xpath).click()
        self.driver.refresh()
        all_num = len(self.find_elems(self.all_column))  # 获取总数
        temp_list = []
        for i in range(all_num):
            temp_list.append(self.find_elems(self.all_column)[i].text.strip())
        while '' in temp_list:
            temp_list.remove('')  # 过滤掉空元素，剩下都是显式元素
        vis_num = len(temp_list)
        if all_num - vis_num - 2 == 2:
            flag_list[0] = 1
        time.sleep(1)
        temp_text1 = self.find_elem(self.userattribute_select_xpath.format(u'姓名')).get_attribute('class')
        temp_text2 = self.find_elem(self.userattribute_select_xpath.format(u'用户组')).get_attribute('class')
        if temp_text1.__contains__('can-drag-sort') and temp_text2.__contains__('can-drag-sort'):
            flag_list[1] = 1
        return flag_list

    # 95

    def show_user_attribute(self):
        """显示用户属性"""
        time.sleep(1)
        self.find_elem(self.user_attributelist_button_xpath).click()
        try:
            self.find_elems(self.user_attributelist_unselected_xpath)
        except:
            pass
        else:
            unselected_len = len(self.find_elems(self.user_attributelist_unselected_xpath))
            for i in range(unselected_len):
                self.find_elem(self.user_attributelist_unselected_xpath).click()
        self.find_elem(self.show_attribute_xpath.format(u"IDV")).click()
        self.find_elem(self.show_attribute_xpath.format(u"状态")).click()
        self.find_elem(self.show_attribute_xpath.format(u"类型")).click()
        self.find_elem(self.show_attribute_xpath.format(u"VDI")).click()
        self.find_elem(self.show_attribute_xpath.format(u"终端MAC")).click()

    def user_sort_rule(self):
        """用户姓名、用户名、用户组、绑定终端管理排序规则设置"""
        flag_list = [0, 0, 0]
        split_str = u"更多"
        sort_value_list = [u"用户名", u"姓名", u"用户组", u"绑定终端", u"IDV终端IP", u"IDV桌面IP", u"VDI终端IP", u"VDI桌面IP", u"云盘"]
        for i in range(len(sort_value_list)):
            self.find_elem(self.user_sort_add_xpath.format(sort_value_list[i])).click()
            time.sleep(2)
            temp_text = self.find_elem(self.all_search_results_xpath).text

            temp_text = temp_text.replace(' ', ' ' * 4)
            temp_text1 = temp_text.replace('\n', ' ' * 4)
            temp_text2 = temp_text1.split(split_str)
            temp_text3 = []
            while '' in temp_text2:
                temp_text2.remove('')
            if i <= 3:
                for j in range(len(temp_text2)):
                    temp_text3.append(temp_text2[j].strip().split(' ' * 4)[i])
                b = sorted(temp_text3)
                if b.__eq__(temp_text3):
                    flag_list[0] = 1
            if i > 3:

                for j in range(len(temp_text2)):
                    temp_text3.append(temp_text2[j].strip().split(' ' * 4)[i - 6])
                a = sorted(temp_text3)

                if a.__eq__(temp_text3):
                    flag_list[1] = 1
            time.sleep(2)

        self.driver.refresh()
        # 验证用户的增序按钮是否被选中
        time.sleep(2)
        temp_text = self.find_elem(self.all_search_results_xpath).text

        temp_text = temp_text.replace(' ', ' ' * 4)
        temp_text1 = temp_text.replace('\n', ' ' * 4)
        temp_text2 = temp_text1.split(split_str)
        temp_text3 = []
        while '' in temp_text2:
            temp_text2.remove('')

        for j in range(len(temp_text2)):
            temp_text3.append(temp_text2[j].strip().split(' ' * 4)[1])

        # 若点击用户名增序后文本不变，则正确
        self.find_elem(self.user_sort_add_xpath.format(sort_value_list[0])).click()

        temp_text = self.find_elem(self.all_search_results_xpath).text

        temp_text = temp_text.replace(' ', ' ' * 4)
        temp_text1 = temp_text.replace('\n', ' ' * 4)
        temp_text2 = temp_text1.split(split_str)
        temp_text4 = []
        while '' in temp_text2:
            temp_text2.remove('')

        for j in range(len(temp_text2)):
            temp_text4.append(temp_text2[j].strip().split(' ' * 4)[1])
        if temp_text3.__eq__(temp_text4):
            flag_list[2] = 1
        return flag_list

    # 82

    def download_usermodel(self):
        """下载用户模板"""
        self.find_elem(self.more_operate_xpath).click()
        self.find_elem(self.download_model_xpath).click()
        time.sleep(4)

    def import_usermodel(self):
        """导入用户模板"""
        time.sleep(2)
        self.find_elem(self.more_operate_xpath).click()
        time.sleep(2)
        self.find_elem(self.import_model_xpath).click()
        time.sleep(1)
        self.find_elem(self.upload_usermodel).click()

    def choose_usermodel(self, path):
        """选择要导入的用户模板"""
        self.upload(path)
        # flag = 0
        #
        # upload_file = automation.WindowControl(searchDepth=2, RegexName=u'.*打开.*')
        # # upload_file.ToolBarControl(ClassName="ToolbarWindow32")
        # # 定位到地址栏
        # upload_file.ButtonControl(Name=u"上一个位置").Click()
        #
        # # 输入地址栏，注意用automation
        # automation.SendKeys(path)
        # automation.SendKey(automation.Keys.VK_ENTER)
        # # 输入文件名
        # upload_file.EditControl(Name=u"文件名(N):").SendKeys(model)
        # upload_file.SplitButtonControl(Name=u"打开(O)").Click()  # 点击打开按钮
        #
        # return flag

    def confirm_import_usermodel(self):
        """确认导入模板"""
        self.find_elem(self.confirm_import_xpath).click()
        time.sleep(2)
        self.find_elem(self.start_importuser_xpath).click()
        time.sleep(2)
        try:
            return self.find_elem(self.import_usermodel_success_xpath).text
        except:
            print("导入失败")
            return ''

    # 78

    def renew_a_user(self, username):
        """还原用户"""
        self.find_elem(self.choose_a_user.format(username)).click()
        time.sleep(2)
        self.find_elem(self.renew_cdesk_xpath).click()
        time.sleep(2)

    def confirm_renew(self, passwd):
        """确认还原用户"""
        self.find_elem(self.renew_button).click()
        self.find_elem(self.pwd_input_xpath).send_keys(passwd)
        self.find_elem(self.confirm_button_xpath).click()

    # 76

    def delete_run_user(self, passwd):
        """删除运行用户"""
        self.find_elem(self.delete_user_xpath).click()
        self.find_elem(self.confirm_deleteuser).click()
        self.find_elem(self.pwd_input_xpath).send_keys(passwd)
        self.find_elem(self.confirm_button_xpath).click()
        try:
            return self.find_elem(self.delete_errer_msg).text
        except:
            return ''

    def delete_norun_user(self):
        """删除某个未运行的用户"""
        self.find_elem(self.delete_user_xpath).click()
        try:
            return self.find_elem(self.import_prompt).text
        except:
            return ''

    def confirm_delete_norun_user(self, passwd=passwd):
        """确认删除某个未运行的用户"""
        self.find_elem(self.confirm_deleteuser).click()
        self.find_elem(self.pwd_input_xpath).send_keys(passwd)
        self.find_elem(self.confirm_button_xpath).click()

        try:
            return self.find_elem(self.delete_success_msg).text
        except:
            return 0

    def login_client(self, name, pwd='123'):
        """用户用利旧登录vdi云桌面"""
        time.sleep(4)

        client_login(name, pwd)

    def close_client(self):
        """用户用利旧关闭vdi云桌面"""
        time.sleep(2)
        client_lvdi_close()

    def close_errormsg(self):
        """利旧客户端登入失败后退出报错信息"""
        time.sleep(2)
        client_error_passwd_click()

    def creat_user(self, uname, realname):
        """新增用户"""
        time.sleep(1)
        self.find_elem(self.new_user_xpath).click()
        time.sleep(1)
        self.find_elem(self.user_info_xpath.format(u'用户名')).send_keys(uname)
        time.sleep(1)
        self.find_elem(self.user_info_xpath.format(u'姓名')).send_keys(realname)
        time.sleep(1)

    def confirm_create_user(self):
        """确认新增用户"""
        self.find_elem(self.confirm_xpath1).click()

    def hide_attribute(self):
        """隐藏部分属性，使‘更多’按钮显示在桌面"""
        self.find_elem(self.user_attributelist_button_xpath).click()
        selected_attribute_num = len(self.find_elems(self.user_attributelist_selected_xpath))
        if selected_attribute_num > 2:
            for i in range(selected_attribute_num - 2):
                self.find_elem(self.user_attributelist_selected_xpath).click()

    def vdi_set(self):
        """点击vdi云桌面"""
        self.find_elem(self.vdi_set_xpath).click()

    def edit_config(self, uname):
        """打开编辑框"""
        time.sleep(1)
        self.find_elem(self.choose_a_user.format(uname)).click()
        time.sleep(1)
        self.find_elem(self.edit_xpath).click()
        time.sleep(1)

    def edit_vdi_mirror(self, vdimirror):
        """修改vdi镜像"""
        self.find_elem(self.chose_vdimirrori_xpath).click()

        self.find_elem(self.vdi_mirror.format(vdimirror)).click()

    def edit_CPU(self):
        """修改CPU"""
        self.find_elem(self.CPU_num).click()
        time.sleep(1)
        self.find_elem(self.CPU_increase).click()
        time.sleep(2)

    def confirm_edit(self):
        """ 确认编辑修改"""
        self.find_elem(self.confirm_button_xpath).click()
        time.sleep(1)
        self.find_elem(self.sure_xpath).click()
        time.sleep(1)

    def renew_CPU(self):
        """还原CPU"""
        self.find_elem(self.CPU_num).click()
        time.sleep(1)
        self.find_elem(self.CPU_decrease).click()

    def edit_trans_info(self, trans):
        """修改利旧传输数据"""
        time.sleep(2)
        ele = self.find_elem(self.spare_DNS_xpath)
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(1)
        self.find_elem(self.trans_info_xpath).click()
        self.find_elem(self.choose_trans.format(trans)).click()

    def edit_check_identity_info(self):
        """修改双网身份验证"""
        time.sleep(1)
        self.scroll_into_view(self.check_identity)
        time.sleep(1)

    def edit_VLAN(self):
        """修改VLAN"""
        time.sleep(1)
        self.find_elem(self.VLAN_num_increase).click()
        time.sleep(1)

    def renew_VLAN(self):
        """"""
        self.find_elem(self.VLAN_num_decrease).click()

    # 关闭编辑框
    def close_edit(self):
        self.find_elem(self.close_xpath).click()

    # 修改内存
    def edit_internal_memory(self):
        time.sleep(1)
        self.find_elem(self.internal_memory_increase).click()
        time.sleep(1)

    # 还原内存
    def renew_internal_memory(self):
        time.sleep(1)
        self.find_elem(self.internal_memory_decrease).click()

    # 修改系统盘大小
    def edit_cdesk(self):
        time.sleep(2)
        self.find_elem(self.cdesk_increase).click()
        time.sleep(2)

    # 还原系统盘
    def renew_cdesk(self):
        self.find_elem(self.cdesk_decrease).click()
        time.sleep(1)

    # 修改个人盘大小
    def edit_ddesk(self):
        time.sleep(1)
        self.find_elem(self.ddesk_increase).click()
        time.sleep(1)

    # 还原个人盘
    def renew_ddesk(self):
        self.find_elem(self.ddesk_decrease).click()
        time.sleep(1)

    # 修改ip
    def edit_ip(self, ip, subnet_mask, gateway, main_dns, prepare_dns):
        time.sleep(1)
        ele = self.find_elem(self.spare_DNS_xpath)
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(1)
        self.edit_text(self.ip_info_xpath.format(u'云桌面IP：'), ip)
        time.sleep(1)
        self.edit_text(self.ip_info_xpath.format(u'云桌面子网掩码：'), subnet_mask)
        time.sleep(1)
        self.edit_text(self.ip_info_xpath.format(u'云桌面网关：'), gateway)
        time.sleep(1)
        self.edit_text(self.ip_info_xpath.format(u'云桌面首选DNS：'), main_dns)
        time.sleep(1)
        self.edit_text(self.ip_info_xpath.format(u'云桌面备用DNS：'), prepare_dns)

    def admin_confirm(self, password=passwd):
        """二次确认密码"""
        self.find_elem(self.pwd_xpath).send_keys(password)
        self.find_elem(self.confirm_button_xpath).click()

    def edit_succ_msg(self):
        """返回修改成功提示"""
        try:
            return self.find_elem(self.edit_succmsg_xpath).text
        except:
            return ''

    def edit_false_msg(self):
        """返回修改失败提示"""
        try:
            return self.find_elem(self.edit_falsemsg_xpath).text
        except:
            return ''

    # 14

    def edit_VLAN_over_error(self, vlan):
        """修改VLAN时超出最大值"""
        self.edit_text(self.edit_VLAN_xpath, vlan)
        time.sleep(1)
        self.find_elem(self.confirm_button_xpath).click()
        value = self.find_elem(self.edit_VLAN_xpath).get_attribute('aria-valuenow')
        return value

    def confirm_edit_vlan(self):
        """确认修改VLAN"""
        time.sleep(1)
        self.find_elem(self.sure_xpath).click()

    def check_over_vlan(self):
        """修改后查看VLAN值"""
        return self.find_elem(self.edit_VLAN_xpath).get_attribute('aria-valuenow')

    def edit_VLAN_other_error(self, vlan):
        """修改VLAN时填入英文、负数、不填"""
        flag = [0, 0, 0]
        for i in range(len(vlan)):
            value = self.find_elem(self.edit_VLAN_xpath).get_attribute('aria-valuenow')
            self.edit_text(self.edit_VLAN_xpath, vlan[i])
            time.sleep(1)
            self.find_elem(self.confirm_button_xpath).click()
            time.sleep(1)
            self.find_elem(self.close_tag_xpath).click()
            time.sleep(2)
            if i < 1:
                if self.find_elem(self.edit_VLAN_xpath).get_attribute('aria-valuenow') == value:
                    flag[i] = 1
            else:
                if self.find_elem(self.edit_VLAN_xpath).get_attribute('aria-valuenow') == '1':
                    flag[i] = 1
            time.sleep(1)
        return flag

    # 37

    def choose_group(self, a_group):
        """选择要修改的组"""
        time.sleep(1)

        self.chainsdubclick(self.choose_a_group.format(a_group))

    # "TODO 该方法可以废弃 可以由edit_userGroupCharacter代替"
    def edit_group(self, group):
        """点击编辑用户组"""
        self.scroll_into_view(self.click_group_xpath.format(group), click_type=1)
        self.chainstay(self.click_group_xpath.format(group))
        time.sleep(0.8)
        self.find_elem(self.edit_a_group.format(group)).click()
        time.sleep(1)
        self.find_elem(self.vdi_set_xpath).click()

    def get_CPU_val(self):
        """获取CPU值"""
        self.find_elem(self.CPU_num).click()
        time.sleep(1)
        val = self.find_elem(self.CPU_choose).text
        time.sleep(1)
        self.find_elem(self.CPU_num).click()
        time.sleep(1)
        return val

    def get_internal_memory_val(self):
        """获取内存值"""
        value = self.find_elem(self.internal_memory_text_xpath).get_attribute('aria-valuenow')
        time.sleep(1)
        return value

    def set_internal_memory_val(self):
        """设置内存值"""
        self.find_elem(self.internal_memory_increase).click()
        time.sleep(1)

    # 34

    def get_cdesk_val(self):
        """获取c盘大小"""
        value = self.find_elem(self.cdesk_val_xpath).get_attribute('aria-valuenow')
        time.sleep(1)
        return value

    def get_ddesk_val(self):
        """获取d盘大小"""
        value = self.find_elem(self.ddesk_val_xpath).get_attribute('aria-valuenow')
        time.sleep(1)

        return value

    def set_cdesk_val(self, val):
        """更改c盘大小"""
        self.edit_text(self.cdesk_val_xpath, val)
        time.sleep(1)

    def set_ddesk_val(self, val):
        """更改d盘大小"""
        self.edit_text(self.ddesk_val_xpath, val)
        time.sleep(1)

    def refresh_edit(self):
        self.find_elem(self.confirm_button_xpath).click()
        time.sleep(1)
        self.find_elem(self.close_tag_xpath).click()
        time.sleep(1)

    # 84

    def group_click(self, father_group):
        """ 点击组"""
        if 0 == self.elem_is_exist(self.parent_group_xpath.format(father_group)):
            time.sleep(3)
            self.click_elem(self.parent_group_xpath.format(father_group))
        else:
            self.scroll_into_view(self.parent_group_xpath.format(father_group))
        time.sleep(2)

    def set_group_name(self, group_name):
        """为新增组填充信息"""
        self.find_elem(self.group_name_xpath).send_keys(group_name)
        time.sleep(1)

    def group_vdi_attribute(self):
        """开启组的vdi属性"""
        self.find_elem(self.vdi_set_xpath).click()
        time.sleep(1)
        self.find_elem(self.vdi_attribute_button_xpath).click()
        time.sleep(1)

    def confirm_create_group(self):
        """确认新建组"""
        time.sleep(1)
        self.find_elem(self.confirm_xpath1).click()
        time.sleep(2)

    def error_msg(self):
        """失败提示"""
        return self.find_elem(self.error_msg_box_xpath)

    # 点击删除用户组按钮
    def click_del_gp_btn(self, ugpname):
        if 0 == self.elem_is_exist(self.userGroup_list_xpath % ugpname):
            pass
        else:
            self.scroll_into_view(self.userGroup_list_xpath % ugpname, click_type=1)
        time.sleep(1)
        self.chainstay(self.userGroup_list_xpath % ugpname)
        time.sleep(2)
        self.click_elem(self.userGroup_list_delButton_xpath % ugpname)
        info = self.get_tips()
        return info

    def delete_user_in_group(self, a_group, pwd=c_pwd):
        """删除用户组里的所有用户"""
        self.group_click(a_group)
        time.sleep(3)
        self.find_elem(self.select_users_xpath).click()
        time.sleep(2)
        self.find_elem(self.delete_user_xpath).click()
        time.sleep(1)
        self.confirm_delete_norun_user(pwd)
        time.sleep(1)

    def delete_group(self, a_group, pwd=c_pwd):
        """删除用户组"""
        self.group_click(a_group)
        self.chainstay(self.click_group_xpath.format(a_group))
        time.sleep(0.5)
        self.click_elem(self.delete_a_group_xpath.format(a_group))
        self.confirm_delete_norun_user(pwd)

    def import_error(self):
        """导入失败，点击确认，返回"""
        time.sleep(1)
        self.find_elem(self.confirm_error_xpath).click()
        time.sleep(1)
        self.find_elem(self.close_import_xpath).click()

    # 73

    def open_clouddisk_attribute(self):
        """开启云盘属性"""
        self.find_elem(self.xdisk_set_xpath).click()
        time.sleep(1)
        self.find_elem(self.clouddisk_attribute_xpath).click()
        time.sleep(1)
        self.find_elem(self.confirm_xpath1).click()
        time.sleep(1)

    def confirm_open_xdisk(self):
        """确认开启云盘"""
        self.find_elem(self.sure_xpath).click()

    def close_vdi_desktop(self, user, passwd=passwd):
        """关闭vdi云桌面"""
        self.find_user(user)
        time.sleep(1)
        self.find_elem(self.cdesk_more_operate.format(user)).click()
        time.sleep(1)
        self.find_elem(self.close_vdi_xpath).click()

        time.sleep(1)
        self.find_elem(self.close_button_xpath).click()

        self.find_elem(self.pwd_input_xpath).send_keys(passwd)
        self.find_elem(self.confirm_button_xpath).click()

    def creat_vdi_cmd(self, ip, user_name, passwd, cmd):
        """连接vdi终端输入命令"""
        return win_conn(ip, user_name, passwd, cmd)

    def create_bigfile_win_ssh(self, ip, cmd):
        """ssh连接终端"""
        server_conn(ip, cmd)

    def edit_xdisk_value(self, value):
        """更改云盘大小"""
        self.find_elem(self.xdisk_set_xpath).click()
        time.sleep(1)
        self.clear_text_info(self.edit_xdisk_xpath)
        self.edit_text(self.edit_xdisk_xpath, value)

    def close_xdisk(self):
        """关闭云盘"""
        self.find_elem(self.clouddisk_attribute_xpath).click()
        time.sleep(1)

    def get_desk_ip(self):
        """获取用户云桌面ip"""
        self.show_user_attribute()

        temp_text = self.find_elem(self.all_search_results_xpath).text
        text = temp_text.split('\n')[4]

        time.sleep(1)
        self.click_elem(self.search_xpath)
        return text

    # 71

    def create_vdi_ssh_shell(self, ip, command):
        """连接vdi终端输入shell命令"""
        return server_conn(ip, command)

    # 72
    #
    def get_max_xdisk(self):
        """获取用户可分配的最大x盘空间"""
        self.click_elem(self.spacedisk_set_xpath)
        max_xdisk_size = self.find_elem(self.max_xdisk_xpath).text
        max_xdisk = max_xdisk_size[10: -2]
        return max_xdisk

    def get_increase_xdisk_wrong_msg(self):
        """获取扩容x盘失败信息"""
        try:
            self.find_elem(self.edit_page)
            return self.find_elem(self.increase_xdisk_xpath)
        except:
            return ''

    def click_confirm(self):
        """点击确定"""
        self.find_elem(self.confirm_button_xpath).click()
        time.sleep(1)

    def click_cancel(self):
        """点击取消"""
        self.find_elem(self.cancel_button_xpath).click()
        time.sleep(1)

    # 50

    def click_external_equipment(self):
        """点击外设策略"""
        self.click_elem(self.external_equipment_xpath)
        time.sleep(1)

    def close_usb_cc_ok(self, external_equipment):
        """关闭存储设备"""
        self.click_elem(self.close_usb_cc_ok_xpath.format(external_equipment))
        time.sleep(1)

    def open_usb_cc_ok(self, external_equipment):
        """打开存储设备"""
        self.click_elem(self.open_usb_cc_ok_xpath.format(external_equipment))
        time.sleep(1)

    def goto_mirror_manage_page(self):
        """进入镜像管理页面"""
        self.click_elem(self.mirror_manage_xpath)
        time.sleep(0.5)

    def into_mirror_cifream(self):
        """进入镜像框架"""
        self.get_ciframe(self.find_elem(self.frame_id_xpath))

    def out_cifream(self):
        """跳出镜像框架"""
        self.back_current_page()

    def click_disk_val(self):
        """点击用户磁盘计算"""
        time.sleep(1)
        self.click_elem(self.user_disk_val_xpath)
        time.sleep(0.5)

    def into_prompt_cifream(self):
        """进入提示框架"""
        self.get_ciframe(self.find_elem(self.prompt_xpath))

    def input_user_num(self, num):
        """输入需要创建的个性用户数"""
        self.edit_text(self.user_num_xpath, num)
        time.sleep(0.5)
        self.click_elem(self.calcu_xpath)
        time.sleep(2)

    def get_disk_val(self):
        """获取用户可分配的最大磁盘空间"""
        # disk_list[0]:系统盘，disk_list[1]:个人盘
        disk_list = [0, 0]
        text = self.find_elem(self.max_disk_xpath).text
        disk_list[0] = re.findall("\d+", text)[0]
        disk_list[1] = re.findall("\d+", text)[1]
        return disk_list

    def close_calsu_page(self):
        """关闭计算页面"""
        self.click_elem(self.close_calsu_xpath)

    # 20
    def get_user_info(self):
        """查看用户详情"""
        self.click_elem(self.info_xpath)

    def get_user_xdisk(self):
        """获取云盘状态及大小"""
        return self.find_elem(self.xdisk_value_xpath).text

    def refresh_webdriver(self):
        """刷新服务器"""
        self.driver.refresh()

    def split_disk_val(self, text):
        """将获取的c、d盘大小提取出来"""
        # space[0]为c盘空间，space[1]为d盘空间
        space = [0, 0]
        total_taxt = text
        c = total_taxt.split(':')[3]
        c = re.findall("\d+", c)[0]
        space[0] = int(c) / 1073741824
        total_taxt = text
        c = total_taxt.split(':')[6]
        c = re.findall("\d+", c)[0]
        space[1] = int(c) / 1073741824

        return space

    def vdi_desk_cmd(self, ip, user_name, passwd, cmd):
        """vdi桌面cmd命令"""
        return get_win_conn_info(ip, user_name, passwd, cmd)

    def split_xdisk_value(self, xdisk_size):

        """从文本中提取云盘大小及剩余空间大小"""
        # xdisk[0]为网盘总空间,xdisk[1]为网盘剩余空间
        xdisk = [0, 0]
        xdisk_free_space = xdisk_size.split(' ')[1]
        xdisk_size = xdisk_size.split(' ')[2]
        xdisk_size = int(xdisk_size)
        xdisk_free_space = int(xdisk_free_space)
        xdisk_free_space = xdisk_free_space / 1024 / 1000
        xdisk_size = xdisk_size / 1024 / 1000
        xdisk_free_space = xdisk_size - xdisk_free_space
        xdisk[0] = xdisk_size
        xdisk[1] = xdisk_free_space
        return xdisk

    def split_internal_memory(self, text):
        """从文本中提取内存大小"""
        text = text.split('Version')[1]
        print text
        memory = re.findall("\d+", text)[0]
        print memory
        memory = int(memory) / 1024 / 1024 / 1024
        return memory

    # ----------------------------------------------------------------------------------------------------------------------
    # 93
    # 拖拽用户组边框显示长用户组名
    def drug_user_border(self):

        ActionChains(self.driver).drag_and_drop(self.find_elem(self.drag_source), self.find_elem(self.drag_target))

        ActionChains(self.driver).perform()

    # ------------------------------吴少峰-------------------------------------#
    # 添加用户组按钮
    usergroup_add_button_xpath = "//*[ @class ='sk-icon-add']"
    # 用户组名称输入
    usergroup_name_input_xpath = u"//label[text()='名称：']/..//input"
    # 用户组名错误提示信息
    usergroup_name_errormsg_xpath = u"//*[@class='el-form-item is-error is-required']//*[contains(text(),'只能包含')]"
    # 告警提示框
    warnning_xpath = "//div[@class='el-message-box']//p"
    warnning_confire_xpath = u"//div[@class='el-message-box']//span[contains(.,'确定')]/.."
    warnning_delete_xpath = u"//div[@class='el-message-box']//span[contains(.,'删除')]/.."
    secret_confire_xpath = u"//div[@class='el-dialog__header']//span[contains(.,'请确认密码')]/../..//div[3]//span[contains(.,'确认')]"
    secret_input_xpath = "//div[@class='el-form-item is-required']//input"
    # 描述设置
    usergroup_describe_xpath = u"//label[text()='描述：']/..//*[@class='el-textarea__inner']"
    # 确认按钮
    confire_button_xpath = u"//div[@class='el-dialog__footer']//*[@class='el-button el-button--primary el-button--mini is-round']//span[contains(text(),'确认')]/.."
    cancel_button_xpath = u"//div[@class='el-dialog__footer']//*[@class='el-button el-button--default el-button--mini is-round']//span[contains(.,'取消')]/.."
    # 提示信息
    tip_xpath = "//div[@role='alert']//*[@class='el-notification__content']"
    # 用户组IDV特性状态
    usergroup_idv_status_xpath = u"//*[text()='IDV云终端：']/ancestor::div[@class='el-form-item']//span[@class='el-switch__core']/.."
    usergroup_idv_status_close_xpath = u"//*[@aria-labelledby='scrollpane-idvPolicy']//span[contains(.,'关闭')]"
    usergroup_idv_status_open_xpath = u"//*[@aria-labelledby='scrollpane-idvPolicy']//span[contains(.,'已开启')]"
    # 用户组VDI特性状态
    usergroup_vdi_status_xpath = u"//*[text()='IDV云终端：']/ancestor::div[@class='el-form-item']//span[@class='el-switch__core']/.."
    usergroup_vdi_status_close_xpath = u"//*[@aria-labelledby='scrollpane-vdiPolicy']//span[contains(.,'关闭')]"
    usergroup_vdi_status_open_xpath = u"//*[@aria-labelledby='scrollpane-vdiPolicy']//span[contains(.,'已开启')]"
    # 用户组IDV特性开关
    usergroup_idv_switch_xpath = u"//*[text()='IDV云终端：']/ancestor::div[@class='el-form-item']//span[@class='el-switch__core']"
    # 用户组VDI特性开关
    usergroup_vdi_switch_xpath = u"//*[text()='VDI云桌面：']/ancestor::div[@class='el-form-item']//span[@class='el-switch__core']"
    # 用户组绑定IDV镜像
    idvimage_bind_xpath = u"//*[@id='scrollpane-idvPolicy']//*[contains(text(),'绑定镜像：')]/parent::div//input"
    # 用户组绑定VDI镜像
    vdiimage_bind_xpath = u"//*[@id='scrollpane-vdiPolicy']//*[contains(text(),'绑定镜像：')]/parent::div//input"
    # 用户详情中vdi镜像内容
    userDetail_imageContent_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='绑定镜像：']/..//div[@class='el-form-item__content']"
    # 用户详情中idv镜像内容
    userDetail_idvImageContent_xpath = u"//div[@id='scrollpane-idvPolicy']//label[text()='绑定镜像：']/..//div[@class='el-form-item__content']"
    # 用户组IDV绑定镜像信息
    idvimage_bind_errormsg_xpath = u"//*[@aria-labelledby='scrollpane-idvPolicy']//*[contains(text(),'必填项')]"
    # idv镜像选择
    idv_image_xpath = "//ul[@class='el-select-group']//span[contains(.,'%s')]"
    # vdi镜像选择
    vdi_image_xpath = "//ul[@class='el-select-group']//span[contains(.,'%s')]"
    # 新建用户
    create_user_xpath = u"//*[@class='el-button filter-item el-button--primary el-button--mini is-round']//span[contains(.,'新建用户')]"
    # 新建或编辑用户处 用户名
    username_xpath = u"//label[text()='用户名：']/..//input"
    # 新建或编辑用户处 用户组输入框
    user_usergroup_xpath = u"//label[text()='用户组：']/..//div[@class='el-input el-popover__reference']//input"
    # 新建或编辑用户处 用户组输入框选项
    user_usergrouplist_xpath = u"//div[@role='tooltip']//div[contains(text(),'%s')]"
    # 新建或编辑用户处 姓名
    name_xpath = u"//label[text()='姓名：']/..//input"
    # 设置系统盘大小及用户详情系统盘内容
    IDV_systemDisk_xpath = "//div[@id='scrollpane-idvPolicy']//div[@class='el-input']//input[@class='el-input__inner']"
    VDI_systemDisk_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='系统盘(GB)：']/..//input"
    userDetail_systemDiskContent_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='系统盘(GB)：']/..//div[@class='el-form-item__content']"
    userDetail_idvSysDiskContent_xpath = u"//div[@id='scrollpane-idvPolicy']//label[text()='系统盘(GB)：']/..//div[@class='el-form-item__content']"
    # vlan输入框
    vlan_input_xpath = "//div[@id='scrollpane-vdiPolicy']//label[text()='VLAN：']/..//input"
    # IDV云桌面设置
    idv_set_xpath = u"//nav[@class='navscroll-js sk-scroll-tabs__header']//*[text()='IDV云终端设置']"
    # 用户组名列表
    userGroup_list_xpath = "//div[@class='el-tree user-group-tree el-tree--highlight-current']//*[contains(text(),'%s')]"
    # 用户组名列表编辑 删除按钮
    userGroup_list_editButton_xpath = u"//div[contains(text(),'%s')]/parent::div//i[@class='el-icon-edit']/parent::button"
    userGroup_list_delButton_xpath = u"//div[contains(text(),'%s')]/parent::div//i[@class='el-icon-delete']/parent::button"
    # 用户——更多按钮
    user_list_more_xpath = u"//span[contains(.,'%s')]/ancestor::tr//button"
    # 功能——更多按钮
    moreButton_xpath = u"//div[@class='sk-more-button filter-item']//span[contains(.,'更多')]/.."
    # 用户姓名列表
    userName_list_xpath = u"//div[@class='cell el-tooltip']//span[text()='%s']"
    # 用户详情按钮
    userDetail_xpath = u"//ul[not(contains(@style,'display: none'))]//li[contains(text(),'详情')]"
    # 用户详情dialog
    userDetailDialog = u"//span[contains(.,'用户详情')]/../.."
    # 用户编辑按钮
    userEdit_xpath = u"//ul[not(contains(@style,'display: none'))]//li[contains(text(),'编辑')]"
    # 用户详情VDI云桌面设置及内容
    userDetail_vdiSet_xpath = u"//div[@class='el-dialog__header']//span[contains(.,'用户详情')]/../..//div[2]//span[contains(.,'VDI云桌面设置')]"
    userDetail_vdiSetContent_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='VDI云桌面设置：']/..//div[@class='el-form-item__content']"
    userDetail_desktopStyle_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='桌面类型：']/..//div[@class='el-form-item__content']"
    userDetail_close_xpath = u"//div[@class='el-dialog']//button[@type='button']//span[contains(.,'关闭')]/.."
    # 用户详情IDV云桌面设置及内容
    userDetail_idvSet_xpath = u"//div[@class='el-dialog__header']//span[contains(.,'用户详情')]/../..//div[2]//span[contains(.,'IDV云终端设置')]"
    userDetail_idvSetContent_xpath = u"//div[@id='scrollpane-idvPolicy']//label[text()='IDV云终端设置：']/..//div[@class='el-form-item__content']"
    userDetail_idvDesktopStyle_xpath = u"//div[@id='scrollpane-idvPolicy']//label[text()='桌面类型：']/..//div[@class='el-form-item__content']"
    userDetail_allowLocationDisk = u"//label[contains(.,'允许使用本地盘：')]/..//div[@class='el-form-item__content']"
    # 桌面类型
    vdidesktop_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='桌面类型：']/parent::div//input"
    idvdesktop_xpath = u"//div[@id='scrollpane-idvPolicy']//label[text()='桌面类型：']/parent::div//input"
    personalityDesktop_xpath = u"//div[@class='el-scrollbar']//span[text()='个性']/.."
    restoreDesktop_xpath = u"//div[@class='el-scrollbar']//span[text()='还原']/.."
    userDetail_desktopContent_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='桌面类型：']/..//div[@class='el-form-item__content']"
    # vdi_CPU
    cpu_account_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='CPU(个)：']/..//input"
    cpu_accountOther_xpath = "//ul[@class='el-scrollbar__view el-select-dropdown__list']//span[text()='%s']/.." % cpusize
    userDetail_cpuContent_xpath = "//div[@id='scrollpane-vdiPolicy']//label[text()='CPU(个)：']/..//div[@class='el-form-item__content']"
    # vdi_内存
    memory_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='内存 (GB)：']/..//input"
    userDetail_memContent_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='内存 (GB)：']/..//div[@class='el-form-item__content']"
    # vdi_个人盘
    personalDisk_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='个人盘(GB)：']/..//input"
    userDetail_perDiskContent_xpath = u"//div[@id='scrollpane-vdiPolicy']//label[text()='个人盘(GB)：']/..//div[@class='el-form-item__content']"
    # 利旧传输
    old_transmission_xpath = u"//label[text()='利旧传输数据：']/..//input"
    # 云盘
    spacedisk_set_xpath = u"//nav[@class='navscroll-js sk-scroll-tabs__header']//*[text()='启用个人云盘']"
    spacedisk_switch_xpath = u"//label[text()='云盘：']/..//div[@role='switch']"
    spacedisk_open_ststus_xpath = u"//label[text()='云盘：']/..//span[contains(.,'已开启')]"
    spacedisk_close_ststus_xpath = u"//label[text()='云盘：']/..//span[contains(.,'关闭')]"
    spacedisk_location_xpath = u"//label[text()='云盘位置：']/..//input"
    spacedisk_size_xpath = u"//label[text()='云盘大小(GB)：']/..//input"
    # 用户自定义图标
    user_defined_xpath = u"//span[contains(.,'%s')]/..//i"
    # 搜索框无数据时
    searchNoData_xpath = u"//span[contains(.,'暂无数据')]"
    # 搜索条数
    searchCount_xpath = "//div[@class='fr']//span[@class='el-pagination__total']"
    # 清空IP
    clearIP_xpath = u"//li[contains(text(),'清空IP')]"
    # 填充IP
    fillIP_xpath = u"//li[contains(text(),'填充IP')]"
    # 填充ip相关 未勾选用户提示信息
    fillIpTip_xpath = "//div[@class='el-message el-message--warning']//*[@class='el-message__content']"
    # 自定义用户提示
    userDefineInfo_xpath = u"//*[text()='该用户的配置与用户所在组不同']"
    # 用户勾选框
    userCheckBox_xpath = u"//span[contains(.,'%s')]/../../..//span[@class='el-checkbox__inner']"
    # 全选框
    allCheckBox_xpath = u"//div[@class='cell' and text()='用户名']/../..//span[@class='el-checkbox__inner']"
    # 起始IP
    initiativeIp_xpath = u"//label[contains(.,'云桌面起始IP：')]/..//input"
    # 子网掩码
    subnetMask_xpath = u"//label[contains(.,'云桌面子网掩码：')]/..//input"
    # 网关
    gateWay_xpath = u"//label[contains(.,'云桌面网关：')]/..//input"
    # 首选DNS
    dns_xpath = u"//label[contains(.,'云桌面首选DNS：')]/..//input"
    # 云桌面IP
    cloud_desk_ip_xpath = u"//label[contains(.,'云桌面IP：')]/parent::div//*[@class='el-form-item__content']"

    # 错误信息文本内容
    def usergroup_name_errormsg(self, path):
        return self.find_elem(path).text

    # 清空路径文本
    def clear_input(self, path):
        self.find_elem(path).send_keys(Keys.CONTROL, 'a')
        self.find_elem(path).send_keys(Keys.BACK_SPACE)

    # vdi属性是否开启判断
    is_vdi_open = u"//*[contains(text(),'VDI云桌面：')]/..//div[@role='switch']"

    # 绑定镜像
    def image_bind(self, character, idvImage=idv_default_image, vdiImage=vdi_default_image):
        if character == idv:
            self.find_elem(self.idvimage_bind_xpath).click()
            time.sleep(com_slp)
            self.find_elem(self.idv_image_xpath % idvImage).click()
        elif character == vdi:
            self.find_elem(self.vdi_set_xpath).click()
            time.sleep(com_slp)
            self.find_elem(self.vdiimage_bind_xpath).click()
            if 0 == self.elem_is_exist(self.vdi_image_xpath % vdiImage):
                self.click_elem(self.vdi_image_xpath % vdiImage)
            else:
                self.scroll_into_view(self.vdi_image_xpath % vdiImage)
        elif character == all:
            self.find_elem(self.idv_set_xpath).click()
            time.sleep(com_slp)
            self.find_elem(self.idvimage_bind_xpath).click()
            time.sleep(com_slp)
            self.find_elem(self.idv_image_xpath % idvImage).click()
            self.find_elem(self.vdi_set_xpath).click()
            info = self.get_elem_attribute(self.is_vdi_open, 'class')
            if "checked" not in info:
                self.find_elem(self.usergroup_vdi_switch_xpath).click()
            self.find_elem(self.vdi_set_xpath).click()
            time.sleep(com_slp)
            self.find_elem(self.vdiimage_bind_xpath).click()
            self.find_elem(self.vdi_image_xpath % vdiImage).click()
        else:
            pass

    # 选择IDV VDI特性
    def choose_Terminal_character(self, character):
        if character == idv:
            self.find_elem(self.idv_set_xpath).click()
            time.sleep(com_slp)
            self.find_elem(self.usergroup_idv_switch_xpath).click()
        elif character == vdi:
            self.find_elem(self.vdi_set_xpath).click()
            time.sleep(com_slp)
            self.find_elem(self.usergroup_vdi_switch_xpath).click()
        elif character == all:
            self.find_elem(self.usergroup_idv_switch_xpath).click()
            self.find_elem(self.vdi_set_xpath).click()
            time.sleep(com_slp)
            self.find_elem(self.usergroup_vdi_switch_xpath).click()
        elif character == ' ':
            pass
        else:
            logging.info("input character error!")

    # 选择桌面类型
    def choose_DesktopStyle(self, path, style):
        self.find_elem(path).click()
        if style == personality:
            self.find_elem(self.personalityDesktop_xpath).click()
        elif style == restore:
            self.find_elem(self.restoreDesktop_xpath).click()
        else:
            logging.info("input style error!")

    # 设置系统盘大小
    def set_systemDisk_content(self, path, content):
        self.clear_input(path)
        self.find_elem(path).send_keys(content)

    # 获取系统盘大小
    def get_systemDisk_content(self, path):
        return self.find_elem(path).get_attribute('aria-valuenow')

    # 打开用户组特性
    def open_character(self, character, userGroupName):
        self.click_elem(self.usergroup_add_button_xpath)
        self.elem_send_keys(self.usergroup_name_input_xpath, userGroupName)
        self.choose_Terminal_character(character)

    # 打开用户特性
    def open_user_character(self, character, userName):
        self.find_elem(self.create_user_xpath).click()
        self.find_elem(self.username_xpath).send_keys(userName)
        self.find_elem(self.name_xpath).send_keys(userName)
        self.choose_Terminal_character(character)

    # 打开云盘
    def open_spaceDisk(self):
        self.find_elem(self.spacedisk_set_xpath).click()
        time.sleep(com_slp)
        self.find_elem(self.spacedisk_switch_xpath).click()

    # 查找某个用户组并创建新用户
    def findUserGroupCreateNewuser(self, userGroupName, userName, character=' '):
        time.sleep(com_slp)
        if 0 == self.elem_is_exist(self.userGroup_list_xpath % userGroupName):
            time.sleep(com_slp)
            self.click_elem(self.userGroup_list_xpath % userGroupName)
        else:
            self.scroll_into_view(self.userGroup_list_xpath % userGroupName, click_type=0)
        if character == ' ':
            self.find_elem(self.create_user_xpath).click()
            self.find_elem(self.username_xpath).send_keys(userName)
            self.find_elem(self.name_xpath).send_keys(userName)
        #       self.find_elem(self.confire_button_xpath).click()
        else:
            self.open_user_character(character, userName)
            self.find_elem(self.name_xpath).send_keys(userName)
            if character == vdi:
                self.find_elem(self.vdi_set_xpath).click()
            elif character == idv:
                self.find_elem(self.idv_set_xpath).click()
            self.image_bind(character)

    #       self.find_elem(self.confire_button_xpath).click()
    # 创建某个用户组并创建新用户
    def createUserGroupCreateNewuser(self, userGroupName, userName, userGroupCharacter=' ', userCharacter=' '):
        self.open_character(userGroupCharacter, userGroupName)
        self.image_bind(userGroupCharacter)
        self.find_elem(self.confire_button_xpath).click()
        time.sleep(com_slp)
        if 0 == self.elem_is_exist(self.userGroup_list_xpath % userGroupName):
            pass
        else:
            self.scroll_into_view(locator=self.userGroup_list_xpath % userGroupName, click_type=1)

        self.scroll_into_view(self.userGroup_list_xpath % userGroupName)
        self.open_user_character(userCharacter, userName)
        self.find_elem(self.name_xpath).send_keys(userName)
        if userCharacter == vdi:
            self.find_elem(self.vdi_set_xpath).click()
        elif userCharacter == idv:
            self.click_elem(self.idv_set_xpath)
        self.image_bind(userCharacter)

    # 编辑用户组特性
    def edit_userGroupCharacter(self, userGroupName, character=' '):
        if 0 == self.elem_is_exist(self.click_group_xpath.format(userGroupName)):
            self.click_elem(self.click_group_xpath.format(userGroupName))
        else:
            self.scroll_into_view(self.click_group_xpath.format(userGroupName), click_type=1)
        self.chainstay(self.click_group_xpath.format(userGroupName))
        self.find_elem(self.userGroup_list_editButton_xpath % userGroupName).click()
        if character != ' ':
            self.choose_Terminal_character(character)
        else:
            pass

    #  self.find_elem(self.confire_button_xpath).click()
    # 修改桌面类型
    def changeDesktopStyle(self, character, deskStyle):
        if character == idv:
            self.choose_DesktopStyle(self.idvdesktop_xpath, deskStyle)
        elif character == vdi:
            self.choose_DesktopStyle(self.vdidesktop_xpath, deskStyle)
        else:
            logging.info("input character error!")

    # 修改CPU个数
    def changeCpuAccount(self):
        self.find_elem(self.cpu_account_xpath).click()
        self.find_elem(self.cpu_accountOther_xpath).click()

    # 修改内存
    def changeMemory(self, memory):
        self.clear_input(self.memory_xpath)
        self.find_elem(self.memory_xpath).send_keys(memory)

    # 修改个人盘
    def changePersonalDisk(self, size):
        self.clear_input(self.personalDisk_xpath)
        self.find_elem(self.personalDisk_xpath).send_keys(size)

    # 查看某用户的用户详情
    def check_userDetail(self, userName):
        time.sleep(3)
        self.find_elem(self.user_list_more_xpath % userName).click()
        time.sleep(com_slp)
        self.find_elem(self.userDetail_xpath).click()

    # 编辑某用户
    def edit_user(self, userName):
        self.search_info(userName)
        time.sleep(3)
        self.find_elem(self.user_list_more_xpath % userName).click()
        time.sleep(com_slp)
        self.find_elem(self.userEdit_xpath).click()

    # 查看特性开启状态
    def characterStatus(self, character):
        status = (0, 1)
        if character == idv:
            self.find_elem(self.idv_set_xpath).click()
            try:
                self.find_elem(self.usergroup_idv_status_open_xpath)
            except:
                logging.info("用户idv特性未开启")
                return status[0]
            else:
                time.sleep(com_slp)
                logging.info("用户idv特性已开启")
                self.find_elem(self.usergroup_idv_switch_xpath).click()
                return status[1]
        elif character == vdi:
            self.find_elem(self.vdi_set_xpath).click()
            try:
                self.find_elem(self.usergroup_vdi_status_open_xpath)
            except:
                logging.info("用户vdi特性未开启")
                return status[0]
            else:
                time.sleep(com_slp)
                logging.info("用户vdi特性已开启")
                self.find_elem(self.usergroup_vdi_switch_xpath).click()
                return status[1]
        elif character == space:
            self.find_elem(self.spacedisk_set_xpath).click()
            try:
                self.find_elem(self.spacedisk_open_ststus_xpath)
            except:
                logging.info("用户云盘特性未开启")
                return status[0]
            else:
                time.sleep(com_slp)
                logging.info("用户云盘特性已开启")
                self.find_elem(self.spacedisk_switch_xpath).click()
                return status[1]

    # 开启特性
    def openCharacter(self, character):
        if character == idv:
            self.find_elem(self.idv_set_xpath).click()
            self.find_elem(self.usergroup_idv_switch_xpath).click()
        if character == vdi:
            self.find_elem(self.vdi_set_xpath).click()
            self.find_elem(self.usergroup_vdi_switch_xpath).click()
        if character == space:
            self.find_elem(self.spacedisk_set_xpath).click()
            self.find_elem(self.spacedisk_switch_xpath).click()

    # 二次告警
    def warnning_info(self, warnInfo, character=' ', operate=confire):
        if character == ' ':
            assert u'将无法登录VDI桌面' in self.get_elem_text(self.warnning_xpath)
        elif character == idv:
            assert self.find_elem(self.warnning_xpath).text.find(idvCharacterError_info) >= 0
        elif character == vdi:
            assert self.find_elem(self.warnning_xpath).text.find(vdiCharacterError_info) >= 0
        elif character == space:
            assert self.find_elem(self.warnning_xpath).text.find(spaceCharacterError_info) >= 0
        if operate == 'confire':
            self.find_elem(self.warnning_confire_xpath).click()
        elif operate == 'delete':
            self.find_elem(self.warnning_delete_xpath).click()
        self.find_elem(self.secret_input_xpath).send_keys(passwd)
        self.find_elem(self.secret_confire_xpath).click()

    # 特性详情
    def idvCharacterDetail(self):
        """IDV特性信息"""
        self.find_elem(self.idv_set_xpath).click()
        idvDesktop = self.find_elem(self.idvdesktop_xpath).get_attribute('value')
        idvImage = self.find_elem(self.idvimage_bind_xpath).get_attribute('value')
        idvSysdisk = self.get_systemDisk_content(self.IDV_systemDisk_xpath)
        idvCharacterDetail = {'idvDesktop': idvDesktop, 'idvImage': idvImage, 'idvSysdisk': idvSysdisk}
        return idvCharacterDetail

    def vdiCharacterDetail(self):
        """VDI特性信息"""
        self.find_elem(self.vdi_set_xpath).click()
        vdiVlan = self.find_elem(self.vlan_input_xpath).get_attribute('value')
        vdiDesktop = self.find_elem(self.vdidesktop_xpath).get_attribute('value')
        vdiImage = self.find_elem(self.vdiimage_bind_xpath).get_attribute('value')
        vdiCpu = self.find_elem(self.cpu_account_xpath).get_attribute('value')
        vdiMem = self.find_elem(self.memory_xpath).get_attribute('value')
        vdiSys = self.get_systemDisk_content(self.VDI_systemDisk_xpath)
        vdiPer = self.find_elem(self.personalDisk_xpath).get_attribute('value')
        #        vdiOld = self.find_elem(self.old_transmission_xpath).get_attribute('value')
        # 列表中未加入vdiOld  即利旧传输特性的数据
        vdiCharacterDetail = {'vdiVlan': vdiVlan, 'vdiDesktop': vdiDesktop, 'vdiImage': vdiImage, 'vdiCpu': vdiCpu,
                              'vdiMem': vdiMem, 'vdiSys': vdiSys, 'vdiPer': vdiPer}
        return vdiCharacterDetail

    def spaceCharacterDetail(self):
        self.find_elem(self.spacedisk_set_xpath).click()
        spaceLocation = self.find_elem(self.spacedisk_location_xpath).get_attribute('value')
        spaceSize = self.find_elem(self.spacedisk_size_xpath).get_attribute('value')

        spaceCharacterDetail = {'spaceLocation': spaceLocation, 'spaceSize': spaceSize}
        return spaceCharacterDetail

    def characterDetail(self, character):
        if character == idv:
            return self.idvCharacterDetail()
        elif character == vdi:
            return self.vdiCharacterDetail()
        elif character == space:
            return self.spaceCharacterDetail()
        elif character == all:
            idvchdet = self.idvCharacterDetail()
            vdichdet = self.vdiCharacterDetail()
            spacechdet = self.spaceCharacterDetail()
            idvchdet.update(vdichdet)
            idv_vdi_space = idvchdet
            idv_vdi_space.update(spacechdet)
            return idv_vdi_space

    chose_group_xpath = u"//*[@role='tooltip']//*[@role='group']//*[contains(text(),'{}')]"

    # 选择用户所属用户组
    def choose_userGroup(self, userGroupName):
        self.find_elem(self.user_usergroup_xpath).click()
        self.scroll_into_view(locator=self.chose_group_xpath.format(userGroupName), click_type=1)
        time.sleep(1)
        self.click_elem(self.chose_group_xpath.format(userGroupName))
        self.find_elem(self.vdi_set_xpath).click()

    # 属性比对
    def property_compare(self, characterList, character):
        flag = 0
        if character == all:
            flag = 1
        if character == idv or flag == 1:
            self.find_elem(self.idv_set_xpath).click()
            assert self.find_elem(self.usergroup_idv_status_open_xpath).text == open_info
            assert self.find_elem(self.idvdesktop_xpath).get_attribute('value') == characterList.get('idvDesktop')
            assert self.find_elem(self.idvimage_bind_xpath).get_attribute('value') == characterList.get('idvImage')
            assert self.get_systemDisk_content(self.IDV_systemDisk_xpath) == characterList.get('idvSysdisk')
        if character == vdi or flag == 1:
            self.find_elem(self.vdi_set_xpath).click()
            assert self.find_elem(self.usergroup_vdi_status_open_xpath).text == open_info
            assert self.find_elem(self.vlan_input_xpath).get_attribute('value') == characterList.get('vdiVlan')
            assert self.find_elem(self.vdidesktop_xpath).get_attribute('value') == characterList.get('vdiDesktop')
            assert self.find_elem(self.vdiimage_bind_xpath).get_attribute('value') == characterList.get('vdiImage')
            assert self.find_elem(self.cpu_account_xpath).get_attribute('value') == characterList.get('vdiCpu')
            assert self.find_elem(self.memory_xpath).get_attribute('value') == characterList.get('vdiMem')
            assert self.get_systemDisk_content(self.VDI_systemDisk_xpath) == characterList.get('vdiSys')
            assert self.find_elem(self.personalDisk_xpath).get_attribute('value') == characterList.get('vdiPer')
        if character == space or flag == 1:
            self.find_elem(self.spacedisk_set_xpath).click()
            assert self.find_elem(self.spacedisk_location_xpath).get_attribute('value') == characterList.get(
                'spaceLocation')
            assert self.find_elem(self.spacedisk_size_xpath).get_attribute('value') == characterList.get('spaceSize')

    # 判断是否为自定义用户
    def judgeUserDefine(self, userName):
        try:
            self.find_elem(self.user_defined_xpath % userName)
        except:
            logging.info("该用户为普通组内用户")
            pass
        else:
            logging.info("该用户是自定义用户")

    # 更多按钮下的选项
    def moreButtonList(self, path):
        time.sleep(3)
        self.find_elem(self.moreButton_xpath).click()
        self.find_elem(path).click()

    # 填充IP
    def fillip(self, ip, subnetMask, gateWay, dns, status):
        time.sleep(com_slp)
        if status == noDNS or status == all:
            self.find_elem(self.initiativeIp_xpath).send_keys(ip)
            self.find_elem(self.subnetMask_xpath).send_keys(subnetMask)
            self.find_elem(self.gateWay_xpath).send_keys(gateWay)
        if status == noIP or status == all:
            self.find_elem(self.dns_xpath).send_keys(dns)
        time.sleep(com_slp)
        self.find_elem(self.confire_button_xpath).click()

    xpath_attributes_visibility_panel_btn = u"//*[@class='filter-item el-dropdown']"
    xpath_attributes_type_check_icon = u"//span[text()='类型']/preceding-sibling::i"
    xpath_attributes_status_check_icon = u"//span[text()='状态']/preceding-sibling::i"
    xpath_attribute_type_trigger = u"//span[@class='el-table__column-filter-trigger']/ancestor::div[1][text()='类型']"
    xpath_attribute_status_trigger = u"//span[@class='el-table__column-filter-trigger']/ancestor::div[1][text()='状态']"
    "//ul[@class='el-table-filter__list']/child::li"
    xpath_attribute_type_filter_item_all = u"//ul[@class='el-table-filter__list']/child::li[text()='全部']"
    xpath_attribute_type_filter_item_local = u"//ul[@class='el-table-filter__list']/child::li[text()='本地']"
    xpath_attribute_type_filter_item_ad = u"//ul[@class='el-table-filter__list']/child::li[text()='AD域']"
    xpath_attribute_status_filter_item_normal = u"//ul[@class='el-table-filter__list']/child::li[text()='正常']"
    xpath_attribute_status_filter_item_forbidden = u"//ul[@class='el-table-filter__list']/child::li[text()='禁用']"

    # 打开自定义字段显隐面板
    # 自定义显示用户属性

    def make_sure_attribute_checked(self, xpath):
        item = self.find_elem(xpath)
        css_class = item.get_attribute("class")
        if css_class == "icon-empty":
            item.click()

    def make_sure_filter_attributes_checked(self):
        self.find_elem(self.xpath_attributes_visibility_panel_btn).click()  # 点击眼睛状图标
        self.make_sure_attribute_checked(self.xpath_attributes_type_check_icon)
        self.make_sure_attribute_checked(self.xpath_attributes_status_check_icon)
        self.click_elem(self.search_xpath)  # 点击空白处收起图标

    def check_filter_item(self):
        self.find_elem(self.xpath_attribute_type_trigger).click()
        self.find_elem(self.xpath_attribute_type_filter_item_all)
        self.find_elem(self.xpath_attribute_type_filter_item_local)
        self.find_elem(self.xpath_attribute_type_filter_item_ad)

        self.find_elem(self.xpath_attribute_status_trigger).click()
        self.find_elem(self.xpath_attribute_status_filter_item_normal)
        self.find_elem(self.xpath_attribute_status_filter_item_forbidden)

    def getTipMessage(self):
        time.sleep(1)
        tip_message = self.find_elem(self.tip_xpath)
        print(tip_message)
        if tip_message:
            return tip_message.text
        else:
            return ""

    # 需要输入二次确认密码提示信息
    tip_xpath1 = u"//*[contains(@class,'el-message-box__message')]//p"

    def get_tips(self):
        time.sleep(1)
        return self.get_elem_text(self.tip_xpath1)

    # ---------------------------------------------------------hqf----------------------------------------------------
    # 用户管理界面
    user_xpath = u"//*[text()='首页']"
    # 所测试的用户组所在的用户组
    select_user_group_xpath = ur"//div[@class='custom-tree-node']/descendant::div[contains(text(),'{0}')]/" \
                              ur"ancestor::div[@class='el-tree-node__content']/span"
    # 选择云桌面设置
    vdi_configure_xpath = u"//*[text()='VDI云桌面设置']"
    # 云桌面类型选择
    vdi_type_choose_xpath = u"//*[text()='桌面类型：']/parent::div/div//input"
    # 新建所需测试的用户
    # 新建用户按钮
    new_user_button_xpath = ur"//*[@class='sk-toolbar']/div//*[contains(., '新建用户')]/span"
    # 新建用户的用户名框
    new_user_name_xpath = u"//*[text()='用户名：']/parent::div/descendant::input"
    # 新建用户的姓名框
    new_user_names_xpath = u"//*[text()='姓名：']/parent::div/descendant::input"
    # 删除测试用户
    choose_user_xpath = ur"//*[text()='{0}']/ancestor::tr//*[@class='el-checkbox__inner']"
    delete_user_button_xpath = ur"//*[@class='sk-toolbar']/div//*[contains(., '删除用户')]/span"
    # 所测试的用户所在的用户组
    vdi_user_group_xpath = ur"//div[@class='custom-tree-node']/descendant::div[contains(text(),'{0}')]"
    # 所测试用户的更多按钮
    user_more_button_xpath = ur"//*[contains(text(),'{0}')]/ancestor::tr//*[contains(text(),'更多')]"
    # 测试用户的更多选项里的编辑按钮
    user_compile_xpath = ur"//body/ul/div/li"
    # 云桌面类型选项（个性或还原）
    vdi_type_xpath = ur"//*[@x-placement='bottom-start']//ul//span[contains(.,'{}')]"
    # 镜像的选择框
    vdi_image_choose_xpath = ur"//*[text()='绑定镜像：']/parent::div/div//input"
    # 镜像的选项
    vdi_image1_xpath = ur"//*[contains(text(),'{0}')]"
    # 确认编辑按钮
    confirm_compile_button_xpath = ur"//*[contains(text(),'{0}')]/ancestor::div[@class='el-dialog']" \
                                   ur"/div[@class='el-dialog__footer']/div/button"
    # 提示
    warning_xpath = r"//*[@class='el-message-box']/div/div/span"
    # 警告内容
    warning_text_xpath = ur"//*[@class='el-message-box']/div[@class='el-message-box__content']" \
                         ur"/div[@class='el-message-box__message']/p/div"
    # 确认警告
    confirm_warning_xpath = r"//*[@class='el-message-box']/div[@class='el-message-box__btns']/button"
    # 二次确认管理员密码
    manager_password_text_xpath = u"//*[text()='请确认密码']"
    # 输入管理员密码
    manager_password_xpath = ur"//*[text()='请确认密码']/ancestor::div[@class='el-dialog']/div[@class='el-dialog__body']" \
                             ur"//div[@class='el-input']/input"
    # 确认输入的管理员密码
    confirm_manager_password_xpath = ur"//*[text()='请确认密码']/ancestor::div[@class='el-dialog']" \
                                     ur"/div[@class='el-dialog__footer']/div/button"
    # 云桌面管理栏
    cloud_desktop_xpath = u"//span[contains(.,'云桌面管理')]"
    # 云桌面管理的用户更多选项里的关机按钮
    user_close = ur"//*[@x-placement='bottom-start']//li[contains(.,'关机')]/.."
    # 点击外设策略
    vdi_Peripheral_strategy_xpath = ur"//*[text()='外设策略']"
    # 获取云桌面的IP地址
    get_desktop_ip_xpath = ur"//*[contains(text(),'{0}')]/ancestor::tr//td[14]"

    # A1.61
    cpu_choose_xpath = ur"//*[text()='CPU(个)：']/parent::div/div//input"
    cpu_number_xpath = ur"//*[@x-placement='bottom-start']//*[contains(text(),'{0}')]"
    decrease_storage_xpath = ur"//*[text()='内存 (GB)：']/parent::div/div/div/span[@class='el-input-number__decrease']"
    increase_storage_xpath = ur"//*[text()='内存 (GB)：']/parent::div/div/div/span[@class='el-input-number__increase']"

    # A1.62
    # 编辑用户系统盘和个人盘大小的更改
    dec_inc_size_xpath = ur"//*[text()='{0}']/parent::div/div/div/span[@class='el-input-number__{1}']"
    dec_disable_xpath = ur"//*[text()='{0}']/parent::div/div/div//span"

    # A1.33
    # 点击用户组编辑
    user_group_xpath = "//div[@class='custom-tree-node']/descendant::div[contains(text(),'{0}')]/parent::div"
    user_group_edit_xpath = r"//div[@class='custom-tree-node']/descendant::div[contains(text(),'{0}')]/parent::div//button"
    mem_size_xpath = ur"//*[text()='内存 (GB)：']/parent::div/div//input"

    # A1.81
    # 重置用户密码
    # 用户重置密码
    user_password_reset_xpath = ur"// *[@class='el-dropdown-menu el-popper sk-more-button__dropmenu " \
                                ur"el-dropdown-menu--mini']//*[contains(.,'重置密码')]/li "
    # 确认重置密码按钮
    password_reset_button_xpath = u"//*[@class='el-message-box']/div[@class='el-message-box__btns']/button[1]"

    # A1.21
    # 不能修改VDI云桌面特性的提示框
    prompt_frame_xpath = r"//p[@class='el-message__content']"
    # 修改VDI云桌面特性成功的提示框
    success_prompt_frame_xpath = ur"//*[text()='用户VDI云桌面特性修改成功！']"
    # 打开个人云盘
    vdi_per_net_disk_xpath = ur"//*[text()='启用个人云盘']"
    vdi_net_disk_xpath = ur"//*[text()='云盘：']/parent::div/div//input"

    # A 1.17
    # 系统盘大小输入框
    disk_size_xpath = ur"//*[text()='系统盘(GB)：']/parent::div/div//input"
    # 判断云桌面是否开启
    open_desktop_text_xpath = ur"//*[text()='VDI云桌面：']/parent::div/div/span"
    # 开启云桌面特性
    desktop_xpath = ur"//*[text()='VDI云桌面：']/parent::div/div/div/span"

    # 在测试的用户组下新建测试的用户
    def new_test_user(self, u_group, u_name):
        self.select_user_group()
        self.click_elem(self.vdi_user_group_xpath.format(u_group))
        self.click_elem(self.new_user_button_xpath)
        self.elem_send_keys(self.new_user_name_xpath, u_name)
        self.elem_send_keys(self.new_user_names_xpath, test_username)
        self.confirm_compile(confirm_button_type[0])

    # 删除测试的用户
    def delete_test_user(self, group, user_name):
        self.select_user_group()
        self.click_elem(self.vdi_user_group_xpath.format(group))
        self.click_elem(self.choose_user_xpath.format(user_name))
        self.click_elem(self.delete_user_button_xpath)
        self.confirm_warning()
        self.confirm_manager_password()

    # 选择用户组
    def select_user_group(self):
        self.click_elem(self.user_manage_xpath)  # 进入用户管理
        self.click_elem(self.select_user_group_xpath.format(user_group))  # 进入所测试用户组所在的用户组vdi_A

    # 进入用户编辑模块框
    def user_compile(self):
        self.click_elem(self.user_compile_xpath)

    # 点击用户云桌面设置
    def desktop_configure(self):
        self.click_elem(self.vdi_configure_xpath)

    # 点击确认编辑，保存更改
    def confirm_compile(self, confirm):
        self.click_elem(self.vdi_Peripheral_strategy_xpath)  # 点击外设策略，用于退出镜像的选择，显示出确认按钮
        self.click_elem(self.confirm_compile_button_xpath.format(confirm))  # 确认编辑

    # vdi更改的警告框，返回警告框文本
    def get_alter_warning(self):
        try:
            self.find_elem(self.warning_xpath)
        except:
            return 0
        else:
            return self.get_elem_text(self.warning_xpath)

    # 确认警告
    def confirm_warning(self):
        self.click_elem(self.confirm_warning_xpath)  # 确认警告

    def get_manager_password(self):
        try:
            self.find_elem(self.manager_password_text_xpath)
        except:
            return 0
        else:
            return self.get_elem_text(self.manager_password_text_xpath)

    # 二次管理员密码输入及确认
    def confirm_manager_password(self):
        self.elem_send_keys(self.manager_password_xpath, login_user["passwd"])  # 输入管理员密码
        self.click_elem(self.confirm_manager_password_xpath)  # 确认更改

    # 获取用户的云桌面IP
    def get_desktop_ip(self, test_user):
        self.find_user(test_user)
        return self.get_elem_text(self.get_desktop_ip_xpath)

    # 用户云桌面关机
    def close_desk(self, use_name):
        self.click_elem(self.cloud_desktop_xpath)
        time.sleep(3)
        self.find_user(use_name)
        self.scroll_into_view(self.user_more_button_xpath.format(use_name))
        self.click_elem(self.user_close)
        self.confirm_warning()
        self.confirm_manager_password()

    # A1.59用例页面操作
    # 更改A159_1用户的云桌面类型
    def vdi_desktop_type_1(self):
        self.new_test_user(user_group_name[0], user_A159)
        time.sleep(3)
        self.click_elem(self.user_more_button_xpath.format(user_A159))  # 点击用户的更多选择按钮
        self.user_compile()  # 进入用户编辑模块框
        self.desktop_configure()
        time.sleep(3)
        self.click_elem(self.vdi_type_choose_xpath)  # 点击云桌面类型，进行将个性改为还原
        self.click_elem(self.vdi_type_xpath.format(vdi_type[1]))  # 选择还原类型
        self.click_elem(self.vdi_image_choose_xpath)  # 配置还原类型的镜像
        self.click_elem(self.vdi_image1_xpath.format(select_vdi_restore_image[0]))
        time.sleep(2)
        self.confirm_compile(confirm_button_type[1])

    # 更改A159_2用户的云桌面类型
    def vdi_desktop_type_2(self):
        self.new_test_user(user_group_name[1], user_A259)
        time.sleep(5)
        self.click_elem(self.user_more_button_xpath.format(user_A259))
        self.user_compile()
        self.desktop_configure()
        self.click_elem(self.vdi_type_choose_xpath)  # 点击云桌面类型，进行将个性改为还原
        self.click_elem(self.vdi_type_xpath.format(vdi_type[0]))
        self.click_elem(self.vdi_image_choose_xpath)
        self.click_elem(self.vdi_image1_xpath.format(select_vdi_image["标配vdi镜像"]))
        time.sleep(2)
        self.confirm_compile(confirm_button_type[1])
        self.confirm_warning()

    # A1.60用例页面操作
    # 更改A160用户绑定的镜像
    def vdi_image_change(self):
        self.new_test_user(user_group_name[0], user_A160)
        time.sleep(10)
        self.click_elem(self.user_more_button_xpath.format(user_A160))
        self.user_compile()
        self.desktop_configure()
        self.click_elem(self.vdi_image_choose_xpath)
        time.sleep(1)
        self.scroll_into_view(self.vdi_image1_xpath.format(select_vdi_image["高配vdi镜像"]))
        time.sleep(2)
        self.confirm_compile(confirm_button_type[1])

    # A1.61用例页面操作
    # 编辑用户cpu,内存的更改
    def u_confirm(self, cpunumber):
        self.click_elem(self.vdi_user_group_xpath.format(user_group_name[0]))
        self.click_elem(self.user_more_button_xpath.format(user_A161))  # 点击用户的更多选择按钮
        self.user_compile()
        self.desktop_configure()
        self.click_elem(self.cpu_choose_xpath)
        self.click_elem(self.cpu_number_xpath.format(cpunumber))
        self.confirm_compile(confirm_button_type[1])
        self.confirm_warning()

    def dec_storage(self):
        self.click_elem(self.vdi_user_group_xpath.format(user_group_name[0]))
        self.click_elem(self.user_more_button_xpath.format(user_A161))  # 点击用户的更多选择按钮
        self.user_compile()
        self.desktop_configure()
        self.click_elem(self.decrease_storage_xpath)
        self.confirm_compile(confirm_button_type[1])
        self.confirm_warning()

    def inc_storage(self):
        self.click_elem(self.vdi_user_group_xpath.format(user_group_name[0]))
        self.click_elem(self.user_more_button_xpath.format(user_A161))  # 点击用户的更多选择按钮
        self.user_compile()
        self.desktop_configure()
        self.click_elem(self.increase_storage_xpath)
        self.confirm_compile(confirm_button_type[1])
        self.confirm_warning()

    # A1.62用例页面操作
    # 点击云桌面管理
    def desk(self):
        self.click_elem(self.vdi_user_group_xpath.format(user_group_name[0]))

    # 编辑用户系统盘和个人盘大小的更改
    def vm_sys_disk_size(self, sys_or_disk, inc_or_dec):
        self.click_elem(self.user_more_button_xpath.format(user_A162))  # 点击用户的更多选择按钮
        self.user_compile()
        self.desktop_configure()
        time.sleep(1)
        if inc_or_dec == select["inc"]:
            self.click_elem(self.dec_inc_size_xpath.format(sys_or_disk, inc_or_dec))
            self.confirm_compile(confirm_button_type[1])
            self.confirm_warning()
        elif inc_or_dec == select["dec"]:
            time.sleep(1)
            dec_class = self.get_elem_attribute(self.dec_disable_xpath.format(sys_or_disk), "class")
            if dec_class == r"el-input-number__decrease is-disabled":
                dec_button = r"is_disable"
                self.confirm_compile(confirm_button_type[1])
                self.confirm_warning()
                return dec_button

    #  删除A162用户
    def delete(self):
        self.click_elem(self.choose_user_xpath.format(user_A162))
        self.click_elem(self.delete_user_button_xpath)
        self.confirm_warning()
        self.confirm_manager_password()

    # A1.33用例页面操作
    # 修改用户组VDI设置中CPU、内存,将原先标配修改为6核4G内存
    def user_group_edit(self, memory, number, ):
        self.click_elem(self.vdi_user_group_xpath.format(user_group_name[2]))
        self.chainstay(self.user_group_xpath.format(user_group_name[2]))
        time.sleep(2)
        self.click_elem(self.user_group_edit_xpath.format(user_group_name[2]))
        self.desktop_configure()
        self.edit_text(self.mem_size_xpath, memory)
        self.click_elem(self.cpu_choose_xpath)
        self.click_elem(self.cpu_number_xpath.format(number))
        self.confirm_compile(confirm_button_type[2])
        self.confirm_warning()

    # A1.81用例页面操作
    # 选择用户，点击密码重置
    def user_reset_password(self, user_name):
        self.search_info(user_name)
        self.click_elem(self.user_more_xpath)  # 点击更多操作
        self.click_elem(self.user_password_reset_xpath)
        self.click_elem(self.password_reset_button_xpath)  # 重置用户密码

    # A1.21用例页面操作
    # 用户在线或休眠时设置VDI系统盘,个人盘，闪电云盘
    def per_network_disk(self, u_group, u_name):
        self.select_user_group()
        self.click_elem(self.vdi_user_group_xpath.format(u_group))
        self.click_elem(self.new_user_button_xpath)
        self.elem_send_keys(self.new_user_name_xpath, u_name)
        self.elem_send_keys(self.new_user_names_xpath, test_username)
        self.click_elem(self.vdi_per_net_disk_xpath)
        self.click_elem(self.vdi_net_disk_xpath)
        self.confirm_compile(confirm_button_type[0])

    def online_user_sys_disk(self, uname, sys_or_disk):
        self.click_elem(self.user_more_button_xpath.format(uname))  # 点击用户中的更多选项
        self.user_compile()  # 进入用户编辑模块框
        if sys_or_disk == select["sys"] or select["disk"]:
            self.desktop_configure()
            self.click_elem(self.dec_inc_size_xpath.format(sys_or_disk, select["inc"]))
        # elif sys_or_disk == select["net"]：
        self.confirm_compile(confirm_button_type[1])
        self.confirm_warning()
        if self.find_elem(self.prompt_frame_xpath):  # 判断是否是不能修改的提示
            return 0
        elif self.find_elem(self.success_prompt_frame_xpath):  # 判断是否是修改成功的提示
            return 1

    # 不可修改系统盘大小，提示框
    prompt_text_xpath = r"//*[@class='layui-layer-ico layui-layer-ico2']"
    # 镜像编辑，不可编辑提示框的确认按钮
    confirm_prompt_xpath = r"//*[@class='layui-layer-btn layui-layer-btn-']/a"
    # 取消镜像编辑的按钮
    cancel_edit_xpath = "//*[@class='btn_sq_light btn_right']"
    # 终端管理，胖终端,终端用户绑定，解绑按钮
    binding_user_xpath = "//*[@class='btn_light']"
    # 点击确认解绑或解绑
    ok_xpath = "//*[@id='btns_ok']"
    # 终端绑定用户的用户名框ID
    input_username_xpath = "//*[@id='userId12']"

    def single_idv_login(self, ip, name):
        """
        在web上初始化终端，重启终端，终端初始化，用户登入终端
        :param ip: 所要连接，初始化，登入的idv终端
        :param idv_name: 要连接的终端名
        :param name: 所要绑定的用户的用户名
        :return:
        """
        id = IdvPage(self.driver)
        id.goto_idv_terminal_page()
        id.terminal_init(ip)
        idv_initialization_click(ip)
        idv_pattern_chose(ip, pattern='single', name=name)
        mirror_dowload(ip)
        idv_login(ip, user_name=name, pwd='123')

    # A.35设置IDV桌面类型
    def set_idv_desktop_type1(self):
        self.goto_usermanage_page()
        self.create_group_openidv("idv1", idv_test_user1, idv_test_user1)
        idv_change_pwd(ip4, idv_test_user1, pwd)
        self.single_idv_login(ip4, idv_test_user1)

    def set_idv_desktop_type2(self):
        self.goto_usermanage_page()
        self.create_group_openidv("idv2", idv_test_user2, idv_test_user2)
        idv_change_pwd(ip4, idv_test_user2, pwd)
        self.single_idv_login(ip4, idv_test_user2)

    # 删除二级用户组下的测试用户
    def delete_user1(self, group, user_name):
        self.click_elem(self.vdi_user_group_xpath.format(group))
        self.click_elem(self.choose_user_xpath.format(user_name))
        self.click_elem(self.delete_user_button_xpath)
        self.confirm_warning()
        self.confirm_manager_password()
        time.sleep(1)

    def open_uesr_spacedisk(self, user_name):
        self.search_info(name=user_name)  # 搜索用户
        time.sleep(0.5)
        self.click_elem(self.user_more_xpath)  # 点击更多操作
        self.click_elem(self.editor_btns_xpath)  # 点击编辑
        self.find_elem(self.idv_policy).click()  # 点击左侧idv设置
        time.sleep(2)
        self.open_spaceDisk()
        self.confirm_warning()

    # 用例A1.69
    def idv_Local_disk(self):
        flag_list = [0, 0, 0, 0]
        self.goto_usermanage_page()
        self.create_group_openidv(idv_user_group2, u"个性", select_idv_personality_images[0])
        time.sleep(1)
        self.create_user_in_group(idv_user_group2, "idv07", "idv07")
        idv_change_pwd(ip4, "idv04", pwd)
        self.search_info(name="idv07")  # 搜索用户
        time.sleep(0.5)
        self.click_elem(self.user_more_xpath)  # 点击更多操作
        self.click_elem(self.editor_btns_xpath)  # 点击编辑
        self.find_elem(self.idv_policy).click()  # 点击左侧idv设置
        self.checkbox_set(u"使用本地盘", 'close')  # 关闭本地盘
        self.click_elem(self.confirm_xpath2)  # 点击确认
        info1 = self.get_alter_warning()
        if info1 != 0:
            flag_list[0] = 1
        self.confirm_warning()
        info2 = self.get_manager_password()
        if info2 != 0:
            flag_list[1] = 1
        self.confirm_manager_password()
        self.single_idv_login(ip4, "idv07")
        info = self.creat_vdi_cmd(ip4, 'Administrator', 'rcd', "cd D:")
        if info.__contains__("系统找不到指定的驱动器"):
            flag_list[2] = 1
        else:
            flag_list[2] = 0
        self.creat_vdi_cmd(ip4, 'Administrator', 'rcd', "logout")
        self.edit_gp_idv(idv_user_group2, isopen_idv=None, idv_or_vdi=u"idv", cd_type=None, image=None,
                         isopen_local_disk='close',
                         check_name=u"使用本地盘")
        self.search_info(name="idv07")  # 搜索用户
        time.sleep(0.5)
        self.click_elem(self.user_more_xpath)  # 点击更多操作
        self.click_elem(self.editor_btns_xpath)  # 点击编辑
        self.find_elem(self.idv_policy).click()  # 点击左侧idv设置
        self.checkbox_set(u"使用本地盘", 'open')  # 关闭本地盘
        self.click_elem(self.confirm_xpath2)  # 点击确认
        self.click_elem(self.sure_xpath)  # 点击确定
        time.sleep(2)
        if self.elem_is_exist(self.confirm_passwd_xpath) == 0:
            self.send_passwd_confirm(passwd=passwd)  # 输入用户名和密码
        self.single_idv_login(ip4, login_idv_name, "idv07")
        self.creat_vdi_cmd(ip4, 'Administrator', 'rcd', "r'create_new_file,D:\3M.txt,test'")
        info = get_win_conn_info(ip4, 'Administrator', 'rcd', "r'dir D:\test.txt")
        if info != "找不到文件":
            flag_list[3] = 1
        else:
            flag_list[3] = 0
        self.creat_vdi_cmd(ip4, 'Administrator', 'rcd', "logout")
        self.delete_test_user(idv_user_group2, "idv07")
        self.del_group(idv_user_group2, passwd)

    # 删除用户组下所有用户
    def del_user_in_group(self, group_name):
        self.scroll_into_view(self.click_group_xpath.format(group_name))
        self.chainstay(self.click_group_xpath.format(group_name))
        if self.elem_is_exist("//*[@class='el-table__row '][1]") == 0:
            self.del_user(passwd)
            self.find_elem(u"//p[contains(text(), '删除用户成功')]")

    # 收集日志成功
    user_log_succ_xpath = u"//*[@class='el-dialog']//span[contains(.,'请点击链接下载：')]"

    def collect_log_succ(self):
        """查看初始化是否完成"""
        time.sleep(10)
        try:
            return self.get_elem_text(self.user_log_succ_xpath)  # 存在
        except:
            return ''

    def user_recovery(self, gp_name):
        """删除用户和用户组"""
        self.driver.refresh()
        time.sleep(1.5)
        self.back_current_page()
        self.goto_usermanage_page()
        if gp_name in self.get_value(self.all_group_xpath):
            self.del_user_in_group(gp_name)
        time.sleep(2)
        self.del_group_exist(gp_name)

    # 跳转到用户管理界面
    def goto_usermanage(self):
        self.click_elem(self.usermanage_xpath)  # 进入用户管理

    # 点击删除用户组按钮
    def click_del_gp_btn(self, ugpname):
        if 0 == self.elem_is_exist(self.userGroup_list_xpath % ugpname):
            pass
        else:
            self.scroll_into_view(self.userGroup_list_xpath % ugpname, click_type=1)
        time.sleep(1)
        self.chainstay(self.userGroup_list_xpath % ugpname)
        time.sleep(2)
        self.click_elem(self.userGroup_list_delButton_xpath % ugpname)
        info = self.get_tips()
        return info

    # 点击某个用户组列表
    def click_usergp_list(self, ugp_name):
        time.sleep(2)
        self.click_elem(self.userGroup_list_xpath % ugp_name)

    # 云桌面ip
    def cloud_desk_ip(self):
        self.scroll_into_view(self.cloud_desk_ip_xpath)
        print self.get_elem_text(self.cloud_desk_ip_xpath)
        return self.get_elem_text(self.cloud_desk_ip_xpath)

    # 点击取消
    def click_cancel(self):
        self.click_elem(self.cancel_button_xpath)

    # 编辑桌面类型
    def edit_gp_deskstyle(self, name, character, style):
        self.edit_group1(name)
        self.changeDesktopStyle(character, style)
        self.image_bind(character)
        self.click_confirm()
        self.confirm_warning()


if __name__ == "__main__":
    pass
