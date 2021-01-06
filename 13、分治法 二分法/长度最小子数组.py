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

import bisect
from typing import List


class Solution:
    ##二分法 因为涉及到 "连续子数组"，一旦提到连续二字，我们想到可以通过 二分法 来简化处理。时间复杂度：O(nlog(n))。
    #其实二分查找的关键就是那个递增的有序数列，从而可以每次抛弃一半的可选解。
    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        plow=0
        phigh=n
        min=-1
        while plow<=phigh:
            mid=(plow+phigh)//2
            #判断当前长度的最大和是否大于等于 s
            if self.getMaxSum(mid,nums)>=s:
                phigh=mid-1 #减小长度
                min=mid #更新最小值
            else:
                plow=mid+1 #增大长度
        return 0 if min==-1 else min

    def getMaxSum(self,mid,nums):
        n=len(nums)
        maxSum=sum(nums[:mid])
        sum_ = 0
        for i in range(mid,n):
            # 加一个数字减一个数字，保持长度不变
            sum_=sum_+nums[i]
            sum_=sum_-nums[i-mid]
            # 更新 maxSum
            maxSum=max(maxSum,sum_)
        return maxSum




if __name__ == '__main__':
    s = 4
    nums = [2,3,1,2,4,3]
    S=Solution()
    res=S.minSubArrayLen2(s,nums)
    print(res)