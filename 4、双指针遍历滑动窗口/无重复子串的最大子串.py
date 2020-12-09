# -*- coding: utf-8 -*-
"""
@File    :   无重复子串的最大子串.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/10/13 15:06    1.0         None
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#  示例 1:
#  输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

#  示例 2:
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

#  示例 3:
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#  请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

滑动窗口一般都是定义一个slow指针，然后一个fast指针不断向前滑动(循环遍历)，这个过程中我们要判断：
是否找到了窗口，
窗口时否满足要求
窗口缩减等
"""

__author__ = 'haochen214934'

#Hash+双指针滑动窗口 o(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=[]
        max=0
        plow=0
        phigh=1
        while plow<phigh and phigh<len(s) and plow<len(s):
            if s[phigh] not in s[plow:phigh]:
                phigh=phigh+1
            elif phigh-plow==1:
                result.append(s[plow:phigh])
                _max = len(s[plow:phigh])
                if _max >= max:
                    max = _max
                phigh = phigh + 1
                plow=plow+1
            else:
                result.append(s[plow:phigh])
                _max=len(s[plow:phigh])
                if _max>=max:
                    max=_max
                plow = plow + 1
        print(max,result)


if __name__ == '__main__':
    s="abcdawwkjhga"
    a=Solution()
    a.lengthOfLongestSubstring(s)