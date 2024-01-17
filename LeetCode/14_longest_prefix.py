"""
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
提示：
1 <= strs.length <= 200
0 <= strs[i].length <= 200
["","a"]
strs[i] 仅由小写英文字母组成
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        pre_fix = "" #最长前缀
        if len(strs[0]) == 0:
            return ""
        # if len(strs) ==1: #列表中只有一个元素
        #     return strs[0]
        for str in strs[0]:
            pre_fix = pre_fix+str
            for s in strs:
                if s.startswith(pre_fix): #匹配上了
                    continue
                else:
                    return pre_fix[:-1]
        return pre_fix   #完全匹配


if __name__ == '__main__':
    strs =["flower", "flower", "flower", "flower"]
    print(Solution().longestCommonPrefix(strs))
