"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

分析：
暴力解法：（超时）
两个循环

一次循环：类似双指针
在一次循环中设置一个最小价格

"""
import time
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #暴力解法，时间 O(n^2)
        max_profit = 0
        for i,start in enumerate(prices):
            for j, end in enumerate(prices[i+1:]):
                max_profit = max(max_profit,end-start)
        return max_profit

    def max_profit(self,prices: List[int]) -> int:
        min_price = prices[0] #默认第一个为最小，循环中更新
        max_profit = float()
        for price in prices:
            max_profit = max(max_profit,price-min_price)
            min_price = min(min_price,price) #计算最小
        return max_profit


if __name__ == '__main__':
    #prices = [7, 1, 5, 3, 6, 4]
    #大量数据查看性能, 15s
    prices = []
    n = 10000
    while n>0:
        prices.append(n)
        n = n-1
    t1 = time.perf_counter()
    print(Solution().max_profit(prices))
    t2 = time.perf_counter()
    print("time:",t2-t1)