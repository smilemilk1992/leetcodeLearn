# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的中位数。
#  进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？
#
#  示例 1：
#  输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#
#  示例 2：
#  输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#
#  示例 3：
#  输入：nums1 = [0,0], nums2 = [0,0]
# 输出：0.00000
#
#  示例 4：
#  输入：nums1 = [], nums2 = [1]
# 输出：1.00000
#
#  示例 5：
#  输入：nums1 = [2], nums2 = []
# 输出：2.00000
#
#  提示：
#  nums1.length == m
#  nums2.length == n
#  0 <= m <= 1000
#  0 <= n <= 1000
#  1 <= m + n <= 2000
#  -106 <= nums1[i], nums2[i] <= 106
#
#  Related Topics 数组 二分查找 分治算法
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res=nums1+nums2
        res.sort()
        n=len(res)
        mid=n//2
        ys=n%2
        if ys==1:
            return res[mid]
        else:
            return (res[mid-1]+res[mid])/2.0

if __name__ == '__main__':
    s=Solution()
    nums1 = [1]
    nums2 = []
    f=s.findMedianSortedArrays(nums1,nums2)
    print(f)