# -*- coding: utf-8 -*-
"""
@File    :   26、顺时针遍历数组.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/25 15:12    1.0         None
"""
__author__ = 'haochen214934'
class Solution:
    def traverse(self, nums):
        m=len(nums)
        n=len(nums[0])
        dp=[[False]*n for _ in range(m)]
        flag=1 # 1 右 2 下 3 左 4 上
        i=0
        j=0
        res=[]
        while True:
            if i>=m or j>=n or dp[i][j]:
                break
            dp[i][j]=True
            res.append(nums[i][j])
            if flag==1:
                if j==n-1 or dp[i][j+1]:
                    i=i+1
                    flag = 2
                else:
                    j=j+1
            elif flag==2:
                if i==m-1 or dp[i+1][j]:
                    j=j-1
                    flag = 3
                else:
                    i=i+1
            elif flag==3:
                if j==0 or dp[i][j-1]:
                    i = i - 1
                    flag=4
                else:
                    j=j-1
            elif flag==4:
                if i==0 or dp[i-1][j]:
                    j = j + 1
                    flag=1
                else:
                    i=i-1
        print(res)


if __name__ == '__main__':
    s = Solution()
    matrix = [
        [1,  4,  7,  11, 15],
        [2,  5,  8,  12, 19],
        [3,  6,  9,  16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    s.traverse(matrix)