# -*- coding: utf-8 -*-
"""
@File    :   最长公共子序列.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/8 16:27    1.0         None
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
#
#  一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
#
#  若这两个字符串没有公共子序列，则返回 0。
#
#  示例 1:
#  输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace"，它的长度为 3。
#
#  示例 2:
#  输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。
#
#  示例 3:
#  输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0。
#
#  提示:
#  1 <= text1.length <= 1000
#  1 <= text2.length <= 1000
#  输入的字符串只含有小写英文字符。
#
#  Related Topics 动态规划
"""
__author__ = 'haochen214934'

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        m=len(text1) #列
        n=len(text2) #行
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1 if text2[0]==text1[0] else 0
        for j in range(1,m):
            dp[j][0]= 1 if text1[j] == text2[0] else dp[j - 1][0]
        for i in range(1,n):
            dp[0][i] = 1 if text1[0] == text2[i] else dp[0][i - 1]
        for i in range(1,m):
            for j in range(1,n):
                if text1[i]==text2[j]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]


if __name__ == '__main__':
    s=Solution()
    text1 = "abcde"
    text2 = "ace"
    f=s.longestCommonSubsequence(text1,text2)
    print(f)