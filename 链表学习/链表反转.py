class Node(object):
    '''节点'''
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleLinkList(object):
    def __init__(self, node=None):  # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self._head = node

    def reversed1(self,node):
        #链表反转-非递归实现 就地反转，遍历链表，逐个逆转 时间复杂度O(n) 1->2->3->4
        if node is None or node.next is None:
            return node
        pre=None
        cur=node
        while cur is not None:
            p=cur.next
            cur.next=pre
            pre=cur
            cur=p
        return pre


    def reversed2(self,node):
        #链表反转-递归实现 不断逆转当前结点，直到链表尾端，时间复杂度O(n) 1->2->3->4
        if node is None or node.next is None:
            return node
        pnext = node.next
        node.next = None
        reversed = self.reversed2(pnext)
        pnext.next = node
        return reversed


    def reversed3(self,node,pre=None):
        #链表反转-递归实现 不过递归传入当前结点和前序结点，代码可读性要好点，时间复杂度O(n) 1->2->3->4
        if node is None or node.next is None:
            return node
        if node.next is None:
            node.next = pre
            return node
        else:
            pnext = node.next
            node.next = pre
            return self.reversed3(pnext, node)



    def tail_node(self,lists):#list 转链表  尾部添加 1->2->3->4
        head=Node(lists[0])
        tail=head
        for li in lists[1:]:
            node=Node(li)
            tail.next=node
            tail=node
        return head


    def printfs(self,node):#遍历
        while node is not None:
            if node.next is not None:
                print(node.elem,end="->")
            else:
                print(node.elem, end="")
            node=node.next

if __name__ == '__main__':
    s=SingleLinkList()
    lists=[1,2,3,4]
    node1=s.tail_node(lists)
    node=s.reversed3(node1)
    s.printfs(node)