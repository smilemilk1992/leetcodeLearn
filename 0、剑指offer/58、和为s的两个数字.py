# -*- coding: utf-8 -*-
"""
@File    :   58、和为s的两个数字.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/22 17:13    1.0         None
# 输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
#
#  示例 1：
#  输入：nums = [2,7,11,15], target = 9
# 输出：[2,7] 或者 [7,2]
#
#  示例 2：
#  输入：nums = [10,26,30,31,47,60], target = 40
# 输出：[10,30] 或者 [30,10]
#
#  限制：
#  1 <= nums.length <= 10^5
#  1 <= nums[i] <= 10^6
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res=[]
        map={}
        for i in nums:
            if target-i in map.keys():
                res.append(i)
                res.append(target-i)
            else:
                map[i]=1
        return res[-2:]


if __name__ == '__main__':
    s=Solution()
    nums = [16,16,18,24,30,32]
    target = 48
    f=s.twoSum(nums,target)
    print(f)