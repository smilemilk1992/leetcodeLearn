# -*- coding: utf-8 -*-
"""
@File    :   翻转矩阵.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/23 17:31    1.0         None
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    '''
    这个题的思路是:先将矩阵的第一行pop，再把剩余的矩阵翻转到需要的形式再进行pop循环，直到矩阵为空。
    强行用了一下numpy，感觉是这种小规模的东西用numpy是真的慢啊。。。也是我自己安排的有些麻烦

    设置顺时针方向
    遍历矩阵，根据边界和是否访问过该节点来更新方向
    '''

    def trans_matrix(self, matrix: List[List[int]]) -> List[int]:
        # 沿着中间列左右翻转
        for i in range(len(matrix)):
            for j in range(0, len(matrix[i]) // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][len(matrix[i]) - 1 - j]
                matrix[i][len(matrix[i]) - 1 - j] = temp

        # 沿着主对角线上下翻转
        for i in range(len(matrix)):
            for j in range(0, i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        return matrix


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    flag = s.trans_matrix(matrix)
    print(flag)
