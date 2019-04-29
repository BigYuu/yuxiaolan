#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/8/26 14:55
"""
import pytest
import time
from selenium import webdriver
from WebPages.LoginPage import Login
from TestData.Logindata import *
from configparser import ConfigParser
from Common import file_dir
from Common.serverconn import *
from WebPages.AuthenmanagePage import AuthenManage
import allure

driver = None


@pytest.fixture
def login_fixture():
    """登录验证前置条件"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


# 下载浏览器配置
@pytest.fixture
def download_fixture():
    """下载用例前置条件"""
    cp = ConfigParser()
    cp.read(file_dir.config_dir + "\\chrome_set.cfg")
    option = webdriver.ChromeOptions()
    option.add_argument(cp.get('personal_set', 'pset'))  # 个人chrome浏览器配置 chrome://version
    driver = webdriver.Chrome(chrome_options=option)
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def com_fixture():
    """共用前置条件"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    t = Login(driver)
    t.login(c_user, c_pwd)
    yield driver
    driver.quit()

@pytest.fixture
def ad_fixture():
    """共用前置条件"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    t = Login(driver)
    t.login(c_user, c_pwd)
    p = AuthenManage(driver)
    p.goto_adm()
    p.input_all_info()
    p.choose_ou('hjq')
    p.choose_ou('AD域认证测试')
    yield driver
    driver.quit()


@pytest.fixture
def cmd_fixture():
    """云桌面管理前置条件"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    t = Login(driver)
    t.login(username, passwd)
    t.goto_cloud_desk_manage()
    yield driver
    driver.quit()


@pytest.fixture
def warming_fixture():
    """告警前置条件"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    t = Login(driver)
    t.login(username, passwd)
    yield driver
    driver.quit()


@pytest.fixture
def mirroring_fixture():
    cp = ConfigParser()
    cp.read(file_dir.config_dir + "\\chrome_set.cfg")
    option = webdriver.ChromeOptions()
    option.add_argument(cp.get('personal_set', 'pset'))  # 个人chrome浏览器配置 chrome://version
    driver = webdriver.Chrome(chrome_options=option)
    driver.maximize_window()
    driver.get(url)
    t = Login(driver)
    t.login(username, passwd)
    yield driver
    driver.quit()


@pytest.fixture
def user_pm_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    t = Login(driver)
    t.login(username, passwd)
    time.sleep(1)
    t.go_to_user_manage_page()
    yield driver
    driver.quit()


@pytest.fixture
def permission_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    t = Login(driver)
    t.login(username, passwd)
    t.go_to_permission_page()
    yield driver
    driver.quit()



@pytest.fixture
def vdi_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    t = Login(driver)
    t.login(username, passwd)
    t.go_to_vdi_terminal_page()
    yield driver
    driver.quit()
    pass


@pytest.fixture
def idv_fixture():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    t = Login(driver)
    t.login(username, passwd)
    t.go_to_idv_terminal_page()
    yield driver
    driver.quit()


@pytest.fixture(autouse=True)
def common_function(request):
    function_name = request._pyfuncitem.name
    logging.info("[start test case]:" + function_name + ">>>>>测试用例执行开始-------")
    yield
    logging.info("[end test case]:" + function_name + ">>>>>测试用例执行结束-------")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if not driver:
        return

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            f = driver.get_screenshot_as_png()
            allure.MASTER_HELPER.attach('screenshot', f, type=allure.MASTER_HELPER.attach_type.PNG)

        report.extra = extra

@pytest.fixture
def url_fixture(url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    t = Login(driver)
    t.login(username, passwd)
    yield driver
    driver.quit()
