#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: LinMengYao
@contact: linmengyao@ruijie.com
@software: PyCharm
@time: 2018/12/14 14:36
"""

from Common.Basicfun import BasicFun
from selenium.webdriver.common.keys import Keys
import time


class PermissionSet(BasicFun):
    """管理员账号设置模块"""
    # 高级配置标签
    advanced_config_xpath = u"//*[@class='el-menu']//*[text()='高级配置']"
    # 系统设置标签
    system_setting_xpath = u"//*[@class='el-menu']//*[text()='系统设置']"
    # 管理员账号设置标签
    admin_setting_xpath = u"//span[contains(text(),'管理员账号设置')]"
    # 用户管理标签
    user_manage_xpath = u"//span[contains(text(),'用户管理')]"
    # 按钮_新建
    create_new_xpath = "//*[@class='sk-more-button filter-item']//button"
    # 下拉选项_新建账号
    create_account_xpath = u"//li[contains(text(),'新建账号')]"
    # 搜索框_管理员
    search_admin_xpath = "//*[@class='filter-item el-input el-input--suffix']/input"
    # 输入框_管理员名称
    admin_name_xpath = "//*[@class='el-form new-account-form']/div[1]/div/div/input"
    # 验证提示_管理员名称
    warn_admin_name_xpath = "//*[@class='el-form new-account-form']/div[1]/div/div[2]"
    # 输入框_姓名
    name_xpath = "//*[@class='el-form new-account-form']/div[2]/div/div/input"
    # 输入框_密码
    password_xpath = "//*[@class='el-form new-account-form']/div[3]/div/div/input"
    # 验证提示_密码
    warn_password_xpath = "//*[@class='el-form new-account-form']//div[@class='el-form-item__error']"
    # 输入框_确认密码
    assure_password_xpath = "//*[@class='el-form new-account-form']/div[4]/div/div/input"
    # 验证提示_确认密码
    warn_assure_password_xpath = "//*[@class='el-form new-account-form']/div[4]/div/div[2]"
    # 按钮_用户组
    user_group_xpath = "//*[@class='el-form-item']/div/div[1]/div[3]/button"
    # 按钮_胖终端组
    idv_group_xpath = "//*[@class='el-form-item']/div/div[2]/div[3]/button"
    # 按钮_瘦终端组
    vdi_group_xpath = "//*[@class='el-form-item']/div/div[3]/div[3]/button"
    # 按钮_确定
    submit_xpath = "//*[@class='el-dialog__footer dialog-footer__custom']/button[1]"
    # 按钮_取消
    cancel_xpath = "//*[@class='el-dialog__footer dialog-footer__custom']/button[2]"
    # 搜索框_用户组
    keyword_search_xpath = "//*[@class='el-input el-input--suffix']/input"
    # 按钮_确定_用户组
    add_group_submit_xpath = "//*[@class='add-tree-body']/div[2]/button[1]"
    # 管理员账号设置_第1条_管理员
    result_admin_xpath = "//*[@class='el-table__body']/tbody/tr[1]/td[2]/div[1]/span[1]"
    # 管理员账号设置_第1条_状态
    result_status_xpath = "//*[@class='el-table__body']/tbody/tr[1]/td[3]/div[1]/span"
    # 管理员账号设置_第1条_类型
    result_type_xpath = "//*[@class='el-table__body']/tbody/tr[1]/td[4]/div[1]/span"
    # 管理员账号设置_第1条_用户组
    result_user_xpath = "//*[@class='el-table__body']/tbody/tr[1]/td[5]/div[1]/span"
    # 管理员账号设置_第1条_胖终端组
    result_idv_xpath = "//*[@class='el-table__body']/tbody/tr[1]/td[6]/div[1]/span"
    # 管理员账号设置_第1条_瘦终端组
    result_vdi_xpath = "//*[@class='el-table__body']/tbody/tr[1]/td[7]/div[1]/span"
    # 创建管理员成功提示
    message_right_xpath = "//*[@class='el-notification right']"
    # 编辑管理员修改成功提示
    edit_admin_success_xpath = "//*[@class='el-notification__content']/p"
    # 创建管理员数据不合法提示
    create_invalid_info_xpath = "//*[@class='el-message el-message--warning']"
    # 注销
    logout_xpath = u"//li[contains(text(),'注销')]"
    # 欢迎您logo
    welcome_user_xpath = "//*[@class='sk-navitem__user']"
    # 提示框_账号不带资源时提交
    message_no_resource_xpath = "//*[@class='el-message-box__btns']"
    # 按钮_第一行_修改用户组
    edit_user_group_xpath = "//*[contains(text(),'{}')]/ancestor::tr/td[5]//button[contains(@class,'add-button')]"
    # 按钮_第一行_修改idv终端组
    edit_idv_group_xpath = "//*[contains(text(),'{}')]/ancestor::tr/td[6]//button[contains(@class,'add-button')]"
    # 按钮_第一行_修改vdi终端组
    edit_vdi_group_xpath = "//*[contains(text(),'{}')]/ancestor::tr/td[7]//button[contains(@class,'add-button')]"
    # 按钮_第一行_更多
    more_xpath = "//*[@class='sk-table sk-app__inner']/div[2]/div[3]//*[@class='el-table__row'][1]/td[8]/div/div"
    # 按钮_第一行_更多-编辑
    more_edit_xpath = u"//ul[@x-placement='bottom-start']//li[contains(text(),'编辑') and @class='el-dropdown-menu__item']"
    # 编辑_管理员名称
    edit_admin_name_xpath = "//*[@for='name']/following-sibling::div/div/input"
    # 编辑_姓名
    edit_name_xpath = "//*[@for='realName']/following-sibling::div/div/input"
    # 按钮_第一行_更多-重置密码
    more_reset_password_xpath = \
        "//ul[@x-placement='bottom-start']//li[contains(text(),'重置密码') and @class='el-dropdown-menu__item']"
    # 重置密码_密码
    reset_password_xpath = "//*[@for='password']/following-sibling::div/div/input"
    # 重置密码_确认密码
    reset_assure_password_xpath = "//*[@for='confirmPassword']/following-sibling::div/div/input"
    # 编辑/重置密码_确认
    edit_submit_xpath = "//*[@class='el-dialog__footer dialog-footer__custom']/button[1]"
    # 按钮_第一行_更多-删除
    more_del_xpath = "//ul[contains(@x-placement,'bottom-')]//li[contains(text(),'删除')]"
    # 内容_选中的组
    content_selection_xpath = "//*[@class='sk-composite-tree__list']"
    # 记录条数统计
    count_record_xpath = "//*[@class='el-pagination__total']"
    # 按钮_全局删除
    del_lot_xpath = "//*[@class='sk-toolbar']/div/button"
    # 按钮_添加用户组
    add_user_group_xpath = "//button[@class='el-button add-group-btn el-button--primary el-button--mini is-round is-noLabel']"
    # 添加用户组_输入框_名称
    add_user_group_name_xpath = "//*[@for='userGroupBaseInfo.name']/following-sibling::div/div/input"
    # 添加用户(组)_按钮_确认
    add_user_group_submit_xpath = "//*[@class='dialog-footer']/button[1]"
    # 按钮_新建用户
    create_user_xpath = "//*[@class='sk-toolbar']/div[1]/button[1]"
    # 新建用户_用户名
    create_user_name_xpath = "//*[@for='userBaseInfo.userName']/following-sibling::div/div/input"
    # 新建用户_姓名
    create_real_name_xpath = "//*[@for='userBaseInfo.realName']/following-sibling::div/div/input"
    # 按钮_用户字段筛选按钮
    user_filter_xpath = "//*[@class='fl']/div[3]"
    # 用户字段筛选_用户组
    user_filter_group_xpath = "//*[@class='el-dropdown-menu el-popper el-dropdown-menu--column']/li[4]"
    # 搜索框_用户
    user_search_xpath = "//*[@class='fl']/div/input"
    # 终端管理标签
    terminal_manage_xpath = u"//*[@class='el-menu']//*[text()='终端管理']"
    # 密码修改标签
    modify_password_xpath = u"//*[@class='el-menu']//*[text()='密码修改']"
    # 瘦终端（VDI）标签
    terminal_vdi_xpath = u"//*[@class='el-menu']//*[text()='瘦终端（VDI）']"
    # 终端搜索框
    terminal_search_xpath = "//*[@class='search_input1']"
    # 全选CheckBox
    terminal_all_select_xpath = "//*[@id='content_table_selectTrueOrFalse']"
    # 按钮_变更分组
    change_group_xpath = "//*[@id='btn_change_group']"
    # 设置分组页面
    page_setting_group_xpath = "//*[@class='layui-layer layui-layer-iframe']"
    # 终端管理记录条数
    terminal_total_count_xpath = "//*[@id='total_count']"
    # 选择终端_设置分组
    choose_terminal_xpath = "//*[@id='terminalGroup']"
    # 按钮_确定_设置分组
    submit_terminal_xpath = "//*[@id='btns_ok']"
    # 密码修改_原密码
    old_password_xpath = u"//*[contains(text(),'原密码：')]/parent::div//input"
    # 密码修改_新密码
    new_password_xpath = u"//*[contains(text(),'新密码：')]/parent::div//input"
    # 密码修改_确认密码
    confirm_password_xpath = u"//*[contains(text(),'确认密码：')]/parent::div//input"
    # 密码修改_确定按钮
    mew_pwd_submit_xpath = u"//span[contains(text(),'确认')]"
    # 密码修改_修改成功_确定按钮
    info_pwd_success_xpath = "//*[@class='el-button el-button--default el-button--mini is-round el-button--primary ']"
    # 按钮_第一行用户_更多
    usr_more_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//span[contains(text(),'更多')]"
    # 用户_用户组下拉框
    usr_gp_select_xpath = "//*[@for='userBaseInfo.userGroup']/following-sibling::div/span"
    # 用户_编辑
    usr_edit_xpath = u"//li[contains(text(),'编辑')]"
    # 按钮_二次确认提交
    confirm_submit_xpath = "//*[@class='el-message-box']/div[3]/button[1]"
    # 按钮_用户组_VDI云桌面启用/关闭
    idv_func_xpath = "//*[@id='scrollpane-idvPolicy']//*[@class='el-switch__core']"
    # 下拉框_用户组_绑定镜像
    select_base = u"//*[@placeholder='请选择1个镜像']"
    # 按钮_用户-更多（全局）
    usr_overall_more = "//*[@class='sk-more-button filter-item']"
    # 下拉框_消息发送-发送对象
    message_obj_xpath = "//*[@for='userNames']/following-sibling::div/div/input"
    # 输入框_消息发送-标题
    message_title_xpath = "//*[@for='title']/following-sibling::div/div/input"
    # 输入框_消息发送-内容
    message_content_xpath = "//*[@for='content']/following-sibling::div/div/textarea"
    # 按钮_发送对象-确定
    message_obj_submit_xpath = "//*[@class='el-dialog__body']//*[@role='tree']/ancestor::div[4]" \
                               "/following-sibling::div/div/button[1]"
    # 下拉框_用户-更多（全局）-消息记录
    message_log_xpath = "//*[@x-placement='bottom-start']/div[2]"
    # 搜索框_用户-更多（全局）-消息列表
    message_search_xpath = "//*[@class='sk-table']//*[@class='fl']/div/input"
    # 搜索按钮_用户-更多（全局）-消息列表
    message_search_btn_xpath = "//*[@class='sk-table']//*[@class='fl']/div/span/span/i"
    # 云桌面管理标签
    desk_manage_xpath = u"//*[@role='menubar']//*[text()='云桌面管理']"
    # 按钮_云桌面管理-更多
    desk_more_xpath = "//tbody/tr[1]/td[16]/div/div"
    # 搜索框_云桌面管理
    desk_search_xpath = "//*[@class='fl']/div[1]/input"

    # 跳转到管理员账号设置页面
    def go_admin_setting(self):
        self.click_elem(self.advanced_config_xpath)  # 点击高级配置
        self.click_elem(self.system_setting_xpath)  # 点击系统设置
        time.sleep(0.5)
        self.scroll_into_view(self.admin_setting_xpath)  # 点击管理员账号设置
        time.sleep(1)

    # 验证用户登录是否正确
    def welcome_user_logo(self, user):
        assert self.find_elem(self.welcome_user_xpath).text.__contains__(user)

    # 跳转到用户管理页面
    def go_user_management(self):
        time.sleep(1)

        self.click_elem(self.user_manage_xpath)

    # 跳转到瘦终端（VDI）页面
    def go_vdi(self):
        self.find_elem(self.terminal_manage_xpath).click()
        self.find_elem(self.terminal_vdi_xpath).click()

    # 跳转到密码修改页面修改密码 //p[@class='el-message__content']
    def go_modify_password(self, old_pwd, new_pwd, confirm_pwd):
        self.find_elem(self.advanced_config_xpath).click()
        self.find_elem(self.system_setting_xpath).click()
        self.find_elem(self.modify_password_xpath).click()
        time.sleep(1)
        self.find_elem(self.old_password_xpath).send_keys(old_pwd)
        self.find_elem(self.new_password_xpath).send_keys(new_pwd)
        self.find_elem(self.confirm_password_xpath).send_keys(confirm_pwd)
        self.find_elem(self.mew_pwd_submit_xpath).click()
        self.find_elem(self.info_pwd_success_xpath).click()

    # 打开新建账号页面
    def create_new_account(self):
        time.sleep(2)
        self.find_elem(self.create_new_xpath).click()  # 点击新建
        self.find_elem(self.create_account_xpath).click()  # 点击新建账号

    # 新建账号_输入必填项
    def input_required_data(self, admin_name, name, password, assure_password):
        self.find_elem(self.admin_name_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.admin_name_xpath).send_keys(admin_name)
        self.find_elem(self.name_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.name_xpath).send_keys(name)
        self.find_elem(self.password_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.password_xpath).send_keys(password)
        self.find_elem(self.assure_password_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.assure_password_xpath).send_keys(assure_password)
        self.find_elem(self.submit_xpath).click()

    # 新建账号_添加用户组
    def add_user_group_account(self, keyword_search_user):
        self.find_elem(self.user_group_xpath).click()  # 点击用户组“+”按钮
        self.search_and_choose_group(keyword_search_user)  # 搜索并勾选用户组
        self.find_elem(self.add_group_submit_xpath).click()  # 确认

    # 新建账号_添加第10级用户组
    def add_ten_user_group(self, keyword_search_ten_user):
        self.find_elem(self.user_group_xpath).click()
        self.find_elem(self.keyword_search_xpath).send_keys(keyword_search_ten_user)
        for i in range(2, 11):  # 分别点击9个子级名
            target = str(i) + '级'
            target_xpath = "//*[text()='" + target + "']"
            self.find_elem(target_xpath).click()
        self.find_elem("//*[text()='10级']/parent::div//*[@class='el-checkbox__input']").click()  # 勾选第10个子级
        self.find_elem(self.add_group_submit_xpath).click()

    # 新建账号_添加胖终端组
    def add_idv_group_account(self, keyword_search_idv):
        self.find_elem(self.idv_group_xpath).click()  # 点击胖终端组“+”按钮
        self.search_and_choose_group(keyword_search_idv)  # 搜索并勾选idv组
        self.find_elem(self.add_group_submit_xpath).click()  # 确认

    # 新建账号_添加瘦终端组
    def add_vdi_group_account(self, keyword_search_vdi):
        self.click_elem(self.vdi_group_xpath)  # 点击瘦终端组“+”按钮
        self.search_and_choose_group(keyword_search_vdi)  # 搜索并勾选vdi组
        self.find_elem(self.add_group_submit_xpath).click()  # 确认

    # 在用户管理展开10级用户组节点
    def open_ten_group(self):
        self.find_elem("//*[@class='el-col el-col-24']//*[contains(text(),'vdi2')]/parent::div/preceding-sibling::"
                       "span").clisk()

    # 账号不选择资源提交时的提示框验证
    def message_no_resource(self):
        self.find_elem(self.message_no_resource_xpath + "/button[2]").click()  # 点击取消
        self.find_elem("//*[@class='el-dialog__title']")  # 是否能找到“新建”窗体
        self.find_elem(self.submit_xpath).click()  # 重新点击确认按钮提交
        self.find_elem(self.message_no_resource_xpath + "/button[1]").click()  # 点击确定

    # 勾选用户组
    def choose_group(self, keyword):

        target = "//*[text()='" + keyword + "']/preceding-sibling::label/span"
        self.find_elem(target).click()

    # 按管理员名称搜索
    def search_by_admin_name(self, admin_name):
        self.find_elem(self.search_admin_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)  # 清空搜索框
        self.find_elem(self.search_admin_xpath).send_keys(admin_name)  # 搜索管理员姓名
        self.find_elem(self.search_admin_xpath).send_keys(Keys.ENTER)  # 回车

    # 修改用户组勾选

    def edit_user_group(self, g_user, choose_group):
        self.find_elem(self.edit_user_group_xpath.format(g_user)).click()  # 点击第一行用户组的“+”按钮
        self.choose_group(u'总览')  # 全选用户组再取消全选
        self.choose_group(u'总览')
        self.check_num_user_group(u'1')  # 验证选中的用户组个数是否为1
        self.search_and_choose_group(choose_group)  # 搜索并勾选用户组
        self.find_elem(self.add_group_submit_xpath).click()  # 确认

    # 修改idv终端组勾选
    def edit_idv_group(self, g_user, choose_group):
        time.sleep(0.5)
        self.click_elem(self.edit_idv_group_xpath.format(g_user))  # 点击第一行用户组的“+”按钮
        content = self.find_elem(self.content_selection_xpath).text  # 获取右侧显示的所选终端组
        group = content.split()
        for g in group:  # 按照终端组名搜索组并去掉勾选
            if (g == u'未分组') or (g == u'未绑定用户终端组'):
                pass
            else:
                self.search_and_choose_group(g)
        self.check_num_user_group(u'2')  # 验证选中的终端组个数是否为2
        self.search_and_choose_group(choose_group)  # 搜索并勾选终端组
        self.find_elem(self.add_group_submit_xpath).click()  # 确认

    # 修改vdi终端组勾选
    def edit_vdi_group(self, g_user, choose_group):
        time.sleep(0.5)
        self.click_elem(self.edit_vdi_group_xpath.format(g_user))
        content = self.find_elem(self.content_selection_xpath).text
        group = content.split()
        for g in group:
            if g == u'未分组':
                pass
            else:
                self.search_and_choose_group(choose_group)
        self.check_num_user_group(u'1')
        self.search_and_choose_group(choose_group)
        self.find_elem(self.add_group_submit_xpath).click()

    # 用户/idv终端/vdi终端组中搜索并勾选
    def search_and_choose_group(self, choose_group):
        self.find_elem(self.keyword_search_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)  # 防止多次搜索
        self.find_elem(self.keyword_search_xpath).send_keys(choose_group)  # 搜索
        self.choose_group(choose_group)  # 勾选

    # 编辑管理员
    def edit_admin(self, u_name, edit_admin_name, edit_name):
        time.sleep(0.5)
        self.find_elem(self.usr_more_xpath.format(u_name)).click()  # 点击第一行更多
        self.find_elem(self.more_edit_xpath).click()  # 点击编辑
        self.find_elem(self.edit_admin_name_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.edit_admin_name_xpath).send_keys(edit_admin_name)  # 输入管理员名称
        self.find_elem(self.edit_name_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.edit_name_xpath).send_keys(edit_name)  # 输入姓名
        self.find_elem(self.edit_submit_xpath).click()  # 确认

    # 重置密码
    def reset_password(self, u_name, reset_password, reset_assure_password):
        time.sleep(0.5)
        self.find_elem(self.usr_more_xpath.format(u_name)).click()
        self.find_elem(self.more_reset_password_xpath).click()
        self.find_elem(self.reset_password_xpath).send_keys(reset_password)
        self.find_elem(self.reset_assure_password_xpath).send_keys(reset_assure_password)
        self.find_elem(self.edit_submit_xpath).click()
        assert self.find_elem(self.message_right_xpath).text.__contains__(u'重置密码成功')  # 验证是否有提示
        time.sleep(1)

    # 删除单个管理员及验证
    def del_admin_check(self, u_name):
        time.sleep(0.5)
        self.find_elem(self.usr_more_xpath.format(u_name)).click()
        self.find_elem(self.more_del_xpath).click()
        self.find_elem(self.confirm_submit_xpath).click()  # 点击确认
        self.find_elem(self.edit_admin_success_xpath).text.__contains__(u'删除成功')
        assert self.count_record() == 0  # 验证是否0条记录

    # 批量删除管理员及验证
    def del_lot_admin_check(self):
        count_before = self.count_record()
        self.find_elem("//*[@class='has-gutter']/tr/th[1]//*[@class='el-checkbox__inner']").click()  # 全选CheckBox
        self.find_elem(self.del_lot_xpath).click()
        self.find_elem(self.confirm_submit_xpath).click()  # 点击确认
        self.find_elem(self.message_right_xpath).text.__contains__(u'删除成功')
        if count_before <= 10:  # 少于10条记录即等于全部删除
            assert self.count_record() == 0
        else:
            count = count_before - 10  # 大于10条记录即剩余条数等于总条数-10条
            assert self.count_record() == count
        time.sleep(5)

    # 模糊查询管理员
    def fuzzy_query_admin_check(self, fuzzy):
        self.search_by_admin_name(fuzzy)  # 输入模糊查询条件
        count = self.count_record()
        for i in range(1, count + 1):  # 根据记录条数组建xpath路径
            record_name_xpath = "//tbody/tr[" + str(i) + "]/td[2]/div/span"
            assert self.find_elem(record_name_xpath).text.__contains__(fuzzy)  # 验证搜索出的管理员是否包含关键字

    # 返回记录条数
    def count_record(self):
        content = self.find_elem(self.count_record_xpath).text
        num = content.split()
        return int(num[1])

    # 注销
    # 编辑页面时的成功提示
    infor_xpath = '//*[@class="el-notification__closeBtn el-icon-close"]'

    def logout(self):
        if self.elem_is_exist2(self.infor_xpath, wait_times=3) is not None:
            self.click_elem(self.infor_xpath)
        time.sleep(1)
        self.back_current_page()
        self.click_elem(self.logout_xpath)
        self.find_elem("//*[@class='sk-login__logo']")

    # 添加用户组
    def add_user_group_check(self, group_name, base=0):
        self.find_elem(self.add_user_group_xpath).click()  # 点击“+”按钮
        self.find_elem(self.add_user_group_name_xpath).send_keys(group_name)  # 名称
        if base:
            self.idv_func()
        else:  # base=0：跳过，不绑定镜像
            pass
        self.find_elem(self.add_user_group_submit_xpath).click()  # 确认
        assert self.find_elem(self.message_right_xpath).text.__contains__(u'用户组创建成功')  # 验证提示
        time.sleep(1)

    # 开启vdi特性并选择镜像
    def idv_func(self):
        self.find_elem(self.idv_func_xpath).click()
        self.find_elem(self.select_base).click()
        self.find_elem("//li[text()='可绑定镜像']/following-sibling::li").click()  # 随便选择一个可绑定的镜像

    # 编辑用户组镜像
    def edit_usr_gp_base(self, group_name):
        edit_xpath = "//div[@class='custom-tree-node']//div[contains(.,'" + group_name + "')]" \
                                                                                         "/..//i[@class='el-icon-edit']/.."
        stay_xpath = "//*[@class='user-group']/div[2]//*[contains(text(),'" + group_name + "')]"
        self.chainstay(stay_xpath)
        self.find_elem(edit_xpath).click()
        self.idv_func()
        self.find_elem(self.add_user_group_submit_xpath).click()
        self.find_elem(self.confirm_submit_xpath).click()
        self.find_elem(self.message_right_xpath).text.__contains__(u'修改成功')

    # 在用户组中点击一个用户组
    # 用户组编辑也页面
    edit_group_xpath = u"//*[contains(text(),'编辑用户组')]"
    close_group_edit_xpath = u"//span[text()='取消']"

    def click_user_group(self, user_group, wait_times=8):
        try:
            self.scroll_into_view(u"//div[contains(text(),'{}')]".format(user_group),
                                  wait_times=wait_times)
            if self.elem_is_exist2(self.edit_group_xpath) is not None:
                self.find_elem(self.edit_group_xpath).click()
            flag = u'用户组存在'
            time.sleep(1)
        except:
            flag = u'用户组不存在'
        return flag

    # 在用户组中点击一个用户组的展开按钮
    def click_group_unfold(self, user_group):
        self.scroll_into_view(u"//div[contains(text(),'{}')]/ancestor::div[@class='el-tree-node__content']/span"
                              .format(user_group))
        assert self.click_user_group(user_group) == u'用户组存在'

    # 循环创建用户组并验证层级关系
    def create_user_group_round_check(self, template, n, base=0):
        group_name = template + str(2)
        self.add_user_group_check(group_name, base)  # 创建用户组名称为“模板+2”
        self.click_user_group(group_name)
        for i in range(3, n + 1):  # 循环创建n个子级
            batch_name = template + str(i)
            self.add_user_group_check(batch_name, base)
            upper_group_name = template + str(i - 1)
            crazy_xpath = "//*[@class='user-group']/div[2]//*[contains(text(),'" + upper_group_name + "')]" \
                                                                                                      "/ancestor::div/parent::div//*[contains(text(),'" + batch_name + "')]"
            if self.elem_is_exist2(crazy_xpath) is not None:
                flag = u'{0}层级的上一级用户是{1}层级用户组显示正常'.format(i, i - 1)
            # 验证在上一级中是否能找到新建的用户组
            else:
                flag = u'{0}层级的用户组显示不正常'.format(i)
            time.sleep(1)
            self.click_user_group(batch_name)
            assert flag.__contains__(u'用户组显示正常')

            # 循环展开n级用户组

    def unfold_user_group(self, n):
        for i in range(2, n):  # 从2级分组开始点击展开
            target = str(i) + u'级'
            self.click_group_unfold(target)
        user_group = str(n) + u'级'
        self.click_user_group(user_group)  # 点击n级标签用于创建子级或查看其下用户
        return user_group  # 返回组名

    # 搜索用户并验证用户名是否相符
    def search_user(self, user_name):
        self.find_elem(self.user_search_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.user_search_xpath).send_keys(user_name)
        self.find_elem(self.user_search_xpath).send_keys(Keys.ENTER)
        num = self.count_record()  # 记录条数
        for i in range(1, num + 1):
            assert self.get_usr_name(i) == user_name  # 第i条记录的用户名

    # 新建并验证用户
    # 开启vdi用户属性
    vdi_attribute_button_xpath = u"//*[text()='VDI云桌面：']/ancestor::div[@class='el-form-item']" \
                                 u"//span[@class='el-switch__core']"
    # vdi用户桌面类型选择
    vdi_desk_type_xpath = u'//*[contains(text(),"VDI云桌面：")]/ancestor::div[@class="form-item-wrap"]' \
                          u'//*[contains(text(),"桌面类型：")]/parent::div//input'
    # 桌面类型选择
    desk_type_chose_xpath = u'//*[@x-placement="bottom-start"]//*[text()="{}"]'
    # idv用户组绑定镜象
    vdi_group_mirror_bind_xpath = u'//*[contains(text(),"VDI云桌面：")]/ancestor::div[@class="form-item-wrap"]' \
                                  u'//*[contains(text(),"绑定镜像：")]/parent::div//input'
    # vdi用户镜像修改'//*[@x-placement="bottom-start"]//li[@class="el-select-dropdown__item"]/span'
    change_mirror_xpath = "//span[contains(text(),'{}')]/parent::li"
    # 修改用户组点击确认
    confirm_group_change_xpath = '//*[@class="el-button el-button--primary el-button--mini is-round"]'

    def create_user_check(self, user_name, real_name, mirror_name=u'test_vdi_restore_win7_rcd'):
        num_before = self.count_record()  # 记录条数
        self.find_elem(self.create_user_xpath).click()  # 点击新建用户按钮
        self.find_elem(self.create_user_name_xpath).send_keys(user_name)  # 输入用户名
        self.find_elem(self.create_real_name_xpath).send_keys(real_name)  # 输入姓名
        self.scroll_into_view(self.vdi_attribute_button_xpath)
        self.click_elem(self.vdi_desk_type_xpath)
        self.click_elem(self.desk_type_chose_xpath.format(u'还原'))
        self.click_elem(self.vdi_group_mirror_bind_xpath)
        time.sleep(1)
        self.scroll_into_view(self.change_mirror_xpath.format(mirror_name))
        self.click_elem(self.vdi_group_mirror_bind_xpath)
        self.click_elem(self.confirm_group_change_xpath)
        self.find_elem(self.edit_admin_success_xpath).text.__contains__(u'用户创建成功')  # 验证提示
        num = self.count_record()
        assert num == num_before + 1  # 验证记录条数

    # 终端管理点击某个分组
    def terminal_group_click(self, group_name):
        time.sleep(2)
        self.get_ciframe("frameContent")
        group_name_xpath = "//*[@id='groupContent']//*[text()='" + group_name + "']"
        self.find_elem(group_name_xpath).click()
        self.back_current_page()

    # 搜索终端，返回记录条数，再变更终端组
    def search_terminal(self, terminal_name):
        time.sleep(2)  # 等待i_frame页面出现
        self.get_ciframe("frameContent")  # 切换到终端管理i_frame
        self.get_ciframe("content")
        self.find_elem(self.terminal_search_xpath).send_keys(terminal_name)
        self.find_elem(self.terminal_search_xpath).send_keys(Keys.ENTER)
        count = self.find_elem(self.terminal_total_count_xpath).text
        return int(count)

    # 变更终端分组
    def change_terminal_group(self, ter_name):
        self.find_elem(self.terminal_all_select_xpath).click()
        self.find_elem(self.change_group_xpath).click()
        param = self.get_iframe_last_id(self.page_setting_group_xpath)  # get“设置分组”页面i_frame随机数
        setting_group_frame = "layui-layer-iframe" + param  # 拼接i_frame id
        self.get_ciframe(setting_group_frame)
        self.find_elem(self.choose_terminal_xpath).click()
        terminal_xpath = "//*[@id='terminalGroup']//*[text()='" + ter_name + "']"
        self.find_elem(terminal_xpath).click()
        self.find_elem(self.submit_terminal_xpath).click()

    # get用户ip
    def get_usr_ip(self, n):
        return self.find_elem(u"//tbody/tr[{}]/td[6]//div".format(n)).text

    # get用户名
    def get_usr_name(self, n):
        return self.find_elem(u"//tbody/tr[{}]/td[2]//div".format(n)).text

    # 对用户组发送消息，返回组下用户名
    # 发送信息xpath
    send_message_xpath = u"//ul[contains(@x-placement,'bottom-')]//li[contains(text(),'发送消息')]"

    def send_message_gp(self, gp, title, content):
        self.find_elem(self.usr_overall_more).click()
        self.find_elem(self.send_message_xpath).click()  # 点击发送消息（xpath与编辑用户相同）
        self.find_elem(self.message_obj_xpath).click()
        crazy_xpath = "//*[@class='el-dialog__body']//*[@role='tree']//*[contains(text(),'" + gp + "')]" \
                                                                                                   "/parent::div/preceding-sibling::label/span"
        self.scroll_into_view(crazy_xpath)
        self.find_elem(self.message_obj_submit_xpath).click()
        self.find_elem(self.message_title_xpath).send_keys(title)
        self.find_elem(self.message_content_xpath).send_keys(content)
        self.find_elem(self.submit_xpath).click()
        assert self.find_elem(self.message_right_xpath).text.__contains__(u'消息发送成功')

    #  返回记录当前组下的用户名
    def get_usr_list(self):
        num = self.count_record()  # 获取记录条数
        if num:
            usr_list = []
            for i in range(1, num + 1):
                usr_list.append(self.get_usr_name(i))
        else:  # 如果记录数等于0抛异常
            raise Exception
        return usr_list

    # 打开消息记录列表
    def open_message_log(self):
        self.find_elem(self.usr_overall_more).click()
        self.find_elem(self.message_log_xpath).click()

    # 查看并验证是否消息记录的搜索结果为0条
    def view_message_check(self, message):
        self.find_elem(self.message_search_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.message_search_xpath).send_keys(message)
        self.find_elem(self.message_search_btn_xpath).click()
        count_xpath = "//*[@class='sk-table']//*[@class='fr']/div/span[1]"
        if message == u'普通管理员信息':
            assert self.find_elem(count_xpath).text != u'共 0 条'
        else:
            assert self.find_elem(count_xpath).text == u'共 0 条'

    # 跳转到云桌面管理页面
    def go_desk_manage(self):
        self.find_elem(self.desk_manage_xpath).click()
        time.sleep(1)

    # 对用户发起远程协助
    remote_xpath = "//ul[@x-placement='bottom-start']//li[contains(text(),'远程协助') and @class='el-dropdown-menu__item']"

    def remote(self, usr):
        desk_ip = self.get_desk_ip(usr)
        desk_status_xpath = "//tbody/tr[1]/td[5]/div/span/span"
        if self.count_record():
            if self.get_elem_text(desk_status_xpath) == u'运行':  # 判断桌面是否为运行状态
                self.find_elem(self.desk_more_xpath).click()  # 点击更多
                self.find_elem(self.remote_xpath).click()  # 点击远程协助
            else:
                raise Exception
        else:
            raise Exception
        return desk_ip

    # 搜索用户并返回云桌面ip
    def get_desk_ip(self, usr):
        self.find_elem(self.desk_search_xpath).send_keys(usr)
        self.find_elem(self.desk_search_xpath).send_keys(Keys.ENTER)
        desk_ip_xpath = "//tbody/tr[1]/td[8]/div/span"
        return self.find_elem(desk_ip_xpath).text

    # 比对搜索终端结果
    def check_search_terminal(self, ter_name, count):
        for i in range(0, count):
            num = i + 1
            assert self.get_usr_ip(num).__contains__(ter_name)

    # 比对新建账号数据
    def check_account(self, admin_name, status_normal, type_admin, keyword_search_user='',
                      keyword_search_idv='', keyword_search_vdi='', user=0, idv=0, vdi=0, action=0):
        if action == 0:  # 0：新建
            assert self.find_elem(self.message_right_xpath).text.__contains__(u'添加管理员成功')
        elif action == 1:  # 1：编辑用户组
            assert self.find_elem(self.message_right_xpath).text.__contains__(u'更新用户组权限成功')
        elif action == 2:  # 2：编辑idv组
            assert self.find_elem(self.message_right_xpath).text.__contains__(u'更新胖终端组权限成功')
        elif action == 3:  # 3：编辑vdi组
            assert self.find_elem(self.message_right_xpath).text.__contains__(u'更新瘦终端组权限成功')
        elif action == 4:
            assert self.find_elem(self.edit_admin_success_xpath).text.__contains__(u'修改成功')
        self.search_by_admin_name(admin_name)
        assert self.find_elem(self.result_admin_xpath).text.strip() == admin_name
        assert self.find_elem(self.result_status_xpath).text.strip() == status_normal
        assert self.find_elem(self.result_type_xpath).text.strip() == type_admin
        if user:
            if user == -1:  # -1：跳过不比对
                pass
            else:  # 1：比对，有用户组
                assert self.find_elem(self.result_user_xpath).text.strip() == u'未分组， ' + keyword_search_user

        else:
            assert self.find_elem(self.result_user_xpath).text == ''  # 0：比对，没有用户组
        if idv:
            if idv == -1:
                pass
            else:
                assert self.find_elem(self.result_idv_xpath).text.strip() == keyword_search_idv + u'， 未分组， 未绑定用户终端组'
        else:
            assert self.find_elem(self.result_idv_xpath).text == ''
        if vdi:
            if vdi == -1:
                pass
            else:
                assert self.find_elem(self.result_vdi_xpath).text.strip() == keyword_search_vdi + u'， 未分组'
        else:
            assert self.find_elem(self.result_vdi_xpath).text == ''

    # get管理员绑定的用户组列表
    def get_adm_usr_gp(self):
        gp_str = self.find_elem(self.result_user_xpath).text.strip()
        gp_list = gp_str.split(u'， ')
        return gp_list

    # get用户管理的用户组列表 //*[@class='custom-tree-node']/div
    def get_usr_manage_gp(self):
        self.click_all_group_unfold(self.group_can_fold_xpath)
        gp_str = self.find_elem("//*[@role='group']").text.strip()
        gp_list = gp_str.split()
        return gp_list

    # get用户的用户组列表
    def get_usr_gp(self):
        gp_str = self.find_elem("//*[@class='el-tree user-group-tree']//*[contains(text(),'总览')]"
                                "/parent::div/parent::div/following-sibling::div").text.strip()
        gp_list = gp_str.split()
        return gp_list

    # 修改用户所属分组（随机）
    def edit_usr_check(self, user):
        self.whether_usr_gp_open()
        selected_gp = self.find_elem("//tbody/tr[1]/td[4]").text
        self.find_elem(self.usr_more_xpath.format(user)).click()
        self.find_elem(self.usr_edit_xpath).click()
        self.find_elem(self.usr_gp_select_xpath).click()
        usr_gp_list = self.get_usr_gp()  # 获取可选的分组列表
        back_list = self.get_usr_gp()
        crazy_xpath = "//*[@class='el-tree user-group-tree']//*[contains(text(),'" + selected_gp + "')]" \
                                                                                                   "/parent::div/preceding-sibling::label/span"
        self.find_elem(crazy_xpath).click()  # 取消当前所选的分组
        usr_gp_list.remove(selected_gp)  # 将当前所选分组从列表中剔除
        crazy_xpath_again = "//*[@class='el-tree user-group-tree']//*[contains(text(),'" + usr_gp_list[0] + "')]" \
                                                                                                            "/parent::div/preceding-sibling::label/span"
        self.find_elem(crazy_xpath_again).click()  # 勾选列表第一个分组
        self.find_elem(self.usr_gp_select_xpath).click()  # 收起分组下拉框
        self.find_elem(self.add_user_group_submit_xpath).click()
        self.find_elem(self.info_pwd_success_xpath).click()
        self.find_elem(self.message_right_xpath).text.__contains__(u'用户信息修改成功')
        assert self.find_elem("//tbody/tr[1]/td[4]").text == usr_gp_list[0]
        return back_list

    # 比对_管理员名称_错误提示
    def check_warn_admin_name(self):
        assert self.find_elem(self.create_invalid_info_xpath).text.__contains__(u'数据不合法')
        assert self.find_elem(self.warn_admin_name_xpath).text.__contains__(u'只能包含英文,数字,中文')

    # 比对_密码_错误提示
    def check_warn_password(self):
        assert self.find_elem(self.create_invalid_info_xpath).text.__contains__(u'数据不合法')
        assert self.find_elem(self.warn_password_xpath).text.__contains__(u'密码只允许数字和字母组成')

    # 比对_确认密码_错误提示
    def check_warn_assure_password(self):
        assert self.find_elem(self.create_invalid_info_xpath).text.__contains__(u'数据不合法')
        assert self.find_elem(self.warn_assure_password_xpath).text.__contains__(u'密码与确认密码不一致')

    # 检查拥有第10级用户组的管理员的用户管理权限
    def check_ten_user_group(self):
        for i in range(2, 10):
            target = str(i) + u'级'
            self.click_group_unfold(target)  # 点击用户组展开按钮
            self.click_user_group(target)  # 点击用户组（用于显示组下用户）
            assert self.count_record() == 0  # 权限约束不可见父级用户
        self.click_user_group(u'10级')
        assert self.count_record() != 0  # 可见10级分组用户

    # 验证组个数
    def check_num_user_group(self, count):
        self.find_elem("//*[@class='sk-composite-tree__title']").text.__eq__(count + u'个用户组')

    # 验证该组下所有用户的用户组属性
    def chk_usr_gp_attr(self, group_name, user_name):
        group_attribute_xpath = u"//*[contains(text(),'{}')]/ancestor::tr//td[4]//span".format(user_name)
        assert self.find_elem(group_attribute_xpath).text == group_name

    # 用户组是否展示，未展示则勾选
    def whether_usr_gp_open(self):
        self.find_elem(self.user_filter_xpath).click()
        crazy_xpath = "//*[@class='el-dropdown-menu el-popper el-dropdown-menu--column']/li[4]/i"
        attr = self.find_elem(crazy_xpath).get_attribute('class')
        if attr == "icon-empty":
            self.find_elem(self.user_filter_group_xpath).click()
        else:
            self.find_elem(self.user_filter_xpath).click()

    """"===========4.0版本chengll新增方法=============="""
    # 选择普通管理员账号单选框
    chose_manger_xpath = u"//*[contains(text(),'{}')]/ancestor::tr/td//span[@class='el-checkbox__inner']"

    def delete_manger_user(self, name):
        """删除管理员账号"""
        self.driver.refresh()
        self.search_by_admin_name(name)
        time.sleep(0.5)
        self.click_elem(self.chose_manger_xpath.format(name), wait_times=5)
        self.click_elem(self.del_lot_xpath)
        self.click_elem(self.confirm_submit_xpath)  # 点击确认
        time.sleep(1)

    def create_new_mannger(self, admin_name, name, password, assure_password, keyword_search_user=None,
                           keyword_search_idv=None, keyword_search_vdi=None):
        """ #新建管理员账号,输入用户名密码"""

        self.create_new_account()
        if keyword_search_user is not None:
            self.add_user_group_account(keyword_search_user)
        if keyword_search_idv is not None:
            self.add_idv_group_account(keyword_search_idv)
        if keyword_search_vdi is not None:
            self.add_vdi_group_account(keyword_search_vdi)
        self.input_required_data(admin_name, name, password, assure_password)
        if keyword_search_user is None and keyword_search_vdi is None and keyword_search_idv is None:
            self.find_elem(self.info_pwd_success_xpath).click()

    # 展开用户
    group_can_fold_xpath = "//span[@class='el-tree-node__expand-icon el-icon-caret-right']"

    def click_all_group_unfold(self, locator):
        """点击展开按钮"""
        if self.elem_is_exist2(locator) is not None:
            elems = self.find_elems(locator, wait_times=5)
            for item in elems:
                item.click()
            self.click_all_group_unfold(locator)
        else:
            pass

    def search_use_info(self, user_name):
        """搜索管理员信息"""
        self.find_elem(self.user_search_xpath).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(self.user_search_xpath).send_keys(user_name)
        self.find_elem(self.user_search_xpath).send_keys(Keys.ENTER)
        time.sleep(0.5)

    # 给管理员新增用户组时选择用户组前的单选框
    chose_group_xpath = u"//*[text()='{}']/preceding-sibling::label/span"

    def chose_user_group(self, g_name, choose_group):
        self.find_elem(self.edit_user_group_xpath.format(g_name)).click()  # 点击第一行用户组的“+”按钮
        self.choose_group(u'总览')  # 全选用户组再取消全选
        self.choose_group(u'总览')
        for name in choose_group:
            self.scroll_into_view(self.chose_group_xpath.format(name))
        self.find_elem(self.add_group_submit_xpath).click()

    #     选择上级用户xpaht输入框
    input_up_group_xpaht = '//*[@class="el-input el-popover__reference"]//input[@class="el-input__inner"]'
    #     选择上级用户xpath
    up_group_xpaht = '//div[contains(text(),"{}")]/ancestor::div[@class="el-tree-node__content"]//span[@class="el-checkbox__inner"]'

    def creat_new_group(self, group_name, up_group, base=0):
        time.sleep(0.5)
        self.find_elem(self.add_user_group_xpath).click()  # 点击“+”按钮
        self.find_elem(self.add_user_group_name_xpath).send_keys(group_name)  # 名称
        self.find_elem(self.input_up_group_xpaht).click()
        self.scroll_into_view(self.up_group_xpaht.format(up_group))
        self.find_elem(self.input_up_group_xpaht).click()
        if base:
            self.idv_func()
        else:  # base=0：跳过，不绑定镜像
            pass
        self.click_elem(self.add_user_group_submit_xpath)  # 确认
        assert self.find_elem(self.message_right_xpath).text.__contains__(u'用户组创建成功')  # 验证提示
    # 用户管理拖拽框位置
    size_info_xpath = "//*[@class='sk-split-pane-resizer__bar is-vertical ']"
    def drage_user_info_size(self):
        """将用户管理信息位置变宽"""
        self.drag_element(self.size_info_xpath)


if __name__ == "__main__":
    pass
