# -*- coding: utf-8 -*-
"""
@File    :   11、矩阵中的路径-head.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/11 16:46    1.0         None
# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果
# 一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
#
#  [["a","b","c","e"],
# ["s","f","c","s"],
# ["a","d","e","e"]]
#
#  但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
#
#  示例 1：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CCED"
# 输出：true
#
#  示例 2：
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#
#  提示：
#
#  1 <= board.length <= 200
#  1 <= board[i].length <= 200
#  注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
#  Related Topics 深度优先搜索
"""
__author__ = 'haochen214934'

from typing import List

'''
方法一：深度优先搜索
思路与算法

设函数 \text{check}(i, j, k)check(i,j,k) 判断以网格的 (i, j)(i,j) 位置出发，能否搜索到单词 \text{word}[k..]word[k..]，其中 \text{word}[k..]word[k..] 表示字符串 \text{word}word 从第 kk 个字符开始的后缀子串。如果能搜索到，则返回 \text{true}true，反之返回 \text{false}false。函数 \text{check}(i, j, k)check(i,j,k) 的执行步骤如下：

如果 \text{board}[i][j] \neq s[k]board[i][j] =s[k]，当前字符不匹配，直接返回 \text{false}false。
如果当前已经访问到字符串的末尾，且对应字符依然匹配，此时直接返回 \text{true}true。
否则，遍历当前位置的所有相邻位置。如果从某个相邻位置出发，能够搜索到子串 \text{word}[k+1..]word[k+1..]，则返回 \text{true}true，否则返回 \text{false}false。
这样，我们对每一个位置 (i,j)(i,j) 都调用函数 \text{check}(i, j, 0)check(i,j,0) 进行检查：只要有一处返回 \text{true}true，就说明网格中能够找到相应的单词，否则说明不能找到。

为了防止重复遍历相同的位置，需要额外维护一个与 \text{board}board 等大的 \text{visited}visited 数组，用于标识每个位置是否被访问过。每次遍历相邻位置时，需要跳过已经被访问的位置。
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))
            return result
        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    s=Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    f=s.exist(board,word)
    print(f)