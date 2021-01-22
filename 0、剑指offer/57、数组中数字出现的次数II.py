# -*- coding: utf-8 -*-
"""
@File    :   57、数组中数字出现的次数II.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/22 17:08    1.0         None
# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
#  示例 1：
#  输入：nums = [3,4,3,3]
# 输出：4
#
#  示例 2：
#  输入：nums = [9,1,7,9,7,9,7]
# 输出：1
#
#  限制：
#  1 <= nums.length <= 10000
#  1 <= nums[i] < 2^31
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = {}
        for i in range(len(nums)):
            if nums[i] not in res.keys():
                res[nums[i]] = 1
            else:
                res[nums[i]] += 1
        result = sorted(res.items(), key=lambda x: x[1], reverse=False)
        return result[0][0]