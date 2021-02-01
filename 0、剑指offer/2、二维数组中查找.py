# 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个
# 整数，判断数组中是否含有该整数。
#
#  示例:
#  现有矩阵 matrix 如下：
#
#
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#
#  给定 target = 5，返回 true。
#
#  给定 target = 20，返回 false。
#
#  限制：
#  0 <= n <= 1000
#
#  0 <= m <= 1000
#
#
#
#  注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
#  Related Topics 数组 双指针
from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        for nums in matrix:
            flag=self.twoPice(nums,target)
            if flag:
                return flag
        return False

    #二分法（双指针）
    def twoPice(self,nums,target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return False

    def findNumberIn2DArray1(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        row=0
        column=n-1

        while row<m and column>0:
            if matrix[row][column]>target:
                column=column-1
            elif matrix[row][column]<target:
                row=row+1
            else:
                return True
        return False




if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    target=25
    f=s.findNumberIn2DArray1(matrix,target)
    print(f)
