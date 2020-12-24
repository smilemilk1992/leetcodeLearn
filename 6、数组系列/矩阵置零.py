# -*- coding: utf-8 -*-
"""
@File    :   矩阵置零.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/23 18:02    1.0         None
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
#
#  示例 1:
#
#  输入:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出:
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#
#
#  示例 2:
#
#  输入:
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出:
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#
#  进阶:
#  一个直接的解决方案是使用 O(mn) 的额外空间，但这并不是一个好的解决方案。
#  一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
#  你能想出一个常数空间的解决方案吗？
#
#  Related Topics 数组
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    '''
    即分别定义两个list : zeroLine 和 zeroRow来储存出现零的位置。
    '''
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lenrow = len(matrix)
        lencol = len(matrix[0])
        zeroRow = [False] * lenrow
        zeroCol = [False] * lencol

        for l in range(lenrow):
            for r in range(lencol):
                if matrix[l][r] == 0:
                    zeroRow[l] = True
                    zeroCol[r] = True

        for l in range(lenrow):
            if zeroRow[l] is True:
                matrix[l] = [0] * lencol
            else:
                for r in range(lencol):
                    if zeroCol[r] is True:
                        matrix[l][r] = 0
        return matrix

    def setZeroes1(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        flagRow=[False]*row
        flagCol=[False]*col
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    flagRow[i]=True
                    flagCol[j]=True

        for i in range(row):
            if flagRow[i]==True:
                matrix[i]=[0]*col
            else:
                for j in range(col):
                    if flagCol[j]==True:
                        matrix[i][j]=0
        return matrix

if __name__ == '__main__':
    s = Solution()
    matrix = [
        [0, 1, 2, 0],
        [3, 4, 0, 2],
        [1, 3, 1, 5]
    ]
    flag = s.setZeroes1(matrix)
    print(flag)

