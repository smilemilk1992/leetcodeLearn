# -*- coding: utf-8 -*-
"""
@File    :   打乱数组.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/24 15:36    1.0         None
# 给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
#
#  实现 Solution class:
#
#
#  Solution(int[] nums) 使用整数数组 nums 初始化对象
#  int[] reset() 重设数组到它的初始状态并返回
#  int[] shuffle() 返回数组随机打乱后的结果
#
#  示例：
# 输入
# ["Solution", "shuffle", "reset", "shuffle"]
# [[[1, 2, 3]], [], [], []]
# 输出
# [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]
#
# 解释
# Solution solution = new Solution([1, 2, 3]);
# solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3,
# 1, 2]
# solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
# solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
#
#  提示：
#  1 <= nums.length <= 200
#  -106 <= nums[i] <= 106
#  nums 中的所有元素都是 唯一的
#  最多可以调用 5 * 104 次 reset 和 shuffle
"""
__author__ = 'haochen214934'

import copy
from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.array=nums
        self.original=nums.copy()


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original


    def shuffle(self) -> List[int]:#打乱一个数组
        """
        Returns a random shuffling of the array.
        """
        # random.shuffle(self.array)
        # return self.array
        ans = copy.deepcopy(self.array)
        for i in range(len(ans)):
            j = random.randint(i, len(ans) - 1)
            ans[i], ans[j] = ans[j], ans[i]
        return ans



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == '__main__':
    num=[1, 2, 3]
    s=Solution(num)
    print(s.shuffle())