# -*- coding: utf-8 -*-
"""
@File    :   快速排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/9/15 18:43    1.0         None
"""
__author__ = 'haochen214934'

from typing import List

'''
它采用了一种分治的策略，通常称其为分治法
时间复杂度：O(nlogn)
空间复杂度：快速排序使用递归，递归使用栈，因此它的空间复杂度为O(logn)
稳定性：快速排序无法保证相等的元素的相对位置不变，因此它是不稳定的排序算法

该方法的基本思想是：

1．先从数列中取出一个数作为基准数。
2．分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。 

https://blog.csdn.net/weixin_43250623/article/details/88931925
'''

class Solution(object):
    def quick_sort(self,alist,start,end):
        """快速排序"""
        if start >= end:  # 递归的退出条件
            return
        mid = alist[start]  # 设定起始的基准元素
        low = start  # low为序列左边在开始位置的由左向右移动的游标
        high = end  # high为序列右边末尾位置的由右向左移动的游标
        while low < high:
            # 如果low与high未重合，high(右边)指向的元素大于等于基准元素，则high向左移动-找到第一个小于基准数的
            while low < high and alist[high] >= mid:
                high -= 1
            alist[low] = alist[high]  # 走到此位置时high指向一个比基准元素小的元素,将high指向的元素放到low的位置上,此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处
            # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
            while low < high and alist[low] < mid: #-找到第一个大于等于基准数的
                low += 1
            alist[high] = alist[low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处
        # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置,左边的元素都比基准元素小,右边的元素都比基准元素大
        alist[low] = mid  # 将基准元素放到该位置,
        # 对基准元素左边的子序列进行快速排序
        self.quick_sort(alist, start, low - 1)  # start :0  low -1 原基准元素靠左边一位
        # 对基准元素右边的子序列进行快速排序
        self.quick_sort(alist, low + 1, end)  # low+1 : 原基准元素靠右一位  end: 最后

    def permute(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums, 0, len(nums) - 1)
        print(nums)



class TOPK(object):
    '''
    TOPK 问题
    '''
    def partition(self,nums: List[int],low: int,high: int):
        mid = nums[low]  # 设定起始的基准元素
        while low<high:
            while low<high and nums[high]>=mid:
                high=high-1
            nums[low]=nums[high]
            while low<high and nums[low]<mid:
                low=low+1
            nums[high]=nums[low]
        nums[low]=mid
        return low

    def permute(self, nums: List[int],k:int) -> int:
        k=k-1 #第k小
        # k=len(nums)-k #第k大
        l=0
        h=len(nums)-1
        while l<h:
            j=self.partition(nums,l,h) #取得基准数索引
            if j==k:
                break
            elif j<k:
                l=j+1
            else:
                h=j-1
        return nums[k]


if __name__ == '__main__':
    num = [4,3,2,10,12,1,5,6]
    a=Solution()
    a.permute(num)