# -*- coding: utf-8 -*-
"""
@File    :   49、数组中的逆序对-head.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/18 18:10    1.0         None
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
#  示例 1:
#  输入: [7,5,6,4]
# 输出: 5
#
#  限制：
#
#  0 <= 数组长度 <= 50000
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    #会存在超时
    def reversePairs(self, nums: List[int]) -> int:
        res=0
        length=len(nums)
        for i in range(length-1):
            for j in range(i+1,length):
                if nums[i]>nums[j]:
                    res=res+1
        return res

    def reversePairs1(self, nums: List[int]) -> int:
        # 计算逆序数就发生在排序的过程中，利用了「排序」以后数组的有序性。关键在于「合并两个有序数组」的步骤，利用数组的部分有序性，一下子计算出一个数之前或者之后元素的逆序的个数. 前面「分」的时候什么都不做，第 2 个子区间元素归并回去的时候，计算逆序对的个数.
        size = len(nums)
        if size < 2:
            return 0

        # 用于归并的辅助数组
        temp = [0 for _ in range(size)]
        return self.count_reverse_pairs(nums, 0, size - 1, temp)

    def count_reverse_pairs(self, nums, left, right, temp):
        # 在数组 nums 的区间 [left, right] 统计逆序对
        if left == right:
            return 0

        mid = (left + right) // 2
        left_pairs = self.count_reverse_pairs(nums, left, mid, temp)
        right_pairs = self.count_reverse_pairs(nums, mid + 1, right, temp)
        reverse_pairs = left_pairs + right_pairs
        # print("current", nums, nums[mid], nums[mid + 1])

        # 代码走到这里的时候，[left, mid] 和 [mid + 1, right] 已经完成了排序并且计算好逆序对
        if nums[mid] <= nums[mid + 1]:
            # 此时不用计算横跨两个区间的逆序对，直接返回 reverse_pairs
            # 为什么不用？当前if条件满足时，说明[mid + 1, right]所有数字都比[left, mid]的大，继续计算横跨逆序对没有意义，相当于剪枝。
            # print("reverse only", left, mid, right, left_pairs, right_pairs)
            return reverse_pairs

        reverse_cross_pairs = self.merge_and_count(nums, left, mid, right, temp)
        # print("reverse + cross", left, mid, right, left_pairs, right_pairs, reverse_cross_pairs)
        return reverse_pairs + reverse_cross_pairs

    def merge_and_count(self, nums, left, mid, right, temp):
        """
        已知条件：[left, mid] 有序，[mid + 1, right] 有序。只在后面数组元素出列的时候，数一数前面这个数组还剩下多少个数字，
        由于"前"数组和"后"数组都有序，此时"前"数组剩下的元素个数 mid - i + 1 就是与"后"数组元素出列的这个元素构成的逆序对个数
        """
        for i in range(left, right + 1):
            # temp存储merge之前的原nums数组。在merge过程中，temp不变，修改的是nums数组。
            temp[i] = nums[i]

        i = left
        j = mid + 1
        res = 0
        for k in range(left, right + 1):
            # 每一次合并nums，都需要判断数组下标是否越界。
            if i > mid:
                # i > mid 表示 i 已经遍历完了第一个部分的所有数，mid 是第一个部分的最后一个位置的下标。
                # 所以当前合并过程可以忽略i坐标，直接把j坐标所在元素合并到nums。
                nums[k] = temp[j]
                j += 1
            elif j > right:
                # 表示 j 已经遍历完了第二个部分的所有数， right 是第二个部分的最后一个位置的下标。
                # 所以当前合并过程可以忽略j坐标，直接把i坐标所在元素合并到nums。
                nums[k] = temp[i]
                i += 1
            # 走到这里时，说明i，j都没有越界，可以直接比较、合并到nums。
            elif temp[i] <= temp[j]:
                # 此时前数组元素出列，不统计逆序对
                nums[k] = temp[i]
                i += 1
            else:
                # 此时后数组元素出列，统计逆序对，快就快在这里，一次可以统计出一个区间的个数的逆序对
                nums[k] = temp[j]
                j += 1
                # 例：[7, 8, 9][4, 6, 9]，4 与 7 以及 7 后面所有的数都构成逆序对
                res += (mid - i + 1)
        return res



if __name__ == '__main__':
    s=Solution()
    nums=[7,5,6,4]
    f=s.reversePairs1(nums)
    print(f)