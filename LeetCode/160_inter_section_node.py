"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
图示两个链表在节点 c1 开始相交：
分析：
从后往前思考，其实相交就是后面有一部分相等，从后边对齐查看是否相等便可知相交
但是，链表只能从头访问，于是问题变成了，查找两个链表尾对齐的起始位置（长度差|len（a）-len(B)|）
链表右对齐，在看是否相等（相交）
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        说好一起出发，走到尽头见不到你，于是走过你来时的路，等到相遇时才发现，你也走过我来时的路。
        :param headA:
        :param headB:
        :return:
        """
        pA = headA #指针
        pB = headB #指针
        if (pA==None or pB == None): return None
        while pA !=pB:
           pA = headB if pA == None else pA.next #走到尽头，回到你来时的路 #未到头，继续走
           pB = headA if pB == None else pB.next  #三目运算符
        return pA


