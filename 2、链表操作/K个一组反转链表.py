# -*- coding: utf-8 -*-
"""
@File    :   K个一组反转链表.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/8 16:12    1.0         None

# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#  k 是一个正整数，它的值小于或等于链表的长度。
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
#
#  示例：
#  给你这个链表：1->2->3->4->5
#  当 k = 2 时，应当返回: 2->1->4->3->5
#  当 k = 3 时，应当返回: 3->2->1->4->5
#
#  说明：
#  你的算法只能使用常数的额外空间。
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
https://coordinate.blog.csdn.net/article/details/80696835?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromBaidu-1.not_use_machine_learn_pai&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromBaidu-1.not_use_machine_learn_pai
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

    '''
    [1,2,3,4,5]
    #  当 k = 2 时，应当返回: 2->1->4->3->5
    #  当 k = 3 时，应当返回: 3->2->1->4->5
    关于这个问题，首先我们很容易想到的思路就是通过两个指针指向一个group的头和尾，
    然后对这个group做reverse操作，如果这两个指针间的距离小于k，我们不进行操作。
    另外，我们要确定我们reverse的边界，我这里假设边界为（pre, lat）（取k=3的情况）
    https://blog.csdn.net/qq_17550379/article/details/80647926
    '''
    def rollback(self,head:ListNode,k: int)->ListNode:#[1,2,3,4,5,6] 2 1 4 3 6 5
        if not head or k<=1:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        cur=head
        t=1
        while cur!=None:
            if t % k == 0:
                pre = self.reverse(pre, cur.next)
                cur = pre.next
            else:
                cur = cur.next
            t=t+1
        return dummy.next



    def reverse(self,pre,lat):
        lpre=pre.next
        cur = lpre.next
        while cur!=lat:
            lpre.next=cur.next
            cur.next=pre.next
            pre.next=cur
            cur=lpre.next
        print(self.print_item(lpre))
        return lpre





    def print_item(self,head:ListNode):
        while head:
            print(head.val)
            head=head.next







if __name__ == '__main__':
    a=[1,2,3,4,5,6]
    s=Solution()
    l1=s.tail_add(a)
    r1=s.rollback(l1,2)
    s.print_item(r1)