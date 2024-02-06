"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
分析：
子串一定是一个连续的区间，因此用滑动窗口
设置一个窗口，用于存放满足条件的内容，记录最长长度，同时这个窗口需要入不重复的值，因此用set()
设置两个指针，来指向这个子串的左右，一次枚举子串的起始位置（k）

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0  #窗口滑动的时候移出左边的元素
        lookup = set() #滑动窗口
        n = len(s)
        max_len = 0
        cur_len = 0  #当前窗口的长度
        for i in range(n): #枚举，以这个指针为起始的最长子串
            while s[i] in lookup: #检查到重复时，将左指针前移一格，滑窗长度-1
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            cur_len += 1 #当前窗口长度+1
            lookup.add(s[i]) #新元素添加到滑窗
            if cur_len > max_len: max_len = cur_len #比较最大长度
        return max_len


if __name__ == '__main__':
    s = "abcabcbb" #abc
    s2 = "abcdebcdedd" #abcde
    s3 ="aaaabcdebbbbedc"#abcdeb
    s4 = "mdcbdenmlkjihgfennnn"#efghijeklmn
    print(Solution().lengthOfLongestSubstring(s4))