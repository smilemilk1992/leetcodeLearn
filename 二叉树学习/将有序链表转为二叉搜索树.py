# -*- coding: utf-8 -*-
"""
@File    :   将有序链表转为二叉搜索树.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/10 10:15    1.0         None

# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
#  示例:
#
#  给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#  Related Topics 深度优先搜索 链表
"""
__author__ = 'haochen214934'

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def tail(self,lists)->ListNode: #改为有序单链表
        root=ListNode(lists[0])
        tail=root

        for li in lists[1:]:
            node=ListNode(li)
            tail.next=node
            tail=node
        return root

    '''
    我们知道，二叉搜索树（BST）中序遍历就是升序序列，那么我们可以从这个角度出发，那么问题就转变为从中序遍历的序列中恢复二叉搜索树。
    那么任选一个元素作为根节点，以元素左边的序列构建左子树，右边序列构建右子树。
    但是由于有限制条件，需要转换为高度平衡二叉树，根据前面给出高度平衡二叉树的概念。那么我们考虑选择数组的中间元素作为根节点来代替前面的任意选择一个元素。
    '''

    def findMidNode(self, head):#快慢指针
        if not head:
            return None
        fast, slow = head, head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if pre:  # 将中间节点的上一个节点指向None，即将原链表在中间节点处拆开 head
            pre.next = None
        return slow

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        mid = self.findMidNode(head) # 调用后原链表被拆开
        root = TreeNode(mid.val)
        if mid==head:
            return root
        root.left=self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root

    def list2link(self, lists):
        if not lists:
            return None
        root=ListNode(lists[0])
        tail=root
        for li in lists[1:]:
            node=ListNode(li)
            tail.next=node
            tail=node
        return root

    def sortedListToBST1(self, head: ListNode) -> TreeNode:#转数组 在转为二叉搜索树 需要额外开辟空间
        if not head:
            return None
        lists=[]
        cur=head
        while cur:
            lists.append(cur.val)
            cur=cur.next
        mid=len(lists)//2
        root=TreeNode(lists[mid])
        root.left=self.sortedListToBST1(self.list2link(lists[:mid]))
        root.right=self.sortedListToBST1(self.list2link(lists[mid+1:]))
        return root

    def printf(self, head: TreeNode):  # 中序遍历
        if head.left:
            self.printf(head.left)
        if head:
            print(head.val)
        if head.right:
            self.printf(head.right)


if __name__ == '__main__':
    a = [1,2,3,4,5,6]
    s = Solution()
    l1 = s.tail(a)
    l2=s.sortedListToBST(l1)
    s.printf(l2)