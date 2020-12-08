# -*- coding: utf-8 -*-
"""
@File    :   链表中间节点.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/8 14:18    1.0         None

给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5,
以及 ans.next.next.next = NULL.
"""
__author__ = 'haochen214934'
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def tail_add(self,lists):
        root=ListNode(lists[0])
        tail=root
        for li in lists[1:]:
            node=ListNode(li)
            tail.next=node
            tail=node
        return root

    #快慢指针 思路:当用慢指针 slow 遍历列表时，让另一个指针 fast 的速度是它的两倍。当 fast 到达列表的末尾时，slow 必然位于中间.
    def middle(self,head:ListNode)->ListNode:
        if not head:
            return head
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow



    def print_item(self,head:ListNode):
        while head:
            print(head.val)
            head=head.next







if __name__ == '__main__':
    a=[2,3,4,5,6,7]
    s=Solution()
    l1=s.tail_add(a)
    r1=s.middle(l1)
    s.print_item(r1)