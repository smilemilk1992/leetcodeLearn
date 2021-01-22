# -*- coding: utf-8 -*-
"""
@File    :   63、队列最大值.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/22 18:14    1.0         None
# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都
# 是O(1)。
#
#  若队列为空，pop_front 和 max_value 需要返回 -1
#  示例 1：
#  输入:
# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# [[],[1],[2],[],[],[]]
# 输出: [null,null,null,2,1,2]
#
#  示例 2：
#  输入:
# ["MaxQueue","pop_front","max_value"]
# [[],[],[]]
# 输出: [null,-1,-1]
#
#  限制：
#  1 <= push_back,pop_front,max_value的总操作数 <= 10000
#  1 <= value <= 10^5
#
#  Related Topics 栈 Sliding Window
"""
__author__ = 'haochen214934'

class MaxQueue:
    def __init__(self):
        self.list = []

    def max_value(self) -> int:
        if not self.list:
            return -1
        return max(self.list)

    def push_back(self, value: int) -> None:
        self.list.append(value)

    def pop_front(self) -> int:
        if not self.list:
            return -1
        return self.list.pop(0)
