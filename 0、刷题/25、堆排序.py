# -*- coding: utf-8 -*-
"""
@File    :   25、堆排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/25 14:59    1.0         None
"""
__author__ = 'haochen214934'

def dumpSort(nums):
    buildMaxHeap(nums)
    for i in range(len(nums)-1,0,-1):
        swap(nums,0,i)
        heapify(nums,0,i-1)
    print(nums)


#初始化堆
def buildMaxHeap(nums):
    for i in range(len(nums)//2 -1,-1,-1):
        heapify(nums,i,len(nums)-1)

#堆化
def heapify(nums,index,length):
    lsoft=2*index+1
    rsoft=2*index+2
    tempIndex=0
    if lsoft<=length and rsoft<=length:
        tempIndex=lsoft if nums[lsoft]>nums[rsoft] else rsoft
    elif lsoft<=length:
        tempIndex=lsoft
    elif rsoft<=length:
        tempIndex=rsoft
    else:
        return
    if nums[tempIndex]>nums[index]:
        swap(nums,tempIndex,index)
        heapify(nums,tempIndex,length)

def insert(nums,data):
    pass
def swap(nums,i,j):
    nums[i],nums[j]=nums[j],nums[i]
if __name__ == '__main__':
    nums=[1,3,2,5,4,7,6]
    dumpSort(nums)
    print(nums)