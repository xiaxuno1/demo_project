"""
给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
分析：
如果numRows=0, 输出为[]
如果numRows=1, 输出为[1]
如果numRows=2, 输出为[[1],[1,1]]
如果numRows=3, 输出为[[1],[1,1,],[1,2,1]
第n行，有n个元素；第i个元素设为f(i),c为第n-1行的值
f(i) = c(i-1)+c(i)
暴力解法：O(n^2)
两个循环
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        yanghui_triangle = []
        if numRows == 0:
            return yanghui_triangle
        #生成所有行
        for i in range(numRows):
            #在「杨辉三角」中，每个数是它左上方和右上方的数的和。实现此，生成一行
            line_list = [1]
            if len(yanghui_triangle): #防止n = 1
                for j in  range(len(yanghui_triangle[-1])):
                    if j == len(yanghui_triangle[-1])-1: #最后一个数，没有右边
                        line_list.append(yanghui_triangle[-1][j])
                    else:
                        line_list.append(yanghui_triangle[-1][j]+yanghui_triangle[-1][j+1])
            yanghui_triangle.append(line_list)
        return yanghui_triangle


if __name__ == '__main__':
    numRows = 5
    print(Solution().generate(numRows))



