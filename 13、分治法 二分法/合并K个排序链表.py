# 给你一个链表数组，每个链表都已经按升序排列。
#
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
#  示例 1：
#
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
#  示例 2：
#  输入：lists = []
# 输出：[]
#
#
#  示例 3：
#  输入：lists = [[]]
# 输出：[]
#
#  提示：
#
#  k == lists.length
#  0 <= k <= 10^4
#  0 <= lists[i].length <= 500
#  -10^4 <= lists[i][j] <= 10^4
#  lists[i] 按 升序 排列
#  lists[i].length 的总和不超过 10^4
#
#  Related Topics 堆 链表 分治算法
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def tail_insert(self,lists):
        head=ListNode(lists[0])
        tail=head
        for li in lists[1:]:
            node=ListNode(li)
            tail.next=node
            tail=node
        return head
    #暴力法
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        res=[]
        for li in lists:
            while li:
                res.append(li.val)
                li=li.next
        res.sort()
        l=ListNode(0)
        tail=l
        for r in res:
            node=ListNode(r)
            tail.next=node
            tail=node
        return l.next

    #分治法
    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        n=len(lists)
        if n==0:
            return None
        if n==1:
            return lists[0]
        l1=lists[0]
        l2=lists[1]
        # 两两比较
        # newNode = self.mergeTwoLists(l1, l2)
        # for i in lists[2:]:
        #     newNode = self.mergeTwoLists(newNode, i)
        # return newNode
        i = 1
        while i < n:
            j = 0
            while j + i < n:
                lists[j] = self.mergeTwoLists(lists[j], lists[j + i])
                j += i * 2
            i *= 2
        return lists[0]

    def mergeTwoLists(self,l1,l2):
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
        tail.next=l1 if l1 else l2
        return head.next


    def printf(self,node):
        while node:
            print(node.val)
            node=node.next

if __name__ == '__main__':
    s=Solution()
    a=[1,4,5]
    b=[1,3,4]
    c=[2,6]
    an=s.tail_insert(a)
    bn=s.tail_insert(b)
    cn=s.tail_insert(c)
    lists=[]
    lists.append(an)
    lists.append(bn)
    lists.append(cn)
    flag=s.mergeKLists1(lists)
    s.printf(flag)
