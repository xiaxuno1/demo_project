"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
思路：
次问题可以看做是顺序问题，
采用栈的方式解决；顺序将左部分入栈，遇到右边部分即出栈
这里用list实现栈
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        buckets_key = {")":"(","}":"{","]":"["}
        statck_list = [] #栈
        for i in s:
            if i in ("(","{","["): #左括号
                statck_list.append(i) #入栈
            else:
                if len(statck_list)==0 or buckets_key[i] != statck_list.pop():  #出栈
                    return False
        #为真的条件；遍历完成，栈内无元素
        if len(statck_list) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s="]"
    print(Solution().isValid(s))


