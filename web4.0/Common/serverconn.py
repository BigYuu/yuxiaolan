#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/8/21 16:06
"""
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from TestData.basicdata import *
from Common.file_dir import *
from Common import Mylog
import telnetlib
import logging
import paramiko
import winrm
import time


def server_conn(ip, command,password=server_pwd):
    """连接服务器"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=ip, username='root', password=password)
    stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
    result = stdout.read()
    ssh.close()
    return result


def terminal_download_conn(ip, dir_path, username='root', password='fjrjroot_123'):
    """连接终端下载文件"""
    scp = paramiko.Transport(ip, 22)
    scp.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(scp)
    files = sftp.listdir(dir_path)
    for f in files:
        sftp.get(os.path.join(dir_path, f), os.path.join(picture_dir, f))
    scp.close()


def server_file_upload(server_ip, target_ip, tdir=u'/测试运营组/自动化测试镜像', sdir=u'/opt/lessons'):
    """从ftp上传文件到服务器,server_ip 服务器IP，target_ip ftp ip"""
    cmds = u'mkdir /mnt/autoupdate;mount -t nfs {0}:/rcd /mnt/autoupdate;' \
           u'cp /mnt/autoupdate{1}/* {2}'.format(target_ip, tdir, sdir)
    server_conn(server_ip, cmds)
    print(u"文件复制完成")


def common_data_upload(server_ip, tdir, sdir):
    """从172.21.112.136上传文件到服务器"""
    server_file_upload(server_ip, '172.21.112.136', tdir, sdir)
    path1 = ur'/mnt/autoupdate{}/'.format(tdir)
    for root, dirs, file_name_list in os.walk(path1):
        for filename in file_name_list:
            if filename is not None:
                md5_vaulee1 = server_conn(server_ip, "md5sum {0}/{1}|awk 'NR==1{print $1}'".format(path1, filename))
                md5_vaulee2 = server_conn(server_ip, "md5sum {0}{1}|awk 'NR==1{print $1}'".format(sdir, filename))
                if md5_vaulee1 == md5_vaulee2:
                    pass
                else:
                    server_conn(server_ip, 'cp /mnt/autoupdate{0}/{1} {2}'.format(path1, filename, sdir))
                    file_name_list.append(filename)
    server_conn(server_ip, 'umount /mnt/autoupdate/;sync')


def get_win_conn_info(ip, user_name, passwd, cmd):
    """连接windows系统虚机，并执行cmd命令，返回结果"""
    # winconn = winrm.Session(r'http://{}/wsman'.format(ip), auth=(user_name, passwd))
    # time.sleep(1)
    # r = winconn.run_cmd(cmd)
    # a = r.std_out
    # winconn.run_cmd('net stop iphlpsvc')
    # return a
    conn = winrm.Protocol(
        endpoint=r'http://{}:5985/wsman'.format(ip), transport='plaintext', username=user_name, password=passwd)
    shell_id = conn.open_shell()
    com = conn.run_command(shell_id, cmd)
    stdout, stderr, return_code = conn.get_command_output(shell_id, com)
    conn.run_command(shell_id, 'net stop iphlpsvc')
    return stdout


def win_conn(ip, user_name, passwd, action_cmd, path='C'):
    """连接windows系统虚机，并执行终端命令，action_cmd是对终端的操作有lock锁屏，login登入，close关机等操作"""

    winconn = winrm.Session(r'http://{0}/wsman'.format(ip), auth=(user_name, passwd))
    time.sleep(1)
    r = winconn.run_cmd(r'echo {0}>{1}:\access.log'.format(action_cmd, path))
    print(r.std_out.decode())  # 打印获取到的信息
    print(r.std_err)  # 打印错误信息
    winconn.run_cmd('net stop iphlpsvc')


def terminal_conn(ip, command):
    """连接终端，并执行shell命令"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ip, username='root', password="fjrjroot_123")
        stdin, stdout, stderr = ssh.exec_command(command, get_pty=True)
        result = stdout.read()
        ssh.close()
        return result
    except Exception as error:
        logging.error(error)
        logging.info("终端连接不上请检查是否断网，或开启终端")


def server_sql_qurey(sshhost, sql, port=5433, qureresult=1, ssh_password=server_pwd):
    """连接postgresql数据库，并执行sql语句,1表示返回执行结果，0 表示不返回执行结果"""
    try:
        with SSHTunnelForwarder(
                (sshhost, 22),  # 指定ssh登录的跳转机的address
                ssh_username="root",  # 跳转机的用户
                ssh_password=ssh_password,  # 跳转机的密码
                remote_bind_address=('127.0.0.1', port)  # 远程绑定的端口
        ) as server:
            server.start()
            if server.is_active:
                print("active")
            else:
                print("NOT active")
            if server.is_alive:
                print("alive")
            else:
                print("NOT alive")
            print 'Server connected via SSH'
            local_port = str(server.local_bind_port)
            engine = create_engine("postgresql://postgres:rcd3000@localhost:" + local_port + "/rcd", max_overflow=-1)
            Session = sessionmaker(bind=engine)
            session = Session()
            if qureresult == 0:
                session.execute(sql)
                session.commit()
                session.close()
            else:
                result = session.execute(sql)
                a = []
                for i in result:
                    a.append(i)
                session.close()
                return a
    except Exception, e:
        logging.error(e)
        logging.exception("数据库异常请检查")


def telnet_switchboard(tnip, agport, command):
    """连接交换机，开启或关闭ag口"""
    tn = telnetlib.Telnet(tnip, port=23, timeout=10)
    tn.read_until('Username:')
    tn.write('admin' + '\n')
    tn.read_until('Password:')
    tn.write('ruijie' + '\n')
    time.sleep(1)
    tn.write('en' + '\n')
    time.sleep(1)
    tn.write('ruijie' + '\n')
    time.sleep(1)
    tn.write('configure' + '\n')  # 输入命令
    time.sleep(1)
    tn.write('int ag {}'.format(agport) + "\n")
    time.sleep(1)
    tn.write(command + '\n')
    time.sleep(1)
    # result1 = tn.read_very_eager()  # 获得结果
    # print result1
    # 命令执行完毕后，终止Telnet连接（或输入exit退出）
    tn.close()  # tn.write('exit\n')


def ip_set(tnip, tname, tmac, tip, router='172.21.204.1', dns='192.168.58.110'):
    """在交换机上给终端分配固定ip
        :tnip 要配地址的交换机ip
        ：tname 终端名称
        ：tmac 终端mac
        ：tip 给终端分配的ip"""
    tn = telnetlib.Telnet(tnip, port=23, timeout=10)
    try:
        tn.read_until('Username:')
        tn.write('admin' + '\n')
    except Exception as u:
        logging.info("不用输入用户名{}".format(u))
        pass
    time.sleep(0.5)
    tn.read_until('Password:')
    tn.write('ruijie' + '\n')
    time.sleep(0.5)
    tn.write('en' + '\n')
    time.sleep(0.5)
    tn.write('ruijie' + '\n')
    time.sleep(0.5)
    tn.write('configure' + '\n')  # 输入命令
    time.sleep(0.5)
    commands = ['ip dhcp pool {}'.format(tname), 'hardware-address {}'.format(tmac), 'host {} 255.255.255.0'.format(tip)
        , 'default-router {}'.format(router), 'dns-server {}'.format(dns)]
    for command in commands:
        tn.write(command + "\n")
        time.sleep(0.5)
    # result1 = tn.read_very_eager()  # 获得结果
    # print result1
    # 命令执行完毕后，终止Telnet连接（或输入exit退出）
    tn.close()  # tn.write('exit\n')


def get_free_info(ip, command):
    """free命令获取服器的信息"""
    result = server_conn(ip, command)
    dict_01 = {}
    list_01 = result.splitlines()
    list_02 = list_01[1].split()
    dict_01["total"] = list_02[1]
    dict_01["used"] = list_02[2]
    dict_01["free"] = list_02[3]
    dict_01["buffers"] = list_02[5]
    dict_01["cached"] = list_02[6]
    return dict_01


def terminal_file_up(ip, local_path, remote_path, username="root", password="fjrjroot_123"):
    scp = paramiko.Transport(ip, 22)
    scp.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(scp)
    sftp.put(local_path, remote_path)


if __name__ == "__main__":
    pass
    win_conn('172.21.195.125',s_user,s_pwd,'x info')
    print get_win_conn_info('172.21.195.125',s_user,s_pwd,r'type C:\access.log')
    # print server_conn('172.21.195.78',"ls -l /opt/cache/cvm/|grep %s |awk '{print $5}'" %'PC_687')
    # print get_win_conn_info('172.21.195.125', s_user, s_pwd, r'net user Administrator /domain')
    # print get_win_conn_info('172.21.195.146',s_user,s_pwd,'wmic ntdomain get domainname,status /value')
    # info = get_win_conn_info(ip="172.21.3.43", user_name=s_user, passwd=s_pwd, cmd='ipconfig')
    # print server_sql_qurey('172.21.195.13',"SELECT  * from sct_user")
    # print get_win_conn_info('172.21.195.171',s_user,s_pwd,'net user Administrator /domain')
    # pass
