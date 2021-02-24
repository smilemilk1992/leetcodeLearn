'''
堆顶元素最大，其他元素都小于等于：堆顶
第K大 用最大堆
9	5	8	2	3	4	7	1
对于大顶堆：arr[i] >= arr[2i + 1] && arr[i] >= arr[2i + 2]
'''


class Solution:
    def findKthLargest(self, nums, k):
        # global length
        length = len(nums)  # 记录堆的大小，以为堆顶删除后，大小改变

        if k > length:
            return

        # 实现K次堆化，找到第k个最大元素
        self.buildMaxHeap(nums)
        print("建堆后的大根堆的堆顶：", nums[0])
        count = 0

        # 注意i从len（nums）- 1 至 1
        for i in range(len(nums) - 1, 0, -1):
            self.swap(nums, 0, i)  # 将堆顶的元素（最大数）放到数组的末尾i

            length -= 1  # 堆中元素-1（必须）！！
            count += 1
            if count == k:
                return nums[i]
            self.heapify(nums, 0, length)  # 重新进行堆化
        # 说明k == len(nums)
        return nums[0]

    # 建堆
    def buildMaxHeap(self, nums):
        for i in range(len(nums) // 2, -1, -1):
            self.heapify(nums, i, len(nums))

    # 堆化
    def heapify(self, nums, i, length):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < length and nums[left] > nums[largest]:  # 注意使用到了全局变量
            largest = left
        if right < length and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            self.swap(nums, i, largest)
            self.heapify(nums, largest, length)  # 递归：看孩子的孩子节点

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]


nums = [3, 2, 1, 5, 6, 4]
a = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
s = Solution()
print(s.findKthLargest(nums, 4))  # 正确为3
print(s.findKthLargest(a, 4))  # 正确为4