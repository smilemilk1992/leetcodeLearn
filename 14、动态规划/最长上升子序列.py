# -*- coding: utf-8 -*-
"""
@File    :   最长上升子序列.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/7 18:15    1.0         None
# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
#  子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序
# 列。
#
#
#  示例 1：
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
#
#  示例 2：
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
#
#  示例 3：
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#
#  提示：
#  1 <= nums.length <= 2500
#  -104 <= nums[i] <= 104
#
#  进阶：
#  你可以设计时间复杂度为 O(n2) 的解决方案吗？
#  你能将算法的时间复杂度降低到 O(n log(n)) 吗?
#
#  Related Topics 二分查找 动态规划
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    # 动态规划 时间复杂度：O(n^2)O(n2)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums == []: return 0
        length = len(nums)
        # 暂存子序列长度，1 个字符显然是长度为 1 的上升子序列
        dp = [1 for _ in range(length)]
        for i in range(length):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    # 状态：dp[i] 表示以 nums[i] 结尾的「上升子序列」的长度
                    # 当nums[i]前面存在小于nums[i]的nums[j],
                    # 则暂存在dp[j]+1就是当前nums[i]的最长增长子序列的长度
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # 二分查找
    def lengthOfLIS1(self, nums: List[int]) -> int:
        if nums == []: return 0
        length = len(nums)
        # 暂存查找到的子序列
        dp = [1 for _ in range(length)]
        lis = 0  # 增长子串的长度
        for n in nums:
            # 利用二分查找法来搜索子序列
            left = 0
            right = lis
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < n:
                    left = mid + 1
                else:
                    right = mid
            if left == lis:
                lis += 1
            dp[left] = n
        return lis

if __name__ == '__main__':
    s=Solution()
    nums=[10,9,2,5,3,7,101,18]
    f=s.lengthOfLIS1(nums)
    print(f)