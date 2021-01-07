# -*- coding: utf-8 -*-
"""
@File    :   test.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/11/18 14:03    1.0         None
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)  # 行
        n = len(grid[0])  # 列
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(m):
            dp[i][0]=dp[i-1][0]+grid[i][0]
        for j in range(n):
            dp[0][j]=dp[0][j-1]+grid[0][j]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=grid[i][j]+min(dp[i][j-1],dp[i-1][j])
        print(dp[-1][-1])


if __name__ == '__main__':
    s = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    s.minPathSum(grid)

