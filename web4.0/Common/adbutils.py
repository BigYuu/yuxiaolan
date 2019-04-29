#! /usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import tempfile
import thread
import threading
import time

_q = threading.RLock()


class AdbUtils:
    def __init__(self):
        self.obj = None
        self.flag = False
        self.result = None

    def __thread_command_process(self, command, aaa):
        self.flag = False
        out_temp = tempfile.SpooledTemporaryFile(bufsize=10 * 1024)
        file_no = out_temp.fileno()
        self.obj = subprocess.Popen(command, stdout=file_no, stderr=file_no)
        # print self.obj.pid
        self.obj.wait()
        out_temp.seek(0)
        _q.acquire()
        self.flag = True
        self.result = out_temp.readlines()
        _q.release()

    def command_process(self, command, timeout):
        begin = time.time()
        self.flag = False
        thread.start_new_thread(self.__thread_command_process, (command, ""))
        while True:
            _q.acquire()
            tmp = self.flag
            _q.release()
            if tmp:
                self.obj.terminate()
                return self.result
            else:
                if time.time() - begin >= timeout / 1000.0:
                    if self.obj is not None:
                        self.obj.terminate()
                    return None
                else:
                    time.sleep(0.01)
