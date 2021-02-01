# -*- coding: utf-8 -*-
"""
@File    :   4、数组topN.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/1 14:56    1.0         None
面试题：
要的还是讲解自己认为有技术难点的项目，然后根据项目技术难点展开，问一下用什么方案解决的，为什么使用这个方案，
还有如果生产上出现问题，页面打不开，访问缓慢，这些问题你是怎么解决的，还会给出一两个算法题，不过面试官会问你的解题思路。
中间还会穿插的问一下相关技术的原理，以及有什么优点，最好是找自己项目运用过的技术，以及懂得相关原理的。
问了一个系统设计，还有一个小的技术问题（二位数组的读取效率）。
算法题：
一面的笔试题：给一个字符串表示的数字，通过移动字符串中的数字得到第一个大于原数的数字；
二面的笔试题：给一个字符串，找出最长无重复字符子串；
"""
__author__ = 'haochen214934'


class Solution:
    def topN(self, Lists, k):
        m=len(Lists)
        n=len(Lists[0])
        res=[Lists[0][0]]
        for i in range(1,m):
            for j in range(1,n):
                print(Lists[i][j])



if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1,  4,  7,  11, 15],
        [2,  5,  8,  12, 19],
        [3,  6,  9,  16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    k = 2
    s.topN(matrix, k)
