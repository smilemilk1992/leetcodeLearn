# -*- coding: utf-8 -*-
"""
@File    :   使数组唯一的最小增量.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/31 14:04    1.0         None
# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
#  返回使 A 中的每个值都是唯一的最少操作次数。
#
#  示例 1:
#  输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
#
#  示例 2:
#  输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
#
#  提示：
#  0 <= A.length <= 40000
#  0 <= A[i] < 40000
#
#  Related Topics 数组
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        res=0
        A.sort()
        flag=A[0]
        for i in range(1,len(A)):
            if A[i]<=flag:
                res=res+flag-A[i]+1
                A[i]=flag+1
            flag=A[i]
        return res


if __name__ == '__main__':
    s=Solution()
    A=[3,2,1,2,1,7]
    s.minIncrementForUnique(A)