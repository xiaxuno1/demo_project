"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。
分析：
所谓轴对称，就是从根节点出发，查看左右子树翻转相等，左子树翻转等于右子树；这与翻转二叉树异曲同工
问题是如何判定相等？node.value

暴力方法：no
    将根的右子树翻转，判断翻转后的左右子树是否相等,存在的问题是翻转后的子树怎么比较还是要用递归
递归：
终止条件：node == None
减少规模：
只要每一层都对称，则对称
关注点
实际比较如下：
    第二层：通过第一层节点，左右子树的值是否相等
    第三层：通过第二层节点，左子树的右节点和右子树的左节点是否相等，左子树的左节点和右子树的右节点是否相等

"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None: #防止root =[] ，n<1
            return True
        def dfs(left_tree: Optional[TreeNode],right_tree: Optional[TreeNode]):
            #判断n层对称？n-1层节点的left.val == n-1层的right.val;这就是n-1层
            if left_tree == right_tree ==None:  #仅当左右子树层数相同到最后一层，才对称
                return True
            if left_tree == None or right_tree == None: #左右的高度不相等，直接返回
                return False
            if left_tree.val !=right_tree.val:
                return False
            #左子树的右节点与右子树的左节点相等，右子树的左节点与左子树的右节点比较
            return dfs(left_tree.left,right_tree.right) and dfs(left_tree.right,right_tree.left) #判断下一层是否对称
        return dfs(root.left,root.right)

if __name__ == '__main__':
    print(" 00"*189)
