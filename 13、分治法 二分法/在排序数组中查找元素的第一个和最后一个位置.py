# -*- coding: utf-8 -*-
"""
@File    :   在排序数组中查找元素的第一个和最后一个位置.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/6 14:11    1.0         None
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
#  如果数组中不存在目标值 target，返回 [-1, -1]。
#
#  进阶：
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
#
#  示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
#  示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
#  示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#  提示：
#  0 <= nums.length <= 105
#  -109 <= nums[i] <= 109
#  nums 是一个非递减数组
#  -109 <= target <= 109
#
#  Related Topics 数组 二分查找
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right=self.lowwer_bound(nums,target),self.higher_bound(nums,target)
        if left==right:
            return [-1,-1]
        else:
            return [left,right-1]

    def lowwer_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] < target:  # <=
                left = mid + 1
            else:
                right = mid
        return left

    def higher_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] <= target:  # <=
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == '__main__':
    s=Solution()
    nums = [1,2,2,2,3,4,5]
    target = 2
    flag=s.searchRange(nums,target)
    print(flag)