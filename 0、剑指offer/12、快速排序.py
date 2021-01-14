# -*- coding: utf-8 -*-
"""
@File    :   12、快速排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/13 15:43    1.0         None
"""
__author__ = 'haochen214934'

from typing import List


class Solution(object):
    def quick_sort(self,alist,start,end):
        if start>=end:
            return
        low=start
        high=end
        mid=alist[start]
        while low<high:
            while low<high and alist[high]>=mid:
                high=high-1
            alist[low]=alist[high]
            while low<high and alist[low]<mid:
                low=low+1
            alist[high]=alist[low]
        alist[low]=mid
        self.quick_sort(alist,start,low-1)
        self.quick_sort(alist,low+1,end)

    def permute(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums,0,len(nums)-1)
        print(nums)

if __name__ == '__main__':
    num = [4,3,2,10,12,1,5,6]
    a=Solution()
    a.permute(num)