# -*- coding: utf-8 -*-
"""
@File    :   两数之和.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/10/13 10:28    1.0         None
"""
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#  示例:
#  给定 nums = [2, 7, 11, 15], target = 9
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
__author__ = 'haochen214934'


from typing import List


#方法一：(有序数组)双指针 o(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        low=0
        high=len(nums)-1
        while low<=high:
            if nums[low]+nums[high]==target:
                result.insert(0,low)
                result.insert(1,high)
                return result
            if nums[low]+nums[high]>target:
                high=high-1
            if nums[low]+nums[high]<target:
                low=low+1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    a=Solution()
    result = a.twoSum(nums,target)
    print(result)