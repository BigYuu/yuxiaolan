#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll && houjinqi
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/10/11 16:50
"""

# 内存异常-后台修改命令
edit_ram_command = u'cd /usr/bin;mv -n ipmitool ipmitool.back;echo -e \'#!/bin/bash\n\n/usr/bin/ipmitool.back $@\n\necho "ECC $(date)"\n\n\'>>ipmitool;chmod +x ipmitool'
# 内存-后台还原命令
# recover_ram_cpu_command = u'cd /usr/bin;mv ipmitool.back ipmitool'
# CPU异常-后台修改命令
edit_cpu_command = u'echo -e \'echo "Upper Non-critical going high  1234  $(date)"\'>>/usr/bin/ipmitool'
# 内存和CPU-后台还原命令
recover_ram_cpu_command = u'cd /usr/bin;mv ipmitool.back ipmitool'

# 镜像空间目录
lessons_doc = u'/opt/lessons'
# 系统空间目录
system_doc = u'/'

# 获取此服务器型号信息
host_info_command = u'ipmitool fru'

# 为了能够mount，往/etc/fstab添加空行
edit_fstab = u'echo \' \'>>/etc/fstab'
# RCD服务器ssd cache目录变为只读
ro_cache_rcd_command = u'mount -o remount,ro /opt/cache/'
# RCD服务器ssd cache目录恢复
recover_cache_rcd_command = u'mount -o remount,rw /opt/cache/'

# 共享目录变成只读
ro_share_rcd_command = u'mount -o remount,ro /opt/ftpshare/share/'
ro_share_rcm_command = u'umount /opt/ftpshare/share/,mount.ntfs -3g -o ro /opt/data/share.img /opt/ftpshare/share/'
# 共享目录恢复(rcm待验证)
recover_share_rcd_command = u'mount -o remount,rw /opt/ftpshare/share/'
revover_share_rcm_command = u'umount /opt/ftpshare/share/,mount.ntfs -3g -o rw /opt/data/share.img /opt/ftpshare/share/'

# 已连接网卡
eth_list = []
# 停止第三块网卡
down_eth2_command = u'ifdown eth2;ifdown eth3'
# 恢复第三块网卡
up_eth2_command = u'ifup eth2;ifup eth3'

# 修改网卡速度为100Mb/s
edit_netspeed_command = u'ethtool -s {} speed 100 duplex full'
# 恢复网卡速度为1000Mb/s
recover_netspeed_command = u'ethtool -s {} speed 1000 duplex full'

# 配置错误网关
# edit_gateway_command = u'echo \'NETWORKING=yes\nHOSTNAME=RCD.127.0.0.1\nGATEWAY=1.1.1.1\' >/etc/sysconfig/network'
# 恢复网关
# recover_gateway_command = u'echo \'NETWORKING=yes\nHOSTNAME=RCD.127.0.0.1\nGATEWAY=172.21.195.1\' >/etc/sysconfig/network'

# 破坏并恢复网关
gateway_command = u'echo \'NETWORKING=yes\nHOSTNAME=RCD.127.0.0.1\nGATEWAY=1.1.1.1\' >/etc/sysconfig/network;service network restart;sleep 50;echo \'NETWORKING=yes\nHOSTNAME=RCD.127.0.0.1\nGATEWAY=172.21.195.1\' >/etc/sysconfig/network;service network restart;sleep 600;/usr/lib/python2.6/site-packages/rccsystem/rccsystem-remote -h 127.0.0.1:9093 reboot_system'

# # 修改虚拟服务器172.21.195.204业务网为当前服务器业务ip
# edit_wan0_command = u'sed -i \'s/10.14.194.205/10.14.194.{0}/\' /etc/keepalived/keepalived.conf&&sed -i \'s/10.14.194.205/10.14.194.{0}/\' /etc/rcd_ha/rcd_ha.conf'
# # 恢复虚拟服务器172.21.195.204业务网
# recover_wan0_command = u'sed -i \'s/10.14.194.{0}/10.14.194.205/\' /etc/keepalived/keepalived.conf&&sed -i \'s/10.14.194.{0}/10.14.194.205/\' /etc/rcd_ha/rcd_ha.conf'

# 修改虚拟服务器172.21.195.216存储网为当前服务器存储ip
edit_bond1_command = u'sed -i \'s/10.14.195.216/10.14.195.{0}/\' /etc/sysconfig/network-scripts/ifcfg-bond1'
# 恢复虚拟服务器172.21.195.216存储网
recover_bond1_command = u'sed -i \'s/10.14.195.{0}/10.14.195.216/\' /etc/sysconfig/network-scripts/ifcfg-bond1'
# 重启network服务
restart_network = u'service network restart'
