# -*- coding: utf-8 -*-
"""
@File    :   前K个高频元素.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/5 14:19    1.0         None
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#  示例 1:
#  输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
#  示例 2:
#  输入: nums = [1], k = 1
# 输出: [1]
#
#  提示：
#  你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
#  你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
#  你可以按任意顺序返回答案。
#  Related Topics 堆 哈希表
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res={}
        for n in nums:
            if n not in res.keys():
                res[n]=1
            else:
                res[n]+=1
        res=sorted(res.items(),key=lambda x:x[1],reverse=True) #True降序 false升序
        return [x[0] for x in res[:k]]

if __name__ == '__main__':
    s=Solution()
    nums = [1]
    flag=s.topKFrequent(nums,1)
    print(flag)