from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        n=len(nums)
        for j in range(n):
            if nums[j]!=val:
                nums[i]=nums[j]
                i=i+1
        return i


if __name__ == '__main__':
    s=Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    f=s.removeElement(nums,val)
    print(f)