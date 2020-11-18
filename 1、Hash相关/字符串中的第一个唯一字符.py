# -*- coding: utf-8 -*-
"""
@File    :   字符串中的第一个唯一字符.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/10/13 14:10    1.0         None
"""
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
#s = "leetcode"
#返回 0.
#s = "loveleetcode",
# 返回 2.

__author__ = 'haochen214934'

from typing import List


class Solution:
    def unique(self, s):
        map={}
        #第一步 将字符串存储到字典 重复的value设置为-1
        for i,v in enumerate(s):
            if v not in map.keys():
                map[v]=i
            else:
                map[v]=-1

        #第二步 根据value值大小进行升序排序 去掉value=-1的 第一个value就是我们要输出的值
        map=sorted(map.items(), key=lambda x: x[1], reverse=False)
        for k,v in map:
            if v!=-1:
                return v
        return -1




if __name__ == '__main__':
    s = "loveleetcode"
    a=Solution()
    result = a.unique(s)
    print(result)