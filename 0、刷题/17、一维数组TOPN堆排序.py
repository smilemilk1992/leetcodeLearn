'''
https://blog.csdn.net/qq_34840129/article/details/80638225
https://blog.csdn.net/qq_28063811/article/details/93034625

9	5	8	2	3	4	7	1
对于大顶堆：arr[i] >= arr[2i + 1] && arr[i] >= arr[2i + 2]

1	3	5	4	2	8	9	7
对于小顶堆：arr[i] <= arr[2i + 1] && arr[i] <= arr[2i + 2]

Step 1： 构造初始堆
初始化堆时是对所有的非叶子结点进行筛选
最后一个非终端元素的下标是[n/2]向下取整，所以筛选只需要从第[n/2]向下取整个元素开始，从后往前进行调整。

Step 2：进行堆排序
堆排序是一种选择排序。建立的初始堆为初始的无序区。
排序开始，首先输出堆顶元素（因为它是最值），将堆顶元素和最后一个元素交换，这样，第n个位置（即最后一个位置）作为有序区，前n-1个位置仍是无序区，对无序区进行调整，得到堆之后，再交换堆顶和最后一个元素，这样有序区长度变为2。。。
不断进行此操作，将剩下的元素重新调整为堆，然后输出堆顶元素到有序区。每次交换都导致无序区-1，有序区+1。不断重复此过程直到有序区长度增长为n-1，排序完成。

https://blog.csdn.net/chibangyuxun/article/details/53018294
若想得到升序，则建立大顶堆，若想得到降序，则建立小顶堆
'''
class Solution:
    def topN(self, nums, k):
        self.buidMaxHeap(nums)
        for i in range(len(nums)-1,0,-1):
            self.swap(nums,0,i)
            self.heapify(nums,0,i-1)
        print(nums,nums[-k])

    def buidMaxHeap(self,nums):
        for i in range(len(nums)//2 -1,-1,-1):
            self.heapify(nums,i,len(nums)-1)

    def heapify(self,nums,index,length):
        left=2*index+1
        right=2*index+2
        tempIndex=0
        if left<=length and right<=length:
            tempIndex=left if nums[left]>nums[right] else right
        elif left<=length:
            tempIndex=left
        elif right<=length:
            tempIndex=right
        else:
            return
        if nums[tempIndex]>nums[index]:
            self.swap(nums,tempIndex,index)
            self.heapify(nums,tempIndex,length)

    def swap(self,nums,a,b):
        nums[a],nums[b]=nums[b],nums[a]


if __name__ == '__main__':
    s = Solution()
    matrix = [1, 5, 4, 8, 7, 6, 11, 9,15]
    k=5
    s.topN(matrix, k)
