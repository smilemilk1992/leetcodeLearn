# -*- coding: utf-8 -*-
"""
@File    :   找出两个单链表的第一个公共节点.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/5 17:58    1.0         None
"""
__author__ = 'haochen214934'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:


    def commonNode(self,headA:ListNode,headB:ListNode)->ListNode:
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1








