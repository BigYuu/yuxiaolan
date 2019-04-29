#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: zhouxihong
@contact: zhouxihong@ruijie.com
@software: PyCharm
@time: 2018/10/11
"""
import os
import re
import json
class DutGetShow:

    def __init__(self):
        pass

    def dut_show_autoget_blank_list(self, show_info, value_title, value_title_end=None):
        """
        列表为空格区分的形式
        Index     Peer IP              Port      State         Mac Address
        1         13.0.3.3             10000     Run           5869.6c7a.685e
        """
        col_len_list = []
        # 创建字典
        dict_value = {}
        rol_title_list = []
        title_row = []
        show_info_list_line = show_info.split("\n")
        if re.match(r'.*show.*', show_info_list_line[0]):
            show_info_list_line.remove(show_info_list_line[0])
        if re.match(r'.*#.*', show_info_list_line[-1]):
            show_info_list_line.remove(show_info_list_line[-1])
        for i in show_info_list_line:
            if '' in show_info_list_line:
                show_info_list_line.remove('')
            if '------' in i:
                show_info_list_line.remove(i)
            if '====' in i:
                show_info_list_line.remove(i)
        length = len(show_info_list_line)
        for line_len_num in range(0, length):
            if value_title in show_info_list_line[line_len_num]:  # ***********
                start_num = line_len_num
            if value_title_end is not None:
                if value_title_end in show_info_list_line[line_len_num]:
                    end_num = line_len_num
            else:
                end_num = length
        for k in range(start_num, end_num):
            col_value_list = re.split(r'\s{1,}', show_info_list_line[k])
            if value_title in col_value_list:
                title_row = col_value_list
                x_len = len(title_row)
                for i in range(x_len):
                    if title_row[i] == value_title:
                        new_list_title_key = i
            else:
                if col_value_list != "":
                    title_col = col_value_list[new_list_title_key]  # 表头的列值位*****
                    rol_title_list.append(title_col)
                    if new_list_title_key + 1 < x_len:
                        for s in range(new_list_title_key + 1, x_len):  # 需要变参的地方
                            key_name = '%s/%s' % (title_col, title_row[s])
                            dict_value[key_name] = col_value_list[s]
                    if new_list_title_key > 0:
                        for s in range(0, new_list_title_key):  # 需要变参的地方
                            ##遍历列头边的值
                            key_name = '%s/%s' % (title_col, title_row[s])
                            dict_value[key_name] = col_value_list[s]
        dict_value[value_title + "_list"] = rol_title_list
        return dict_value

    def dut_get_show_df(self, show_info, key1, key2):
        show_info = show_info.replace(' on', '')
        return self.dut_show_autoget_blank_list(show_info, 'Mounted')[key1+'/'+key2]

    def dut_get_show_df_user_space(self,show_info, key1, key2):
        show_info = show_info.replace(' on', '')
        dict = self.dut_show_autoget_blank_list(show_info, 'Filesystem')
        i = 0
        summ = 0
        while True:
            if (key1+str(i)+'/'+key2) in dict:
               summ = summ + int(dict[key1+str(i)+'/'+key2])
            if i >= 90:
                break
            i = i + 1
        return summ
