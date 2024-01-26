"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
分析：
回文：12321 123321 相当于对称
基本思路：头和尾判断，不断往中间移动，直到头尾相等，表示TRUE
实现：首先想到的是双指针，
一个指向回文左一个指向回文右，相等左指针左移：.next 右指针右移：？
换个思路：从中间开始 比较两边是否相等？存在问题：如何找到中间？head.next.val =head.val  ,但是像12321这种，左右共用的无法确定；
我们在开始无法确定是那种情况；---先将其存储为列表
递归：
终止条件：head.next = None  链表末尾
减少规模：往中间靠，直到头尾相等或者头指向尾，尾指向头
head.val == ispalindrome()

对称就一位这头尾相等，栈可以满足，先进后出
栈实现：
依次入栈，
什么时候停止入栈？
如果：入栈节点值与下一个节点值相等就出栈    head
判断：栈不为空FALSE，栈为空则TRUE

快慢指针：
设置两个指针一个一次走一步，一个一次走两步，则快指针到头时,慢指针刚到终点，以此实现了指向中间

暴力想法：
将链表反转，然后判断值是否相等，
"""
# Definition for singly-linked list.
from typing import Optional
import copy


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        暴力算法,时间和空间复杂度 O(n);性能较低
        :param head:
        :return:
        """
        prev = None  #前一个节点
        original_head = copy.deepcopy(head) #深拷贝一份原始数据
        curr =head  #当前节点
        while (curr !=None):
            next = curr.next  #暂时存储下一个节点，防止指针改变后无法找到
            curr.next = prev  #当前节点指向前一个节点
            prev = curr   #前节点后移
            curr = next #当前节点后移
        #恢复head, 反转存在prev中
        head = original_head
        while prev.val == head.val:  #判断是否相等，原则上只需要判断一半，但是不知道中间在哪里
            prev = prev.next
            head = head.next
            if prev is None: return  True#完全相等
        return False

class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        列表存储后使用双指针
        :param head:
        :return:
        """
        head_list = []
        while head != None:
            head_list.append(head.val)
            head = head.next
        #对列表使用双指针
        frist = 0
        tail = -1
        for i in range(len(head_list)):
            if head_list[frist] != head_list[tail]:
                return False
            else:
                frist = frist+1
                tail = tail-1
        return True

    def centre(self): #快慢指针，找中点
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            #有可能快指针走不到终点，一次走两步，如果倒数第二次走了只有一步呢？，中点有肯能有一个（奇数个），也有可能有两个（偶数）
            fast = fast.next.next #一次走两步
            slow = slow.next #一次走一步
        return slow




if __name__ == '__main__':
    nums = [1,1,2,1]
    head = ListNode(nums[0])
    now_node = head  #当前节点初始化
    for i in nums[1:]:
        node = ListNode(i) #创建一个新节点
        #当前节点next指向创建节点
        now_node.next = node
        now_node = now_node.next

    print(Solution1().isPalindrome(head))
