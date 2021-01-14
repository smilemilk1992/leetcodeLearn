# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
#
#  示例1：
#
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#
#  限制：
#
#  0 <= 链表长度 <= 1000
#
#  注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/
#  Related Topics 分治算法

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
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