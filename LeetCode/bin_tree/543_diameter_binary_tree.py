"""
给你一棵二叉树的根节点，返回该树的 直径 。
二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
两节点之间路径的 长度 由它们之间边数表示。
分析：
树的深度优先遍历算法的改进
首先我们知道：树的直径，就是树中最长路径包含的节点数-1，此路径不一定从root出发
观察：
假设存在一条最长路径，观察此路径，在路径上必然可以找到一个类似root的节点，此路径长度 = 该节点左子树的深度+该节点右子树的深度
求子树深度？
我们用深度优先遍历算法可以解决。（递归从根节点出发，遍历到最深处（node == node）返回），如何求其深度值
如何确定这个节点？
我们无法准确知道这个节点？但是我们可以记录每个节点的深度，去最大的深度便是该节点
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  #记录直径，下面的方法，求每个节点为根的深度，记录期间的最大深度
        def depth(node:Optional[TreeNode]): #深度优先
            #递归终止条件
            if node is None:
                return 0 #深度为0
            #减少规模的递归条件
            print(node.val)
            left = depth(node.left) #左子树的深度
            right = depth(node.right) #右子树的深度
            #记录修改最长路径,此路径长度 = 该节点左子树的深度+该节点右子树的深度
            self.diameter = max(self.diameter,left+right)
            #节点的深度，max(左子树深度,右子树深度）
            return max(left,right)+1
        depth(root)
        return self.diameter