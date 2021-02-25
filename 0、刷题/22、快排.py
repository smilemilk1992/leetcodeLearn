# -*- coding: utf-8 -*-
"""
@File    :   22、快排.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/25 13:48    1.0         None
"""
__author__ = 'haochen214934'

def quickSort(nums):
    check(nums,0,len(nums)-1)
    return nums

def check(nums,start,end):
    if start>=end:
        return
    low=start
    high=end
    mid=nums[start]
    while low<high:
        while low<high and nums[high]>=mid:
            high=high-1
        nums[low]=nums[high]
        while low<high and nums[low]<mid:
            low=low+1
        nums[high]=nums[low]
    nums[low]=mid
    check(nums,start,low-1)
    check(nums,low+1,end)

if __name__ == '__main__':
    nums=[1,4,2,5,7,3,6]
    result=quickSort(nums)
    print(result)
