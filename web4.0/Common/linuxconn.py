#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/8/27 15:17
"""

import paramiko
from Common import file_dir
def return_ssh(ip, post, name, password, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, post, name, password)
    stdin, stdout, stderr = ssh.exec_command(command)
    text = stdout.read()
    ssh.close()
    return text

if __name__ == "__main__":
    a = return_ssh('172.21.195.13','22','root','35w_"{<L','df -h')
    print(a)