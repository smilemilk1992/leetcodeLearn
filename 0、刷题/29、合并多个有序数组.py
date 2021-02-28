def mergeSort(nums):
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    left=mergeSort(nums[:mid])
    right=mergeSort(nums[mid:])
    return merge(left[0],right[0])

def merge(left,right):
    l=0
    r=0
    res=[]
    while l<len(left) and r<len(right):
        if left[l]<=right[r]:
            res.append(left[l])
            l=l+1
        else:
            res.append(right[r])
            r=r+1
    res=res+left[l:]
    res=res+right[r:]
    return [res]


if __name__ == '__main__':
    nums=[[1,2,3],[2,3,5],[6,7,9],[7,8,9],[3,5,6]]
    s=mergeSort(nums)
    print(s)