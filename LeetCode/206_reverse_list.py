"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
分析：
反转实际上就是将指针反向，
考虑递归：
终止条件：head.next = None
减少规模： 如果head都已经反转，则 head.next.next = head  #即下一个节点的next指针指向head

"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None): #防止head = []情况
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head  #指针反转  head.next.next = head  head的下一个节点的next指向head
        head.next = None  #将节点的next指针置为空，防止成环
        return new_head

# 采用迭代的方法
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #迭代，将每个指针反向：head.next.next = head,需要先村春head.next
        prev = None
        curr = head
        while (curr != None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev




if __name__ == '__main__':
    #链表初始化
    nums = [1,2,3,4,5]
    head = ListNode(nums[0])
    now_node = head  #当前节点初始化
    for i in nums[1:]:
        node = ListNode(i) #创建一个新节点
        #当前节点next指向创建节点
        now_node.next = node
        now_node = now_node.next

    Solution1().reverseList(head)

