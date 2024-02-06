"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
分析：
DP :时间O（n）,空间O(n)
假设爬到了n阶，则可知
f(n) = f(n-1)+f(n-2)；即n阶的方案数等于n-1阶的方案和n-2阶的方案和
f(1) = 1
f(2) = 2
f(3) = 111/12/21 = 3
符合,转移方程和边界都知道
采用滚动数组的方式节省空间
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        p = q = int(0)
        r = int(1)
        for i in range(n):
            p = q #q前移
            q = r #r前移
            r = p+q  #f(n) = f(n-1) +f(n-2)
        return r

if __name__ == '__main__':
    n = 4
    print(Solution().climbStairs(n))
