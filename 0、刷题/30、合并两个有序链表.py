class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def tail_node(self,nums):
        head=ListNode(nums[0])
        tail=head
        for i in nums[1:]:
            node=ListNode(i)
            tail.next=node
            tail=node
        return head

    def merge(self,node1,node2):
        head=ListNode(-1)
        tail=head
        while node1 and node2:
            if node1.val<node2.val:
                tail.next=node1
                node1=node1.next
            else:
                tail.next=node2
                node2=node2.next
            tail=tail.next
        tail.next=node1 if node1 else node2
        return head.next

    def printf(self,nodes):
        while nodes:
            print(nodes.val)
            nodes=nodes.next


if __name__ == '__main__':
    s=Solution()
    num1=[1,3,5,7,9]
    num2=[2,4,6,8,10]
    node1=s.tail_node(num1)
    node2 = s.tail_node(num2)
    f=s.merge(node1,node2)
    s.printf(f)