#!/usr/bin/python
# -*- coding: UTF-8 -*-


"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/8/20 17:57
"""
import logging
from logging.handlers import RotatingFileHandler
import time
import sys
from Common import file_dir

fmt = " %(asctime)s  %(levelname)s %(filename)s %(funcName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

# handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())

# handler_2 = RotatingFileHandler(file_dir.log_dir+"//UI_CloudOffice_log_{0}.log".format(curTime),
# backupCount=20,encoding='utf-8')
# 将日志输出的指定的文件中
# logging.basicConfig(filename=file_dir.log_dir+"//UI_CloudOffice_log_{0}.log".format(curTime),format=fmt,
#                     datefmt=datefmt,level=logging.INFO)

logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, stream=sys.stdout)
