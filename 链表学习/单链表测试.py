# -*- coding: utf-8 -*-
"""
@File    :   单链表测试.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/1 15:58    1.0         None
"""
__author__ = 'haochen214934'
class Node(object):
    '''节点'''
    def __init__(self,elem):
        self.elem=elem
        self.next=None


class SingleLinkList(object):
    '''单链表'''
    def __init__(self,node=None): # 使用一个默认参数，在传入头结点时则接收，在没有传入时，就默认头结点为空
        self._head=node

    def is_empty(self):
        '''链表是否为空'''
        return self._head==None

    def length(self):
        '''链表长度'''
        cur=self._head
        count=0
        while cur!=None:
            count = count + 1
            cur=cur.next
        return count


    def travel(self):
        '''遍历整个列表'''
        cur=self._head
        while cur!=None:
            print(cur.elem,end=" ")
            cur=cur.next

    def head(self, item):
        '''链表头部添加元素'''
        flag=Node(item)
        flag.next=self._head
        self._head=flag

    def tail(self, item):
        '''链表尾部添加元素'''
        flag = Node(item)
        if self.is_empty():# 由于特殊情况当链表为空时没有next，所以在前面要做个判断
            self.__head = flag
        else:
            cur=self._head
            while cur!=None: #一直遍历到最后一个
                if not cur.next: #最后一个就退出
                    break
                cur=cur.next
            cur.next=flag

    def insert(self, index, item):
        '''指定位置添加元素'''
        if index<=0:#判断是否头插
            self.head(item)
        elif index>=self.length():#判断是否尾部插入
            self.tail(item)
        else:#中间插入
            flag=Node(item)
            cur=self._head
            count=0
            while cur!=None:
                if count==index:
                    flag.next=cur.next
                    cur.next=flag
                    break
                else:
                    cur=cur.next
                    count=count+1


    def remove(self, item):
        '''删除节点'''
        if self.is_empty() or not self.search(item):
            return False
        cur=self._head
        while cur!=None:
            if item==self._head.elem:#考虑头节点
                self._head=cur.next
                return True
            elif cur.next.elem==item:
                cur.next=cur.next.next
                return True
            else:
                cur=cur.next
        return False


    def search(self, item):
        '''查找节点是否存在'''
        cur=self._head
        while cur!=None:
            if cur.elem==item:
                return True
            cur=cur.next
        return False

if __name__ == '__main__':
    # node = Node(100)  # 先创建一个节点传进去
    ll = SingleLinkList()
    ll.head(111)
    ll.head(222)
    ll.tail(333)
    ll.tail(3333)
    ll.head(1)
    ll.insert(-3,345)
    ll.remove(33333)
    print(ll.is_empty())
    print(ll.length())
    ll.travel()