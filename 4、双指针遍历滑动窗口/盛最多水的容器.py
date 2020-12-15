# -*- coding: utf-8 -*-
"""
@File    :   盛最多水的容器.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/15 14:51    1.0         None
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
#  说明：你不能倾斜容器。
#
#  示例 1：
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#  示例 2：
# 输入：height = [1,1]
# 输出：1
#
#  示例 3：
# 输入：height = [4,3,2,1,4]
# 输出：16
#
#  示例 4：
# 输入：height = [1,2,1]
# 输出：2
#  提示：
#  n = height.length
#  2 <= n <= 3 * 104
#  0 <= height[i] <= 3 * 104
#
#  Related Topics 数组 双指针

种方法背后的思路在于，两线段之间形成的区域总是会受到其中较短那条长度的限制。此外，两线段距离越远，得到的面积就越大。

我们在由线段长度构成的数组中使用两个指针，一个放在开始，一个置于末尾。 此外，我们会使用变量 maxarea 来持续存储到目前为止所获得的最大面积。 在每一步中，我们会找出指针所指向的两条线段形成的区域，更新 maxarea，并将指向较短线段的指针向较长线段那端移动一步。
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        max = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area >= max:
                max = area
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return max


if __name__ == '__main__':
    s=Solution()
    height=[1,1]
    s.maxArea(height)