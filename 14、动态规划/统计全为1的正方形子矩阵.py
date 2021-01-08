# -*- coding: utf-8 -*-
"""
@File    :   统计全为1的正方形子矩阵.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/8 17:19    1.0         None
# 给你一个 m * n 的矩阵，矩阵中的元素不是 0 就是 1，请你统计并返回其中完全由 1 组成的 正方形 子矩阵的个数。
#
#  示例 1：
#  输入：matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# 输出：15
# 解释：
# 边长为 1 的正方形有 10 个。
# 边长为 2 的正方形有 4 个。
# 边长为 3 的正方形有 1 个。
# 正方形的总数 = 10 + 4 + 1 = 15.

#  示例 2：
#  输入：matrix =
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# 输出：7
# 解释：
# 边长为 1 的正方形有 6 个。
# 边长为 2 的正方形有 1 个。
# 正方形的总数 = 6 + 1 = 7.
#
#  提示：
#  1 <= arr.length <= 300
#  1 <= arr[0].length <= 300
#  0 <= arr[i][j] <= 1
#
#  Related Topics 数组 动态规划
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    #实际上最大正方形边长就是以(i,j)为右下角的正方形个数。我们只需要将所有边长加起来即可。
    def countSquares(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                res += dp[i][j]
        print(dp)
        return res

if __name__ == '__main__':
    s=Solution()
    m=[
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]
    f=s.countSquares(m)
    print(f)