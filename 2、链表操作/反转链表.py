# -*- coding: utf-8 -*-
"""
@File    :   22、反转链表.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/9 14:28    1.0         None
"""
__author__ = 'haochen214934'
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

    def revolve(self,head:ListNode)->ListNode:#就地反转
        if not head:
            return head
        pre=None
        cur=head
        while cur:
            pnext=cur.next
            cur.next=pre
            pre=cur
            cur=pnext
        return pre


    def print_item(self,head:ListNode):
        while head:
            print(head.val)
            head=head.next



if __name__ == '__main__':
    a=[1,2,3,4,5,6]
    s=Solution()
    l1=s.tail_add(a)
    r1=s.revolve(l1)
    s.print_item(r1)