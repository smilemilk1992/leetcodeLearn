# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
#  注意：
#
#  答案中不可以包含重复的四元组。
#
#  示例：
#
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#
#  Related Topics 数组 哈希表 双指针
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        if len(nums)<4:
            return result
        nums.sort()
        for i in range(len(nums)):
            if nums[0]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                m=j+1
                n=len(nums)-1
                while m<n:
                    if nums[i]+nums[j]+nums[m]+nums[n]==target:
                        if [nums[i],nums[j],nums[m],nums[n]] not in result:
                            result.append([nums[i],nums[j],nums[m],nums[n]])
                        while m<n and nums[m]==nums[m+1]:
                            m=m+1

                        while m<n and nums[n]==nums[n-1]:
                            n=n-1
                        m=m+1
                        n=n-1
                    elif nums[i]+nums[j]+nums[m]+nums[n]<target:
                        m=m+1
                    else:
                        n=n-1
        print(result)
        return result



if __name__ == '__main__':
    s=Solution()
    nums = [-2,-1,-1,1,1,2,2]
    target = 0
    s.fourSum(nums,target)