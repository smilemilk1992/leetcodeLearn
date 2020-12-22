# -*- coding: utf-8 -*-
"""
@File    :   环形链表II.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/18 15:32    1.0         None
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
#  为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，po
# s 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
#  说明：不允许修改给定的链表。
#
#  进阶：
#  你是否可以使用 O(1) 空间解决此题？
#
#  示例 1：
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#  示例 2：
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#  示例 3：
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#
#  提示：
#  链表中节点的数目范围在范围 [0, 104] 内
#  -105 <= Node.val <= 105
#  pos 的值为 -1 或者链表中的一个有效索引
#
#  Related Topics 链表 双指针
"""
__author__ = 'haochen214934'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def add_tail(self,lists):
        head=ListNode(lists[0])
        tail=head
        for i in lists[1:]:
            node=ListNode(i)
            tail.next=node
            tail=node
        tail.next=head
        return head

    #快慢指针
    '''
    快慢指针（无额外空间）
    初始时，快慢指针同时指向头结点。
    若快指针且快指针的下一节点不为空，则慢指针走一步，快指针走两步；若某时，快慢指针相遇，标明链表有环；快慢指针相遇时，头结点与快慢指针相遇节点同步（每次走一步）向前走，直至再次相遇，该相遇节点为入环的第一个节点。
    若快指针或快指针的下一节点为空，标明链表无环，返回空。
    '''
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return None
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast==slow:
                while head != slow:
                    head = head.next
                    slow = slow.next
                return head
        return None

    #hash
    def hasCycle1(self, head: ListNode) -> ListNode:
        map={}
        while head:
            if head not in map.keys():
                map[head]=1
            else:
                return head
            head=head.next
        return None

    def items(self,head):
        if not head:
            return None
        while head:
            print(head.val)
            head=head.next

if __name__ == '__main__':
    head=[3,2,0,-4]
    s=Solution()
    tail=s.add_tail(head)
    cc=s.hasCycle(tail)
    s.items(cc)