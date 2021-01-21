# 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出
# 这个数字。
#
#
#
#  示例 1:
#
#  输入: [0,1,3]
# 输出: 2
#
#
#  示例 2:
#
#  输入: [0,1,2,3,4,5,6,7,9]
# 输出: 8
#
#
#
#  限制：
#
#  1 <= 数组长度 <= 10000
#  Related Topics 数组 二分查找
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid]==mid:
                left=mid+1
            else:
                right=mid-1
        return left
if __name__ == '__main__':
    s=Solution()
    xx=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
    # xx=[2]
    f=s.missingNumber(xx)
    print(f)