# -*- coding: utf-8 -*-
"""
@File    :   子集.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/24 15:05    1.0         None
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
#  说明：解集不能包含重复的子集。
#
#  示例:
#
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#  Related Topics 位运算 数组 15、回溯算法
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    #位运算
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allset = 2 ** len(nums)

        result = []
        for i in range(allset):
            item = []
            for j in range(len(nums)):
                if i & (2 ** j):
                    item.append(nums[j])
            result.append(item)
        return result

    #回溯法
    def subsets1(self, nums: List[int]) -> List[List[int]]:
        item = []
        result = [[]]
        nums.sort()  # 排序

        def generate(i, nums, item, result):
            if i >= len(nums):
                return
            item.append(nums[i])
            result.append(list(item))
            generate(i + 1, nums, item, result)
            item.pop() #有点像中序遍历
            generate(i + 1, nums, item, result)

        generate(0, nums, item, result)
        return result

    #大神版本
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        for i in nums:
            item = []
            for j in res:
                if j + [i] not in res:
                    item = item + [j + [i]]
            res = res + item
        return res

if __name__ == '__main__':
    s=Solution()
    nums = [1, 2, 3]
    flag=s.subsets1(nums)
    print(flag)