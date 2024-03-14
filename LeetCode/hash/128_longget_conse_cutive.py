"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
分析：解决思路：
设当前元素为x,以当前元素为起点的连续序列为：x,x+1,x+2,...x+n 总共有n个
使用遍历:O(n^3)超时
    遍历每个元素x,找出连续的x+1,x+2...，如果这样的话，最坏每个元素可能都得遍历
优化1：
实际上，知道了x,则它最多len(nums)的连续序列已经确定，可以考虑用hash表来换取时间，这样x只需要一次循环nums就能知道最大；
其实，我们在遍历过程中知道了连续序列：x,x+1,x+2,...x+n，如果要下一个数为x+1,其匹配数不能不x的数的，再查找就重复了；因此遇到这种跳过即可
即要求的x，一定不存在x-1,否则x-1,x...为最大序列，不用比较x

"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest_conse_cutive = 1
        for num in nums:
            longest_cur = 1
            target = num
            for n in nums:
                if target+1 in nums: #找到目标元素
                    longest_cur +=1
                    target += 1
                else:break
            if longest_conse_cutive<longest_cur:
                longest_conse_cutive = longest_cur
        return longest_conse_cutive

    def longestConsecutive2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        longest_conse_cutive = 1
        nums_set = set(nums)
        for num in nums_set:
            if num-1 not in nums_set: #x-1存在直接跳过查找
                longest_cur = 1
                target = num
                while target + 1 in nums_set:  # 找到目标元素
                    longest_cur += 1
                    target += 1
                if longest_conse_cutive < longest_cur:
                    longest_conse_cutive = longest_cur
        return longest_conse_cutive


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    nums2= [0,-1]
    #[1, 2, 3, 4]  4
    print(Solution().longestConsecutive2(nums2))