"""
给你两个整数，被除数 dividend 和除数 divisor。将两数相除，要求 不使用 乘法、除法和取余运算。
整数除法应该向零截断，也就是截去（truncate）其小数部分。例如，8.345 将被截断为 8 ，-2.7335 将被截断至 -2 。
返回被除数 dividend 除以除数 divisor 得到的 商 。
注意：假设我们的环境只能存储 32 位 有符号整数，其数值范围是 [−231,  231 − 1] 。
本题中，如果商 严格大于 231 − 1 ，则返回 231 − 1 ；如果商 严格小于 -231 ，则返回 -231 。
分析：
正负号可以通过异或知道
在计算机组成原理中说明了除法，乘法，减法其实都是用加法实现的；
从十进制中可知，除法就是减法，笨办法就是绝对值不断相减直至小于0;
递归思想：()
终止条件：|dividend|-|divisor|<0
减少规模：|dividend|-|divisor|...
缺点：(除数和被除数差距太大这样递归可能使递归层数很深)
改进：

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




if __name__ == '__main__':
    a = 2147483647 #负数在内存中补码表示，移位也是补码移位
    b = 2
    Solution().divide(a,b)
