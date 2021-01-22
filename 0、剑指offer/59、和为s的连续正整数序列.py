# -*- coding: utf-8 -*-
"""
@File    :   59、和为s的连续正整数序列.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/22 17:19    1.0         None
# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#  序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#
#  示例 1：
#  输入：target = 9
# 输出：[[2,3,4],[4,5]]
#  示例 2：
#  输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#
#  限制：
#  1 <= target <= 10^5
#
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res=[]
        low=1
        high=2
        while low<high:
            flag=[x for x in range(low,high+1)]
            if target>sum(flag):
                high=high+1
            elif target<sum(flag):
                low=low+1
            else:
                res.append([x for x in range(low,high+1)])
                high = high + 1
                low = low + 1
        return res

if __name__ == '__main__':
    s=Solution()
    target = 15
    s.findContinuousSequence(target)