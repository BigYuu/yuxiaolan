#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: LinMengYao/houjinqi
@contact: linmengyao@ruijie.com
@software: PyCharm
@time: 2018/12/27 11:25
"""
import datetime
import re
import time

from selenium.webdriver.common.keys import Keys

from Common.Basicfun import BasicFun
# from TestData.ImageData import over_time
from TestData.ImageData import base_path
from TestData.Logindata import *
from WebPages.AuthenmanagePage import AuthenManage
from WebPages.adnroid_vdi_page import AndroidVdi
from WebPages.permission_setPage import PermissionSet


class Image(BasicFun):
    """image management module"""

    img_manage_frame = "frameContent"
    up_download_xpath = u"//span[contains(text(),'上传 / 下载')]"
    img_dir_xpath = "//*[@id='image_dir_btn']"
    add_img_xpath = "//*[@id='add_image']"
    add_img_page_xpath = "//*[@class='layui-layer layui-layer-iframe']"
    img_type_xpath = "//*[@id='desktop']"
    img_name_xpath = "//*[@id='image_name']"
    iso_xpath = "//*[@id='iso']"
    os_xpath = "//*[@id='os']"
    btn_ok_xpath = "//*[@id='btns_ok']"
    img_list_xpath = "//*[@id='imageListForm']"
    vdi_switch_stat_xpath = "//label[text()='VDI云桌面：']/following-sibling::div/span"
    vdi_switch_xpath = "//label[text()='VDI云桌面：']/following-sibling::div/div"
    vdi_img_cbb_xpath = "//*[@for='vdiPolicy.imageIds']/following-sibling::div/div"
    optional_img_xpath = u"//li[text()='可绑定镜像']/following-sibling::li"

    # 用户管理-idv特性状态
    idv_switch_stat_xpath = "//label[text()='VDI云桌面：']/following-sibling::div/span"
    # 用户管理-idv特性开启/关闭按钮
    idv_switch_xpath = "//label[text()='IDV云终端：']/following-sibling::div//span[contains(text(),'已')]"
    # 用户管理-idv特性选择镜像
    idv_img_cbb_xpath = "//*[@for='idvPolicy.imageIds']/following-sibling::div/div"
    # 用户管理-用户的idv桌面系统盘大小
    idv_system_disk_xpath = "//*[@aria-labelledby='scrollpane-idvPolicy']/descendant::div[@class='el-input']/input"

    # 用户管理-用户的vdi桌面系统盘大小
    vdi_system_disk_xpath = '//*[contains(text(),"系统盘")]/following-sibling::*/descendant::*[@class="el-input"]/input'
    # 用户管理-用户的vdi桌面内存大小
    vdi_system_memory_xpath = '//*[contains(text(),"内存")]/following-sibling::*/descendant::*[@class="el-input"]/input'

    # 用户管理-某用户组
    group_xpath = "//*[@class='custom-tree-node']/child::div[contains(.,'{}')]"
    # 用户管理-某用户组删除按钮
    delete_group_xpath = "//div[contains(text(),'{}')]/parent::div//i[@class='el-icon-delete']/parent::button"
    # 用户管理-某用户组删除确认按钮
    delete_group_sure_xpath = "//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']"
    # 按钮_新建用户
    create_user_xpath = "//*[@class='sk-toolbar']/div[1]/button[1]"
    # 新建用户_用户名
    create_user_name_xpath = "//*[@for='userBaseInfo.userName']/following-sibling::div/div/input"
    # 新建用户_姓名
    create_real_name_xpath = "//*[@for='userBaseInfo.realName']/following-sibling::div/div/input"
    # 添加用户(组)_按钮_确认
    add_user_group_submit_xpath = "//*[@class='dialog-footer']/button[1]"
    # 创建管理员成功提示
    message_right_xpath = "//*[@class='el-notification right']"

    # 根据镜像名选择到的镜像xpath
    image_frame_xpath = "//div[@title='{}']"
    # 根据镜像名选择到的镜像框内编辑按钮xpath
    image_edit_button_xpath = u"//div[@title='{}']/../following-sibling::div/descendant::span[contains(text(),'编辑')]"
    # 根据镜像名选择到的镜像框内复制按钮xpath
    image_copy_button_xpath = u"//div[@title='{}']/../following-sibling::div/descendant::span[contains(text(),'复制')]"
    # 根据镜像名选择到的镜像框内更多按钮xpath
    image_more_button_xpath = u"//div[@title='{}']/../following-sibling::div/descendant::span[contains(text(),'更多')]"
    # 根据镜像名选择到的镜像框内更多内的删除按钮xpath
    image_delete_button_xpath = u"//div[@title='{}']/../following-sibling::div/descendant::span[contains(text()," \
                                u"'更多')]/../following-sibling::*/descendant::span[contains(text(),'删除')]"
    # 是否删除镜像确认框xpath
    image_delete_sure_frame_xpath = "//*[@class='layui-layer layui-layer-dialog']"
    # 确认删除镜像按钮xpath
    sure_button_xpath = "//a[@class='layui-layer-btn0']"
    # 取消删除镜像按钮xpath
    cancel_button_xpath = "//a[@class='layui-layer-btn1']"
    # 删除镜像提示已被绑定消息框xpath
    image_bind_warn_frame_xpath = "//*[@class='layui-layer layui-layer-dialog']"

    # 编辑界面frame的xpath
    image_edit_page_xpath = "//*[@class='layui-layer layui-layer-iframe']"
    # 编辑界面空白处xpath
    image_edit_page_blank_xpath = "//*[@class='dailog_page']"
    # 编辑界面镜像类型选择xpath
    image_edit_desktop_type_xpath = '//*[@id="desktop"]'
    # 编辑界面镜像类型选择xpath
    image_edit_os_type_xpath = '//*[@id="os"]'
    # IDV镜像编辑界面修改系统盘输入框xpath
    idv_image_edit_system_disk_xpath = "//*[@id='system_disk_size_idv']"
    # VDI镜像编辑界面修改系统盘输入框xpath
    vdi_image_edit_system_disk_xpath = "//*[@id='system_disk_size']"
    # 编辑界面确认xpath
    image_edit_page_sure_xpath = "//*[@class='btn_sq_dark btn_left']"
    # 编辑界面确认并启动xpath
    image_edit_page_sure_start_xpath = "//*[@id='btns_start']"
    # 编辑界面内存大小xpath
    image_edit_memory_size = "//*[@id='memory_size']"
    # 编辑界面镜像名称xpath
    image_edit_image_name = '//*[@id="image_name"]'

    # 复制镜像界面的xpath
    copy_page_xpath = "//*[@class='layui-layer layui-layer-iframe']"
    # 复制镜像界面的镜像名输入框
    copy_page_image_name_xpath = "//*[@id='image_name']"
    # 复制镜像界面的镜像文件名输入框
    copy_page_image_filename_xpath = "//*[@id='image_fileName']"
    # 复制镜像界面的确定按钮
    copy_page_image_sure_button_xpath = "//*[@id='btns_ok']"
    # 镜像被绑定标志xpath
    image_bind_xpath = u"//div[@title='{}']/../preceding-sibling::div[@class='tmpl_bind']"

    # 镜像已启动状态xpath
    image_start_status_xpath = '//*[@title="{}"]/../preceding-sibling::div/child::*[@title="正在启动中"]'
    # 镜像更新状态
    image_update_status_xpath = ''

    # 关闭镜像xpath
    close_image_xpath = '//*[@id="close_image"]'
    # 关闭镜像界面xpath
    close_image_page_xpath = "//*[@class='layui-layer layui-layer-iframe']"
    # 选择镜像xpath
    select_close_image_xpath = '//*[@class="input_checkbox2_select"]'
    # 未选择镜像xpath
    unselect_close_image_xpath = '//*[@class="input_checkbox2_unselect"]'
    # 关闭镜像确定xpath
    close_image_sure_xpath = '//*[@id="btns_ok"]'
    # 关闭镜像取消xpath
    close_image_cancel_xpath = '//*[@id="btns_cancel"]'
    # 当前启动镜像数量
    image_start_count_xpath = '//*[@id="dailog_page_count"]'
    # 弹出提示窗口确定按钮
    frame_sure_xpath = '//*[@class="layui-layer-btn0"]'

    # 镜像ISO界面删除xpath
    delete_iso_xpath = u"//*[text()='删除']"
    # 镜像ISO界面返回xpath
    iso_back_button_xpath = u"//*[text()='返回']"
    # 查看是否有镜像ISO xpath
    iso_name_xpath = '//*[contains(text(),"{}")]'

    # 错误信息
    errorName_xpath = "//*[@id='errorName']"

    # 3.2
    #     # 镜像管理
    #     img_manage_xpath = "//*[@class='menu-wrapper']//*[text()='镜像管理']"
    #     # 镜像ISO xpath
    #     iso_manage_xpath = '//*[@id="iso_btn"]'
    #     # 选择ISO xpath
    #     select_iso_xpath = '//*[contains(text(),"{}")]/../preceding-sibling::td/input'
    #     # 用户管理标签
    #     user_manage_xpath = '//*[text()="用户管理"]'

    # 4.0
    # 镜像管理
    img_manage_xpath = "//*[@class='el-scrollbar__view']//*[text()='镜像管理']"
    # 用户管理标签
    user_manage_xpath = '//*[text()="用户管理"]'
    # ISO管理xpath
    iso_manage_xpath = '//*[@id="iso"]'
    # 镜像ISO xpath
    iso_image_xpath = '//*[@id="base_iso"]'
    # 选择ISO xpath
    select_iso_xpath = '//*[contains(text(),"{}")]/../preceding-sibling::td/input'

    # 关闭云桌面特性后提示信息确认按钮xpath
    close_vm_sure_xpath = "//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']"

    def go_img_manage(self):
        """go to image management page  进入镜像管理页面"""
        self.find_elem(self.img_manage_xpath).click()
        time.sleep(1)
        self.get_ciframe(self.img_manage_frame)

    def upload_img(self, file_dir, file_name):
        """open the upload / download page to upload an image 打开上传/下载中的上传"""
        self.click_elem(self.up_download_xpath)
        self.find_elem(self.img_dir_xpath).click()
        self.file_upload(local_path=file_dir, file_name=file_name, times=100)

    def add_img(self, img_type, name, iso, os):
        """add iso image and input attribute 添加ISO镜像并且编辑属性"""
        if name in self.get_value(self.img_list_xpath):
            self.wait_image_update_cpmpleted(name)
            self.del_img(name)
            time.sleep(5)
        self.close_img()
        self.find_elem(self.add_img_xpath).click()  # 点击新增
        self.back_current_page()
        self.go_common_frame()
        # 选择镜像类型
        self.find_elem(self.img_type_xpath).click()
        select_img_type_xpath = self.img_type_xpath + "/option[contains(text(),'" + img_type + "')]"
        self.find_elem(select_img_type_xpath).click()
        # 输入镜像名称
        self.find_elem(self.img_name_xpath).send_keys(name)
        # 选择ISO安装光盘
        self.click_elem(self.iso_xpath)
        select_iso_xpath = self.iso_xpath + "/option[text()='" + iso + "']"
        self.find_elem(select_iso_xpath).click()
        # 选择操作系统
        self.find_elem(self.os_xpath).click()
        os_xpath = self.os_xpath + "/option[contains(text(),'Windows " + os + "')]"
        self.find_elem(os_xpath).click()
        self.find_elem(self.btn_ok_xpath).click()
        self.back_current_page()
        self.get_ciframe(self.img_manage_frame)
        self.get_elem_text(self.img_list_xpath).__contains__(name)
        self.back_current_page()

    """
    用户组中需要idv1，vdi1用户组
    镜像管理中需要名称为IDV_win7_Image_Test、VDI_win7_Image_Test的镜像
    """

    def check_img_state(self, name):
        """wait util the image is done"""
        stat_xpath = "//*[@id='imageListForm']//*[text()='" + name + "']/parent::div/preceding-sibling::div[2]"
        self.get_elem_text(stat_xpath)

    def sys_message_suc(self):
        """whether page show the successful information 查看是否成功"""
        ps = PermissionSet(self.driver)
        self.find_elem(ps.message_right_xpath).text.__contains__(u'成功')

    def vdi_func(self, img):
        """open vdi policy and select image 开启vdi特性，并且选择vdi用户的镜像"""
        self.scroll_into_view(self.vdi_switch_xpath)
        stat = self.get_elem_text(self.vdi_switch_stat_xpath)
        if u'关闭' in stat:
            self.find_elem(self.vdi_switch_xpath).click()
        self.scroll_into_view(self.vdi_img_cbb_xpath)
        # img_xpath = self.optional_img_xpath + u"/ul//*[text()='" + img + u"']"
        img_xpath = self.optional_img_xpath + u" /ul//*[contains(text(), ' " + img + u"')]"
        self.find_elem(img_xpath).click()

    def create_usr_with_vdi(self, name, realname, img):
        """
        create user with image 创建用户并且绑定镜像
        """
        ps = PermissionSet(self.driver)
        count1 = ps.count_record()
        self.find_elem(ps.create_user_xpath).click()
        self.find_elem(ps.create_user_name_xpath).send_keys(name)
        self.find_elem(ps.create_real_name_xpath).send_keys(realname)
        self.vdi_func(img)
        self.find_elem(ps.add_user_group_submit_xpath).click()
        self.sys_message_suc()
        count2 = ps.count_record()
        assert count2 == count1 + 1

    chose_idvmirrori_xpath = u"//*[@id='scrollpane-idvPolicy']//*[contains(text(),'绑定镜像：')]/parent::div//input"
    img_name1 = u"//span[contains(text(),'{}')]"

    def idv_func(self, img):
        """
        开启idv特性，并且选择镜像
        参数：镜像名
        """
        self.scroll_into_view(self.idv_switch_xpath)
        stat = self.get_elem_text(self.idv_switch_xpath)
        if stat == u'已关闭':
            self.find_elem(self.idv_switch_xpath).click()
        self.find_elem(self.chose_idvmirrori_xpath).click()  # 点击绑定镜像
        self.scroll_into_view(self.img_name1.format(img), click_type=1)
        self.find_elem(self.img_name1.format(img)).click()  # 绑定镜像

    def create_usr_with_idv(self, name, realname, img):
        """
        新建用户并且绑定idv镜像
        参数：用户登录名，用户名，镜像名
        """
        ps = PermissionSet(self.driver)
        count1 = ps.count_record()
        self.find_elem(ps.create_user_xpath).click()
        self.find_elem(ps.create_user_name_xpath).send_keys(name)
        self.find_elem(ps.create_real_name_xpath).send_keys(realname)
        self.idv_func(img)
        self.find_elem(ps.add_user_group_submit_xpath).click()
        self.sys_message_suc()
        count2 = ps.count_record()
        assert count2 == count1 + 1

    def click_image_edit(self, vm_name):
        """
        使鼠标悬停到镜像上，点击镜像编辑，打开编辑界面
        参数：镜像名称
        """
        self.scroll_into_view(self.image_frame_xpath.format(vm_name), click_type=1)
        self.chainstay(self.image_frame_xpath.format(vm_name))
        self.find_elem(self.image_edit_button_xpath.format(vm_name)).click()
        self.get_random_iframe(self.image_edit_page_xpath)

    def click_image_copy(self, vm_name):
        """
        使悬停到镜像上，点击镜像复制，打开复制界面
        参数：镜像名称
        """
        self.scroll_into_view(self.image_frame_xpath.format(vm_name), click_type=1)
        self.chainstay(self.image_frame_xpath.format(vm_name))
        self.find_elem(self.image_copy_button_xpath.format(vm_name)).click()

    def click_image_delete(self, vm_name):
        """
        使悬停到镜像上，点击镜像删除
        参数：镜像名称
        """
        self.scroll_into_view(self.image_frame_xpath.format(vm_name), click_type=1)
        self.chainstay(self.image_frame_xpath.format(vm_name))
        self.find_elem(self.image_more_button_xpath.format(vm_name)).click()
        self.find_elem(self.image_delete_button_xpath.format(vm_name)).click()

    def get_random_iframe(self, iframe_div_xpath):
        """
        当iframe的ID是变动时，切换到此iframe
        通过get_iframe_last_id获取变动的ID，使用get_ciframe切换
        参数：iframe所在div的元素
        """
        self.back_current_page()
        random = self.get_iframe_last_id(iframe_div_xpath)
        iframe_id = "layui-layer-iframe" + random
        self.get_ciframe(iframe_id)

    def get_current_iframe(self, iframe_id_xpath):
        """
        切换到当前iframe的框架内
        参数：iframe的ID
        """
        self.back_current_page()
        self.get_ciframe(iframe_id_xpath)

    def create_user_with_vdi(self, group, user_name, image):
        """
         进入用户管理界面，在某用户组中创建用户，开启vdi特性绑定镜像
         参数：用户组名，用户名，镜像名
        """
        ps = PermissionSet(self.driver)
        ps.go_user_management()
        ps.click_user_group(group)
        self.create_usr_with_vdi(user_name, user_name, image)  # 创建用户绑定该镜像

    def create_user_with_idv(self, group, user_name, image):
        """
         进入用户管理界面，在某用户组中创建用户，开启idv特性绑定镜像
         参数：用户组名，用户名，镜像名
        """
        ps = PermissionSet(self.driver)
        ps.go_user_management()
        ps.click_user_group(group)
        self.create_usr_with_idv(user_name, user_name, image)  # 创建用户绑定该镜像

    def close_user_vdi(self, user_name):
        """
         关闭vdi特性
         参数：用户名
        """
        ad = AuthenManage(self.driver)
        ad.find_elem(ad.user_manage_xpath).click()
        ad.find_elem(ad.search_xpath).send_keys(user_name, Keys.ENTER, Keys.CONTROL, 'a', Keys.BACK_SPACE)
        ad.find_elem(ad.chose_user_xpath.format(user_name)).click()
        ad.find_elem(ad.user_manage_more_button_xpath).click()
        ad.find_elem(ad.user_manage_edit_button_xpath).click()
        self.scroll_into_view(self.vdi_switch_xpath)
        stat = self.get_elem_text(self.vdi_switch_xpath)
        if stat == u'已开启':
            self.find_elem(self.vdi_switch_xpath).click()
        ad.find_elem(ad.vm_type_info_form_sure_button_xpath).click()
        self.find_elem(self.close_vm_sure_xpath).click()
        ad.find_elem(ad.input_passwd_xpath).send_keys(passwd)
        ad.find_elem(ad.input_passwd_sure_button_xpath).click()

    def close_user_idv(self, user_name):
        """
         关闭idv特性
         参数：用户名
        """
        ad = AuthenManage(self.driver)
        ad.find_elem(ad.user_manage_xpath).click()
        ad.find_elem(ad.search_xpath).send_keys(user_name, Keys.ENTER, Keys.CONTROL, 'a', Keys.BACK_SPACE)
        ad.find_elem(ad.chose_user_xpath.format(user_name)).click()
        ad.find_elem(ad.user_manage_more_button_xpath).click()
        ad.find_elem(ad.user_manage_edit_button_xpath).click()
        self.scroll_into_view(self.idv_switch_stat_xpath)
        stat = self.get_elem_text(self.idv_switch_stat_xpath)
        if stat == u'已开启':
            self.find_elem(self.idv_switch_xpath).click()
        ad.find_elem(ad.vm_type_info_form_sure_button_xpath).click()
        self.find_elem(self.close_vm_sure_xpath).click()
        ad.find_elem(ad.input_passwd_xpath).send_keys(passwd)
        ad.find_elem(ad.input_passwd_sure_button_xpath).click()

    def delete_image(self, image_name):
        """
         删除镜像
         参数：镜像名
        """
        self.back_current_page()
        self.go_img_manage()
        self.click_image_delete(image_name)
        self.back_current_page()
        self.find_elem(self.sure_button_xpath).click()
        time.sleep(3)

    def delete_user(self, user_name):
        """
         删除用户
         参数：用户名
        """
        ad = AuthenManage(self.driver)
        ad.find_elem(ad.user_manage_xpath).click()
        ad.find_elem(ad.search_xpath).send_keys(user_name, Keys.ENTER, Keys.CONTROL, 'a', Keys.BACK_SPACE)
        ad.find_elem(ad.chose_user_xpath.format(user_name)).click()
        ad.find_elem(ad.user_manage_delete_user_xpath).click()
        ad.find_elem(ad.user_manage_delete_confirm_xpath).click()
        ad.find_elem(ad.input_passwd_xpath).send_keys(passwd)
        ad.find_elem(ad.input_passwd_sure_button_xpath).click()
        time.sleep(3)

    user_more_xpath = u"//*[@class='el-table__body']//span[contains(text(),'更多')]"

    def user_idv_system_disk(self, user_name):
        """
         当前用户idv桌面的系统盘大小
         参数：用户名
         返回：当前用户idv桌面的系统盘大小
        """
        ad = AuthenManage(self.driver)
        ad.find_elem(ad.user_manage_xpath).click()
        ad.find_elem(ad.search_xpath).send_keys(user_name, Keys.ENTER, Keys.CONTROL, 'a', Keys.BACK_SPACE)
        ad.click_elem(self.user_more_xpath)
        ad.find_elem(ad.user_manage_edit_button_xpath).click()
        return ad.find_elem(self.idv_system_disk_xpath).get_attribute('aria-valuenow')

    def user_vdi_system_disk(self, user_name):
        """
         当前用户vdi桌面的系统盘大小
         参数：用户名
         返回：当前用户vdi桌面的系统盘大小
        """
        ad = AuthenManage(self.driver)
        ad.find_elem(ad.user_manage_xpath).click()
        ad.find_elem(ad.search_xpath).send_keys(user_name, Keys.ENTER, Keys.CONTROL, 'a', Keys.BACK_SPACE)
        ad.find_elem(ad.chose_user_xpath.format(user_name)).click()
        ad.find_elem(ad.user_manage_more_button_xpath).click()
        ad.find_elem(ad.user_manage_edit_button_xpath).click()
        return ad.find_elem(self.idv_system_disk_xpath).get_attribute('aria-valuenow')

    def add_user_group_check(self, group_name, vdi_base=0, idv_base=0):
        """
        添加用户组,并且选择是否绑定idv镜像
        参数：用户组名，镜像名，0代表不绑定
        返回：当前镜像的系统盘大小
        """
        disk_value = 0
        self.find_elem(self.user_manage_xpath).click()
        self.find_elem(PermissionSet.add_user_group_xpath).click()
        self.find_elem(PermissionSet.add_user_group_name_xpath).send_keys(group_name)
        if idv_base:
            self.idv_func(idv_base)
            disk_value = self.find_elem(self.idv_system_disk_xpath).get_attribute('aria-valuenow')
        else:  # base=0：跳过，不绑定镜像
            pass
        if vdi_base:
            self.vdi_func(vdi_base)
            disk_value = self.find_elem(self.vdi_system_disk_xpath).get_attribute('aria-valuenow')
        else:  # base=0：跳过，不绑定镜像
            pass
        self.find_elem(PermissionSet.add_user_group_submit_xpath).click()  # 确认
        self.find_elem(PermissionSet.message_right_xpath).text.__contains__(u'用户组创建成功')  # 验证提示
        return disk_value

    def delete_user_group(self, group_name):
        """
        删除用户组,并且选择是否绑定idv镜像
        参数：用户组名，镜像名，0代表不绑定
        返回：当前镜像的系统盘大小
        """
        self.find_elem(self.user_manage_xpath).click()
        self.chainstay(self.group_xpath.format(group_name))
        self.find_elem(self.delete_group_xpath.format(group_name)).click()
        self.find_elem(self.delete_group_sure_xpath).click()
        self.find_elem(AuthenManage.input_passwd_xpath).send_keys(passwd)
        self.find_elem(AuthenManage.input_passwd_sure_button_xpath).click()
        time.sleep(3)

    def click_user_group(self, user_group):
        """
        在用户组中点击一个用户组
        参数：用户组名
        """
        self.find_elem("//*[@class='user-group']/div[2]//*[contains(text(),'" + user_group + "')]").click()

    def create_user(self, user_name, real_name):
        """
        在用户组中新建一个用户
        参数：用户登录名，用户名
        """
        self.find_elem(self.create_user_xpath).click()  # 点击新建用户按钮
        self.find_elem(self.create_user_name_xpath).send_keys(user_name)  # 输入用户名
        self.find_elem(self.create_real_name_xpath).send_keys(real_name)  # 输入姓名
        self.find_elem(self.add_user_group_submit_xpath).click()  # 确认
        self.find_elem(self.message_right_xpath).text.__contains__(u'用户创建成功')  # 验证提示
        time.sleep(5)

    u"-----------------------------------------余小兰封装部分--------------------------------------"
    # 镜像正在更新，请稍后
    img_update_xpath = u"//div[contains(text(),'{}')]/..//preceding-sibling::div[contains(@class,'tmpl_torrent_update')]/div[2]"
    # 镜像即将发布或者需要安装GT提示信息
    img_pub_now = u"//div[contains(text(),'{}')]/..//preceding-sibling::div[contains(@class,'tmpl_torrent')]/div"
    # 镜像管理-镜像发布时间发布时间
    img_pub_time_xpath = u"//div[contains(text(),'{}')]/..//preceding-sibling::div[contains(@class,'tmpl_torrent')]"
    # 根据传入的镜像名获取镜像的最外层div
    img_xpath = u"//*[contains(text(),'{}')]//ancestor::div[contains(@class,'tmpl_item')]"
    # 镜像列表
    img_item = "//div[contains(@class,'tmpl_item')]"
    # 镜像详情-镜像名称
    detail_left = "//div[contains(@class,'detail_left')]"
    # 镜像启动三角尖
    img_is_star = "//div[contains(text(),'{}')]/../..//img[contains(@class,'tmpl_active_img')]"
    # 高性能选择框
    high_performance_xpath = "//*[@id='config_2']"
    # 自定义选择框
    custom_xpath = "//*[@id='config_3']"
    # 内存输入框
    memory_size_xpath = "//*[@id='memory_size']"
    # 系统内存
    system_disk_size_xpath = "//*[@id='system_disk_size']"
    img_is_bangding = u"//div[contains(text(),'{}')]/../..//div[@class='tmpl_active']/img"

    def add_img_cofig_diff(self, img_type, name, iso, os, config_type, memory_size=None, system_disk_size=None):
        """添加不同配置（标准，高，自定义）的镜像"""
        self.find_elem(self.add_img_xpath).click()
        self.back_current_page()
        random = self.get_iframe_last_id(self.add_img_page_xpath)
        add_img_frame_id = "layui-layer-iframe" + random
        self.get_ciframe(add_img_frame_id)
        self.find_elem(self.img_type_xpath).click()
        select_img_type_xpath = self.img_type_xpath + "/option[contains(text(),'" + img_type + "')]"
        self.find_elem(select_img_type_xpath).click()
        self.find_elem(self.img_name_xpath).send_keys(name)
        self.find_elem(self.iso_xpath).click()
        select_iso_xpath = self.iso_xpath + "/option[text()='" + iso + "']"
        self.find_elem(select_iso_xpath).click()
        self.find_elem(self.os_xpath).click()
        os_xpath = self.os_xpath + "/option[contains(text(),'Windows " + os + "')]"
        self.find_elem(os_xpath).click()
        if u"高性能" in config_type:
            self.find_elem(self.high_performance_xpath).click()
        elif u"自定义" in config_type:
            self.find_elem(self.custom_xpath).click()
            self.clear_text_info(self.memory_size_xpath)  # 清空默认内存数据
            self.find_elem(self.memory_size_xpath).send_keys(memory_size)  # 输入内存大小
            self.clear_text_info(self.system_disk_size_xpath)  # 清空默认系统盘大小
            self.find_elem(self.system_disk_size_xpath).send_keys(system_disk_size)  # 输入系统盘大小,此处a1_15的用户将磁盘的大小设置为100
        self.find_elem(self.btn_ok_xpath).click()
        self.back_current_page()
        self.get_ciframe(self.img_manage_frame)
        self.get_elem_text(self.img_list_xpath).__contains__(name)
        self.back_current_page()

    # 查看镜像详情
    img_info_xpath = u"//div[contains(text(),'{}')]//parent::div[@class='tmpl_info']/.." \
                     u"//div[contains(@class,'tmpl_type')]//following-sibling::div[contains(@class,'os_ico_big')]"
    # 镜像详细信息-CPU
    img_detail_cpu = "//*[@id='cpu_num']"
    # 镜像详细信息-内存
    img_detail_memory_size = "//*[@id='memory_size']"
    # 镜像详细信息-系统盘
    img_detail_system_disk_size = "//*[@id='system_disk_size']"
    # 镜像详细信息-镜像名称
    img_name = "//*[@id='image_name']"

    def check_img_info(self, img_name):
        """查看镜像详情"""
        self.scroll_into_view(self.image_frame_xpath.format(img_name), click_type=1)
        self.chainstay(self.image_frame_xpath.format(img_name))
        time.sleep(1)
        self.click_elem(self.img_info_xpath.format(img_name))
        random = self.get_iframe_last_id(self.add_img_page_xpath)  # 进入镜像详细信息iframe
        img_detail_iframe_id = "layui-layer-iframe" + random
        self.get_ciframe(img_detail_iframe_id)

    # 镜像详情页面--文本框值
    def get_value(self, locator):
        return self.get_elem_text(locator=locator)

    # 镜像详情关闭按钮
    img_detail_close_button = "//*[@id='btns_ok']"

    def close_img_info(self):
        """关闭镜像详情页关闭按钮"""
        self.find_elem(self.img_detail_close_button).click()  # 点击镜像详情页关闭按钮
        self.back_current_page()

    def del_img(self, img_name):
        """删除镜像"""
        self.scroll_into_view(self.image_frame_xpath.format(img_name), click_type=1)
        self.chainstay(self.image_frame_xpath.format(img_name))
        self.find_elem(self.image_more_button_xpath.format(img_name)).click()  # 点击具体的镜像名下的更多按钮
        self.find_elem(self.image_delete_button_xpath.format(img_name)).click()  # 更多-删除
        self.back_current_page()
        self.find_elem(self.sure_button_xpath).click()
        time.sleep(3)
        self.get_ciframe(self.img_manage_frame)

    # 根据镜像名选择到的镜像框内更多内的安装驱动按钮xpath
    image_installdriver_button_xpath = u"//div[@title='{}']/../following-sibling::div/descendant::span[contains(text()," \
                                       u"'更多')]/../following-sibling::*/descendant::span[contains(text(),'删除')]/../..//span[contains(text(),'驱动安装')]"
    # 终端型号
    terminal_model = "//*[@id='terminal_model']"
    # 根据终名称勾选安装驱动
    terminal_driver = "//div[contains(@title,'{}')]/div[1]"
    # 确定安装驱动
    sure_install_driver_btn = "//*[@id='btns_ok']"

    # 安装驱动(目前只做匹配Rain终端系列)
    def install_driver(self, img_name, serial, version, terminal_name):
        """img_name:镜像名称 serial:系列 version:版本 terminal_name:安装驱动的终端"""
        self.scroll_into_view(self.image_frame_xpath.format(img_name), click_type=1)
        self.chainstay(self.image_frame_xpath.format(img_name))
        self.find_elem(self.image_more_button_xpath.format(img_name)).click()  # 点击具体的镜像名下的更多按钮
        self.find_elem(self.image_installdriver_button_xpath.format(img_name)).click()  # 更多-驱动安装
        self.back_current_page()
        random = self.get_iframe_last_id(self.add_img_page_xpath)
        img_detail_iframe_id = "layui-layer-iframe" + random
        self.get_ciframe(img_detail_iframe_id)
        time.sleep(0.5)
        print(serial)
        print(version)
        if (serial == u'300' or serial == u'400') and (version == u'1'):
            self.select_list_chose(self.terminal_model, "Rain300/400系列(硬件版本：V1.XX)")
            time.sleep(5)
        elif (serial == u'305' or serial == u'405') and (version == u'1'):
            self.select_list_chose(self.terminal_model, "Rain305/405系列(硬件版本：V1.XX)")
        elif (serial == u'310' or serial == u'410') and (version == u'1'):
            self.select_list_chose(self.terminal_model, "Rain310/410系列(硬件版本：V1.XX)")
        elif (serial == u'310' or serial == u'410') and (version == u'2'):
            self.select_list_chose(self.terminal_model, "Rain310/410系列(硬件版本：V2.XX)")
        elif (serial == u'320') and (version == u'1'):
            self.select_list_chose(self.terminal_model, "Rain320系列(硬件版本：V1.XX)")
        elif (serial == u'320') and (version == u'2'):
            self.select_list_chose(self.terminal_model, "Rain320系列(硬件版本：V2.XX)")
        self.find_elem(self.terminal_driver.format(terminal_name)).click()  # 根据终端名称勾选安装的驱动
        self.find_elem(self.sure_install_driver_btn).click()  # 点击确定安装驱动
        self.back_current_page()
        self.click_elem(self.sure_button_xpath)  # 再次点击确定

    # 确定并启动按钮
    btns_start_xpath = "//*[@id='btns_start']"
    # 镜像发布时间iframe
    img_public_xpath = "//*[@class='layui-layer layui-layer-iframe'][2]"
    # 立即发布单选框
    immediaterelease_xpath = "//*[@id='immediateRelease']"
    # 标准配置单选框
    standard_config = "//*[@id='config_1']"

    #  编辑镜像为不同的配置,此处情况为镜像被绑定
    def editor_img_sysconfig(self, sysconfig_type, memory_size="2", system_disk_size="40", pubdate=None):
        """sysconfig_type:系统配置"""
        if sysconfig_type == u"标准配置":
            self.click_elem(self.standard_config)
        elif sysconfig_type == u"高性能":
            self.click_elem(self.high_performance_xpath)
        elif sysconfig_type == u"自定义":
            self.click_elem(self.custom_xpath)
            self.clear_text_info(self.memory_size_xpath)  # 清空默认内存数据
            self.find_elem(self.memory_size_xpath).send_keys(memory_size)  # 输入内存大小
            self.clear_text_info(self.system_disk_size_xpath)  # 清空默认系统盘大小
            self.find_elem(self.system_disk_size_xpath).send_keys(system_disk_size)  # 输入系统盘大小,此处a1_15的用户将磁盘的大小设置为100
        if pubdate is not None:
            time.sleep(1)
            self.find_elem(self.btns_start_xpath).click()
            self.back_current_page()
            if self.elem_is_exist(self.img_public_xpath) == 0:
                self.get_random_iframe(self.img_public_xpath)
                if pubdate == u"立即发布":
                    self.click_elem(self.immediaterelease_xpath)
                    self.click_elem(self.btn_ok_xpath)  # 点击确认
                elif pubdate == u"稍后发布":
                    self.click_elem(self.btn_ok_xpath)  # 点击确认
        else:
            self.click_elem(self.btn_ok_xpath)
        self.back_current_page()
        self.get_ciframe(self.img_manage_frame)

    # 关闭镜像按钮
    close_img_xpath = "//*[@id='close_image']"
    # 确定按钮
    sure_btn_xpath = "//*[@class='layui-layer-btn0']"
    # 通过镜像名称来选择需要删除镜像
    close_check_box = "//div[contains(text(),'{}')]/..//preceding-sibling::div[contains(@class,'checkbox_item')]"

    def close_img(self):
        self.back_current_page()
        self.go_img_manage()
        self.click_elem(self.close_img_xpath)  # 点击关闭镜像
        self.back_current_page()
        self.get_random_iframe(self.image_edit_page_xpath)
        self.click_elem(self.btn_ok_xpath)  # 点击确定
        self.back_current_page()
        # 镜像未开启关闭镜像
        if self.elem_is_exist(self.sure_btn_xpath) == 0:
            self.click_elem(self.sure_btn_xpath)
            self.get_random_iframe(self.image_edit_page_xpath)
            self.click_elem(self.close_image_cancel_xpath)
            self.back_current_page()
        self.get_ciframe(self.img_manage_frame)

    # 根据镜像名来启动镜像
    start_btn_xpath = u"//div[@title='{}']/../following-sibling::div/descendant::span[contains(text(),'启动')]"

    def img_start_nopub(self, img_name):
        """未被还原用户或组绑定时启动镜像，即不要设置发布时间节点"""
        self.scroll_into_view(self.image_frame_xpath.format(img_name), click_type=1)
        # self.scroll_into_view()
        self.chainstay(self.image_frame_xpath.format(img_name))
        self.find_elem(self.start_btn_xpath.format(img_name)).click()
        self.back_current_page()
        self.click_elem(self.sure_btn_xpath)

    # 发布时间输入框
    pub_time_xpath = "//*[@id='releaseTime']"
    # 稍后发布单选框
    pub_later_xpath = "//*[@id='alterRelease']"
    # 选择时间
    select_time_xpath = "//*[@class='laydate-btns-time']"
    # day
    date_list_xpath = u"//*[@class='layui-laydate-content']//table//tbody//*[@class='layui-this']//preceding-sibling::td[1]"
    # 小时
    hourse_xpath = u"//ul[@class='layui-laydate-list laydate-time-list']//p[text()='时']/..//li[text()='{}']"
    # 分钟
    minute_xpath = u"//ul[@class='layui-laydate-list laydate-time-list']//p[text()='分']/..//li[text()='{}']"
    # 确定时间修改
    sure_time_editor = "//*[@class='laydate-btns-confirm']"

    # 镜像被还原用户或组绑定时，需要添加确认镜像发布时间
    def click_img_start(self, vm_name, pudate_time=None, d=0, h=0, m=0):
        """根据vmname启动镜像,pudate_time:镜像发布时间"""
        self.scroll_into_view(self.image_frame_xpath.format(vm_name), click_type=1)
        self.chainstay(self.image_frame_xpath.format(vm_name))
        time.sleep(0.5)
        self.find_elem(self.start_btn_xpath.format(vm_name)).click()
        time.sleep(1)
        if pudate_time == u"立即发布":
            self.get_random_iframe(self.image_edit_page_xpath)
            self.click_elem(self.immediaterelease_xpath)  # 点击立即发布单选框
        if pudate_time == u"稍后发布":
            self.get_random_iframe(self.image_edit_page_xpath)
            self.click_elem(self.pub_time_xpath)  # 点击发布时间输入框
            if d != 0 or h != 0 or m != 0:
                info = self.set_pub_time(da=d, ho=h, mi=m)
                self.click_elem(self.date_list_xpath)  # 选择日期
                if h != 0 or m != 0:
                    self.click_elem(self.select_time_xpath)  # 点击选择时间
                    self.scroll_into_view(self.hourse_xpath.format(info['hours']))  # 鼠标滚动并点击到相对应的小时
                    self.scroll_into_view(self.minute_xpath.format(info['minute']))  # 鼠标滚动并点击到相对应的分钟上
            self.click_elem(self.sure_time_editor)
            time.sleep(1)
        self.click_elem(self.btn_ok_xpath)  # 点击确认

    def set_pub_time(self, da=0, ho=0, mi=0):
        """设置镜像发布时间"""
        pub_time = (datetime.datetime.now() + datetime.timedelta(days=da, hours=ho, minutes=mi)).strftime(
            "%Y-%m-%d %H:%M:%S")
        date_info = dict()
        info = str(pub_time)
        date_info['day'] = info[8:10]
        date_info['hours'] = info[11:13]
        date_info['minute'] = info[14:16]
        return date_info

    # 某个镜像的终端类型
    img_terminal_type = u"//*[@id='imageListForm']/div[{}]//img[contains(@class,'tmpl_type')]"

    def get_terminal_type(self, item):
        terminal_type_icon = str(self.get_elem_attribute(self.img_terminal_type.format(item), attribute="src"))
        return terminal_type_icon

    def copy_img(self, by_copy_img, copy_img):
        """
        :param by_copy_img: 被复制镜像名称
        :param copy_img: 复制后镜像名称
        """
        self.click_image_copy(vm_name=by_copy_img)  # 点击编辑
        self.back_current_page()
        self.get_random_iframe(self.image_edit_page_xpath)  # 进入到镜像复制页面
        self.find_elem(self.img_name).send_keys(copy_img)  # 输入复制后的镜像名称
        self.click_elem(self.btn_ok_xpath)

    def goto_driver_install(self, img_name):
        """进入驱动安装页面"""
        self.scroll_into_view(self.image_frame_xpath.format(img_name), click_type=1)
        self.chainstay(self.image_frame_xpath.format(img_name))
        self.find_elem(self.image_more_button_xpath.format(img_name)).click()  # 点击具体的镜像名下的更多按钮
        self.find_elem(self.image_installdriver_button_xpath.format(img_name)).click()  # 更多-驱动安装
        self.back_current_page()
        random = self.get_iframe_last_id(self.add_img_page_xpath)
        img_detail_iframe_id = "layui-layer-iframe" + random
        self.get_ciframe(img_detail_iframe_id)

    # 界面下方管理员工具
    down_tool = "//*[@id='down_tool']"
    down_tool_admin = "//*[@id='down_tool_admin']"

    def admin_tool_dowload(self, a):
        """管理员工具下载"""
        self.find_elem(self.down_tool_admin).click()  # 点击立即下载按钮
        time.sleep(2)
        self.download()
        time.sleep(a)

    # 镜像在更新或者发布时镜像os_ico元素不会出现
    os_ico_xpath = u"//*[text()='{}']/../..//div[contains(@class,'os_ico')]"
    refresh = u"//*[@id='refresh']"

    # 等待镜像更新或者发布完成
    def wait_image_update_cpmpleted(self, img_name):
        self.back_current_page()
        self.get_ciframe(self.img_manage_frame)
        self.click_elem(self.refresh)
        time.sleep(5)
        try:
            self.wait_elem_not_presence(self.img_update_xpath.format(img_name))
        except Exception as error:
            print(u"镜像发布或更新完成")

    # 系统正在处理请求
    sys_please_xpath = "//*[@class='layui-layer-content layui-layer-padding']"

    def wait_image_copy_completed(self):
        """等待镜像复制完成"""
        self.back_current_page()
        self.wait_elem_not_presence(self.sys_please_xpath)
        time.sleep(1)
        self.get_ciframe(self.img_manage_frame)

    iframe_id_xpath = "//*[@class='layui-layer layui-layer-iframe']"

    def get_frame_id(self):
        self.back_current_page()
        ele = self.find_elem(self.iframe_id_xpath)
        s = ele.get_attribute("id")
        return re.findall('.*?(\d+)', s)[0]

    common_frame_xpath = "layui-layer-iframe{}"

    def go_common_frame(self):
        self.back_current_page()
        time.sleep(1)
        fid = self.get_frame_id()
        self.get_ciframe(self.common_frame_xpath.format(fid))

    iso_manage = u"//*[contains(text(),'ISO管理')]"
    refresh_xpath = u"//span[contains(text(),'刷新')]"
    return_btns = u"//span[contains(text(),'返回')]"

    # 进入ISO刷新iso列表
    def go_iso_and_refresh(self, is_return=0):
        self.back_current_page()
        self.get_ciframe(self.img_manage_frame)
        self.click_elem(self.iso_manage)  # 点击ISO管理
        self.click_elem(self.iso_image_xpath)  # 点击镜像ISO
        self.back_current_page()
        self.click_elem(self.refresh_xpath)  # 点击刷新按钮
        time.sleep(1)
        if is_return == 1:  # is_return=1点击返回
            self.click_elem(self.return_btns)
            self.get_ciframe(self.img_manage_frame)

    # 根据ISO名称删除ISO文件
    iso_label = u"//span[contains(text(),'{}')]/../..//preceding-sibling::td//label"
    iso_del_xpath = u"//span[contains(text(),'删除')]"

    # 进入ISO删除ISO文件
    def go_iso_and_del(self, iso_name, is_return=0):
        self.back_current_page()
        self.get_ciframe(self.img_manage_frame)
        self.click_elem(self.iso_manage)  # 点击ISO管理
        self.click_elem(self.iso_image_xpath)  # 点击镜像ISO
        self.back_current_page()
        self.click_elem(self.iso_label.format(iso_name))  # 选择单选框
        self.click_elem(self.iso_del_xpath)  # 点击删除
        self.click_elem(self.refresh_xpath)  # 点击刷新
        time.sleep(1.5)
        if is_return == 1:  # is_return=1点击返回
            self.click_elem(self.return_btns)
            self.get_ciframe(self.img_manage_frame)

    def del_iso_exist(self, iso_name, is_return=0):
        """删除已存在的iso文件"""
        self.back_current_page()
        self.get_ciframe(self.img_manage_frame)
        self.click_elem(self.iso_manage)  # 点击ISO管理
        self.click_elem(self.iso_image_xpath)  # 点击镜像ISO
        self.back_current_page()
        self.click_elem(self.refresh_xpath)  # 点击刷新
        if self.elem_is_exist(self.iso_label.format(iso_name)) == 0:
            self.click_elem(self.iso_label.format(iso_name))  # 选择单选框
            self.click_elem(self.iso_del_xpath)  # 点击删除
        time.sleep(1.5)
        if is_return == 1:  # is_return=1点击返回
            self.click_elem(self.return_btns)
            self.get_ciframe(self.img_manage_frame)

    # 判断镜像iso列表是否存在所需要的iso文件，若不存在则下载iso文件
    iso_span = u"//*[contains(text(),'{}')]"

    def add_iso_not_exist(self, iso_name):
        """iso文件不存在时，上传iso文件"""
        self.back_current_page()
        self.get_ciframe(self.img_manage_frame)
        self.click_elem(self.iso_manage)  # 点击ISO管理
        self.click_elem(self.iso_image_xpath)  # 点击镜像ISO
        self.back_current_page()
        self.click_elem(self.refresh_xpath)  # 点击刷新
        if self.elem_is_exist(self.iso_span.format(iso_name)) == 1:  # 镜像列表不存在则下载
            self.click_elem(self.return_btns)  # 点击返回
            time.sleep(1)
            self.get_ciframe(self.img_manage_frame)
            self.upload_img(base_path, iso_name)  # 下载文件
            flag = 1
            return flag
        else:
            self.click_elem(self.return_btns)  # 点击返回
            self.get_ciframe(self.img_manage_frame)
        time.sleep(2)

    def edit_image_name_os(self, image_name, new_name=None, os=None, image_type=None):
        """修改镜像名称或操作系统"""
        self.click_image_edit(vm_name=image_name)
        if image_type != None:
            self.find_elem(self.img_type_xpath).click()
            select_img_type_xpath = self.img_type_xpath + "/option[contains(text(),'" + image_type + "')]"
            self.find_elem(select_img_type_xpath).click()
        if new_name is not None:
            self.clear_text_info(self.image_edit_image_name)
            self.find_elem(self.image_edit_image_name).send_keys(new_name)  # 修改镜像名称
        if os is not None:
            self.find_elem(self.os_xpath).click()
            os_xpath = self.os_xpath + "/option[contains(text(),'Windows " + os + "')]"
            self.find_elem(os_xpath).click()
        else:
            pass
        self.find_elem(self.image_edit_page_sure_xpath).click()  # 点击确定
        self.back_current_page()
        self.get_ciframe(self.img_manage_frame)

    sysdisk_size_xpath = u"//input[@id='system_disk_size_idv']"
    def get_sysdisk_size(self,imgname):
        self.click_image_edit(imgname)
        disksize = self.get_elem_attribute(self.sysdisk_size_xpath, 'value')
        return disksize

    def click_cancel(self):
        self.click_elem(self.close_image_cancel_xpath)
        time.sleep(1)

    def copy_image(self, by_copy, copy_name):
        """复制镜像（避免各种意外）"""
        self.wait_image_update_cpmpleted(by_copy)  # 等待镜像更新成功
        n = 0
        while n < 10:
            try:
                self.copy_img(by_copy, copy_name)  # 复制镜像
                self.back_current_page()
                # 镜像正在复制或新增提示信息确定按钮
                if self.elem_is_exist(self.sure_button_xpath) == 1:
                    self.wait_image_copy_completed()
                    break
            except:
                if self.elem_is_exist(self.sure_button_xpath) == 0:
                    self.driver.refresh()
                    self.back_current_page()
                    self.go_img_manage()
                    self.close_img()
                    time.sleep(6)
                else:
                    pass
            n = n + 1

    # 镜像更新中。。。
    img_updating = u"//*[text()='镜像更新中，请稍候......']"

    def img_recovery(self, img_name=None):
        """镜像管理后置条件"""
        self.driver.refresh()
        self.back_current_page()
        self.go_img_manage()
        # 关闭无论如何关闭镜像
        self.close_img()
        # 等待镜像更新完成并删除镜像
        if img_name != None and img_name in self.get_value(self.img_list_xpath):
            self.wait_image_update_cpmpleted(img_name)
            self.del_img(img_name)
            time.sleep(3)
        else:
            pass


if __name__ == '__main__':
    pass
