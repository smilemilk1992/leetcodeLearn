class Solution:
    def merge(self, nums1,nums2):
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
        nums=nums+nums1[l1:]
        nums=nums+nums2[l2:]
        return nums

if __name__ == '__main__':
    s=Solution()
    nums1=[1,2,3]
    nums2=[2,3,5]
    flag=s.merge(nums1,nums2)
    print(flag)
