# -*- coding: utf-8 -*-
"""
@File    :   46、礼物的最大价值.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/18 17:08    1.0         None
# 在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直
# 到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
#
#
#
#  示例 1:
#
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 12
# 解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
#
#  提示：
#  0 < grid.length <= 200
#  0 < grid[0].length <= 200
#
#  Related Topics 动态规划
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)  # 行
        n = len(grid[0])  # 列
        # 定义 dp 数组
        dp = [[0] * (n) for _ in range(m)]
        print(dp)
        # 初始化
        dp[0][0] = grid[0][0]
        # 对第一行和第一列进行处理
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[-1][-1]

if __name__ == '__main__':
    s=Solution()
    grid=[[1,3,1],[1,5,1],[4,2,1]]
    f=s.maxValue(grid)
    print(f)