"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
分析：找出基本定式：每个位置的路径数 = 位置左边路径数+位置右边路径数，这就是杨辉三角
化为数学式：
dp(i)(j) = dp(i-1)(j) +dp(i)(j-1)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)] #按照行建立列表，并初始化路径数
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    Solution().uniquePaths(4,5)