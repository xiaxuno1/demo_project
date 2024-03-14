"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k
同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
分析：
多重循环：超时
三数和x+y+x = 0，固定x,就变成两数和y+z = -x;其中target = -x
两数求和no.1前面用hash解决过
排序+双指针：
先进行排序，需要满足：x<y<z然后固定x,双指针y,z；y向左z向右移动求值
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] #存储结果
        for j,num in enumerate(nums):
            target = -num
            res_one = [] #存储一个结果
            hashtable = dict()  # 创建一个hash表
            for i, num_ in enumerate(nums):  #查找
                if i == j: #遍历到自己时排除
                    continue
                if num_ in hashtable:  #对与当前num查询hash表中是否存在target-num
                    res_one =  [num,nums[hashtable[num_]], nums[i]]
                    res_one.sort()
                    if res_one not in res:
                        res.append(res_one)
                hashtable[target-nums[i]] = i
        return res

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort() #排序
        res = [] #存储结果
        #第一个数x
        for first in range(n):
            #不重复,重复的跳过
            if first>0 and nums[first] == nums[first-1]:
                continue

            #第三个数为从后向前走
            third = n-1
            target = -nums[first] #y+z = -x

            #第二个数x<y
            for second in range(first+1,n):
                #不重复
                if second>first+1 and nums[second] == nums[second-1]:
                    continue
                #不断移动z指针，保证y指针在z指针的左边
                while second < third and nums[second] +nums[third] > target:
                    third -=1
                if second == third: #重合了
                    break
                if nums[second]  +nums[third] == target:
                    res.append([nums[first],nums[second],nums[third]])

        return res


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum2(nums))