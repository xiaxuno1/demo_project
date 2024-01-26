"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
分析：
翻转的意思是以root为轴翻折，对其子树进行同样操作；包含了大量相似的操作，考虑递归
递归：
终止条件：node == None
减少规模：
假设root.left和root.right已经完成翻转，可将root翻转 root.left  =root.right ;root.right = root.left;
假设root.left.left 已经完成翻转，可将root.left翻转
由此，发现了减少规模的方法

"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #终止条件
        if root ==None:
            return
        #减少规模,交换左右子树
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root


if __name__ == '__main__':
    #初始化一棵二叉树
    root = TreeNode(1)
    tn2 = TreeNode(2)
    tn3 = TreeNode(3)
    root.right = tn2
    tn2.left = tn3

    Solution().invertTree(root)
    print(root)