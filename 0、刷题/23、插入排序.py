# -*- coding: utf-8 -*-
"""
@File    :   23、插入排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/25 14:20    1.0         None
"""
__author__ = 'haochen214934'
def insertSort(nums):
    length=len(nums)
    for i in range(1,length):
        current=nums[i]
        j=i-1
        while j>=0 and current<=nums[j]:
            nums[j+1]=nums[j]
            j=j-1
        nums[j+1]=current
    return nums


if __name__ == '__main__':
    nums=[1,3,2,5,4,7,6]
    insertSort(nums)