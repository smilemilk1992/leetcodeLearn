# -*- coding: utf-8 -*-
"""
@File    :   最长回文子串.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/6 15:20    1.0         None
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
#  示例 1：
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#
#
#  示例 2：
#  输入: "cbbd"
# 输出: "bb"
#
#  Related Topics 字符串 动态规划

动态规划的思路：

对递归问题采用穷举法求解，也就是画出递归树；
通过递归树就会发现子问题重复的问题；
采用备忘录来记录子问题的解；
利用计算顺序采取刷表的方式来代替递归。
"""
__author__ = 'haochen214934'

class Solution:
    #动态规划-重要的是写出动态转移方程 时间复杂度O(n2)
    def longestPalindrome(self, s: str) -> str:
        # : str表示输入是str类型，->str表示输出是str类型，两者都是python3的注释
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 L+1,L表示子串索引i，j的距离差
        for L in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+L 得到子串的结束位置
            for i in range(n):
                j = i + L
                if j >= n:
                    break
                if L == 0:  # L=0，表示串长度为1，只有一个字符，索引i和j的差为0
                    dp[i][j] = True
                elif L == 1:  # L=1,表示串长为2，串有两个字符，索引i和j的差为1
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and L + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans


if __name__ == '__main__':
    s=Solution()
    x="babad"
    flag=s.longestPalindrome(x)
    print(flag)
