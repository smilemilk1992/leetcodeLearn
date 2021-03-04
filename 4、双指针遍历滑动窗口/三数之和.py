# -*- coding: utf-8 -*-
"""
@File    :   三数之和.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/16 15:07    1.0         None
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。
#
#  注意：答案中不可以包含重复的三元组。
#  示例：
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
#  Related Topics 数组 双指针
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    #先排序
    #后指针
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 存储结果列表
        res_list = []
        if len(nums)<3:
            return res_list
        # 对nums列表进行排序，无返回值，排序直接改变nums顺序
        nums.sort()
        for i in range(len(nums)):
            # 如果排序后第一个数都大于0，则跳出循环，不可能有为0的三数之和
            if nums[i] > 0:
                break
            # 排序后相邻两数如果相等，则跳出当前循环继续下一次循环，相同的数只需要计算一次
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 记录i的下一个位置
            j = i + 1
            # 最后一个元素的位置
            k = len(nums) - 1
            while j < k:
                # 判断三数之和是否为0
                if nums[j] + nums[k] == -nums[i]:
                    # 把结果加入数组中
                    res_list.append([nums[i], nums[j], nums[k]])
                    # 判断j相邻元素是否相等，有的话跳过这个
                    while j < k and nums[j] == nums[j + 1]: j += 1
                    # 判断后面k的相邻元素是否相等，是的话跳过
                    while j < k and nums[k] == nums[k - 1]: k -= 1
                    # 没有相等则j+1，k-1，缩小范围
                    j += 1
                    k -= 1
                # 小于-nums[i]的话还能往后取
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1
                else:
                    k -= 1
        return res_list

    def threeSum1(self, nums: List[int]) -> List[List[int]]:
        result=[]
        if len(nums)<3:
            return result
        nums.sort()
        for i in range(len(nums)):
            if nums[0]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums) - 1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    result.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j=j+1
                    while j<k and nums[k]==nums[k-1]:
                        k=k-1
                    j=j+1
                    k=k-1
                elif nums[i]+nums[j]+nums[k]<0:
                    j=j+1
                else:
                    k=k-1
        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        result=[]
        if len(nums)<3:
            return result
        nums.sort()
        for i in range(len(nums)):
            if nums[0]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    result.append([nums[i],nums[j],nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j=j+1
                    while j<k and nums[k]==nums[k-1]:
                        k=k-1
                    j=j+1
                    k=k-1
                elif nums[i]+nums[j]+nums[k]<0:
                    j=j+1
                else:
                    k=k-1
        return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s=Solution()
    rs=s.threeSum2(nums)
    print(rs)