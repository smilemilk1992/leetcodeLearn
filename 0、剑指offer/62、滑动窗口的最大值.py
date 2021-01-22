# -*- coding: utf-8 -*-
"""
@File    :   62、滑动窗口的最大值.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/22 17:44    1.0         None
# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
#
#  示例:
#
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#
#  提示：
#
#  你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
#
#  注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/
#  Related Topics 队列 Sliding Window
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        n=len(nums)
        if not nums:
            return res
        if k>=n:
            res.append(max(nums))
            return res
        for i in range(n-k+1):
            res.append(max(nums[i:i+k]))
        return res
if __name__ == '__main__':
    s=Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    f=s.maxSlidingWindow(nums,k)
    print(f)