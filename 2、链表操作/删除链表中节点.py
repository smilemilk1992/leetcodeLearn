# -*- coding: utf-8 -*-
"""
@File    :   删除链表中节点.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/8 15:01    1.0         None

# 请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。
#  现有一个链表 -- head = [4,5,1,9]，它可以表示为:
#  示例 1：
#  输入：head = [4,5,1,9], node = 5
# 输出：[4,1,9]
# 解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
#
#  示例 2：
#  输入：head = [4,5,1,9], node = 1
# 输出：[4,5,9]
# 解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
#
#  提示：
#  链表至少包含两个节点。
#  链表中所有节点的值都是唯一的。
#  给定的节点为非末尾节点并且一定是链表中的一个有效节点。
#  不要从你的函数中返回任何结果。
#
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

    def deleteNode(self,head:ListNode,k: int)->ListNode:#[2,3,4,5,6,7]
        if not head:
            return head
        cur=head
        while cur and cur.next:
            if cur.next.val==k:
                cur.next=cur.next.next
            if cur.val==k:#头部
                head=cur.next
            cur=cur.next
        return head





    def print_item(self,head:ListNode):
        while head:
            print(head.val)
            head=head.next







if __name__ == '__main__':
    a=[1,2,6,3,4,5,6]
    s=Solution()
    l1=s.tail_add(a)
    r1=s.deleteNode(l1,6)
    s.print_item(r1)