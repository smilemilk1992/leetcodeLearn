# -*- coding: utf-8 -*-
"""
@File    :   截取单链表中后K个节点.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/8 10:13    1.0         None
使用两个指针，先让前面的指针走到正向第k个结点，这样前后两个指针的距离差是k-1，之后前后两个指针一起向前走，前面的指针走到最后一个结点时，后面指针所指就是后K个结点
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

    def TopN(self,head:ListNode,k: int)->ListNode:
        if not head:
            return None
        front=head
        back=head
        while k>1 and front.next: #前一个先走K步
            front=front.next
            k=k-1

        while front.next:#后面一起走
            back=back.next
            front=front.next
        return back

    def print_item(self,head:ListNode):
        while head:
            print(head.val)
            head=head.next







if __name__ == '__main__':
    a=[2,3,4,5,6]
    s=Solution()
    l1=s.tail_add(a)
    r1=s.TopN(l1,3)
    s.print_item(r1)