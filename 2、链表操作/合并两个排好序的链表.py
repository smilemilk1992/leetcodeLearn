# -*- coding: utf-8 -*-
"""
@File    :   合并两个排好序的链表.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/8 10:39    1.0         None
将两个有序链表合并为一个新的有序链表并返回, 新链表是通过拼接给定的两个链表的所有节点组成的。

大体思路:可以使用递归来快速解决
1.判断L1,L2是否为空
2.创建一个头指针
3.判断当前L1,L2指向的节点值的大小.根据结果,让头指针指向小节点,并让这个节点往下走一步,作为递归函数调用的参数放入,返回的就是新的两个值的比较结果,则新的比较结果放入头结点的下一个节点.
4.返回头结点

解题思路
　　使用头结点root进行辅助操作，创建一个头结点，再使用两个引用指向两个链表的头结点，将较小的结点值的结点摘下来接到root链表的末尾，同时被摘的链头引用移动到下一个结点，一直操作，直到原先两个链表中有一个为空，最后再将没空的链表剩余结点接到root链表的末尾。最后返回root的下一个结点，其就为新的链表头。
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

    #双指针法
    def merge(self,one:ListNode,two:ListNode)->ListNode:
        head=ListNode(0) #创建一个头结点，最后还要删除掉
        tail=head
        while one and two:
            if one.val<=two.val:
                tail.next=one
                one=one.next
            else:
                tail.next=two
                two=two.next
            tail=tail.next #移动到新的尾结点

        # 将其中一个没有走到头的链表直接链接到新链表root的后面
        tail.next=one if one else two
        return head.next

    #递归
    def merge1(self,one:ListNode,two:ListNode)->ListNode:

        if not one:
            return two
        if not two:
            return one
        if one.val<=two.val:
            head=one
            head.next=self.merge1(one.next,two)
        else:
            head=two
            head.next=self.merge1(one,two.next)
        return head



    def print_item(self,head:ListNode):
        while head:
            print(head.val)
            head=head.next







if __name__ == '__main__':
    a=[1,3,5,7]
    b=[2,4,6,8]
    s=Solution()
    l1=s.tail_add(a)
    l2 = s.tail_add(b)
    c=s.merge1(l1,l2)
    s.print_item(c)