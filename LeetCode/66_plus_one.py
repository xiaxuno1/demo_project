"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
分析：
先组成整数，+1得最终整数，转为字符串迭代，放入digits
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for i in digits:#组成字符串表示的整数
            num = num+str(i)
        plus_one_num = str(int(num)+1) #+1
        for i in range(len(plus_one_num)):
            #位数超出，添加到后面
            if i < len(num):
                digits[i] = int(plus_one_num[i])
            else:digits.append(int(plus_one_num[i]))
        return digits

if __name__ == '__main__':
    digits =[1,2,3]
    print(Solution().plusOne(digits))