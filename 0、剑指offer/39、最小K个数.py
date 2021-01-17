# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
#
#
#  示例 1：
#
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#
#
#  示例 2：
#
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#
#
#
#  限制：
#
#
#  0 <= k <= arr.length <= 10000
#  0 <= arr[i] <= 10000
#
#  Related Topics 堆 分治算法
from typing import List


class Solution:
    #快排
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        self.check(arr,0,len(arr)-1)
        return arr[:k]

    def check(self,arr,left,right):
        if left>=right:
            return
        low=left
        high=right
        temp=arr[left]
        while low<high:
            while low<high and arr[high]>=temp:
                high=high-1

            while low<high and arr[low]<temp:
                low=low+1
            arr[high],arr[low]=arr[low],arr[high]
        arr[low]=temp

        self.check(arr,left,low-1)
        self.check(arr,low+1,right)


if __name__ == '__main__':
    s=Solution()
    arr = [0,1,2,1]
    k = 1
    f=s.getLeastNumbers(arr,k)
    print(f)
