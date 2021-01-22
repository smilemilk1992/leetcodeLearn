# -*- coding: utf-8 -*-
"""
@File    :   56、数组中数字出现的次数.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/22 16:46    1.0         None
# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
#  示例 1：
#  输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
#
#  示例 2：
#  输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]
#
#  限制：
#  2 <= nums.length <= 10000
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        res = {}
        for i in range(len(nums)):
            if nums[i] not in res.keys():
                res[nums[i]] = 1
            else:
                res[nums[i]] += 1
        result = sorted(res.items(), key=lambda x: x[1], reverse=False)
        return [x[0] for x in result[:2]]

if __name__ == '__main__':
    s=Solution()
    nums = [1, 2, 10, 4, 1, 4, 3, 3]
    f=s.singleNumbers(nums)
    print(f)