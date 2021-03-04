# -*- coding: utf-8 -*-
"""
@File    :   38、链表里面删除重复的数字_只出现一次.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/3/4 15:04    1.0         None
删除有序链表中重复出现的元素
给出一个升序排序的链表，删除链表中的所有重复出现的元素，只保留原链表中只出现一次的元素。
例如：
给出的链表为1 \to 2\to 3\to 3\to 4\to 4\to51→2→3→3→4→4→5, 返回1\to 2\to51→2→5.
给出的链表为1\to1 \to 1\to 2 \to 31→1→1→2→3, 返回2\to 32→3.
"""
__author__ = 'haochen214934'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def tail_insert(self,nums):
        nodes=ListNode(nums[0])
        tail=nodes
        for i in  nums[1:]:
            node=ListNode(i)
            tail.next=node
            tail=node
        return nodes

    def deleteNode(self,head):
        root=head
        while root.next:
            pnext=root.next
            curVal=root.val
            if curVal==pnext.val:
                root.next=pnext.next
            else:
                root=root.next
        self.printf(head)


    def printf(self,node):
        while node:
            print(node.val)
            node=node.next

if __name__ == '__main__':
    s=Solution()
    nums=[1,1,2,3,3]
    nodes=s.tail_insert(nums)
    f=s.deleteNode(nodes)