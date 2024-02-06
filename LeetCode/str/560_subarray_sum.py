"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
子数组是数组中元素的连续非空序列。
分析：
1.可以遍历数组，将target = k-num 存为hashtable:{k-num}这样如果遇到target = nums[i]便可知此两个数符合的项；
2.子数组的个数可以为 1,2,3,4，...len(nums)
3.三个数符合的如何判断呢？生成的hashtable key = k-num  前缀和


举例：
nums = [1,2,3,4,5,6] k = 9
hash_table = {8:1,7:2,6:3,5:4,3:2}
暴力：枚举  超出时间
题目说了是连续序列，如果[i,...,j]为字序列，则 0<=i<=j<=len(nums)-1; k= sum(nums[i]+...+nums[j])
i和j可以用枚举实现；
优化：
遍历的i不可避免；想法为优化j,提前结束j 没想到

前缀和+哈希表优化？？？
题目说了是连续序列，如果[i,...,j]为字序列，则 0<=i<=j<=len(nums)-1; k= sum(nums[i]+...+nums[j])
前缀和记为pre; k = pre[j]-pre[i-1]

"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #暴力枚举
        ans = 0 #记录个数
        for i,start in enumerate(nums):
            sum = start
            if sum == k: #当i=j，即只有一个元素
                ans = ans+1
            for j ,end in enumerate(nums[i+1:]):
                sum = sum+end
                if sum == k: #满足条件的
                    ans = ans +1

        return ans


if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 3
    print(Solution().subarraySum(nums, k))