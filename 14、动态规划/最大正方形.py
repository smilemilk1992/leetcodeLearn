# -*- coding: utf-8 -*-
"""
@File    :   最大正方形.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/8 17:46    1.0         None
# 在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
#
#  示例 1：
#
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：4
#
#  示例 2：
#
# 输入：matrix = [["0","1"],["1","0"]]
# 输出：1
#
#  示例 3：
#
# 输入：matrix = [["0"]]
# 输出：0
#
#  提示：
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 300
#  matrix[i][j] 为 '0' 或 '1'
#
#  Related Topics 动态规划
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                elif i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) +1
                res=max(res,dp[i][j])
        return res**2

if __name__ == '__main__':
    s = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    f=s.maximalSquare(matrix)
    print(f)
