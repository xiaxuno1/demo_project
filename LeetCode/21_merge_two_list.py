"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
解决：
两个链表比较，小的将结果放入新链表，大的放入保留进行下一轮比较;
递归解法：
    终止条件：两个列表都为空
    减少规模的方法：列表是有序的，比较第一个元素，较小的元素指向其余结果合并集
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def mergeTwoLists(self,l1, l2):
        纯列表的实现，不用定义节点
        :param l1:
        :param l2:
        :return:
        if len(l1)==0: return l2  # 终止条件，直到两个链表都空
        if len(l2)==0: return l1
        if l1[0] <= l2[0]:  # 递归调用,减少规模的方法
            l1[1:] =self.mergeTwoLists(l1[1:],l2)
            return l1
        else:
            l2[1:] = self.mergeTwoLists(l1,l2[1:])
            return l2
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:return list2
        if not list2:return list1
        if list1.val<=list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2


if __name__ == '__main__':
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    print(Solution().mergeTwoLists(list1, list2))
