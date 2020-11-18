# -*- coding: utf-8 -*-
"""
@File    :   冒泡排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/9/15 16:13    1.0         None
"""
__author__ = 'haochen214934'

from typing import List

'''
步骤：
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

第一遍
123546
'''
class Solution(object):
    def permute(self, nums: List[int]) -> List[int]:
        length=len(nums)
        for i in range(length): #趟数
            for j in range(1,length):#每一趟都两两比较
                if nums[j-1]>nums[j]:
                    nums[j-1],nums[j]=nums[j],nums[j-1]
        print(nums)


if __name__ == '__main__':
    num = [3, 1, 2, 5, 444,23,12,7]
    a=Solution()
    a.permute(num)