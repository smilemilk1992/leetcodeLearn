# -*- coding: utf-8 -*-
"""
@File    :   两数相加.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/11/25 16:08    1.0         None
"""
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 对于逆序处理应该首先想到栈
__author__ = 'haochen214934'
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def list_tail(self,lists:List[int])->ListNode: #尾插法
        root=ListNode(lists[0])
        tail=root
        for li in lists[1:]:
            node=ListNode(li)
            tail.next=node
            tail=node
        return root

    def list_head(self,lists:List[int])->ListNode: #头插法
        head=ListNode(lists[0])
        for li in lists[1:]:
            node=ListNode(li)
            node.next=head
            head=node
        return head

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1=[]
        s2=[]
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        s1.reverse()
        s2.reverse()
        ans=ListNode(0)
        tail=ans
        flag=0 #进位
        while s1 or s2 or flag!=0:
            a=0 if not s1 else s1.pop()
            b=0 if not s2 else s2.pop()
            cur=a+b+flag
            flag=cur//10 #取整 进位
            cur=cur%10 #取余数
            curnode=ListNode(cur)
            tail.next=curnode
            tail=curnode
        return ans.next

    def print_list(self,nodes):                      #打印链表
        while nodes:
            if  nodes.next != None:
                print(nodes.val, end='->')
            else:
                print(nodes.val,end = '\n')
            nodes = nodes.next

if __name__ == '__main__':
    a=[2,4,9]
    b=[5,6,4,9]
    s=Solution()
    l1=s.list_tail(a)
    l2=s.list_tail(b)
    ans=s.addTwoNumbers(l1,l2)
    s.print_list(ans)
    # s.print_list(s.list_head(a))