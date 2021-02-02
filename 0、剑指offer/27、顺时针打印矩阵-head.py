# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
#  示例 1：
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#  示例 2：
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#  限制：
#  0 <= matrix.length <= 100
#  0 <= matrix[i].length <= 100
#
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
#  Related Topics 数组
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rs=[]
        m=len(matrix)
        n=len(matrix[0])
        visited = [[None for x in range(n)] for x in range(m)]
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
    f=s.spiralOrder(matrix)
    print(f)
