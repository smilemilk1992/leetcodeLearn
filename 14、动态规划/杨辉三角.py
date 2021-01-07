# -*- coding: utf-8 -*-
"""
@File    :   杨辉三角.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/7 17:23    1.0         None
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#  在杨辉三角中，每个数是它左上方和右上方的数的和。
#
#  示例:
#  输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#  Related Topics 数组
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp=[]
        for i in range(1,numRows+1):
            if i<=2:
                dp.append([1]*i)
            else:
                dp.append([1]+[0]*(i-2)+[1])
        for i in range(0,numRows):
            for j in range(i+1):
                if dp[i][j]==0:
                    dp[i][j]=dp[i-1][j-1]+dp[i-1][j]

        return dp

if __name__ == '__main__':
    s=Solution()
    numRows=2
    s.generate(numRows)