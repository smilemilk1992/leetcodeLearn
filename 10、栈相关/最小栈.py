# -*- coding: utf-8 -*-
"""
@File    :   最小栈.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/4 14:29    1.0         None

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) – 将元素 x 推入栈中。
pop() – 删除栈顶的元素。
top() – 获取栈顶元素。
getMin() – 检索栈中的最小元素。

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); --> 返回 -3.
minStack.pop();
minStack.top(); --> 返回 0.
minStack.getMin(); --> 返回 -2.
"""
__author__ = 'haochen214934'

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lists=[]


    def push(self, x: int) -> None:#将元素 x 推入栈中。
        self.lists.insert(0,x)


    def pop(self) -> None:#删除栈顶的元素。
        self.lists.pop(0)


    def top(self) -> int:#获取栈顶元素。
        return self.lists[0]


    def getMin(self) -> int:#检索栈中的最小元素。
        return min(self.lists)


if __name__ == '__main__':
    s=MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    print(s.pop())
    print(s.top())
    print(s.getMin())
