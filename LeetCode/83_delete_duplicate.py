"""
给定一个已排序(升序)的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head.next is not None: #链表结尾
            if head.val ==head.next.val: #重复 删除
                #head.next = None #删除
                head.next = head.next.next #指向下一个
            head = head.next #下一个判断


if __name__ == '__main__':
    #链表初始化
    nums = [1,1,2,3,3]
    head = ListNode(nums[0])
    now_node = head  #当前节点初始化
    for i in nums[1:]:
        node = ListNode(i) #创建一个新节点
        #当前节点next指向创建节点
        now_node.next = node
        now_node = now_node.next

    Solution().deleteDuplicates(head)