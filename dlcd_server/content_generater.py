# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: content_generater
# Author: xiaxu
# DATA: 2023/6/15
# Description:帧内容生成器
# ---------------------------------------------------
from dlcd_server.file_read_ini import INIOp
from dlcd_server.data_translate import deci_to_str


class ContenGenerater():
    def __init__(self,file_path = 'DlcdjcSet1.ini'):
        self.cfg = INIOp(file_path)

    def mnl_data(self, sub_type, sub_type_loc =1, section="模拟量配置", split_method = ","):
        """
        获取指定section的内容，按照 ，分割 去除空格
        获取的设定值默认为最后一列
        """
        content_strs=''
        start_loc = 0 #开始位置标记
        for content in self.cfg.get_section_content(section=section,split_method=split_method):
            if start_loc >0:
                if eval(content[sub_type_loc])==sub_type:
                    content_strs = content_strs+deci_to_str(int(eval(content[len(content)-1])*10),"<H",file_width=4)
            start_loc = start_loc+1
        if len(content_strs)==0:
            print('注意：类型 {0} 没有生成内容数据，section: {1}，位置 {2}'.format(sub_type,section,sub_type_loc))
        return content_strs


    def heart_beats(self):
        return 'FF'*7

    def alarm_content(self):
        total = eval(self.cfg.get('报警开关量配置','总数'))
        if total%8:
            nums = total//8+1
        else:
            nums = total//8
        return 'FF'*nums

    def status_data(self):
        total = eval(self.cfg.get('模块开关量配置', '总数'))
        return "01"*25

    def ld_curve(self):
        """雷电波形曲线信息"""

    def get_type(self):
        """获取每个类型的数量"""




if __name__ == '__main__':
    content = ContenGenerater()
    content.alarm_content()
    print(content.mnl_data(1))

