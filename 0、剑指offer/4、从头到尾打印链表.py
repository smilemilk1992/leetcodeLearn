# 输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
#
#
#
#  示例 1：
#
#  输入：head = [1,3,2]
# 输出：[2,3,1]
#
#
#
#  限制：
#
#  0 <= 链表长度 <= 10000
#  Related Topics 链表
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        c = self.reversed1(head)
        while c:
            res.append(c.val)
            c = c.next
        return res

    #链表反转
    def reversed1(self, node):  # https://blog.csdn.net/qq_17550379/article/details/80647926
        # 链表反转-非递归实现 就地反转，遍历链表，逐个逆转 时间复杂度O(n) 1->2->3->4
        if node is None or node.next is None:
            return node
        pre = None
        cur = node
        while cur is not None:
            p = cur.next
            cur.next = pre
            pre = cur
            cur = p
        return pre



