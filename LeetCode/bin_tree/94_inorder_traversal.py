"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
分析：
中序遍历：左根右
采用递归
"""
# Definition for a binary tree node.
import copy
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

res = []
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #递归调用时，无法存储 结果list，因此采用闭包函数来实现存储结果;闭包函数:增强功能，这里我不改变LDR,又想存储结果，因此用闭包函数
        res = []
        def ldr(root: Optional[TreeNode]):
            if root is None:  #root为空
                return res
            if root.left is not None: #左
                ldr(root.left)
            res.append(root.val) #根
            if root.right is not None: #右
                ldr(root.right)
        ldr(root)
        return res









if __name__ == '__main__':
    #初始化一棵二叉树
    root = TreeNode(1)
    tn2 = TreeNode(2)
    tn3 = TreeNode(3)
    root.right = tn2
    tn2.left = tn3

    print(Solution().inorderTraversal(root))

    print(Solution().inorderTraversal(root))