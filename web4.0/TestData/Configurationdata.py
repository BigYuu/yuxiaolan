#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: houjinqi
@contact: houjinqi@ruijie.com
@software: PyCharm
@time: 2018/12/14 11:21
"""
from TestData.basicdata import *
name_list = [u'中国五矿集团', u'大连理工大学', u'中国大唐集团', u'移动', u'松山市', u'武当山']
channel_list = [u'huawei', u'华3', u'深信服', u'中兴', u'联想+']
maintainer_list = [u'张3', u'李4-@._', u'王五.', u'李逵@鲁智深', u'宋江-',u'秦始皇_']
telephone_list = [u'10086', u'10000', u'4008-111-000', u'123456789', u'88888888', u'86-136-4681-4682', u'00000000']

customer_info_list = []

test_name = u'admin'
test_passwd = [c_pwd, u'1234567890', u'asd123mcv_', u'_______', u'aaaaaabbbb']
# 获取服务器时间
get_server_time = u'date "+%Y-%m-%d %H:%M:%S"'

# 修改服务器时间
set_server_time = u"date -s {}"
