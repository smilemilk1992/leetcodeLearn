# -*- coding: utf-8 -*-
"""
@File    :   13、剪绳子.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/13 16:10    1.0         None
# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
# 请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18
#  示例 1：
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1
#
#  示例 2:
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
#
#  提示：
#  2 <= n <= 58
#  注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/
#  Related Topics 数学 动态规划
"""
__author__ = 'haochen214934'

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        dp=[float("-inf")]*(n+1)
        dp[1]=1
        dp[2]=2
        dp[3]=3
        dp[4]=4
        for i in range(5,n+1):
            for j in range(1,i):#至少切一刀
                dp[i]=max(dp[i-j]*dp[j],dp[i])
        return dp[n]

if __name__ == '__main__':
    s=Solution()
    n=10
    f=s.cuttingRope(n)
    print(f)