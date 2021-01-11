# -*- coding: utf-8 -*-
"""
@File    :   组合总和II.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/11 14:32    1.0         None
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
#  candidates 中的每个数字在每个组合中只能使用一次。
#  说明：
#  所有数字（包括目标数）都是正整数。
#  解集不能包含重复的组合。
#
#  示例 1:
#  输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
#  示例 2:
#  输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]
#  Related Topics 数组 回溯算法
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def helper(i, cur_sum, ans):
            if cur_sum == target:
                res.append(ans)
                return
            if i == n or cur_sum > target:
                return
            for j in range(i, n):
                if j != i and candidates[j] == candidates[j - 1]: #如果重复则跳过
                    continue
                if cur_sum + candidates[j] > target:
                    break
                helper(j + 1, cur_sum + candidates[j], ans + [candidates[j]])
        helper(0, 0, [])
        return res



if __name__ == '__main__':
    s=Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    f=s.combinationSum2(candidates,target)
    print(f)