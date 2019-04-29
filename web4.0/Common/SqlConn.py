#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/8/20 18:01
"""
from configparser import ConfigParser
from Common import file_dir
from Common import Mylog
import logging
import pymysql


def DataConn():
    try:
        # 获取配置文件
        cp = ConfigParser()
        cp.read(file_dir.config_dir + "\\webconn.cfg")
        # 用配置文件链接数据库
        conn = pymysql.connect(host=cp.get('py_mysql', 'host'), port=int(cp.get('py_mysql', 'port')),
                               user=cp.get('py_mysql', 'user'), passwd=cp.get('py_mysql', 'passwd'),
                               charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        return conn, cur
    except Exception as error:
        logging.error(error)
        logging.exception('连接不上数据库，请确认数据链接是否正确')


if __name__ == "__main__":
    pass
    # a, b = DataConn()
    # SQL = ' '
    # b.execute(SQL)
    # print(b.fetchone())
    # a.close()

