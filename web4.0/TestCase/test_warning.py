#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author: chengll && houjinqi
@contact: chengll@ruijie.com
@software: PyCharm
@time: 2018/10/11 16:50
"""
import pytest, re
from Common.serverconn import *
from TestData.Logindata import *
from WebPages.warningpage import *


class Test_Warning:

    # @pytest.mark.warning
    # def test_ram_warning(self, com_fixture):
    #     logging.info("----------------------------------告警管理A1.1 内存ECC告警开始执行-----------------------------")
    #     try:
    #         server_conn(mainip, edit_ram_command)
    #         p = WarningPage(com_fixture)
    #         logging.info('判断内存ECC告警与实际相符')
    #         final = p.get_warning_is_show(p.warning_ram_xpath.format(mainip))
    #         assert final == 1
    #         logging.info("----------------------------------测试用例结束------------------------------")
    #     except Exception as e:
    #         logging.info("用例执行异常，原因是：" + e)
    #     finally:
    #         server_conn(mainip, recover_ram_cpu_command)
    #         time.sleep(6)
    #
    # @pytest.mark.warning
    # def test_cpu_warning(self, com_fixture):
    #     logging.info("-------------------------------告警管理A1.2 CPU配置异常告警开始执行---------------------------")
    #     try:
    #         server_conn(mainip, edit_ram_command)
    #         server_conn(mainip, edit_cpu_command)
    #         p = WarningPage(com_fixture)
    #         logging.info('判断CPU异常告警与实际相符')
    #         final = p.get_warning_is_show(p.warning_cpu_xpath.format(mainip))
    #         assert final == 1
    #         logging.info("----------------------------------测试用例结束------------------------------")
    #     except Exception as e:
    #         logging.info("用例执行异常，原因是：" + e)
    #     finally:
    #         server_conn(mainip, recover_ram_cpu_command)
    #         time.sleep(6)

    @pytest.mark.warning
    def test_lessons_space(self, com_fixture):
        logging.info("-------------------------------告警管理A1.3 镜像空间使用告警开始执行---------------------------")
        try:
            doc_falloc(mainip, lessons_doc)
            p = WarningPage(com_fixture)
            logging.info('判断镜像空间使用异常告警与实际相符')
            final = p.get_warning_is_show(p.warning_lessons_xpath.format(mainip))
            assert final == 1
            logging.info("----------------------------------测试用例结束------------------------------")
        except Exception as e:
            logging.info("用例执行异常，原因是：" + e)
        finally:
            doc_free(mainip, lessons_doc)
            time.sleep(6)

    @pytest.mark.warning
    def test_system_space(self, com_fixture):
        logging.info("------------------------------告警管理A1.4 系统空间使用告警开始执行----------------------------")
        try:
            doc_falloc(mainip, system_doc)
            p = WarningPage(com_fixture)
            logging.info('判断系统空间使用异常告警与实际相符')
            final = p.get_warning_is_show(p.warning_system_xpath.format(mainip))
            assert final == 1
            logging.info("----------------------------------测试用例结束------------------------------")
        except Exception as e:
            logging.info("用例执行异常，原因是：" + e)
        finally:
            doc_free(mainip, system_doc)
            time.sleep(6)

    # @pytest.mark.warning
    # def test_cache_readonly(self, com_fixture):
    #     logging.info("--------------------------告警管理A1.5 ssd cache目录变为只读告警开始执行------------------------")
    #     server_kind = host_info(mainip)
    #     if server_kind == 'RCD':
    #         try:
    #             server_conn(mainip, edit_fstab)
    #             server_conn(mainip, ro_cache_rcd_command)
    #             p = WarningPage(com_fixture)
    #             logging.info('判断cache目录变为只读告警与实际相符')
    #             final = p.get_warning_is_show(p.warning_cache_xpath.format(mainip))
    #             assert final == 1
    #             logging.info("----------------------------------测试用例结束------------------------------")
    #         except Exception as e:
    #             logging.info("用例执行异常，原因是：" + e)
    #         finally:
    #             server_conn(mainip, recover_cache_rcd_command)
    #             time.sleep(6)
    #     else:
    #         logging.info('非RCD不需要测试本用例')
    #         assert True

    # @pytest.mark.warning
    # def test_share_readonly(self, com_fixture):
    #     logging.info("--------------------------告警管理A1.6 共享目录变成只读告警开始执行-----------------------")
    #     server_kind = host_info(mainip)
    #     try:
    #         if server_kind == 'RCD':
    #             server_conn(mainip, ro_share_rcd_command)
    #         elif server_kind == 'RCM':
    #             server_conn(mainip, ro_share_rcm_command)
    #         else:
    #             logging.info('此类型服务器无需测试')
    #             assert True
    #         p = WarningPage(com_fixture)
    #         logging.info('判断共享目录变为只读告警与实际相符')
    #         final = p.get_warning_is_show(p.warning_share_xpath.format(mainip))
    #         assert final == 1
    #         logging.info("----------------------------------测试用例结束------------------------------")
    #     except Exception as e:
    #         logging.info("用例执行异常，原因是：" + e)
    #     finally:
    #         if server_kind == 'RCD':
    #             server_conn(mainip, recover_share_rcd_command)
    #         elif server_kind == 'RCM':
    #             server_conn(mainip, revover_share_rcm_command)
    #         else:
    #             pass
    #         time.sleep(6)

    @pytest.mark.warning
    def test_eth_disconn(self, com_fixture):
        logging.info("--------------------------------告警管理A1.7 网卡未连接告警开始执行----------------------------")
        if host_info(mainip) == 'RCD':
            try:
                p = WarningPage(com_fixture)
                logging.info('判断网卡未连接告警与实际相符')
                server_conn(mainip, down_eth2_command)
                time.sleep(600)
                p.goto_warning_page()
                p.goto_warning_iframe()
                assert p.get_warning_info(p.warning_eth_xpath.format(mainip))
                logging.info("----------------------------------测试用例结束------------------------------")
            except Exception as e:
                logging.info("用例执行异常，原因是：" + e)
            finally:
                server_conn(mainip, up_eth2_command)
                time.sleep(600)
        else:
            logging.info('无法判断服务器类型，用例跳过')
            assert True


    # @pytest.mark.warning
    # def test_network_speed(self, com_fixture):
    #     logging.info("----------------------------告警管理A1.8 网卡速度变为百兆告警开始执行--------------------------")
    #     try:
    #         netspeed_edit(mainip)
    #         time.sleep(600)
    #         p = WarningPage(com_fixture)
    #         p.goto_warning_page()
    #         p.goto_warning_iframe()
    #         eth_check(mainip)
    #         logging.info('判断网卡速度告警与实际相符')
    #         eth = str(int(eth_list[0].split('eth')[1]) + 1)
    #         assert p.get_warning_info(p.warning_netspeed_xpath.format(mainip, eth, eth_list[0]), wait_times=5)
    #         logging.info("----------------------------------测试用例结束------------------------------")
    #     except Exception as e:
    #         logging.info("用例执行异常，原因是：" + e)
    #     finally:
    #         netspeed_recover(mainip)
    #         time.sleep(600)

    @pytest.mark.warning
    def test_gateway_error(self, com_fixture):
        logging.info("----------------------------告警管理A1.10 业务网关不可达告警开始执行----------------------------")
        try:
            server_conn(mainip, gateway_command)
            time.sleep(800)
            p = WarningPage(com_fixture)
            p.login_again()
            p.goto_warning_page()
            p.goto_warning_iframe()
            logging.info('判断业务网关不可达告警与实际相符')
            assert p.get_warning_info(p.warning_gateway_xpath.format(mainip))
            logging.info("----------------------------------测试用例结束------------------------------")
        except Exception as e:
            logging.info("用例执行异常，原因是：" + e)
        finally:
            pass

    # @pytest.mark.warning
    # def test_wan1_conflict(self, com_fixture):
    #     logging.info("------------------------------告警管理A1.12 存储网络冲突告警开始执行----------------------------")
    #     try:
    #         server_conn('172.21.195.216', edit_bond1_command.format(int(mainip.split('.')[3]) + 1))
    #         server_conn('172.21.195.216', restart_network)
    #         time.sleep(600)
    #         p = WarningPage(com_fixture)
    #         p.goto_warning_page()
    #         p.goto_warning_iframe()
    #         logging.info('判断业务网关不可达告警与实际相符')
    #         assert p.get_warning_info(p.warning_storageip_xpath.format(mainip, mainip.split('.')[3], wait_times=5))
    #         logging.info("----------------------------------测试用例结束------------------------------")
    #     except Exception as e:
    #         logging.info("用例执行异常，原因是：" + e)
    #     finally:
    #         server_conn('172.21.195.216', recover_bond1_command.format(mainip.split('.')[3]))
    #         server_conn('172.21.195.216', restart_network)
    #         time.sleep(600)

    @pytest.mark.warning
    @pytest.mark.case_level_1
    @pytest.mark.smoke_test
    @pytest.mark.case_type_fun
    def test_shaopan(self):
        logging.info("-----------------测试用例--------------------")
        assert 1 == 1
    logging.info("-----------------用例结束--------------------")


if __name__ == '__main__':

    pytest.main(["-k", "test_gateway_error"])
