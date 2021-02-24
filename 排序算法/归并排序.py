# -*- coding: utf-8 -*-
"""
@File    :   归并排序.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Modify Time      @Version    @Desciption
------------      --------    -----------
2020/9/15 18:42    1.0         None
"""
__author__ = 'haochen214934'

class Solution(object):
    def merge(self,arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # 创建临时数组
        L = [0] * (n1)
        R = [0] * (n2)

        # 拷贝数据到临时数组 arrays L[] 和 R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

            # 归并临时数组到 arr[l..r]
        i = 0  # 初始化第一个子数组的索引
        j = 0  # 初始化第二个子数组的索引
        k = l  # 初始归并子数组的索引

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # 拷贝 L[] 的保留元素
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # 拷贝 R[] 的保留元素
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self,arr, l, r):
        if l < r:
            m = int((l + (r - 1)) / 2)
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.merge(arr, l, m, r)
        print(arr)
        return arr


if __name__ == '__main__':
    s=Solution()
    nums=[1,4,2,3,6,5,9,7,8]
    f=s.mergeSort(nums,0,len(nums)-1)
    print(f)