# -*- coding: utf-8 -*-
"""
@File    :   最大矩阵.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/8 17:59    1.0         None
# 给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
#  示例 1：
# 输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"]
# ,["1","0","0","1","0"]]
# 输出：6
# 解释：最大矩形如上图所示。
#
#  示例 2：
# 输入：matrix = []
# 输出：0
#
#  示例 3：
# 输入：matrix = [["0"]]
# 输出：0
#
#  示例 4：
# 输入：matrix = [["1"]]
# 输出：1
#
#  示例 5：
# 输入：matrix = [["0","0"]]
# 输出：0
#
#  提示：
#  rows == matrix.length
#  cols == matrix[0].length
#  0 <= row, cols <= 200
#  matrix[i][j] 为 '0' 或 '1'
#
#  Related Topics 栈 数组 哈希表 动态规划
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        maxarea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                width = dp[i][j] = dp[i][j - 1] + 1 if j else 1  # 计算最大宽度并使用它更新dp
                for k in range(i, -1, -1):  # 倒序遍历每一行
                    width = min(width, dp[k][j])  # 最小宽度（同一列 上下几行的最小【最大宽度】）
                    maxarea = max(maxarea, width * (i - k + 1))  # 同一列上下几行的最小【最大宽度】*行数=当前行最大面积
        return maxarea

if __name__ == '__main__':
    s = Solution()
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]]
    f=s.maximalRectangle(matrix)
    print(f)
