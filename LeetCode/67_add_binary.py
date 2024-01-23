"""
给你两个二进制字符串 a 和 b ，以二进制字符串的形式返回它们的和。
分析：
按照1位加法器设置求和；
一位求和位0、1
设置一个进位标志：carry_bit
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry_bit = "0" #进位标志，在一位求和中使用
        result = "" #存放结果
        #一位求和，从后往前
        for i in range(max(len(a),len(b))):
            #位数不一致超出索引,"0填充"
            if i>=len(a):
                temp = "0"+b[-i-1]+carry_bit
            elif i>=len(b):
                temp = a[-i-1]+"0"+carry_bit
            else:temp = a[-i-1]+b[-i-1]+carry_bit
            #查看有多少个“0”,以此确定结果位和进位
            temp_count = temp.count("1") #三位相加，1的个数
            if temp_count ==0:
                result = "0"+result
                carry_bit = "0"
            elif temp_count == 1:
                result = "1"+result
                carry_bit = "0"
            elif temp_count == 2:
                result = "0"+result
                carry_bit = "1"
            elif temp_count == 3:
                result = "1"+result
                carry_bit = "1"
        #最后的进位
        if carry_bit == "1":
            result = carry_bit+result
        return result


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    print(Solution().addBinary(a, b))
