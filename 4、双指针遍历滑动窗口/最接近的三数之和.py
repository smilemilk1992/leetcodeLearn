# -*- coding: utf-8 -*-
"""
@File    :   最接近的三数之和.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/16 16:52    1.0         None
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。
#
#  示例：
#
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#  提示：
#  3 <= nums.length <= 10^3
#  -10^3 <= nums[i] <= 10^3
#  -10^4 <= target <= 10^4
#
#  Related Topics 数组 双指针
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()#排序
        tag=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j <k:
                flag=nums[i]+nums[j]+nums[k]
                if abs(tag-target)>abs(flag-target):
                    tag=flag
                if flag==target:
                   return target
                elif flag>target:
                    k=k-1
                else:
                    j=j+1
        return tag

if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target=1
    s = Solution()
    rs = s.threeSumClosest(nums,target)
    print(rs)