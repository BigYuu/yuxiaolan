#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@software: PyCharm
@time: 2019/03/07 14:24
"""
import time
import re
import uiautomation as automation
from selenium.webdriver import ActionChains
from Common.Basicfun import BasicFun
from TestData.basicdata import *
from Common.terminal_action import *
from TestData.patchUpgradedata import *
from WebPages.LoginPage import Login
from selenium import webdriver
import logging
from LoginPage import *
import time
import datetime
from Common.Basicfun import BasicFun


class patch_upgradePage(BasicFun):
    # 框架ID
    iframe_id_xpath = "//*[@id='frameContent']"
    # 高级配置
    advanced_xpath = u"//*[@class='el-submenu__title']//*[text()='高级配置']"
    # 部署与升级
    deployment_and_upgrade_xpath = u"//*[@class='el-submenu__title']//*[text()='部署与升级']"
    # 云主机升级
    cloud_host_upgrade_xpath = u"//span[text()='云主机升级']/.."
    # 补丁包升级按钮
    patch_upgrade_btn_xpath = u"//a[@class='btn' and contains(text(),'补丁包升级')]"
    # 选中OS包
    choose_OS_xpath = u"//*[text()='{}']/ancestor::tr//input"
    # 点击删除补丁包
    delete_patch_xpath = u"//ul[contains(.,'删除') and @x-placement='bottom-end']"
    # 确定
    confirm_button_xpath = u"//*[@class='panelButton']//*[@value='确定']"
    # 二次密码确认
    confirm_pwd_xpath = "//*[@class='el-button el-button--primary el-button--mini is-round']"
    # 确认按钮
    confire_btn_xpath = u"//button[contains(.,'确认')]"
    # 确认密码
    confirm_passwd_xpath = "//input[@type='password']"
    # 确认密码的确认按钮
    confire_pwd_btn_xpath = u"//div[@class='el-dialog']//button[contains(.,'确认')]"

    # 获取所有补丁包信息
    all_patch_info_xpath = u"//*[@class='sk-app__inner is-minScreen']//*[@class='el-scrollbar__wrap']"

    # 获取所有OS包信息
    all_os_info_xpath = u"//*[@id='upgradeListForm:upgradeTable']//tbody"
    # 确认删除的iframe
    confirm_iframe_xpath = "//*[@id='confirmMessageDialog']"
    # 上传OS包
    upload_OS_xpath = u"//*[@class='headerActions']//*[contains(text(),'上传OS升级包')]"
    # 刷新
    refresh_patch_xpath = u"//*[@class='headerActions']//*[@class='btn refresh']"
    # 刷新补丁包按钮
    refresh_patch_btn_xpath = u"//button[@class='el-button el-button--default el-button--mini is-round']"
    # 进入云主机升级界面
    # 上传OS升级包按钮
    upload_os_btn_xpath = u"//a[@class='btn' and contains(text(),'上传OS升级包')]"
    # 删除按钮
    delete_btn_xpath = u"//a[@class='btn' and contains(text(),'删除')]"
    # 升级按钮
    upgrade_btn_xpath = u"//td[contains(text(),'%s')]/..//a[@class='btn' and contains(text(),'升级')]"
    # 补丁包状态栏
    patch_status_xpath = "//tr[%s]//td[3]"
    # 告警
    warning_btn_xpath = u"//div[@class='el-badge sk-navitem__badge' and contains(.,'告警')]"
    # 告警信息网格
    warning_info_xpath = "//tbody"
    # 框架ID
    frame_id_xpath = u"//*[@id='frameContent']"
    # 上传补丁包按钮
    upload_patch_btn_xpath = u"//button[contains(.,'上传补丁包')]"
    # 检测到的补丁包列表
    patch_check_list_xpath = "//*[@class='el-scrollbar']//div[@class='el-scrollbar__wrap']"
    # 补丁包列表为空
    patch_list_empty_xpath = u"//span[contains(.,'未检测到补丁包，请上传')]"
    # 更多
    more_xpath = "//span[contains(.,'{}')]/ancestor::*[@class='patch-collapse-item']//*[@class='more-icon el-icon-more']"
    # 被选中的升级包的更多
    choosed_patch_more_xpath = u"//div[@class='table']//span[text()='{0}']//ancestor::div[@class='table']//i[@class='more-icon el-icon-more']"
    # 选中的补丁包
    choose_patch_xpath = u"//*[contains(text(),'{}')]/ancestor::div[@class='patch-collapse-item__wrap']"
    # 开始升级按钮
    start_update_btn_xpath = u"//*[contains(text(),'开始升级')]"

    # 被选中的补丁包按钮
    selected_patch_btn_xpath = u"//*[@class='patch-collapse-item__wrap']" \
                               u"//span[contains(.,'%s')]/../../.." \
                               u"//i[@class='select-icon sk-icon sk-icon-success is-selected']"
    # 可选中的补丁包按钮
    select_patch_btn_xpath = u"//span[contains(.,'%s')]/../../.." \
                             u"//i[@class='select-icon sk-icon sk-icon-available']"
    # 下一步按钮
    next_btn_xpath = u"//span[contains(.,'下一步')]"
    # 开始升级按钮
    begin_upgrade_xpath = u"//button[contains(.,'开始升级')]"
    # 可用服务器列表
    server_list_xpath = "//tbody//tr"
    # 提示框
    tip_xpath = "//*[@role='alert']//*[contains(text(),'%s')]"
    # 确认按钮
    upgrade_confire_btn_xpath = u"//button[contains(.,'确认')]"
    # 确认密码框
    pwd_xpath = "//input[@type='password']"
    # 补丁包升级时提示
    update_prompt_xpath = u"//*[contains(text(),'系统已进入维护模式')]"
    # 升级成功提示
    update_succ_msg = u"//*[contains(text(),'恭喜，所有主机升级完成！')]"
    # 被选中的补丁包
    selected_patch_xpath = u"//*[@role='tabpanel']//*[@class='select-icon sk-icon sk-icon-success is-selected']/../../..//span[@class='title']"
    # 不能用的补丁包
    selcted_disable_xpath = u"//*[@role='button']//*[@class='select-icon sk-icon sk-icon-disable']/../../..//span[@class='title']"
    # 云主机界面
    cloud_desk_xpath = u"//li[@role='menuitem']//*[text()='云主机']"
    # 主备存个数
    ip_num_xpath = u"//tr"
    # 点击上一步
    click_pre_xpath = u"//*[contains(text(),'上一步')]"
    # 点击定时任务
    clock_task_xpath = u"//*[contains(text(),'定时任务')]"
    # 新建定时任务
    create_clock_task_xpath = "//*[@class='sk-icon__hasLabel el-icon-plus']"
    # 新建定时任务iframe
    task_iframe_xpath = "//iframe[@id='userScheduleEditPanel']"
    # 点击任务后的选择框
    task_xpath = "//*[contains(text(),'任务')]/parent::div//*[@class='el-input el-input--suffix']//*[@class='el-input__suffix']"
    # 点击重启任务
    reboot_xpath = "//span[contains(text(),'重启云主机')]/parent::li"
    # 点击关闭云主机任务
    poweroff_xpath = "//span[contains(text(),'关闭云主机')]/parent::li"
    # 点击关闭胖终端任务
    poweroff_IDV_xpath = "//span[contains(text(),'关闭胖终端')]"
    # 点击定时类型
    clock_type = "//*[contains(text(),'定时类型')]/parent::div[@class='el-form-item']//*[@class='el-select']//*[@class='el-input__suffix']"
    # 类型
    task_type_xpath = u"//*[contains(text(),'{}')]/parent::li"
    # 点击周期类型
    zhouqi_xpath = u'//select[@id="scheduleAddForm:cronType"]'
    # 时间（时）
    time_xpath=u"//label[contains(text(),'时间')]/parent::div//input"
    # 主页的用户名输入框
    username_input_xpath = "//*[@name='userName']"
    # 确认创建任务
    confirm_task_xpath = u"//*[@value='确认']"
    # 点击日期
    choose_date=u"//*[@class='el-input__icon el-icon-date']"
    # 今日日期
    tody_xpath=u"//*[@class='el-date-table']//td[@class='available today']"
    # 点击确定
    yes_xpath=u"//button[@class='el-time-panel__btn confirm']"
    # 取消
    close_xpath = u"//*[@class='el-dialog']//span[contains(.,'取消')]//parent::button[@class='el-button el-button--default el-button--mini is-round']"
    # 密码输入框
    passwd_input_xpath = "//*[@name='pwd']"

    # 部署与升级按钮是否存在
    def is_exist_deployment_and_upgrade_btn(self):
        self.click_elem(self.advanced_xpath)
        time.sleep(com_slp)
        return self.elem_is_exist(self.deployment_and_upgrade_xpath)

    # 进入云主机升级界面
    def goto_cloud_host_upgrade(self):
        self.click_elem(self.advanced_xpath)
        time.sleep(com_slp)
        self.click_elem(self.deployment_and_upgrade_xpath)
        time.sleep(com_slp)
        self.click_elem(self.cloud_host_upgrade_xpath)

    # 点击云主机升级按钮
    def click_cloud_host_upgrade_btn(self):
        time.sleep(com_slp)
        self.click_elem(self.cloud_host_upgrade_xpath)

    # 补丁包升级按钮是否存在
    def is_exist_patch_upgrade_btn(self):
        self.get_ciframe(self.find_elem(self.iframe_id_xpath))
        return self.elem_is_exist(self.patch_upgrade_btn_xpath)

    # 点击补丁包升级按钮
    def click_patch_upgrade_btn(self):
        self.get_ciframe(self.find_elem(self.iframe_id_xpath))
        self.click_elem(self.patch_upgrade_btn_xpath)

    # 检测上传的补丁包是否存在补丁包列表中
    def is_exist_check_patch(self):
        time.sleep(2)
        return self.elem_is_exist(self.patch_check_list_xpath)

    # 补丁包列表信息
    def get_all_info_patch(self):
        return self.get_elem_text(self.patch_check_list_xpath)

    # 点击某个补丁包的升级按钮
    def click_upgrade(self, patch_name):
        self.get_ciframe(self.find_elem(self.iframe_id_xpath))
        time.sleep(com_slp)
        self.click_elem(self.upgrade_btn_xpath % patch_name)

    # 点击告警按钮
    def click_warning_btn(self):
        self.find_elem(self.warning_btn_xpath).click()

    # 获取全部告警信息
    def get_all_warning_info(self):
        self.into_cifream()
        return self.get_elem_text(self.warning_info_xpath)

    # 进入框架
    def into_cifream(self):
        self.get_ciframe(self.find_elem(self.frame_id_xpath))

    # 点击OS上传按钮
    def click_upgrade_os_btn(self):
        self.into_cifream()
        self.click_elem(self.upload_os_btn_xpath)

    # 进入补丁包升级页面
    def goto_upload_patch_page(self):
        self.go_common_iframe()
        self.click_elem(self.patch_upgrade_btn_xpath)
        self.back_current_page()
        time.sleep(3)

    # 上传补丁包
    def upload_patch(self, path, name):
        self.click_elem(self.upload_patch_btn_xpath)
        self.file_upload(path, name)
        time.sleep(2)

    def upload_patch_firefox(self, path, name):
        self.click_elem(self.upload_patch_btn_xpath)
        self.upload(path+'\\'+name, 1)
        time.sleep(2)

    # 判断无可进行升级用的服务器   0为无可用服务器  1为有可用服务器
    def not_Upgrade(self):
        elems = self.find_elems(self.server_list_xpath)
        for i in range(len(elems)):
            content = elems[i].get_attribute('class')
            if content.find('disabled-row') >= 0:
                continue
            else:
                return 1
        return 0

    # 提示框
    def isExist_tip(self, content):
        return self.elem_is_exist(self.tip_xpath % content)

    # 判断开始升级按钮是否存在
    def isExist_begin_upgrade_btn(self):
        return self.elem_is_exist(self.begin_upgrade_xpath)

    def delete_patch(self, patch_name):
        """删除OS包"""
        self.go_common_iframe()
        self.click_elem(self.choose_OS_xpath.format(patch_name))
        time.sleep(1)
        self.click_elem(self.delete_patch_xpath)
        time.sleep(1)
        self.back_current_page()
        self.go_confirm_iframe()
        self.click_elem(self.confirm_button_xpath)
        time.sleep(1)
        self.back_current_page()
        text = self.get_all_OS_info()
        if text.__contains__(patch_name):
            return 1
        else:
            return 0

    def get_all_OS_info(self):
        """获取所有OS包"""
        self.go_common_iframe()
        text = self.get_elem_text(self.all_os_info_xpath)
        self.back_current_page()
        return text

    def go_common_iframe(self):
        """进入右侧公共iframe"""
        self.get_ciframe(self.find_elem(self.iframe_id_xpath))

    def go_confirm_iframe(self):
        """进入确认删除提示iframe"""
        self.get_ciframe(self.find_elem(self.confirm_iframe_xpath))

    def out_cifream(self):
        """跳出iframe"""
        self.back_current_page()

    def upload_0S_patch(self, path, name):
        """上传OS包"""
        self.go_common_iframe()
        self.click_elem(self.upload_OS_xpath)
        self.back_current_page()
        self.file_upload(path, name)
        time.sleep(2)

    def refresh_webdriver(self):
        """刷新浏览器"""
        self.driver.refresh()

    def refresh_OS(self):
        """OS包界面点击刷新"""
        self.go_common_iframe()
        self.click_elem(self.refresh_patch_xpath)
        self.back_current_page()

    def refresh_patch(self):
        """补丁包升级界面点击刷新"""
        self.click_elem(self.refresh_patch_btn_xpath)
        time.sleep(120)

    def patch_deleted(self, patchName):
        """删除补丁包"""
        if self.elem_is_exist(self.choose_patch_xpath.format(patchName)) == 0:
            self.click_elem(self.choosed_patch_more_xpath.format(patchName))
        else:
            self.click_elem(self.more_xpath.format(patchName))
        time.sleep(com_slp)
        self.click_elem(self.delete_patch_xpath)
        self.click_elem(self.confire_btn_xpath)
        if not self.elem_is_exist(self.patch_list_empty_xpath):
            return 0
        else:
            text = self.get_elem_text(self.patch_check_list_xpath)
            if text.__contains__(patchName):
                return 1
            else:
                return 0

    def get_all_patch_info(self):
        """获取所有补丁包"""
        return self.get_elem_text(self.all_patch_info_xpath)

    # 点击下一步按钮
    def click_next(self):
        self.click_elem(self.next_btn_xpath)

    # 选中补丁包
    def select_patch(self, patchName):
        if self.get_elem_attribute(self.selected_patch_btn_xpath % patchName, 'class').find('is-selected') >= 0:
            pass
        else:
            self.click_elem(self.select_patch_btn_xpath % patchName)

    # 点击开始升级按钮
    def click_begin_upgrade(self):
        self.click_elem(self.begin_upgrade_xpath)

    # 获取未选中的补丁包列表
    def get_unselected_patch_list(self):
        unselected_patch_list = []
        text = self.get_all_info_patch()
        patch_list = text.split()
        for str in patch_list:
            if str.__contains__('.zip'):
                unselected_patch_list.append(str)
        return list(set(unselected_patch_list[2:]))

    # 点击确认按钮
    def click_confire(self):
        self.click_elem(self.confire_btn_xpath)

    # 输入确认密码
    def send_pwd(self, pwd=c_pwd):
        time.sleep(com_slp)
        self.elem_send_keys(self.pwd_xpath, pwd)
        time.sleep(2)
    def close_confirm_pwd(self):
        self.click_elem(self.confire_pwd_btn_xpath)
        time.sleep(2)
        self.click_elem(self.close_xpath)
        time.sleep(2)

    # 获取admin-tool的告警框内容
    def close_warning(self):
        text = ''
        win1 = automation.TextControl(Name=u'上传文件类型错误，WEB目录仅允许.zip文件类型且文件名不能带有空格的文件上传。')
        if win1.Exists():
            text = win1.GetWindowText()
            win = automation.ButtonControl(Name=u'确定')
            win.Click()
        return text
    def get_warning_info(self, local_path, file_name,content):
            self.click_elem(self.upload_patch_btn_xpath)
            time.sleep(3)
            win = automation.ButtonControl(Name=u'打开 URL:cbbftpProtocol')
            if win.Exists():
                win.Click()
                edit = automation.EditControl(AutomationId="1001")
                time.sleep(3)
                edit.SendKeys(u"%s{Enter}" % local_path)
                win2 = automation.ListItemControl(Name=u'' + file_name)
                win2.DoubleClick()
                i = 0
                while i < 10:
                    try:
                        time.sleep(2)
                        win3 = automation.TextControl(Name=u"队列:空")
                        if win3.Exists():
                            break
                    except Exception as e:
                        logging.error(e)
                        logging.error("未传输完成，队列不为空")
                        time.sleep(5)
                    i = i + 1
                text = ''
                win1 = automation.TextControl(Name=content)
                if win1.Exists():
                    text = win1.GetWindowText()
                    time.sleep(com_slp)
                    win = automation.ButtonControl(Name=u'确定')
                    win.Click()
                    time.sleep(3)
                # win5 = automation.WindowControl(Name=u"服务器镜像目录 - 已连接 - RuijieFTP")
                win4 = automation.ButtonControl(Name=u"关闭")
                win4.Click()
                return text
            else:
                logging.error("admin tool上传工具未打开")

    def start_update(self):
        """开始升级"""
        self.click_elem(self.start_update_btn_xpath)
        time.sleep(com_slp)
        self.click_elem(self.confire_btn_xpath)
        time.sleep(com_slp)

    def send_passwd_confirm(self, pd=c_pwd):
        """输入密码点击确定"""
        self.find_elem(self.confirm_passwd_xpath).send_keys(pd)
        time.sleep(1)
        self.find_elem(self.confirm_pwd_xpath).click()

    def get_upload_msg(self):
        """获取补丁包升级提示语句"""
        try:
            return self.get_elem_text(self.update_prompt_xpath)
        except:
            return ''

    def get_now_version(self, ip):
        """获取当前版本"""
        update = server_conn(ip, u'cat /usr/rcd/version_web.ini')
        updade = update[0][0]
        version = update.split('ruijie.rcc.web.fourVersion=')[1]
        version = re.findall("\d+", version)[0]
        return version

    def check_update_success(self, ip):
        """后台查看日志判断升级是否完成"""
        flag = 0
        version = self.get_now_version(ip)
        for i in range(1, 250):
            try:
                version_now = self.get_now_version(ip)
            except:
                pass
            else:
                if version != version_now:
                    # 升级成功
                    flag = 1
                    time.sleep(2)
                    break
                time.sleep(10)
        return flag

    def login_Reserve_control(self, ip):
        """登录主控查看升级是否成功"""
        # flag=1,升级成功提示
        flag = 0
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(ip)
        t = Login(driver)
        try:
            t.login(username, passwd)
            # t.click_elem(self.confire_btn_xpath)
            flag=1
        except:
            flag=0
        time.sleep(3)

        return flag
    def click_confirm(self):
        """点击确定"""
        self.click_elem(self.confire_btn_xpath)
    def get_selected_patch(self):
        """获取被选中的补丁包名"""
        return self.get_elem_text(self.selected_patch_xpath)

    def get_disable_patch(self):
        """获取不能用的补丁包名"""
        return self.get_elem_text(self.selcted_disable_xpath)

    def delete_upload_patch(self):
        """删除之前上传的包（最多一个不存在的一个可用的）"""
        try:
            disable_name = self.get_disable_patch()
            self.patch_deleted(disable_name)
        except:
            pass
        try:
            disable_name = self.get_selected_patch()
            self.patch_deleted(disable_name)
        except:
            pass

    def drop_version(self, ip,version):
        """后台降版本"""
        server_conn(ip, 'cd /root/&&sh rollback_upgrade.sh "{}" '.format(version))


    def goto_cloud_desk(self):
        """点击云主机"""
        self.click_elem(self.cloud_desk_xpath)

    def click_cloud_desk_update(self):
        """点击云主机升级"""
        self.click_elem(self.cloud_host_upgrade_xpath)

    def get_ip_num(self):
        """获取主备控总个数"""
        self.get_ciframe(self.find_elem(self.iframe_id_xpath))
        num = len(self.find_elems(self.ip_num_xpath)) - 1
        self.out_cifream()
        return num

    def get_Cloud_Hosting(self):
        """获取准备升级的云主机个数"""
        num = len(self.find_elems(self.ip_num_xpath))-1
        return num

    def click_pre(self):
        """点击上一步"""
        self.click_elem(self.click_pre_xpath)

    @staticmethod
    def get_master_url():
        master_url = []
        master_section = ['master', 'master_vir_ip']
        for section in master_section:
            url = "http://{}/main.html#/login".format(cp.get(section, 'ip_1'))
            master_url.append(url)
        return master_url

    @staticmethod
    def get_reserve_url():
        reserve_url = []
        for ip in cluster_ip:
            url = "http://{}/main.html#/login".format(ip)
            reserve_url.append(url)
        return reserve_url

    def edit_text(self, locator, text=''):
        """修改文本框"""
        time.sleep(1)
        self.find_elem(locator).click()
        time.sleep(1)
        self.find_elem(locator).send_keys(Keys.CONTROL, 'a', Keys.BACKSPACE)
        self.find_elem(locator).send_keys(text)
        return text
    def create_clock_task(self,task,t=10):
        """新建定时任务"""
        self.click_elem(self.clock_task_xpath)
        time.sleep(com_slp)
        self.click_elem(self.create_clock_task_xpath)
        time.sleep(com_slp)
        self.click_elem(self.task_xpath)
        time.sleep(2)

        if task==u'重启云主机':
            self.click_elem(self.reboot_xpath)
            time.sleep(com_slp)
        if task == u'关闭云主机':
            self.click_elem(self.poweroff_xpath)
            time.sleep(com_slp)
        if task == u'关闭胖终端':
            self.click_elem(self.poweroff_IDV_xpath)
            time.sleep(com_slp)

        self.click_elem(self.clock_type)
        time.sleep(2)
        self.click_elem(self.task_type_xpath.format(u'指定时间'))
        time.sleep(2)
        self.click_elem(self.choose_date)
        time.sleep(2)
        self.click_elem(self.tody_xpath)
        now_time = datetime.datetime.now()

        task_time = (now_time + datetime.timedelta(minutes=+t)).strftime("%H:%M:%S")
        time.sleep(com_slp)

        self.edit_text(self.time_xpath,task_time)
        time.sleep(1)

        self.click_elem(self.yes_xpath)
        time.sleep(1)
        self.click_elem(self.upgrade_confire_btn_xpath)

        time.sleep(1)
    #转换文件大小单位
    def translate_size(self,filesize):
        if filesize[-1] == 'M':
            size = float(filesize[:-1])/1024
            return size
        if filesize[-1] == 'T':
            size = int(filesize[:-1])*1024
            return size
        if filesize[-1] == 'G':
            return int(filesize[:-1])

    def init_wait(self,t=1800):
        """查看重启是否完成"""
        flag = 0
        for i in range(1, t/10):
            time.sleep(10)
            if self.elem_is_exist(self.passwd_input_xpath) == 0:
                flag = 1
                break
        return flag
    if __name__ == "__main__":
        pass
