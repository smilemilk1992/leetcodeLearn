# -*- coding: utf-8 -*-
"""
@File    :   长度最小子数组.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/16 17:54    1.0         None
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回
#  0。
#
#  示例：
#  输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。

#  进阶：
#  如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
#  Related Topics 数组 双指针 二分查找
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        pass

if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    S=Solution()
    S.minSubArrayLen(s,nums)