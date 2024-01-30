"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。
有序的顺序表：
折半查找：设置low、mid、high位置标记mid = (low/high)/2   O(log2 n)
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        mid = (low + high) // 2
        while low<=high:
            mid = (low+high) //2  # 取整
            if target< nums[mid]:
                high = mid-1
            elif target == nums[mid]:
                return mid #匹配到返回
            else:
                low = mid+1
        #没有匹配到返回它将会被按顺序插入的位置
        return low


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 2
    print(Solution().searchInsert(nums, target))