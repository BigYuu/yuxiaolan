#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import traceback
import tempfile
import time


class MyOs:
    obj = subprocess.Popen

    def __init__(self):
        pass

    def process(self, cmd):
        """
            执行CMD指令，返回相应的执行结果。阻塞函数，无法执行如logcat或top等指令
            :type cmd:str 指令名称
            :rtype: list
        """
        result = self.execute(cmd)
        return self.parseResult(result)

    def cmdParse(self, cmd):
        """
            解析指令列表，如['adb','devices','-l']，解析成'adb devices -l'
            :type cmd:list 指令列表
            :rtype: str
        """
        data = ''
        if isinstance(cmd, str):  # 如果传入的为string类型，直接作为指令
            data = cmd
            return data
        for info in cmd:
            tmp = info + " "
            data += tmp
        return data

    def execute(self, cmd):
        try:
            out_temp = tempfile.SpooledTemporaryFile(bufsize=10 * 1024)
            fileNo = out_temp.fileno()
            self.obj = subprocess.Popen(cmd, stdout=fileNo, stderr=fileNo, shell=True)
            self.obj.wait()
            out_temp.seek(0)
            return out_temp.readlines()
        except Exception, e:
            print e
            print traceback.format_exc()

    def destroy(self):
        self.obj.terminate()

    def parseResult(self, result):
        resultList = []
        if result is None:
            return resultList
        for data in result:
            while True:
                if data == '':
                    break
                if data[-1] == '\r' or data[-1] == '\n':
                    data = data[0:-1]
                else:
                    resultList.append(data)
                    break
        return resultList

    def getCurrentTime(self, format="%Y-%m-%d %H:%M:%S"):
        return time.strftime(format, time.localtime(time.time()))


debug = MyOs()
if __name__ == '__main__':
    print debug.process("adb devices")
    # path = "E:\UmsAutoTest"+"\\"+"recordera"
    # myPath = os.getcwd()
    # logPath = myPath + "\\UmsAutoTestResult"
    # path = logPath + "\\recorder\\"
    # isTrue = os.path.exists(path)
    # if not isTrue:
    #     os.makedirs(path)
    # # while True:
    #     fileName = path + debug.getCurrentTime("%m%d%H%M%S") + ".png"
    #     print ">>>" + str(debug.process("adb shell screencap -p /sdcard/screen.png"))
    #     print ">>>" + str(debug.process("adb pull /sdcard/screen.png " + fileName))
    #     # sleep(0.5)
    # # print debug.process("adb shell top")
    # print '==========='
