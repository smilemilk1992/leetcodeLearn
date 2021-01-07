# -*- coding: utf-8 -*-
"""
@File    :   爬楼梯.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/7 16:33    1.0         None
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#  每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#  注意：给定 n 是一个正整数。
#
#  示例 1：
#  输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
#  示例 2：
#  输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
#
#  Related Topics 动态规划
"""
__author__ = 'haochen214934'

class Solution:

    #斐波那契数列
    def climbStairs(self, n: int) -> int:
        pre=0
        cur=1

        for i in range(n):
            pre,cur=cur,pre+cur
        print(cur)

    #动态规划
    def climbStairs1(self, n: int) -> int:
        if n<=2:
            return n
        dp=[0]*n
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        print(dp[-1])

if __name__ == '__main__':
    s=Solution()
    n=5
    s.climbStairs1(n)