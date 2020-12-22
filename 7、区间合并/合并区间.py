# -*- coding: utf-8 -*-
"""
@File    :   合并区间.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/22 14:27    1.0         None
# 给出一个区间的集合，请合并所有重叠的区间。
#
#  示例 1:
#  输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
#  示例 2:
#  输入: intervals = [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
#  注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
#
#  提示：
#  intervals[i][0] <= intervals[i][1]
#  Related Topics 排序 数组
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res

if __name__ == '__main__':
    s=Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    s.merge(intervals)