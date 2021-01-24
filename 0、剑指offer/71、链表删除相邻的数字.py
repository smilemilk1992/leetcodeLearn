'''
给定一个链表，删除相邻相同数据项。比如2->2->3 返回2->3
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def tailNode(self,lists):
        head=ListNode(lists[0])
        tail=head
        for i in lists[1:]:
            node=ListNode(i)
            tail.next=node
            tail=node
        return head

    def filter(self, root: ListNode) -> ListNode:
        head=root
        while head and head.next:
            if head.val==head.next.val:
                head.next=head.next.next
            else:
                head=head.next
        return root

    def printf(self,root):
        while root:
            print(root.val)
            root=root.next

if __name__ == '__main__':
    s=Solution()
    nums=[1,1,1,1,1,1,2,3,3,4,5,5]
    root=s.tailNode(nums)
    f=s.filter(root)
    s.printf(f)