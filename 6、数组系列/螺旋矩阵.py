# -*- coding: utf-8 -*-
"""
@File    :   螺旋矩阵.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/23 16:45    1.0         None
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
#  示例 1:
#  输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
# 输出: [1,2,3,6,9,8,7,4,5]
#
#  示例 2:
#  输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#  Related Topics 数组
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

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return None
        rs=[]
        m=len(matrix)
        n=len(matrix[0])
        visited = [[None for x in range(n)] for x in range(m)]
        print(visited)
        i=0 #横坐标
        j=0 #纵坐标
        direction=1 # 1:右 2:下 3:左 4:上
        while True:
            if i<0 or j<0 or i==m or j==n or visited[i][j]:
                break
            rs.append(matrix[i][j])
            visited[i][j]=True
            if direction==1:
                if j+1==n or visited[i][j + 1]:
                    i=i+1
                    direction=2
                else:
                    j=j+1
            elif direction==2:
                if i+1==m or visited[i+1][j]:
                    j=j-1
                    direction=3
                else:
                    i=i+1
            elif direction==3:
                if j==0 or visited[i][j-1]:
                    i=i-1
                    direction=4
                else:
                    j=j-1
            elif direction==4:
                if visited[i-1][j]:
                    j=j+1
                    direction=1
                else:
                    i=i-1
            else:
                break
        return rs

if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    flag=s.spiralOrder(matrix)
    print(flag)
