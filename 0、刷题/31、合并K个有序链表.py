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

    def merge(self,nodes):
        if len(nodes)<=1:
            return nodes[0]
        mid=len(nodes)//2
        left=self.merge(nodes[:mid])
        right=self.merge(nodes[mid:])
        return self.mergeSort(left,right)

    def mergeSort(self,left,right):
        head=ListNode(-1)
        tail=head
        while left and right:
            if left.val<=right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next
        tail.next= left if left else right
        return head.next


    def printf(self,nodes):
        while nodes:
            print(nodes.val)
            nodes=nodes.next


if __name__ == '__main__':
    s=Solution()
    nums=[[1,2,3],[2,3,5],[6,7,9],[7,8,9],[3,5,6]]
    nodes=[]
    for n in nums:
        nodes.append(s.tail_node(n))
    f=s.merge(nodes)
    s.printf(f)