# -*- coding: utf-8 -*-
"""
@File    :   双向链表.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/7 13:55    1.0         None
"""
__author__ = 'haochen214934'

class Node(object):
    '''节点'''
    def __init__(self,elem):
        self.elem=elem
        # 前驱区
        self.prev = None
        # 后继区
        self.next = None

class SingleTwoWayLinkList(object):
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
            count=count+1
            cur= cur.next
        return count

    def head(self,item):#在头部添加元素
        flag=Node(item)
        if self.is_empty():  # 为空
            self._head = flag
        else:
            # 待插入节点的后继区指向原头节点
            flag.next=self._head
            # 原头节点的前驱区指向待插入节点
            self._head.prev=flag
            self._head=flag

    def tail(self,item):#在尾部添加元素
        node = Node(item)
        if self.is_empty():
            self._head=node
        else:
            cur = self._head
            while cur.next is not None:
                cur=cur.next
            # 尾部指针指向新结点
            cur.next = node
            #新节点前驱区指向当前节点
            node.prev=cur


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
            #-->
            node.next = cur.next
            #<--
            cur.next.prev=node
            #<--
            node.prev=cur
            #-->
            cur.next = node

    def remove1(self,item):#删除链表里面值
        if self.is_empty():
            return
        cur=self._head
        if cur.next==self._head:#只有一个元素的时候
            if cur.elem==item:
                self._head=None
        elif cur.elem==item:#考虑头部元素
            self._head=cur.next #调整头部节点位置
        else:#考虑尾部的情况
            while cur.next is not None:
                flag=cur.next
                if flag.elem==item:
                    cur.next=flag.next
                    if flag.next is not None:
                        flag.next.prev=cur
                else:
                    cur=cur.next

    def find(self,item):#查询一个元素是否存在
        cur=self._head
        while cur is not None:
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
    link_list = SingleTwoWayLinkList()
    print(link_list.is_empty())
    print(link_list.length())
    # 头部添加元素
    # for i in range(5):
    #     link_list.head(i)

    # 尾部添加元素
    for i in range(6):
        link_list.tail(i)
    link_list.insert(2,9)
    link_list.remove1(0)
    link_list.items()
    print(link_list.find(5))
