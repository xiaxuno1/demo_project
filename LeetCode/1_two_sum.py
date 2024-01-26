"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
"""
from typing import List


class Solution(object):
    def twoSum(self, nums, target):
        """
        暴力枚举 O(n^2)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if i !=j:
                    if nums[i]+nums[j] == target:
                        return [i,j]

#采用hash表实现，
# 关于散列表的定义：数据元素的关键字与器存储地址直接相关：addr = H(key),将关键字
# 本题中：H(key) = target-key,设置dict()作为hash table,dict()的key作为addr
# 本题目中创建一个hash table,判断target-key是否在hash table中,
# #O（n）,空间换时间
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()  #创建一个hash表
        for i, num in enumerate(nums):  #查找
            if num in hashtable:  #对与当前num查询hash表中是否存在target-num
                return [hashtable[num], i]
            hashtable[target-nums[i]] = i
        return []

if __name__ == '__main__':
    nums = [2,2,3,4,5,6,7]
    target = 6
    Solution1().twoSum(nums,target)