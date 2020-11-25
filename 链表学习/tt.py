# -*- coding: utf-8 -*-
"""
@File    :   tt.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/11/25 17:04    1.0         None
"""
__author__ = 'haochen214934'

class Node:                                 #定义节点node
    def __init__(self,item):
        self.item = item
        self.next = None
def creat_list_head(list1):                 #头插法 先使新的节点指向头结点，再把头结点移到第一位
    head = Node(list1[0])
    for element in list1[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head
def creat_list_tail(list1):                 #尾插法 先使尾结点指向新的节点，再把尾结点移到最后
    head = Node(list1[0])
    tail = head
    for element in list1[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def find_node(head, position):  # 链表插入，先找到要插入的节点
    target_node = head			#目标节点从头开始寻找与想要插入的位置
    while target_node != None:
        if target_node.item == position:
            return target_node
        target_node = target_node.next
    return target_node


def Insert_node(head, target_node, num):  # 链表插入
    insert_node = Node(num)
    if not insert_node:
        return None
    insert_node.item= num
    insert_node.next = None
    if target_node == None:  				# 插入到第一个节点
        insert_node.next = head
        return insert_node
    else:
        if target_node.next == None:  		# 插入到最后一个节点
            target_node.next = insert_node
        else:
            insert_node.next = target_node.next		#插入到中间位置
            target_node.next = insert_node
    return head

def print_list(list2):                      #打印链表
    while list2:
        if  list2.next != None:
            print(list2.item, end='->')
        else:
            print(list2.item,end = '')
        list2 = list2.next
list1 = [1,2,3,4]
c1 = creat_list_head(list1)
print_list(c1)
print()
c2 = creat_list_tail(list1)
print_list(c2)
print()
print_list(find_node(c1,2))
