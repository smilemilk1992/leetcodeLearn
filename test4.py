from typing import List


class Node(object):
    '''节点'''
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class Test(object):
    def permute(self, nums: List[int]) -> List[int]:
        self.quick_sort(nums,0,len(nums)-1)
        print(nums)

    #快速排序
    def quick_sort(self,nums,start,end):
        if start>=end:
            return
        low=start
        high=end
        mid=nums[start]
        while low<high:
            while low<high and nums[high]>=mid:
                high=high-1
            nums[low]=nums[high]
            while low<high and nums[low]<mid:
                low=low+1
            nums[high]=nums[low]
        nums[low]=mid
        self.quick_sort(nums,start,low-1)
        self.quick_sort(nums,low+1,end)

    #插入排序
    def insert_sort(self,nums):
        length=len(nums)
        for i in range(1,length):
            current=nums[i]
            j=i-1
            while j>=0 and current<=nums[j]:
                nums[j+1]=nums[j]
                j=j-1
            nums[j+1]=current
        print(nums)

    #归并排序
    def merge_sort(self,nums):
        if len(nums)<=1:
            return nums
        mid=len(nums)//2
        list_left=self.merge_sort(nums[:mid])
        list_right=self.merge_sort(nums[mid:])
        return self.merge(list_left,list_right)

    def merge(self,list_left,list_right):
        l=0
        r=0
        new_list=[]
        while l<len(list_left) and r<len(list_right):
            if list_left[l]<list_right[r]:
                new_list.append(list_left[l])
                l=l+1
            else:
                new_list.append(list_right[r])
                r=r+1
        new_list=new_list+list_left[l:]
        new_list=new_list+list_right[r:]
        return new_list

if __name__ == '__main__':
    s=Test()
    nums=[1,4,3,7,6,5]
    f=s.merge_sort(nums)
    print(f)