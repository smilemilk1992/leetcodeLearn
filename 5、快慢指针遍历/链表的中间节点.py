# -*- coding: utf-8 -*-
"""
@File    :   链表的中间节点.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/22 14:10    1.0         None
# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
#
#  如果有两个中间结点，则返回第二个中间结点。
#
#  示例 1：
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next =
# NULL.

#  示例 2：
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
#
#  提示：
#  给定链表的结点数介于 1 和 100 之间。
#  Related Topics 链表
"""
__author__ = 'haochen214934'

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def add_tail(self,lists):
        head=ListNode(lists[0])
        tail=head
        for i in lists[1:]:
            node=ListNode(i)
            tail.next=node
            tail=node
        return head

    #快慢指针
    def middleNode(self, head: ListNode) -> ListNode:
        pslow=head
        phigh=head
        while phigh and phigh.next:
            pslow=pslow.next
            phigh=phigh.next.next
        return pslow




    def items(self,head):
        if not head:
            return None
        while head:
            print(head.val)
            head=head.next

if __name__ == '__main__':
    head=[1]
    s=Solution()
    tail=s.add_tail(head)
    cc=s.middleNode(tail)
    s.items(cc)