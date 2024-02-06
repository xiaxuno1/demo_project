"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
分析：
hash:
    [num:total] 时间 O(n) 空间O（n)
排序：
    由于规定 多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素，因此排序完成后众数一定再 n/2下标处
随机：
    规定存在众数，因此，随机选择一个数，有很大可能选中；可能不稳定
分治：

BM算法：


"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_dict = {}
        majority = len(nums) // 2
        for num in nums:
            if num in hash_dict:
                hash_dict[num] = hash_dict[num]+1 #次数+1
            else:#新建key-value
                hash_dict[num] = 1
        #遍历字典找出满足的,给定的总是存在多数
        for key in hash_dict.keys():
            if hash_dict[key]> majority:
                return key



if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(Solution().majorityElement(nums))