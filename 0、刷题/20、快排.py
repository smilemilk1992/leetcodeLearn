import random
from typing import List

'''
https://blog.csdn.net/weixin_41685561/article/details/80609430
https://tyler-zx.blog.csdn.net/article/details/82718428?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&dist_request_id=5fa06c8f-ed21-4f6d-9b0a-66d1e6b13a73&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control
快速排序最优时间复杂度时O(nlogn);最差时间复杂度时O(n^2);
平均时间复杂度时O(nlogn);空间复杂度最差是O(n);最优空间复杂度是O(logn);是一种不稳定的算法。
优化：
    1、快排的基准选择
        固定基准
        随机基准
        三数取中
    2、使用插入排序替换快速排序
        假设待排序长度为M，若（high-low+1<M）成立时，使用插入排序。
        if (high - low + 1 < 10)  
        {  
            InsertSort(arr,low,high);  
            return;  
        }//else时，正常执行快排 
    优化1：序列长度达到一定大小时，使用插入排序

优化2：尾递归优化

优化3：聚集元素

优化4：多线程处理快排
    
'''
class Solution:
    def QuickSort(self, nums: List[int]) -> List[int]:
        self.check(0,len(nums)-1,nums)
        return nums
    #三数取中
    def Select_Mid(self,start,end,nums):
        mid=start+((end-start)>>1)
        if nums[mid]>nums[end]:
            nums[mid] , nums[end]=nums[end],nums[mid]
        if nums[start]>nums[end]:
            nums[start] , nums[end]=nums[end],nums[start]
        if nums[mid]>nums[start]:
            nums[mid] , nums[start]=nums[start],nums[mid]
        return nums[start]

    #随机
    def Random1(self,start,end,nums):
        pivot=start+random.randint(0,end-start)
        nums[pivot],nums[start]=nums[start],nums[pivot]
        return nums[start]

    def check(self,start,end,nums):
        if start>=end:
            return
        #如果待排序数组长度小于等于M个数，使用插入排序
        if (end-start+1)<=3:
            self.insertSort(nums)
            return
        low=start
        high=end
        mid=self.Random1(start,end,nums)

        while low<high:
            while low<high and nums[high]>=mid:
                high=high-1
            nums[low]=nums[high]
            while low<high and nums[low]<mid:
                low=low+1
            nums[high]=nums[low]
        nums[low]=mid
        self.check(start,low-1,nums)
        self.check(low+1,end,nums)

    def insertSort(self,nums):
        n=len(nums)
        for i in range(1,n):
            current=nums[i]
            j=i-1
            while j and current<=nums[j]:
                nums[j+1]=nums[j]
                j=j-1
            nums[j+1]=current
        return nums

if __name__ == '__main__':
    s=Solution()
    nums=[1,3,2,8,4,7,6,5]
    f=s.QuickSort(nums)
    print(f)