"""
给定一个二叉树 root ，返回其最大深度。
二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
分析：
递归
终止条件：node == None
减少规模：root的最大深度，可以通过max (root.left maxDepth, root.right maxDepth) +1;
        root.left的最大深度，可以通过max (root.left maxDepth, root.right maxDepth) +1;
        由此减少规模直到root叶子节点
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left_maxDepth = self.maxDepth(root.left)
        right_maxDepth = self.maxDepth(root.right)

        return max(left_maxDepth,right_maxDepth)+1


if __name__ == '__main__':
    #初始化一棵二叉树
    root = TreeNode(1)
    tn2 = TreeNode(2)
    tn3 = TreeNode(3)
    root.right = tn2
    tn2.left = tn3

    print(Solution().maxDepth(root))

