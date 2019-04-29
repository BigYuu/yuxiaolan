# coding=utf-8
import re

from Common.adbutils import AdbUtils
from Common.myos import MyOs

ADB_CMD = "adb"


def get_element_point(element_id):
    """
    获取控件的坐标。
    通过uiautomator将界面布局dump，解析布局xml，获取到控件坐标
    :param element_id: 控件ID
    :return:返回控件的坐标(x,y).获取不到时，返回None
    """
    dump_result = dump_current_page()  # dump 当前界面
    dump_file_name = "dump.xml"
    if dump_result:
        print("get_element_point from " + str(dump_file_name))
        result = get_element_rect(dump_file_name, element_id)  # 获取控件的坐标矩阵
        if result is not None:
            x = result[0] + (result[2] - result[0]) / 2
            y = result[1] + (result[3] - result[1]) / 2
            return x, y
    return None


def get_element_point_by_msg(msg):
    """
    获取控件的坐标。
    通过uiautomator将界面布局dump，解析布局xml，获取到控件坐标
    :param msg: 控件显示内容
    :return:返回控件的坐标(x,y).获取不到时，返回None
    """
    dump_result = dump_current_page()  # dump 当前界面
    dump_file_name = "dump.xml"
    if dump_result:
        print("get_element_point from " + str(dump_file_name))
        result = get_element_rect_by_msg_(dump_file_name, msg)  # 获取控件的坐标矩阵
        if result is not None:
            x = result[0] + (result[2] - result[0]) / 2
            y = result[1] + (result[3] - result[1]) / 2
            return x, y
    return None


def get_element_msg(element_id):
    dump_result = dump_current_page()  # dump 当前界面
    dump_file_name = "dump.xml"
    if dump_result:
        print("get_element_msg from " + str(dump_file_name))
        return get_element_msg_(dump_file_name, element_id)  # 获取控件的坐标矩阵
    return None


def dump_current_page():
    """
    通过uiautomator将当前界面布局dump，并将dump出的布局文件导出到PC
    :return: dump出数据，并导出到PC时返回成功，其它返回失败
    """
    my_os = MyOs()
    result = my_os.process(ADB_CMD + " shell uiautomator dump /sdcard/dump.xml")  # 使用uiautomator dump当前布局
    print("uiautomator dump result :" + str(result))
    if result[0] == "UI hierchary dumped to: /sdcard/dump.xml":
        result = my_os.process(ADB_CMD + " pull /sdcard/dump.xml dump.xml")  # 将布局文件从设备端导出到PC
        print("pull dump result :" + str(result))
        if str(result[0]).__contains__("[100%]") or str(result[0]).__contains__("KB/s"):
            return True
        for msg in result:
            if str(msg).__contains__("Ret=0"):
                return True
    return False


def get_element_rect(dump_file_name, element_id):
    """
    解析布局文件，获取控件ID的矩阵
    :param dump_file_name:
    :param element_id: 控件 ID
    :return: 返回控件矩阵，界面无此ID时，返回None.有多个ID时，返回第1个控件的矩阵
    """
    dump_file = open(dump_file_name)
    regex = "resource-id=\"" + element_id + "\" class=\"\w+(?:\.\w+){1,10}\" "  # 正则控件ID信息
    tmp_list = []
    ini_regex = re.compile(regex)
    while 1:
        line = dump_file.readline()
        if not line:
            break
        tmp_list = line.split(">")
    for tmp in tmp_list:
        result = ini_regex.search(tmp)
        if result is not None:
            regex = "bounds=\".+\""
            ini_regex = re.compile(regex)
            result = ini_regex.search(tmp)
            msg = result.group()
            react_str = msg[8:-1]
            react_str = str(react_str).replace("][", ",").replace("[", "").replace("]", "")
            react_list = react_str.split(",")
            return int(react_list[0]), int(react_list[1]), int(react_list[2]), int(react_list[3])
    return None


def get_element_rect_by_msg_(dump_file_name, msg):
    """
    解析布局文件，获取控件ID的矩阵
    :param msg:
    :param dump_file_name:
    :return: 返回控件矩阵，界面无此ID时，返回None.有多个ID时，返回第1个控件的矩阵
    """
    dump_file = open(dump_file_name)
    regex = "text=(?P<msg>\".*\") resource-id="  # 正则控件ID信息
    tmp_list = []
    ini_regex = re.compile(regex)
    while 1:
        line = dump_file.readline()
        if not line:
            break
        tmp_list = line.split(">")
    for tmp in tmp_list:
        result = ini_regex.search(tmp)
        if result is not None:
            if result.groupdict()["msg"][1:-1] == msg:
                regex = "bounds=\".+\""
                ini_regex = re.compile(regex)
                result = ini_regex.search(tmp)
                msg = result.group()
                react_str = msg[8:-1]
                react_str = str(react_str).replace("][", ",").replace("[", "").replace("]", "")
                react_list = react_str.split(",")
                return int(react_list[0]), int(react_list[1]), int(react_list[2]), int(react_list[3])
    return None


def get_element_msg_(dump_file_name, element_id):
    """
    解析布局文件，获取控件ID的矩阵
    :param dump_file_name:
    :param element_id: 控件 ID
    :return: 返回控件矩阵，界面无此ID时，返回None.有多个ID时，返回第1个控件的矩阵
    """
    dump_file = open(dump_file_name)
    regex = "text=(?P<msg>\".*\") resource-id=\"" + element_id + "\" class=\"\w+(?:\.\w+){1,10}\" "  # 正则控件ID信息
    tmp_list = []
    ini_regex = re.compile(regex)
    while 1:
        line = dump_file.readline()
        if not line:
            break
        tmp_list = line.split(">")
    for tmp in tmp_list:
        result = ini_regex.search(tmp)
        if result is not None:
            msg = result.groupdict()["msg"][1:-1]  # 去除两边的""符号
            print msg.decode("utf8").encode("gbk")
            return msg
    return None


def click(x, y):
    """
    点击指定座标
    :param x: x
    :param y: y
    """
    my_os = MyOs()
    my_os.process(ADB_CMD + " shell input tap " + str(x) + " " + str(y))


def get_current_component_info():
    """
    获取当前界面信息。返回当前界面的包名与activity名的元组
    :return: 返回当前界面的包名与activity名的元组
    """
    adb_utils = AdbUtils()
    data = None
    out = adb_utils.command_process("adb shell \"dumpsys window w | grep name=\"", 2000)
    if out is None:
        return None
    for line in out:
        package = re.search(r'\w+(?:\.\w+){1,10}/\.*\w+(?:\.\w+){0,10}', line)
        if package:
            data = package.group()
            if data == "com.android.systemui.ImageWallpaper":
                continue
            if data.__contains__("/"):  # 不包含/,如：pinpad界面时
                tmp = data.split("/")
                return tmp[0], tmp[1]
            else:
                return data, ""
        else:
            if not line.__contains__("/"):
                package = re.search(r'\w+(?:\.\w+){1,10}', line)
                if package:
                    data = package.group()
                    return data, ""
            # log("can not parse package info")
    return data


def get_current_activity():
    ret = get_current_component_info()
    if ret is not None:
        tmp = str(ret[1])
        if tmp != "":
            if str(ret[1]).startswith(str(ret[0])):
                tmp = str(ret[1]).replace(str(ret[0]), "")
            return tmp
        else:
            return ret[0]
    else:
        return None


if __name__ == '__main__':
    # print get_current_activity()
    print get_current_component_info()
    # x,y = get_element_point("com.ruijie.rccstu:id/btn_disconnect")
    # click(x,y)
