"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
解析：
可以采用no.26的方法，双指针法，本质上都是遍历数组找到条件值操作，移动元素，与按照顺序排序都是一致，
遍历整个数组，找出符合条件，进行操作
双指针法：设置两个指针，一个指针用来表示满足条件，一个指针用来表示不满足条件，通过交换移动位置
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        双指针法：p指向需要存放元素的位置，即前p个元素符合要求；q指向寻找的符合条件的元素
        这里i为q;因此q隐藏
        :param nums:
        :param val:
        :return:
        """
        p = 0 #表示前p个元素符合条件
        length = 0 #表示符合条件的元素个数
        for i in range(len(nums)):
            if nums[i] != val: #符合条件的元素直接往前到位置0
                temp = nums[p]
                nums[p] = nums[i]
                nums[i] = temp
                p = p+1
                length = length+1
        return length


if __name__ == '__main__':
    nums = [2]
    val = 3
    Solution().removeElement(nums,val)
    print(nums)  #nums 改变了
