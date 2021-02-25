# -*- coding: utf-8 -*-
"""
@File    :   测试堆排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/25 9:39    1.0         None
"""
__author__ = 'haochen214934'
'''
堆顶元素最大，其他元素都小于等于：堆顶
第K大 用最大堆
9	5	8	2	3	4	7	1
对于大顶堆：arr[i] >= arr[2i + 1] && arr[i] >= arr[2i + 2]
'''


class Solution:
    def sortList(self, nums):
        self.buildMaxHeap(nums)
        for i in range(len(nums)-1,0,-1):
            print(i)
            self.swap(nums,0,i)
            self.heapify(nums,0,i-1)

        print(nums)

    # 建堆-初始化
    def buildMaxHeap(self, nums):
        for i in range(len(nums)//2 -1,-1,-1):
            self.heapify(nums,i,len(nums)-1)

    # 堆化
    def heapify(self, nums, i, length):
        lsoft=i*2+1
        rsoft=i*2+2
        tempIndex=0
        if lsoft<=length and rsoft<=length:
            tempIndex= lsoft if nums[lsoft]>nums[rsoft] else rsoft
        elif lsoft<=length:
            tempIndex=lsoft
        elif rsoft<=length:
            tempIndex=rsoft
        else:
            return
        if nums[tempIndex]>nums[i]:
            self.swap(nums,tempIndex,i)
            self.heapify(nums,tempIndex,length)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]



a = [70,60,12,40,30,13,10]
s = Solution()
s.sortList(a)