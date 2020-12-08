# -*- coding: utf-8 -*-
"""
@File    :   删除链表倒数第N个节点.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/8 15:27    1.0         None
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

    def deleteTOPN(self,head:ListNode,N: int)->ListNode:#[2,3,4,5,6,7]
        if not head or N<=0:
            return head
        fast=head
        slow=head
        while N>0 and fast:
            fast=fast.next
            N=N-1

        while fast:
            if not fast.next:
                slow.next=slow.next.next
                break
            else:
                slow=slow.next
                fast=fast.next
        return head








    def print_item(self,head:ListNode):
        while head:
            print(head.val)
            head=head.next







if __name__ == '__main__':
    a=[2,3,4,5,6,7]
    s=Solution()
    l1=s.tail_add(a)
    r1=s.deleteTOPN(l1,10)
    s.print_item(r1)