# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: dlcd_main
# Author: xiaxu
# DATA: 2023/6/15
# Description:
# ---------------------------------------------------
import base64
from dlcd_server.crc16 import crc_16
from dlcd_server.data_translate import deci_to_str
from dlcd_server.dlcd_implement import DLCD


def pkg(frame_sub_type,generate_name,frame_type = '20',frame_sub_type_total = 1):
    dlcd = DLCD(frame_type=frame_type)
    sub_type = dlcd.sub_type(type = frame_sub_type)
    if frame_sub_type_total>1:
        content = dlcd.content(generater_name='mnl_data', mnl_sub_type=int(sub_type))
    else:
        content = dlcd.content(generater_name=generate_name)
    time_str = dlcd.time_str()
    length = dlcd.frame_content_lenth(content=content)
    crc_data  = dlcd.vesion+dlcd.data_version+dlcd.frame_type+sub_type+time_str+length+content
    crc_data = base64.b16encode(bytes.fromhex(crc_data)).decode()
    crc = crc_16(" ".join([crc_data[i:i+2] for i in range(0,len(crc_data)//2)]))
    crc = deci_to_str(crc,'<H',4)
    pkg = dlcd.pkg(sub_type,time_str,length,content,crc)
    print(pkg)
    return pkg


if __name__ == '__main__':
    heart_beat = pkg(frame_type='0f',frame_sub_type='OTHERS',generate_name='heart_beats')
    alarm_info =  pkg(frame_type='11',frame_sub_type='OTHERS',generate_name='alarm_content')
    stat_data =  pkg(frame_type='10',frame_sub_type='OTHERS',generate_name='status_data')
    #类型中文前四位大写缩写
    dlgp_mnl = pkg(frame_type='20',frame_sub_type='DLGP',generate_name='mnl_data',frame_sub_type_total=6)
    dlwd_mnl = pkg(frame_type='20',frame_sub_type='DLWD',generate_name='mnl_data',frame_sub_type_total=6)
    hjxx_mnl = pkg(frame_type='20',frame_sub_type='HJXX',generate_name='mnl_data',frame_sub_type_total=6)
    ldsj_mnl = pkg(frame_type='20',frame_sub_type='LDSJ',generate_name='mnl_data',frame_sub_type_total=6)
    hwwd_mnl = pkg(frame_type='20',frame_sub_type='HWWD',generate_name='mnl_data',frame_sub_type_total=6)

