class Solution:
    def topN(self, Lists, k):
        nums=Lists[:k]
        self.check(0,len(nums)-1,nums)
        for i in Lists[k:]:
            if i>nums[-1]:
                nums[-1]=i
                self.check(0, len(nums) - 1, nums)
        print(nums)

    def check(self,start,end ,lists):
        if start >= end:  # 递归的退出条件
            return
        mid = lists[start]
        low=start
        high=end

        while low<high:
            while low<high and lists[high]<=mid:
                high=high-1
            lists[low]=lists[high]
            while low<high and lists[low]>mid:
                low=low+1
            lists[high]=lists[low]
        lists[low]=mid
        self.check(start,low-1,lists)
        self.check(low+1,end,lists)



if __name__ == '__main__':
    s = Solution()
    matrix = [1, 5, 4, 8, 7, 6, 11, 9,15]
    k=5
    s.topN(matrix, k)
