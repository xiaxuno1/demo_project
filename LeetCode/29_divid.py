"""
给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。
整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。
返回被除数 dividend 除以除数 divisor 得到的 商 。
注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−231,  231 − 1] 。
本题中，如果商 严格大于 2^31 − 1 ，则返回 2^31 − 1 ；如果商 严格小于 -2^31 ，则返回 -2^31 。
分析：
正负号可以通过异或知道
在计算机组成原理中说明了除法，乘法，减法其实都是用加法实现的；
从十进制中可知，除法就是减法，笨办法就是绝对值不断相减直至小于0;
递归思想：()
终止条件：|dividend|-|divisor|<0
减少规模：|dividend|-|divisor|...
缺点：(除数和被除数差距太大这样递归可能使递归层数很深)
改进：最终的结果会落在【0，dividend】的某个子区间
    加大步伐设置一个接近序列：approach=divisor*1、divisor*2、divisor*4.....不断加大步伐缩小这个区间
    设置一个接近的上区间 start_interval：approach = start_interval+approach 从上区间开始继续缩小区间
    两个循环复杂度类似类似折半查找



"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        #终止条件
        if abs(divisor) ==1:  #被除为+-1的问题
            if abs(divisor+dividend) != abs(divisor)+abs(dividend):#判断商的正负 负数
                if -abs(dividend)<-2**31: #下溢出
                    return -2**31
                else:return -abs(dividend)
            if abs(divisor+dividend) == abs(divisor)+abs(dividend): #判断商的正负 正数
                if abs(dividend) > 2**31-1: #上溢出
                    return 2**31-1
                else:
                    return abs(dividend)
        if abs(dividend)-abs(divisor)<0 :
            return 0  #商0
        if abs(dividend)-abs(divisor)==0 and abs(divisor+dividend) != abs(divisor)+abs(dividend): #判断商的正负
            return -1  #商-1
        if abs(dividend)-abs(divisor)==0 and abs(divisor+dividend) == abs(divisor)+abs(dividend): #判断商的正负
            return 1  #商1
        #递归条件
        if abs(dividend)-abs(divisor) >0:
            if abs(divisor+dividend) != abs(divisor)+abs(dividend):#判断商的正负
                result = self.divide(dividend + divisor, divisor)  # 商为负数
                return result-1
            if abs(divisor+dividend) == abs(divisor)+abs(dividend): #判断商的正负
                result = self.divide(dividend - divisor, divisor)  # 返回商
                return result + 1

class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:
        if abs(divisor + dividend) != abs(divisor) + abs(dividend):  # 判断商的正负 负数
            is_positive = -1
        else:  # 判断商的正负 正数
            is_positive = 1
        if abs(divisor) ==1:  #被除为+-1的问题
            if is_positive == -1:#判断商的正负 负数
                if -abs(dividend)<-2**31: #下溢出
                    return -2**31
                else:return -abs(dividend)
            if is_positive == 1:  # 判断商的正负 正数
                if abs(dividend) > 2 ** 31 - 1:  # 上溢出
                    return 2 ** 31 - 1
                else:
                    return abs(dividend)
        dividend = abs(dividend)
        divisor = abs(divisor) #取绝对值
        start_interval = 0  #[24,48] 起始区间从0，开始
        quotient = 0 #商
        if dividend-divisor<0: #商0 2/3
            return quotient
        while start_interval+divisor <= dividend: #接近未完成
            result = 1
            approach = divisor  # 接近序列，按照幂升高
            while start_interval+approach < dividend:  # 找符合的区间左边界
                approach = approach << 1
                result = result << 1
            if result>1: #3/3 刚好为1的情况
                result = result>>1
            quotient = quotient+result
            approach = approach >> 1
            start_interval = start_interval + approach  # *2，左区间
        #确定商的正负
        if is_positive == -1:
            return -quotient
        return quotient


if __name__ == '__main__':
    a = 2147483647#负数在内存中补码表示，移位也是补码移位
    b = 2
    print(Solution1().divide(a, b))
