# -*- coding: utf-8 -*-
"""
@File    :   最小路径和.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/7 15:36    1.0         None
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
#  说明：每次只能向下或者向右移动一步。
#
#  示例 1：
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#
#  示例 2：
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#
#  提示：
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 200
#  0 <= grid[i][j] <= 100
#
#  Related Topics 数组 动态规划

题目要求只能往下或者向右走。

则单元格dp(i,j）题解应该是单元格dp（i-1,j）单元格dp（i，j-1）的较小值+单元格（i,j）的值。
考虑特殊情况边界问题：
（1）左边为边界，即i=0情况下，单元格dp(i,j）题解只能从上面来
解为单元格dp（i，j-1）+单元格（i,j）的值。
(2)上边为边界,即j=0情况下。解只能从左边来。解为单元格dp（i-1，j）+单元格（i,j）的值。
（3）上下都是边界，即处于起点位置，直接返回坐标（i,j）。
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid) #行
        n=len(grid[0]) #列
        # 定义 dp 数组
        dp = [[0] * (n) for _ in range(m)]

        # 初始化
        dp[0][0] = grid[0][0]
        # 对第一行和第一列进行处理
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    s=Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    s.minPathSum(grid)