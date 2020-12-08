'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''

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

    #快慢指针
    def revolve(self,head:ListNode,k:int)->ListNode:
        if not head and k<=0:
            return head
        slow = head
        fast = head
        while k>0 and fast:
            fast=fast.next
            k=k-1
        while fast.next:
            fast=fast.next
            slow=slow.next
        fast.next=head
        fast=slow.next # 4 5 6 指向头结点
        # print(self.print_item(fast))
        slow.next=None #截段 1 2 3 后面数 循环链表变为单链表
        return fast






    def print_item(self,head:ListNode):
        while head:
            print(head.val)
            head=head.next







if __name__ == '__main__':
    a=[1,2,3,4,5,6]
    s=Solution()
    l1=s.tail_add(a)
    r1=s.revolve(l1,3)
    s.print_item(r1)