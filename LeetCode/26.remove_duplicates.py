"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
解析：
定义一个等长数组存放bool,重复为True,不重复为FALSE
设置一个target;target初始值为nums[0],遍历数组查找重复值
如果遍历值 >target，修改target
"""
from typing import List


class Solution:
    """
    时间O(n),空间O(n)
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates_lists = [False] #存放是否重复bool,第一个数肯定不重复
        index = 0  #位置索引
        target = nums[0]
        for num in nums[1:]:
            if target == num:
                duplicates_lists.append(True)
            elif target<num:  #不是重复数字
                target = num
                duplicates_lists.append(False)
        for duplicates_list in duplicates_lists:  #
            if duplicates_list is True:  #该位置重复
                del nums[index]  #不能直接对原nums删除，删除后，索引会改变
                index = index-1  #删除后索引-1
                #new_nums.append(nums[index])
            index = index+1
        return len(nums)
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        类冒泡排序
        双指针法；p,q p指向最后一个不重复元素，q指向下一个不重复元素,找到不重复则交换（前移）
        O(n),O（1）
        :param nums:
        :return:
        """
        p = 0
        q = 1
        for i in range(len(nums)-1): #第一个元素默认有序，因此比较次数少一次
            if nums[p]-nums[q]>=0:  #重复时将q向后移动
                q = q+1
            else: #交换,将最后不重复位置移动一位
                p = p+1
                temp = nums[p]
                nums[p] = nums[q]
                nums[q] = temp
                q= q+1
        return p+1


if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    #nums = [1,1,2]
    Solution().removeDuplicates(nums)

