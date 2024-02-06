"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。
说明：你不能倾斜容器。
分析：
就是说找出数组中以序号为长，以数组为宽的两个元素组成矩形的最大值:min(nums[i],nums[j]) * (j-i), i !=j
暴力破解：冒泡法
O(n^2) 超时
双指针法；面积：min(nums[i],nums[j]) * (j-i), i !=j
规律：nums[i]和nums[j]一场一短
若长的向内移动，会导致面积减小
若短的向内移动，会导致面积增大
因此不断将短的向内移动，直到双指针相遇，即可找出最大的面积

"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0 #最大面积
        for i,width1 in enumerate(height):
            for j,width2 in enumerate(height[i+1:]):
                max_area = max(max_area,min(width1,width2)*(j+1)) #这里j从i后面开始代表了宽度
        return max_area

    def maxArea2(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height)-1 #尾部
        while i<j:
            if height[i]<height[j]:
                max_area = max(max_area,height[i]* (j - i))
                i = i+1
            else:
                max_area = max(max_area,height[j] * (j - i))
                j = j-1
        return max_area



if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea2(height))