"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
分析：涉及两个知识点：
二叉排序树：左子树值<根<右子树值;由此也可知二叉排序树的中序遍历就是升序排列
平衡二叉树：每个节点的左右两个子树的高度差的绝对值不超过 1

现在问题为：知道中序遍历、知道平衡 能否确定一棵平衡二叉排序树  答：不能
这样想：如果数组个数为奇数个，我能能唯一确定根在中间；如果数组个数为偶数，则中间有两个元素可以作为根；因此，我们可以指定左或者右来确定
一个满足条件的平衡 二叉搜索树

这样问题变为：
知道一个二叉排序树的root节点，知道中序遍历顺序，求这个平衡 二叉排序树
涉及问题：如何通过有序序列初始化一个排序二叉树；
二叉树的插入可以实现将任意元素插入二叉排序树

暴力方法：
按照二叉排序树插入方法将每一个元素插入，再指定中间元素为root
用递归实现：从root出发，比较val与key ,val大则往左走，val小则往右走;直到终止将
终止条件：
    node == None
减少规模： val ?>key
"""
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #这里局部变量node在bst_insert执行完成后便释放，很难通过内部变量去影响外部root
        #我们想要通过bst_insert方法，将节点插入到root合适的位置，就要让局部变量去改变外部变量root;在C中有指针、引用可以解决；
        # python不支持
        #二分法实现有序数组转换为BST
        if not nums: #nums为空
            return None
        mid = len(nums)//2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node
    #BST的查找,从根节点出发，大往右，小往左，一直到头
    #查找结果：可能匹配到；可能不匹配，不匹配可能结束与叶子节点，也可能
    def bst_search(self,root:TreeNode,key):
        while root != None and key != root.val:  #
            root = root.left if root.val > key else root.right  #val大往左，小往右
        #返回搜索结束的位置，成功则返回node,不成功返回可能为空，叶子节点，可能为适合插入的终端位置
        return root
    #BST的插入
    #插入：大往右，小往左，一直到头插入终端节点
    def bst_insert(self,root:TreeNode,key):
        if root == None:  #为空，直接插入
            insert_node = TreeNode(key) #创建待插入的节点为跟节点
            insert_node.left = None
            insert_node.right = None
            return True
        elif root.val == key: #相等
            return False
        elif root.val>key: #往左
            return self.bst_insert(root.left,key) #往左插入到终端节点
        else:
            return self.bst_insert(root.right,key) #往右插入到终端节点

    #二叉树的构造,其实就是将每个元素插入，然后指定root
    def create_bst(self,nums: List[int]):
        node = None #初始为空
        for num in nums:
            self.bst_insert(node,num)


if __name__ == '__main__':
    nums = [-10, -3, 0, 5, 9]
    Solution().sortedArrayToBST(nums)
