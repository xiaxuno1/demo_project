"""
给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
分析：
暴力：
直观的来说，对每个元素遍历，当前元素找，如果有重复继续，
需要两次循环
hash:{num:index}
一次循环，但是空间复杂的 O（n）

异或运算：
任何数与0异或得原数
任何数与1异或取反
任何数与自己异或得0；
a异或b异或a = a异或a异或b = b
因此全部异或就可以得不等得数


"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for target in nums:
            n = 1  # 记录某个元素出现的次数
            for num in nums:
                if target == num:
                    n = n+1
            if n == 2 : #没有重复的
                return target
        return None

    def single_number(self, nums: List[int]) -> int:
        for target in nums:
            #{num:index},遍历整个nums,在hash_table中查找是否存在key,如果存在删除此key-value,不存在，则添加
            hash_dict = dict()
            for i,num in enumerate(nums):
                if num in hash_dict:
                    del hash_dict[num]
                else:
                    hash_dict[num] = i
            if len(hash_dict):
                for key in hash_dict.keys():
                    return key
    def single_number3(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result^num
        return result





if __name__ == '__main__':
    nums = [2, 2,1]
    print(Solution().single_number3(nums))