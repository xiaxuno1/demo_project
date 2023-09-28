# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: timing
# Author: xiaxu
# DATA: 2023/9/26
# Description:校时数据
# ---------------------------------------------------
from  BjlxBS.bjlx import BJLX
from BjlxBS.base.cfg_info import CFGInfo
import time,struct


class Timing(BJLX):
    def __init__(self):
        super().__init__()
        self._data = b''
        self.set_func_code('46')
        self.set_bcc_code()
        self.set_len()

