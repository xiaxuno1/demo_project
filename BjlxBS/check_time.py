# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: check_time
# Author: xiaxu
# DATA: 2023/10/10
# Description:校时
# ---------------------------------------------------
from BjlxBS.bjlx import BJLX

class Timming(BJLX):
    def __init__(self):
        super().__init__()
        self.set_func_code('46')
        self._data = b''
        self.set_len()
        self.set_bcc_code()