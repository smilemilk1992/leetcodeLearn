# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任
# 意数字。A 不能视为 14。
#
#
#
#  示例 1:
#
#  输入: [1,2,3,4,5]
# 输出: True
#
#
#
#  示例 2:
#
#  输入: [0,0,1,2,5]
# 输出: True
#
#
#
#  限制：
#
#  数组长度为 5
#
#  数组的数取值为 [0, 13] .
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums.sort()
        flag=[]
        for i in range(len(nums)-1):
            if nums[i]==0:
                flag.append(0)
            else:
                if nums[i]+1!=nums[i+1] and nums[i+1]-nums[i]-1>len(flag):
                    return False
                if nums[i]==nums[i+1]:
                    return False
        return True




if __name__ == '__main__':
    s=Solution()
    nums=[0,0,2,2,5]
    f=s.isStraight(nums)
    print(f)