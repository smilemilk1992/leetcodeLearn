# encoding:utf-8
from typing import List

'''
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
'''
class Solution(object):
    def __init__(self):
        self.ans = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums, [])
        return self.ans

    def dfs(self, nums: List[int], track: List[int]):
        if len(track) == len(nums):
            # tmp=track.copy() #需要用到copy来实现复制已有列表的功能，否则用简单的a = b就会把同一个列表指向a，
            self.ans.append(list(track))
        else:
            for num in nums:
                if num not in track:
                    print("做选择 ", track, num)
                    track.append(num) #做选择
                    self.dfs(nums, track)
                    print("撤销 ", track,num)
                    track.remove(num)  # 撤销调上一次选择的结果 回溯



if __name__ == '__main__':
    a = Solution()
    nums = [1, 2, 3]
    res = a.permute(nums)
    print(res)
