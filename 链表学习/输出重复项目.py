# -*- coding: utf-8 -*-
"""
@File    :   输出重复项目.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/3 16:40    1.0         None
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

    def node_tail(self,lists):
        self._head=Node(lists[0])
        tail=self._head
        for li in lists[1:]:
            node=Node(li)
            tail.next=node
            tail=node
        return self._head

    def removeDup(self,node):#[1, 2, 3, 4,1,5,4,6,1] 从有序列表里面删除重复项目
        if node == None or node.next == None:
            return
        outcur = node
        while outcur != None:
            incur = outcur.next
            incurpre = outcur
            while incur != None:
                if incur.elem == outcur.elem:
                    incurpre.next = incur.next
                else:
                    incurpre = incur
                incur = incur.next
            outcur = outcur.next
        return node

    def printfs(self,node):
        if node==None:
            return
        print(node.elem)
        self.printfs(node.next)


if __name__ == '__main__':
    s=SingleLinkList()
    list1 = [1, 2, 3, 4,1,5,4,1,2,6]
    c1 = s.node_tail(list1)
    move=s.removeDup(c1)
    s.printfs(move)
