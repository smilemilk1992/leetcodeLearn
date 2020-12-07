# -*- coding: utf-8 -*-
"""
@File    :   循环链表.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/4 9:52    1.0         None
"""
__author__ = 'haochen214934'

class Node(object):
    '''节点'''
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleCycleLinkList(object):
    def __init__(self, node=None):  # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self._head = node

    def is_empty(self):
        if self._head is None:
            return True
        return False

    def length(self):
        count=0
        if self.is_empty():
            return count
        cur=self._head
        while cur is not None:
            if cur.next==self._head:
                break
            count=count+1
            cur= cur.next
        return count

    def head(self,item):#在头部添加元素
        flag=Node(item)
        if self.is_empty():  # 为空
            self._head = flag
            flag.next = self._head
        else: #当前节点指向头结点  尾节点指向单前节点
            flag.next=self._head
            cur=self._head
            while cur.next!=self._head:
                cur=cur.next
            cur.next=flag
            self._head=flag  #当前指针作为头指针

    def tail(self,item):#在尾部添加元素
        node = Node(item)
        if self.is_empty():
            self._head=node
            node.next=self._head
        else:
            cur = self._head
            while cur.next!=self._head:
                cur=cur.next
            # 尾部指针指向新结点
            cur.next = node
            # 新结点指针指向head
            node.next=self._head

    def insert(self,index,item):#指定位置添加节点
        if index<=0: #头部插入
            self.head(item)
        elif index>=self.length():#尾部插入
            self.tail(item)
        else:#中间插入
            node = Node(item)
            cur = self._head
            # 移动到添加结点位置
            for i in range(index - 1):
                cur = cur.next
            # 新结点指针指向旧结点
            node.next = cur.next
            # 旧结点指针 指向 新结点
            cur.next = node

    def remove1(self,item):#删除链表里面值
        if self.is_empty():
            return
        cur=self._head
        if cur.next==self._head:#只有一个元素的时候
            if cur.elem==item:
                self._head=None
        elif cur.elem==item:#考虑头部元素
            while cur.next!=self._head:
                cur = cur.next
            cur.next=self._head.next
            self._head=self._head.next #调整头部节点位置
        else:
            while cur.next!=self._head:
                flag=cur.next
                if flag.elem==item:
                    cur.next=flag.next
                else:
                    cur=cur.next

    def find(self,item):#查询一个元素是否存在
        cur=self._head
        while cur.next!=self._head:
            if cur.elem==item:
                return True
            cur=cur.next
        return False

    def items(self):#遍历打印
        node=self._head
        while node:
            if node.elem is not None:
                print(node.elem,end=" ")
            node=node.next


if __name__ == '__main__':
    link_list = SingleCycleLinkList()
    print(link_list.is_empty())
    # 头部添加元素
    # for i in range(5):
    #     link_list.head(i)
    # link_list.items()

    # 尾部添加元素
    for i in range(6):
        link_list.tail(i)
    # link_list.insert(2,123)
    link_list.remove1(0)
    # link_list.items()
    print(link_list.find(4))