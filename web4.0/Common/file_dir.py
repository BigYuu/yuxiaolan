#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/8/20 17:59
"""
import os

cur_dir = os.path.split(os.path.abspath(__file__))[0]
config_dir = cur_dir.replace("Common", "config")
log_dir = cur_dir.replace("Common", "Logs")
report_dir = cur_dir.replace("Common", "HtmlReport")
testdata_dir = cur_dir.replace("Common", "TestData")
testcase_dir = cur_dir.replace("Common", "TestCase")
pageobj_dir = cur_dir.replace("Common", "WebPages")
screenshot_dir = cur_dir.replace("Common", "Errorscrenshot")
picture_dir = cur_dir.replace("Common", "pictures")
parent_dir = cur_dir.replace("\Common", "")
