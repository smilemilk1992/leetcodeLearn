# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
#
#  进阶：你能尝试使用一趟扫描实现吗？
#
#
#
#  示例 1：
#
#
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
#
#
#  示例 2：
#
#
# 输入：head = [1], n = 1
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：head = [1,2], n = 1
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  链表中结点的数目为 sz
#  1 <= sz <= 30
#  0 <= Node.val <= 100
#  1 <= n <= sz
#
#  Related Topics 链表 双指针

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def tail(self,lists):
        head=ListNode(lists[0])
        tail=head
        for i in lists[1:]:
            node=ListNode(i)
            tail.next=node
            tail=node
        return head

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res=self.checkLen(head)
        if res==0:
            return None
        if n==res:
            return head.next
        flag=res-n
        root=head
        while flag>1:
            root=root.next
            flag=flag-1
        root.next=root.next.next
        return head


    def checkLen(self,head):
        res=0
        while head:
            res=res+1
            head=head.next
        return res

    def printf(self,head):
        while head:
            print(head.val)
            head=head.next

if __name__ == '__main__':
    s=Solution()
    list = [1, 2, 3, 4, 5]
    n = 1
    head=s.tail(list)
    f=s.removeNthFromEnd(head,n)
    s.printf(f)

