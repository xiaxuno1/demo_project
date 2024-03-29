"""
帧格式的解析
"""
import struct
from collections import defaultdict


class QJKFrame:
    """
    解析QJK的帧内容，以字典格式返回
    """
    def deal_frame_struct(self,frame):
        """
        解析帧结构
        :param frame:一帧 bytes格式
        :return: set:{}
        """
        index = 0 #字节指针
        frame_set = {} #字典形式
        frame_set["head"] = frame[0:index+4]
        index =+4
        frame_set["interface_version"] = frame[index:index+1]
        index =index+1
        frame_set["data_version"] = frame[index:index+1]
        index = index+1
        frame_set["main_type"] = frame[index:index+1]
        index = index+1
        frame_set["time"] = frame[index:index+4]
        index = index+4
        frame_set["content_length"] = frame[index:index+2]
        content_length = struct.unpack("<h",frame[index:index+2])[0] #内容长度解析为十进制长度
        index = index+2
        frame_set["frame_content"] = frame[index:index+content_length]
        index = index+content_length
        frame_set["crc"] = frame[index:index+2]
        index = index+2
        frame_set["tail"] = frame[index:index+4]
        return frame_set

    #解析帧内容格式
    def deal_frame_content_struct(self,content):
        """
        解析帧内容格式,帧内容由三部分重复组成[子类型i,子类型数据长度，子类型数据]...
        :param content:帧内容content,byte格式
        :return:{sub_type:[data1,data2]}  可能存在I系II系 采用multidict,值使用list保持顺序以区分
        """
        content_dict = defaultdict(list)
        index = 0 #指针
        #过滤掉心跳帧
        if b'\xff'*7 in content:
            return {}
        while index < len(content)-1:
            subtype = content[index]
            index = index+1
            subtype_length = struct.unpack("<h",content[index:index+2])[0]
            index = index+2
            subtype_data = content[index:index+subtype_length]
            index = index+subtype_length
            content_dict[subtype].append(subtype_data)
        return content_dict

    #解析硬件平台设备状态信息
    def deal_hardware_platform_info(self,info :bytes):
        """
        解析硬件平台设备状态信息
        :param info:
        :return:defultdict(list)
        """
        info_dict = defaultdict(list)
        index = 0
        info_dict["line_mark"].append(info[index])
        index = index+1
        info_dict["main_line_mark"].append(info[index])
        index = index+1
        equipments_total = info[index]
        info_dict["equipments_taotal"].append(info[index])
        index = index+1
        for i in range(equipments_total):
            equipment_num = info[index]
            index = index+1
            equipment_total = info[index]
            index = index +1
            status_bytes = abs((-equipment_total)//4) #状态字节
            equipment_status = info[index:index+status_bytes]
            index = index+status_bytes
            info_dict[equipment_num].append(equipment_total) #{编号：[数量，状态]}
            info_dict[equipment_num].append(equipment_status)
        return info_dict

    #解析主控单元工作状态
    def deal_MCU_status(self,info):
        """
        主控单元工作状态，
        :param info:
        :return:
        """
        info_dict = defaultdict(list)
        index = 0
        info_dict["equipment_type_total"].append(info[index])
        index = index+1
        equipment_type_num=info[index]
        index = index+1
        equipments_total = info[index]
        info_dict[equipment_type_num].append(info[index])
        index = index+1
        status_bytes = abs((-equipments_total) // 4)  # 状态字节
        equipment_status = info[index:index + status_bytes]
        info_dict[equipment_type_num].append(equipment_status) # {类型：[数量，数据]}
        return info_dict

    #解析继电器状态
    def deal_ralay_status(self,info):
        """
        继电器状态，每个类型存储 key-value形式
        :param info:
        :return:
        """
        info_dict = defaultdict(list)
        index = 0
        info_dict["equipment_type_total"].append(info[index]) #设备类型数量
        equipment_type_total = info[index]
        index = index+1
        for i in range(equipment_type_total):
            equipment_type_num = info[index] #设备类型
            index = index+1
            equipments_total = info[index]
            info_dict[equipment_type_num].append(info[index])
            index = index+1
            status_bytes = abs((-equipments_total) // 8)  # 状态字节
            equipment_status = info[index:index + status_bytes]
            info_dict[equipment_type_num].append(equipment_status)  # {类型：[数量，数据]}
        return info_dict

    #解析区间线路信息
    def deal_section_line_info(self,info):
        """
        继电器状态，每个类型存储 key-value形式
        :param info:
        :return:
        """
        info_dict = defaultdict(list)
        index = 0
        info_dict["equipment_type_total"].append(info[index]) #设备类型数量
        equipment_type_total = info[index]
        index = index+1
        for i in range(equipment_type_total):
            equipment_type_num = info[index] #设备类型
            index = index+1
            equipments_total = info[index]
            info_dict[equipment_type_num].append(info[index])
            index = index+1
            status_bytes = equipments_total  # 状态字节
            equipment_status = info[index:index + status_bytes]
            info_dict[equipment_type_num].append(equipment_status)  # {类型：[数量，数据]}
        return info_dict

    #解析区段逻辑状态
    def deal_section_logic_status(self,info):
        """
        区段逻辑状态，每个类型存储 key-value形式
        :param info:
        :return:
        """
        if len(info) == 0:
            return {}
        info_dict = defaultdict(list)
        index = 0
        info_dict["equipment_type_total"].append(info[index]) #设备类型数量
        equipment_type_total = info[index]
        index = index+1
        info_dict["section_logic"].append(equipment_type_total) #设备类型数量
        status_bytes = equipment_type_total  # 状态字节
        equipment_status = info[index:index + status_bytes]
        info_dict["section_logic"].append(equipment_status)  # {类型：[数量，数据]}
        return info_dict

    #解析 解锁盘 按钮和等状态
    def deal_button_status(self,info):
        """
        继电器状态，每个类型存储 key-value形式
        :param info:
        :return:
        """
        info_dict = defaultdict(list)
        index = 0
        info_dict["equipment_type_total"].append(info[index]) #设备类型数量
        equipment_type_total = info[index]
        index = index+1
        for i in range(equipment_type_total):
            equipment_type_num = info[index] #设备类型
            index = index+1
            equipment_total = info[index]
            info_dict[equipment_type_num].append(info[index])
            index = index+1
            status_bytes = abs((-equipment_total)//4)  # 状态字节
            equipment_status = info[index:index + status_bytes]
            info_dict[equipment_type_num].append(equipment_status)  # {类型：[数量，数据]}
        return info_dict

    #解析 SA
    def deal_SA_status(self,info):
        if len(info) == 0:
            return {}
        info_dict = defaultdict(list)
        index = 0
        info_dict["equipment_type_total"].append(info[index]) #设备类型数量
        equipment_type_total = info[index]
        index = index+1
        for i in range(equipment_type_total):
            info_dict[i].append(info[index])  # 设备类型数量

    #解析 报警信息
    def deal_alarm_info(self,info):
        if len(info) == 0:
            return {}
        info_dict = defaultdict(list)
        index = 0
        info_dict["alarms_total"].append(info[index]) #数量
        equipment_type_total = info[index]
        for i in range(equipment_type_total):
            info_dict[i].append(info[index])  # {i:[类型，序号，描述码]}
            info_dict[i].append(info[index+1])  # {i:[类型，序号，描述码]}
            info_dict[i].append(info[index+2])  # {i:[类型，序号，描述码]}
            index = index+3
        return info_dict



if __name__ == '__main__':
    #frame = "EF EF EF EF 10 10 8C C5 20 FD 65 5D 00 50 12 00 AA AA 05 01 03 3F 02 03 3F 03 02 0F 04 04 3C 05 02 0F 50 12 00 55 55 05 01 03 3F 02 03 3F 03 02 0F 04 04 3C 05 02 0F 27 04 00 01 01 03 3F 28 17 00 02 01 60 42 58 00 00 45 E0 00 00 E0 01 A0 03 02 30 82 00 45 00 1F 07 29 05 00 01 01 02 15 1A 37 00 00 38 01 00 00 36 00 00 1E 58 FE FE FE FE EF EF EF EF 10 10 82 C5 20 FD 65 04 00 00 01 00 00 7A 67 FE FE FE FE"
    frame = "EF EF EF EF 10 10 82 55 73 03 66 07 00 00 04 00 01 01 01 01 75 D4 FE FE FE FE"
    QJK = QJKFrame()
    content = QJK.deal_frame_struct(bytes.fromhex(frame))["frame_content"]
    print(content)
    print(QJK.deal_frame_struct(bytes.fromhex(frame)))
    """
    #状态信息
    content_dict = QJK.deal_frame_content_struct(content)
    print(content_dict)
    hardware_platform_info = QJK.deal_hardware_platform_info(content_dict[80][0])
    MCU_status = QJK.deal_MCU_status(content_dict[39][0])
    print(MCU_status)
    relay_status = QJK.deal_ralay_status(content_dict[40][0])
    print(relay_status)
    section_line_info = QJK.deal_ralay_status(content_dict[41][0])
    print(section_line_info)
    section_logic_status = QJK.deal_section_logic_status(content_dict[55][0])
    print(section_logic_status)
    sa_status = QJK.deal_SA_status(content_dict[54][0])
    print(sa_status)
    """
    #报警信息
    content_dict = QJK.deal_frame_content_struct(content)
    alarm_info = QJK.deal_alarm_info(content_dict[0][0]) #子类型为0中第一组数据
    print(alarm_info)