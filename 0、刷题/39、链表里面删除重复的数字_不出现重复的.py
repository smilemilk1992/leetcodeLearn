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
        flag={}
        cc=[]
        while root:
            flag[root.val] = flag.get(root.val, 0) + 1
            root=root.next
        temp=sorted(flag.items(),key=lambda x:x[1])
        for k,v in temp:
            if v==1:
                cc.append(k)
        f=self.tail_insert(cc)
        self.printf(f)

    def deleteNode1(self,head):
        if not (head and head.next):
            return head
        dummy = ListNode(-1)
        dummy.next = head
        a = dummy
        b = head
        while b and b.next:
            # 初始化的时a指向的是哑结点，所以比较逻辑应该是a的下一个节点和b的下一个节点
            if a.next.val != b.next.val:
                a = a.next
                b = b.next
            else:
                # 如果a、b指向的节点值相等，就不断移动b，直到a、b指向的值不相等
                while b and b.next and a.next.val == b.next.val:
                    b = b.next
                a.next = b.next
                b = b.next
        self.printf(dummy.next)
        return dummy.next


    def printf(self,node):
        while node:
            print(node.val)
            node=node.next

if __name__ == '__main__':
    s=Solution()
    nums=[1,1,2,3,3,4,4,5]
    nodes=s.tail_insert(nums)
    f=s.deleteNode1(nodes)