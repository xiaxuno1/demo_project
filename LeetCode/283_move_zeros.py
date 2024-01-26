"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
分析：
双指针,将非零元素往前移动
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        遍历一次肯定知道所有需要移动的元素，用双指针标记，交换的两个位置
        这里 i实际为另一个指针，指向非零元素
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0 #表示前pointer个元素符合要求（指向排序完成的位置）
        for i,num in enumerate(nums):
            #=0时表示需要移动到后面去，zero_pointer +1
            if num !=0: #!=0表示要与0的位置交换
                temp = nums[pointer]
                nums[pointer] = num
                nums[i] = temp  #与0交换，直接赋值为0
                pointer = pointer+1

if __name__ == '__main__':
    nums = [1, 0, 2,0,5,0,0,0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)








