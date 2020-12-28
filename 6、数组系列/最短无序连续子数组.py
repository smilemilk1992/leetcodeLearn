# -*- coding: utf-8 -*-
"""
@File    :   最短无序连续子数组.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/28 15:38    1.0         None
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
#  你找到的子数组应是最短的，请输出它的长度。
#
#  示例 1:
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
#  说明 :
#  输入的数组长度范围在 [1, 10,000]。
#  输入的数组可能包含重复元素 ，所以升序的意思是<=。
#
#  Related Topics 数组
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    #快慢指针
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if nums is None or len(nums)<1:
            return 0
        cloneNums=nums.copy()
        nums.sort()
        begin=float("inf")
        end=0
        for i in range(len(nums)):
            if nums[i]!=cloneNums[i]:
                begin=min(begin,i)
                end=max(end,i)

        return max(end-begin+1,0)


if __name__ == '__main__':
    s=Solution()
    nums=[2, 6, 4, 8, 10, 9, 15]
    flag=s.findUnsortedSubarray(nums)
    print(flag)