# -*- coding: utf-8 -*-
"""
@File    :   选择排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/9/15 17:35    1.0         None
"""
__author__ = 'haochen214934'

from typing import List

'''
1、在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
2、再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
'''

class Solution(object):
    def permute(self, nums: List[int]) -> List[int]:
        length=len(nums)
        for i in range(length): #趟数
            maxIndex=i #默认最开头的最大
            for j in range(i+1,length):#每一趟都选择最小的 然后交换 第一个与最小的位置
                if nums[j]<nums[maxIndex]:
                    maxIndex=j
            nums[i],nums[maxIndex]=nums[maxIndex],nums[i]
        print(nums)


if __name__ == '__main__':
    num = [3, 1, 2, 5, 444,23,12,7]
    a=Solution()
    a.permute(num)