# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: file_info_update
# Author: xiaxu
# DATA: 2023/10/7
# Description:配置更新
# --------------------------------------------------
from BjlxBS import observer
from BjlxBS.base.function import project_path
import os,time


class FileUpdate(observer.Subject):
    def __init__(self) -> None:
        super().__init__()
        self.frist_time = self.modify_time()  #修改时间
        self.mtime = 0  #获取的修改时间

    def modify_time(self):
        return os.stat('.\\cfg_data\\BjlxSet1.ini').st_mtime

    def isfile_update(self):
        self.mtime = self.modify_time()
        #文件修改过，通知观察者更新数据
        if  self.mtime-self.frist_time>0:
            self.frist_time = self.mtime #更新首次检测时间
            self.notify()
            return True
        else:return False

