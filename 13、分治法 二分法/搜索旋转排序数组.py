# 升序排列的整数数组 nums 在预先未知的某个点上进行了旋转（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。
#  请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
#  示例 1：
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
#
#  示例 2：
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
#  示例 3：
# 输入：nums = [1], target = 0
# 输出：-1
#
#  提示：
#  1 <= nums.length <= 5000
#  -10^4 <= nums[i] <= 10^4
#  nums 中的每个值都 独一无二
#  nums 肯定会在某个点上旋转
#  -10^4 <= target <= 10^4
#
#  Related Topics 数组 二分查找
from typing import List


class Solution:
    #暴力法
    def search(self, nums: List[int], target: int) -> int:
        res=-1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return res

    #二分法 二分查找，要求的是列表的元素必须是有序
    def search1(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[0]<=nums[mid]: #左边是有序的
                if nums[0]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:#右边是有序的
                if nums[mid]<=target<=nums[-1]:
                    left=mid+1
                else:
                    right=mid-1
        return -1

if __name__ == '__main__':
    s=Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    flag=s.search1(nums,target)
    print(flag)