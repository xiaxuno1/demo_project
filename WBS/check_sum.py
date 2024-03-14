"""
校验和:求校验和
"""
import struct,base64

class CheckSum:
    def check_sum(self,str_hex,start,end):
        check_sum = 0
        bytest_hex = bytes.fromhex(str_hex) #str -bytes
        for index,one_hex in enumerate(bytest_hex):
            if index>=start and index<=end:
                check_sum = check_sum+one_hex
        return check_sum


if __name__ == '__main__':
    str1 = "7F 7F 01 00 0F 03 15 01 00 01 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 " \
           "00 00 00 00 00 00 00 00 00 00 00 00 00 00 2B 00 F7 F7"
    check_sum = CheckSum().check_sum(str1, 2, 49)
    print(base64.b16encode(struct.pack("<H",check_sum)))

