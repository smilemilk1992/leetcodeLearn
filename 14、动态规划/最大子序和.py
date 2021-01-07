# -*- coding: utf-8 -*-
"""
@File    :   最大子序和.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/7 14:45    1.0         None
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
#  示例:
#  输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#  进阶:
#  如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#  Related Topics 数组 分治算法 动态规划
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    #动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=cur_sum=nums[0]
        for i in nums[1:]:
            cur_sum=max(cur_sum+i,i)
            max_sum=max(max_sum,cur_sum)
        return max_sum


if __name__ == '__main__':
    s=Solution()
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    f=s.maxSubArray(nums)
    print(f)