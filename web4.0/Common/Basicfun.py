#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/8/26 15:34
"""
import win32gui
import win32con
import win32api
import re
from random import randint
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import uiautomation as automation
from Common.serverconn import *
from Common.mythread import MyThread
from Mylog import *
import logging
import sys

class BasicFun:
    def __init__(self, driver):
        self.driver = driver

    def elem_wait(self, locator, by=By.XPATH, wait_times=7):
        """等待元素可见"""
        if by not in By.__dict__.values():
            logging.error("不支持输入的by表达式")
        t1 = time.time()
        try:
            WebDriverWait(self.driver, wait_times).until(ec.visibility_of_element_located((by, locator)))
            t2 = time.time()
            logging.info(
                "wait element visible start time：{0}，end time：{1},total wait times is: {2}".format(t1, t2, t2 - t1))
        except Exception as timeout:
            # 超时链接截图
            curtime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
            file_path = os.path.join(file_dir.screenshot_dir, "{0}.png".format(curtime))
            self.driver.save_screenshot(file_path)
            logging.exception("等待元素超时，没有找到相应的元素。截屏文件为：{0}".format(file_path))
            raise timeout

    def elem_presence_wait(self, locator, by=By.XPATH, wait_times=7):
        """等待元素出现"""
        if by not in By.__dict__.values():
            logging.error("不支持输入的by表达式")
        t1 = time.time()
        try:
            WebDriverWait(self.driver, wait_times).until(ec.presence_of_element_located((by, locator)))
            t2 = time.time()
            logging.info(
                "wait element presence  time：{0}，end time：{1},total wait times is: {2}".format(t1, t2, t2 - t1))
        except Exception as timeout:
            # 超时链接截图
            curtime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
            file_path = os.path.join(file_dir.screenshot_dir, "{0}.png".format(curtime))
            self.driver.save_screenshot(file_path)
            logging.exception("等待元素超时，没有找到相应的元素。截屏文件为：{0}".format(file_path))
            raise timeout

    def wait_elem_not_presence(self, locator, by=By.XPATH, wait_times=1800):
        """等待元素消失"""
        if by not in By.__dict__.values():
            logging.error("不支持输入的by表达式")
        t1 = time.time()
        try:
            WebDriverWait(self.driver, wait_times).until_not(ec.presence_of_all_elements_located((by, locator)))
            t2 = time.time()
            logging.info(
                "wait element presence  time：{0}，end time：{1},total wait times is: {2}".format(t1, t2, t2 - t1))
        except Exception as timeout:
            # 超时链接截图
            curtime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
            file_path = os.path.join(file_dir.screenshot_dir, "{0}.png".format(curtime))
            self.driver.save_screenshot(file_path)
            logging.exception("等待元素超时，没有找到相应的元素。截屏文件为：{0}".format(file_path))
            raise timeout

    def elem_click_wait(self, locator, by=By.XPATH, wait_times=7):
        """等待元素可点击"""
        if by not in By.__dict__.values():
            logging.error("不支持输入的by表达式")
        t1 = time.time()
        try:
            WebDriverWait(self.driver, wait_times).until(ec.element_to_be_clickable((by, locator)))
            t2 = time.time()
            logging.info(
                "wait element visible start time：{0}，end time：{1},total wait times is: {2}".format(t1, t2, t2 - t1))
        except Exception as timeout:
            # 超时链接截图
            curtime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
            file_path = os.path.join(file_dir.screenshot_dir, "{0}.png".format(curtime))
            self.driver.save_screenshot(file_path)
            logging.exception("等待元素超时，没有找到相应的元素。截屏文件为：{0}".format(file_path))
            raise timeout

    def find_elem(self, locator, by=By.XPATH, wait_times=7):
        """查找在页面可见元素"""
        self.elem_wait(locator, by, wait_times)
        time.sleep(0.3)
        ele = self.driver.find_element(by, locator)
        return ele

    def find_elems(self, locator, by=By.XPATH, wait_times=7):
        """查找一类在页面可见元素"""
        self.elem_wait(locator, by, wait_times)
        eles = self.driver.find_elements(by, locator)
        return eles

    def find_presence_elem(self, locator, by=By.XPATH, wait_times=7):
        """查找存在元素，不一定在页面可见"""
        self.elem_presence_wait(locator, by, wait_times)
        ele = self.driver.find_element(by, locator)
        return ele

    def find_presence_elems(self, locator, by=By.XPATH, wait_times=7):
        """查找一类存在元素，不一定在页面可见"""
        self.elem_presence_wait(locator, by, wait_times)
        eles = self.driver.find_elements(by, locator)
        return eles

    def get_elem_text(self, locator, by=By.XPATH, wait_times=7):
        """获取元素文本"""
        self.elem_presence_wait(locator, by, wait_times)
        ele = self.driver.find_element(by, locator)
        return ele.get_attribute('textContent')

    def elem_send_keys(self, locator, keys, by=By.XPATH, wait_times=7):
        """对元素发送信息"""
        self.find_elem(locator, by, wait_times).send_keys(keys)

    def click_elem(self, locator, by=By.XPATH, wait_times=7):
        """点击元素"""
        self.elem_click_wait(locator, by, wait_times)
        time.sleep(1)
        n = 0
        while n < 3:
            try:
                self.driver.find_element(by, locator).click()
                break
            except:
                time.sleep(1)
            n = n+1

    def get_elem_attribute(self, locator, attribute, by=By.XPATH, wait_times=7):
        """获取元素属性"""
        self.elem_presence_wait(locator, by, wait_times)
        return self.driver.find_element(by, locator).get_attribute(attribute)

    def clear_text_info(self, locator, by=By.XPATH, wait_times=7):
        """清除文本输入框信息不支持火狐浏览器"""
        self.find_elem(locator, by, wait_times).send_keys(Keys.CONTROL, 'a', Keys.BACK_SPACE)

    def clear_text_info2(self, locator):
        """清除文本信息支持火狐浏览器"""
        self.chainsdubclick(locator)
        self.find_elem(locator).send_keys(Keys.BACK_SPACE)

    def get_url(self):
        """获取页面url"""
        return self.driver.current_url

    def get_cwind(self, i):
        """切换窗口"""
        winds = self.driver.window_handles
        self.driver.switch_to.window(winds[i])

    def get_ciframe(self, loactor):
        """切换到iframe"""
        self.driver.switch_to.frame(loactor)

    def back_current_page(self):
        """跳出iframe"""
        self.driver.switch_to.default_content()

    def scroll_into_view(self, locator, by=By.XPATH, wait_times=7, click_type=0):
        """鼠标滚动"""
        self.elem_presence_wait(locator, by, wait_times)
        ele = self.driver.find_element(by, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        if click_type == 0:
            time.sleep(0.5)
            ele.click()

    def download(self, path='D:\\'):
        """chrome浏览器下载设置"""
        win = automation.WindowControl(ClassName="#32770", Name=u'另存为')
        win2 = win.ToolBarControl(AutomationId="1001")
        win2.Click()
        win3 = win.EditControl(AutomationId="41477")
        win3.SendKeys(u'%s{Enter}' % path)
        win4 = win.ButtonControl(AutomationId="1")
        win4.Click()
        # 一级窗口
        # dialog = win32gui.FindWindow("#32770", u"另存为")
        # button = win32gui.FindWindowEx(dialog, 0, "Button", u"保存(&S)")
        # # 2、点击保存按钮
        # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    def upload(self, path, driver_type=0):
        """chrome浏览器上传设置,输入的文件路径,river_type 0 谷歌 1 火狐
        """
        time.sleep(1)
        dialog =''
        if driver_type==0:
            dialog = win32gui.FindWindow("#32770", u"打开")
        elif driver_type==1:
            dialog = win32gui.FindWindow("#32770", u"文件上传")
        else:
            logging.error('浏览器不支持')
        combobox32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        combobox = win32gui.FindWindowEx(combobox32, 0, "ComboBox", None)
        edit = win32gui.FindWindowEx(combobox, 0, "Edit", None)
        button = win32gui.FindWindowEx(dialog, 0, "Button", u"打开(&O)")
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, path.encode('gbk'))
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

    def file_upload(self, local_path, file_name, times=10):
        """admin tool上传文件到服务器"""
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
            while i < times:
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
            # win5 = automation.WindowControl(Name=u"服务器镜像目录 - 已连接 - RuijieFTP")
            win4 = automation.ButtonControl(Name=u"关闭")
            win4.Click()
        else:
            logging.error("admin tool上传工具未打开")

    def get_iframe_last_id(self, locator):
        """当iframe是变动时获取iframe的变动的id,传入iframe所在div的元素定位的方式"""
        self.back_current_page()
        ele = self.find_elem(locator)
        s = ele.get_attribute("id")
        return re.findall('.*?(\d+)', s)[0]

    def open_admin_tool(self):
        """打开URL:AdminTool编辑镜像工具"""
        button = automation.ButtonControl(Name=u'打开 URL:cbbvmviewProtocol')
        if button.Exists(maxSearchSeconds=10):
            button.Click()
        else:
            logging.error("未知错误")

    def open_assistance_tool(self):
        """远程协助打开 URL:cbbremoteviewProtocol"""
        window = automation.PaneControl(searchDepth=1, ClassName='Chrome_WidgetWin_1')
        if window.Exists(maxSearchSeconds=3):
            #pc打开远程协助名称
            dialog = win32gui.FindWindow('Chrome_WidgetWin_1', u'云办公主机 - Google Chrome')
            time.sleep(1)
            win32gui.SetForegroundWindow(dialog)
            time.sleep(2)
            # button = window.ButtonControl(Name=u'打开 AdminTool Launcher')
            # 终端打开远程协助 打开 URL:cbbremoteviewProtocol
            button = window.ButtonControl(Name=u'打开 URL:cbbremoteviewProtocol')
            button.Click()
        else:
            logging.error("未知错误")

    def close_assistance_tool(self):
        """远程协助打开 URL:cbbremoteviewProtocol"""
        window = automation.PaneControl(searchDepth=1, ClassName='Chrome_WidgetWin_1')
        if window.Exists():
            dialog = win32gui.FindWindow('Chrome_WidgetWin_1',u'云办公主机 - Google Chrome')
            time.sleep(1)
            win32gui.SetForegroundWindow(dialog)
            time.sleep(2)
            button = window.ButtonControl(Name=u'取消')
            button.Click()
        else:
            logging.error("未知错误")

    def chainstay(self, loactor, by=By.XPATH, wait_times=20):
        """鼠标悬停"""
        ele = self.find_elem(loactor, by, wait_times)
        ActionChains(self.driver).move_to_element(ele).perform()
        time.sleep(1)

    def chainsdubclick(self, loactor):
        """鼠标双击"""
        ele = self.find_elem(loactor)
        ActionChains(self.driver).double_click(ele).perform()

    def accept_alert(self):
        """接受alert弹框,返回alert框的提示信息"""
        time.sleep(3)
        dialog_box = self.driver.switch_to.alert
        time.sleep(2)
        a = dialog_box.text
        dialog_box.accept()
        return a

    def select_list_chose3(self, locator, name, by=By.XPATH, wait_times=7):
        """select 下拉选择,通过vaule值选择"""
        self.elem_presence_wait(locator, by, wait_times)
        s = self.driver.find_element(by, locator)
        Select(s).select_by_value(name)

    def select_list_chose(self, locator, text, by=By.XPATH, wait_times=7):
        """select 下拉选择,通过text值选择"""
        self.elem_presence_wait(locator, by, wait_times)
        s = self.driver.find_element(by, locator)
        Select(s).select_by_visible_text(text)

    def select_list_chose2(self, locator, index=1, by=By.XPATH, wait_times=7):
        """select 下拉选择随机选择"""
        self.elem_presence_wait(locator, by, wait_times)
        Select(self.driver.find_element(by, locator)).select_by_index(randint(0, index))

    def select_chose_text(self, locator, by=By.XPATH, wait_times=7):
        """select 下拉选择后读取选择框信息"""
        self.elem_presence_wait(locator, by, wait_times)
        option = Select(self.driver.find_element(by, locator)).first_selected_option
        return option.text

    def elem_is_exist2(self, locator, by=By.XPATH,wait_times=2):
        """判断在页面是否存在可见元素，存在返回元素，不存在返回None"""
        try:
            WebDriverWait(self.driver, wait_times).until(ec.visibility_of_element_located((by, locator)))
            ele = self.driver.find_element(by, locator)
            return ele
        except:
            logging.info("元素不存在")
            return None

    def elem_is_exist(self, locator, wait_times=5):
        """判断在页面是否存在可见元素，存在返回0，不存在返回1"""
        try:
            self.find_elem(locator, by=By.XPATH, wait_times=wait_times)
            return 0
        except:
            logging.info("元素不存在")
            return 1

    def image_ip_set(self,):
        """编辑镜像时设置镜像ip"""
        ip_list= self.get_useful_ip()
        server_conn(host_ip, 'echo {}>/opt/ftpshare/share/ip_set.txt'.format(ip_list[0]))
        return ip_list[0]

    def ping_ip(self, temp_ip, i):
        """ping IP 是否可用，可用则返回IP"""
        reload(sys)
        sys.setdefaultencoding('GBK')
        info = os.popen('ping {0}.{1}'.format(temp_ip, i))
        s1 = info.read()
        b = s1.splitlines()[2]
        if b.__contains__(u'请求超时'):
            set_ip = temp_ip + '.' + str(i)
            return set_ip
        else:
            return None

    def get_useful_ip(self):
        """返回可用ip 列表"""
        pthread_list = []
        a = host_ip.split('.', -1)
        a.remove(a[-1])
        temp_ip = '.'.join(a)
        ip_list = list()
        for i in range(2,255):
            t =MyThread(self.ping_ip, args=(temp_ip, i,))
            pthread_list.append(t)
        for i in range(2, 253):
            pthread_list[i].start()
        for i in range(2, 253):
            pthread_list[i].join()
            if pthread_list[i].get_result() is not None:
                ip_list.append(pthread_list[i].get_result())
        return ip_list

    def add_new_window(self,url):
        """打开浏览器新增一个窗口"""
        js = 'window.open({});'.format(url)
        self.driver.execute_script(js)

    def close_remot_assistance(self):
        """关闭远程协助窗口"""
        dialog = win32gui.FindWindow("VNCMDI_Window", "RjRemote Viewer")
        time.sleep(1)
        win32gui.SetForegroundWindow(dialog)
        time.sleep(1)
        win32api.SendMessage(dialog, win32con.WM_CLOSE, 0, 0)

    def drag_element(self,locator,x=50,y=0):
        """元素拖拽"""
        actions = ActionChains(self.driver)
        ele = self.find_elem(locator)
        actions.drag_and_drop_by_offset(ele, x, y)
        actions.perform()