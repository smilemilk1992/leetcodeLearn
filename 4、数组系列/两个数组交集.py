# -*- coding: utf-8 -*-
"""
@File    :   两个数组的交集.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/10/24 10:28    1.0         None
"""
'''
第350题：两个数组的交集
给定两个数组，编写一个函数来计算它们的交集。
示例 1:
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2]

示例 2:
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。

进阶:
如果给定的数组已经排好序呢？将如何优化你的算法呢？
思路：设定两个为0的指针，比较两个指针的元素是否相等。如果指针的元素相等，我们将两个指针一起向后移动，并且将相等的元素放入空白数组。

'''

__author__ = 'haochen214934'


from typing import List


#无序 hash映射 为什么可以这样看呢，因为我们需找出两个数组的交集元素，同时应与两个数组中出现的次数一致。这样就导致了我们需要知道每个值出现的次数，所以映射关系就成了<元素,出现次数>。剩下的就是顺利成章的解题。
class Solution1:
    def twoArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        map={}
        for i in nums1:
            if i not in map.keys():
                map[i]=1
            else:
                map[i]=map[i]+1
        for j in nums2:
            if j in map.keys() and map[j]!=0 and j not in result:
                result.append(j)
                map[j]=map[j]-1
        return result

#先对两个数组进行排序 在用双指针
class Solution2:
    def twoArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        nums1.sort()
        nums2.sort()
        n1=0
        n2=0
        while n1<nums1.__len__() and n2<nums2.__len__():
            if nums1[n1]==nums2[n2]:
                if nums1[n1] not in result:
                    result.append(nums1[n1])
                n1=n1+1
                n2=n2+1
            elif nums1[n1]<nums2[n2]:
                n1=n1+1
            else:
                n2=n2+1
        return result





if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    a=Solution2()
    result = a.twoArray(nums1,nums2)
    print(result)