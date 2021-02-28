# 统计一个数字在排序数组中出现的次数。
#
#
#
#  示例 1:
#
#  输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
#
#  示例 2:
#
#  输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0
#
#
#
#  限制：
#
#  0 <= 数组长度 <= 50000
#
#
#
#  注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
# position-of-element-in-sorted-array/
#  Related Topics 数组 二分查找
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=self.lowwer_bound(nums,target),self.higher_bound(nums,target)
        print(left,right)
        if left==right:
            return 0
        else:
            return right-left

    def lowwer_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:  # <=
                left = mid + 1
            else:
                right = mid
        return left

    def higher_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:  # <=
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == '__main__':
    s=Solution()
    nums = [5,7,8,8,8,10]
    target = 8
    f=s.search(nums,target)
    print(f)