"""
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。
"""
class Solution(object):
    def romanToInt(self, s):
        """
        罗马数字换整数，循环，特殊处理
        :type s: str
        :rtype: int
        """
        num = 0
        roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,"S":0}  #S 为处理特殊情况，用来站位
        for i in range(len(s)):
            #需要特殊处理的数
            if s[i] == "I" and i != (len(s)-1): #非最后一位
                if s[i+1] == "V" or s[i+1] == "X":
                    num = num-roman_dict[s[i]]+roman_dict[s[i+1]]
                    s = s[:i+1]+"S"+s[i+2:]  #i+1替换为无效值
                else:
                    num = num + roman_dict[s[i]]
            elif s[i] == "X" and i != (len(s)-1):
                    if s[i+1] == "L" or s[i+1] == "C":
                        num = num - roman_dict[s[i]] + roman_dict[s[i + 1]]
                        s = s[:i + 1] + "S" + s[i + 2:]  # i+1替换为无效值
                    else:
                        num = num + roman_dict[s[i]]
            elif s[i] == "C" and i != (len(s)-1):
                    if s[i+1] == "D" or s[i+1] == "M":
                        num = num - roman_dict[s[i]] + roman_dict[s[i + 1]]
                        s = s[:i + 1] + "S" + s[i + 2:]  # i+1替换为无效值
                    else:
                        num = num + roman_dict[s[i]]
            else:
                num = num +roman_dict[s[i]]
        return num



if __name__ == '__main__':
    s = "III"
    print(Solution().romanToInt(s))