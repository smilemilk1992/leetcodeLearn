# -*- coding: utf-8 -*-
"""
@File    :   链表求和.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/2 14:57    1.0         None

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

对于逆序处理应该首先想到栈，对吧
"""
__author__ = 'haochen214934'

class Node(object):
    '''节点'''
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class AddLinkList(object):
    def __init__(self, node=None):  # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self._head = node

    def creat_list_tail(self, list):  #1->2->3->4 尾插法 先使尾结点指向新的节点，再把尾结点移到最后
        self._head=Node(list[0])
        tail=self._head
        for li in list[1:]:
            node=Node(li)
            tail.next=node
            tail=node
        return self._head

    def reversal(self,nodes): #单链表反转-就地反转 https://blog.csdn.net/gongliming_/article/details/88712221
        if nodes == None or nodes.next == None:  # 若链表为空或者仅一个数就直接返回
            return nodes
        pre = None
        while nodes!=None:
            next = nodes.next  # 1 将 nodes.next 赋值给 next 变量，即next 指向了节点2，先将节点2 保存起来。
            nodes.next = pre  # 2 将 pre 变量赋值给 nodes.next，即 此时节点1 指向了 None
            pre = nodes  # 3 将 nodes 赋值给了 pre，即 pre 指向节点1，将节点1 设为“上一个节点”
            nodes = next  # 4 将 next 赋值给 nodes，即 nodes 指向了节点2，此时节点2 设为“头节点”
        return pre


    def print_list(self,nodes):                      #打印链表
        while nodes:
            if  nodes.next != None:
                print(nodes.elem, end='->')
            else:
                print(nodes.elem,end = '')
            nodes = nodes.next

    def addTwoNumbers1(self,node1,node2):
        '''
        先转成list 然后计算两个整数和 在转为链表
        '''
        list1=[]
        list2=[]
        while node1!=None:
            list1.append(node1.elem)
            node1=node1.next
        while node2!=None:
            list2.append(node2.elem)
            node2=node2.next
        str1="".join(str(x) for x in list1)
        str2="".join(str(x) for x in list2)
        num=int(str1)+int(str2)
        res=self.creat_list_tail(list(str(num)))
        self.print_list(res)


if __name__ == '__main__':
    a=AddLinkList()
    list1 = [7,2,4,3]
    list2=[5,6,4]
    node1=a.creat_list_tail(list1)
    node2=a.creat_list_tail(list2)
    # a.print_list(node1)
    # print()
    # a.print_list(node2)
    # print()
    a.addTwoNumbers1(node1,node2)
    # a.print_list(a.reversal(node1))

