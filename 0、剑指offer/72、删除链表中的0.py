'''
给定一个链表，其中元素只有0和1，删除0的节点，并返回链表
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
            if head.val==0:#删除头节点
                root=head.next
                head=root
            elif head.next.val==0:#删除其余节点
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
    nums=[0,0,0,1,1,0,0,0,1,1,0,1,0,1,0,0,0]
    root=s.tailNode(nums)
    f=s.filter(root)
    s.printf(f)