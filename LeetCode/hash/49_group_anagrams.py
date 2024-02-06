"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词(单词相同，顺序不同如：tan nat)。
分析：
单词具有相同的字母，组成不同的字符；就是说，对于一个或多个单词，其字母相同，但是字母的排列顺序不同
要求输入分类，实际上就相当于hash，将含有相同字母的存为一起：{“aet”:[1,2,3],"tan":[4,7]}
如何做到：遍历，如何判断tea,应该放入：eat的hash_table中？ 对每个字符排序即可形成相同的key
时间：O(n),空间：最坏：O(n)

"""
import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list) #value为list
        #实现一个键对应多个值的字典,defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要关注添加元素操作了
        #defaultdict 会自动为将要访问的键（就算目前字典中并不存在这样的键）创建映射实体,
        # 不需要这样的特性，你可以在一个普通的字典上使用 setdefault() 方法来代替
        for str in strs:
            key = "".join(sorted(str)) #排序后作为key
            mp[key].append(str)
        return list(mp.values())









if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(sorted(strs[1]))
    print(Solution().groupAnagrams(strs))
