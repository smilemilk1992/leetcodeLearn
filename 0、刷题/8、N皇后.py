# -*- coding: utf-8 -*-
"""
@File    :   8、N皇后.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/4 15:15    1.0         None
"""
__author__ = 'haochen214934'
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#  给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
#
#  每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
#  示例 1：
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#
#  示例 2：
#
# 输入：n = 1
# 输出：[["Q"]]
#
#  提示：
#
#  1 <= n <= 9
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
#
#  Related Topics 回溯算法
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [['.'] * n for i in range(n)]  # 创建棋盘
        queen = set()  # 存储皇后的位置索引
        output = []  # 存储最后的结果
        self.queenDFS(grid, 0, n, queen, output)
        return output

    def queenDFS(self, grid, index, n, queen, output):
        if index == n:
            solution = []
            for _, col in sorted(queen):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)
        for i in range(n):
            if self.isQueenOk(grid, index, i):
                queen.add((index, i))  # 进行选择
                grid[index][i] = 'Q'  # 进行选择
                self.queenDFS(grid, index + 1, n, queen, output)
                grid[index][i] = '.'  # 进行撤销
                queen.remove((index, i))  # 进行撤销

    def isQueenOk(self, grid, row, col):#判斷位置是否合法
        # 纵向合法性校验
        for i in range(row):
            if grid[i][col] == 'Q':
                return False
        # 主对角线合法性校验
        x = row - 1
        y = col - 1
        while x >= 0 and y >= 0:
            if grid[x][y] == 'Q':
                return False
            x -= 1
            y -= 1
        # 副对角线合法性校验
        x = row - 1
        y = col + 1
        while x >= 0 and y < len(grid[0]):
            if grid[x][y] == 'Q':
                return False
            x -= 1
            y += 1
        return True

if __name__ == '__main__':
    s=Solution()
    n=4
    f=s.solveNQueens(n)
    print(f)