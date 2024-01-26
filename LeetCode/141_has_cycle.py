"""
给你一个链表的头节点 head ，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，
评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
如果链表中存在环 ，则返回 true 。 否则，返回 false 。

分析：
环：a.next = b;a可以是当前遍历的元素，但是b呢？
环的存在，一旦循环就会形成死循环
暴力：no
双循环，一次循环在a,一次循环在b；这里错了，因为形成了环，因此循环会在一个环中形成死循环

双指针：
快慢指针，当快指针和慢指针都进入环中时，就变成追及问题；就像在操场跑步，只要时间快的和慢的总会相遇
因此，用快慢指针可以解决

"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast is not None and fast.next is not None and fast.next.next is not None: #没有环时，跑得快的先到终点，有环时将一直循环
            fast = fast.next #fast.next = none时fast.next.next 会出错
            #直到相遇
            if fast ==slow:
                return True
            slow = slow.next
        return False  #没有环



if __name__ == '__main__':
    nums = [3,2,1,-4]
    head = ListNode(nums[0])
    now_node = head  #当前节点初始化
    for i in nums[1:]:
        node = ListNode(i) #创建一个新节点
        #当前节点next指向创建节点
        now_node.next = node
        now_node = now_node.next
    now_node.next = head.next  #形成环


    Solution().hasCycle(head)