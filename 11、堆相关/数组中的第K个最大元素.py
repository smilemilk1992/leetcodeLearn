# -*- coding: utf-8 -*-
"""
@File    :   数组中的第K个最大元素.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/4 17:05    1.0         None
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
#  示例 1:
#  输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#
#  示例 2:
#  输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
#  说明:
#  你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
#  Related Topics 堆 分治算法
堆-堆是为了实现排序而设计的一种数据结构，它不是面向查找操作的
[完全二叉树]
除最后一层，其他层都满了
如果最后一层没满，那么没满的全在右边
满二叉树是特殊完全二叉树
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def quick(self,nums,start,end):
        if start>=end:
            return
        mid=nums[start]
        low=start
        high=end
        while low<high:
            while low<high and nums[high]>=mid:
                high=high-1
            nums[low]=nums[high]
            while low<high and nums[low]<mid:
                low=low+1
            nums[high]=nums[low]
        nums[low]=mid
        self.quick(nums,start,low-1)
        self.quick(nums,low+1,end)

    #快速排序-分治算法
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.quick(nums,0,len(nums)-1)
        return nums[len(nums)-k]

    #堆排序 堆是一棵顺序存储的完全二叉树
    # 其中每个结点的关键字都不大于其孩子结点的关键字，这样的堆称为小根堆。
    # 其中每个结点的关键字都不小于其孩子结点的关键字，这样的堆称为大根堆。
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        pass

if __name__ == '__main__':
    s=Solution()
    num=[3,2,3,1,2,4,5,5,6]
    k=4
    flag=s.findKthLargest(num,k)
    print(flag)