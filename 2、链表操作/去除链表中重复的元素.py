# -*- coding: utf-8 -*-
"""
@File    :   去除链表中重复的元素.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/7 15:46    1.0         None

1、有序重复

2、无序重复
"""
__author__ = 'haochen214934'
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    #有序节点 去重复问题
    def repetition(self,head:ListNode)->ListNode:
        if not head or not head.next:
            return head
        cur=head
        while cur.next is not None:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head


    #无序节点去重复问题 内循环 外循环 [2,2,4,4,9,9,4,4]
    def repetition1(self,head:ListNode)->ListNode:
        if not head or not head.next:
            return head
        outcur=head
        while outcur is not None:
            incur=outcur.next
            pre=outcur
            while incur is not None:
                if outcur.val==incur.val:
                    pre.next=incur.next
                else:
                    pre=incur
                incur=incur.next
            outcur=outcur.next
        return head

    def list_tail(self,lists:List[int])->ListNode: #尾插法
        head=ListNode(lists[0])
        tail=head
        for li in lists[1:]:
            node=ListNode(li)
            tail.next=node
            tail=node
        return head



    def print_list(self,nodes):                      #打印链表
        while nodes:
            if  nodes.next != None:
                print(nodes.val, end='->')
            else:
                print(nodes.val,end = '\n')
            nodes = nodes.next

if __name__ == '__main__':
    a=[2,2,4,4,9,9,4,4]
    s=Solution()
    l1=s.list_tail(a)
    r1=s.repetition1(l1)
    s.print_list(r1)