# -*- coding: utf-8 -*-
"""
@File    :   判断一个单链表中是否有环.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/7 15:30    1.0         None

给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。
"""
__author__ = 'haochen214934'

from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#解决思路使用快慢指针
class Solution:
    def hasCycle(self,head:ListNode)->bool: #尾插法
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow=head
        fast=head
        while slow and fast:
            slow=slow.next
            if fast.next:
                fast=fast.next.next
            else:
                return False
            if slow==fast:
                return True
        return False




if __name__ == '__main__':
    head = [3,2,0,-4]
    pos = 1
    s=Solution()

    ans=s.hasCycle(head)
    s.print_list(ans)
    # s.print_list(s.list_head(a))