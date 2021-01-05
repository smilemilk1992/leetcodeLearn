# -*- coding: utf-8 -*-
"""
@File    :   合并两个有序链表.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/5 14:33    1.0         None
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
#  示例：
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#  Related Topics 递归 链表
"""
__author__ = 'haochen214934'
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def tail_insert(self,nums):#尾插法
        head=ListNode(nums[0])
        tail=head
        for n in nums[1:]:
            node=ListNode(n)
            tail.next=node
            tail=node
        return head

    def head_insert(self,nums):#头插法
        head=ListNode(nums[0])
        for n in nums[1:]:
            node=ListNode(n)
            node.next=head
            head=node
        return head

    #双指针
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head=ListNode(0)
        tail=head
        while l1 and l2:
            if l1.val<=l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
        tail.next= l1 if l1 else l2
        return head.next

    #递归
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val<=l2.val:
            l1.next=self.mergeTwoLists1(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists1(l1,l2.next)
            return l2


    def printf(self,l):
        while l:
            print(l.val)
            l=l.next

if __name__ == '__main__':
    s=Solution()
    a=[1,2,4]
    b=[1,3,4]
    na=s.tail_insert(a)
    nb=s.tail_insert(b)
    nn=s.mergeTwoLists1(na,nb)
    s.printf(nn)