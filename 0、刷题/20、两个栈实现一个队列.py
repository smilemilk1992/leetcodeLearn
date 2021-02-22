# -*- coding: utf-8 -*-
"""
@File    :   20、两个栈实现一个队列.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/22 10:54    1.0         None
入队：元素进栈A
出队：先判断栈B是否为空，为空则将栈A中的元素 pop 出来并 push 进栈B，再栈B出栈，如不为空则栈B直接出栈
"""
__author__ = 'haochen214934'
class Queue:
    def __init__(self):
        self.stockA=[]
        self.stockB=[]

    def push(self,node):#元素A进栈
        self.stockA.append(node)
    def pop(self):
        if self.stockB==[]:
            if self.stockA==[]:
                return None
            else:
                for i in range(len(self.stockA)):
                    self.stockB.append(self.stockA.pop())
        return self.stockB.pop()