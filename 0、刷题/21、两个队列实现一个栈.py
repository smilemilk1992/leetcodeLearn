# -*- coding: utf-8 -*-
"""
@File    :   21、两个队列实现一个栈.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/22 10:59    1.0         None
   使用两个队列数据结构实现一个栈，要求实现栈的出栈和进栈操作。
   push()操作：
       为了保证先进栈的元素一直在栈底，需要将两个队列交替使用，才能满足需求。因此，想法是，我们只在空的那个队列上添加元素，然后把非空的那个队列中的元素全部追加到当前这个队列。这样一来，我们又得到一个空的队列，供下一次添加元素。
    pop()操作：
       因为在添加元素时，我们已经按照进栈的先后顺序把后进栈的元素放在一个队列的头部，所以出栈操作时，我们只需要找到那个非空的队列，并依次取出数据即可。
"""
__author__ = 'haochen214934'

class StackWithTwoQueues(object):
    def __init__(self):
        self._queue1 = []
        self._queue2 = []

    def push(self, x):
        if len(self._queue1) == 0:
            self._queue1.append(x)
        elif len(self._queue2) == 0:
            self._queue2.append(x)
        if len(self._queue2) == 1 and len(self._queue1) >= 1:
            while self._queue1:
                self._queue2.append(self._queue1.pop(0))
        elif len(self._queue1) == 1 and len(self._queue2) > 1:
            while self._queue2:
                self._queue1.append(self._queue2.pop(0))

    def pop(self):
        if self._queue1:
            return self._queue1.pop(0)
        elif self._queue2:
            return self._queue2.pop(0)
        else:
            return None

    def getStack(self):
        print("queue1", self._queue1)
        print("queue2", self._queue2)


sta = StackWithTwoQueues()
sta.push(1)
sta.getStack()
sta.push(2)
sta.getStack()
sta.push(3)
sta.getStack()
sta.push(4)
sta.getStack()
print(sta.pop())
sta.getStack()
print(sta.pop())
sta.getStack()
print(sta.pop())
sta.getStack()