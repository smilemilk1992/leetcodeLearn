class Solution:
    def merge_two(self, nums1,nums2):
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        l1=0
        l2=0
        nums=[]
        while l1<len(nums1) and l2<len(nums2):
            if nums1[l1]<=nums2[l2]:
                nums.append(nums1[l1])
                l1=l1+1
            else:
                nums.append(nums2[l2])
                l2 = l2 + 1
        nums = nums + nums1[l1:]
        nums = nums + nums2[l2:]
        return nums

    #两两比对
    def merge(self,nums):
        nums1=nums[0]
        nums2=nums[1]
        res=self.merge_two(nums1,nums2)
        for i in nums[2:]:
            res=self.merge_two(res,i)
        print(res)



if __name__ == '__main__':
    s=Solution()
    nums=[[1,2,3],[2,3,5],[6,7,9],[7,8,9],[3,5,6]]
    flag=s.merge(nums)
    print(flag)
