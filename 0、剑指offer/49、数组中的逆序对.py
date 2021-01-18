# -*- coding: utf-8 -*-
"""
@File    :   49、数组中的逆序对.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/18 18:10    1.0         None
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
#  示例 1:
#  输入: [7,5,6,4]
# 输出: 5
#
#  限制：
#
#  0 <= 数组长度 <= 50000
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        res=0
        length=len(nums)
        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i]>nums[j]:
                    res=res+1
        return res


if __name__ == '__main__':
    s=Solution()
    nums=[7,5,6,4]
    f=s.reversePairs(nums)
    print(f)