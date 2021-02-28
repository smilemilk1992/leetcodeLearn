def tt(nums,k):
    left,right=0,len(nums)
    while left<right:
        mid=(right+left)//2
        print(left,mid,right)
        if nums[mid]<=k:
            left=mid+1
        else:
            right=mid
    print(left,right)

if __name__ == '__main__':
    nums=[1,2,3,4,4,4,5,6,7,8]
    tt(nums,4)