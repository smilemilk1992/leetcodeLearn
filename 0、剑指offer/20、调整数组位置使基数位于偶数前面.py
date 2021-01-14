# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#
#
#
#  示例：
#
#  输入：nums = [1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 50000
#  1 <= nums[i] <= 10000
from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        low=0
        high=len(nums)-1

        while low<high:
            while low<high and nums[high]%2==0:
                high=high-1
            while low<high and nums[low]%2==1:
                low=low+1
            nums[low],nums[high]=nums[high],nums[low]
        return nums

if __name__ == '__main__':
    s=Solution()
    nums = [2]
    s.exchange(nums)