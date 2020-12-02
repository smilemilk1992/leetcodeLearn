# -*- coding: utf-8 -*-
"""
@File    :   单链表测试1.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/1 18:07    1.0         None
"""
__author__ = 'haochen214934'

class Node(object):
    '''节点'''
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleLinkList(object):
    def __init__(self, node=None):  # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self._head = node

    def creat_list_head(self,list): #4->3->2->1  头插法 先使新的节点指向头结点，再把头结点移到第一位
        for li in list:
            node=Node(li)
            node.next=self._head
            self._head=node
        return self._head


    def creat_list_tail(self,list): #1->2->3->4 尾插法 先使尾结点指向新的节点，再把尾结点移到最后
        self._head=Node(list[0])
        tail=self._head
        for li in list[1:]:
            node = Node(li)
            tail.next=node
            tail=node
        return self._head

    def creat_list_tail1(self,list): #1->2->3->4 尾插法 先使尾结点指向新的节点，再把尾结点移到最后
        ans=None
        for li in list:
            node = Node(li)
            node.next=ans
            ans=node
        return ans


    def print_list(self,nodes):                      #打印链表
        while nodes:
            if  nodes.next != None:
                print(nodes.elem, end='->')
            else:
                print(nodes.elem,end = '')
            nodes = nodes.next
if __name__ == '__main__':
    s=SingleLinkList()
    list1 = [1, 2, 3, 4]
    c1 = s.creat_list_head(list1)
    s.print_list(c1)

    c2 = s.creat_list_tail1(list1)
    s.print_list(c2)