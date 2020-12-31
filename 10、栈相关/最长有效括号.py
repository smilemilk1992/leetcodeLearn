# -*- coding: utf-8 -*-
"""
@File    :   最长有效括号.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/31 16:01    1.0         None
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
#  示例 1:
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#
#  示例 2:
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#
#  Related Topics 字符串 动态规划
"""
__author__ = 'haochen214934'

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = []
        # 当先遇到 `)` 需要先弹出元素，这里可以防止报错
        # 当遇到的 `()` 的字符时，-1 在计算长度的时候，发挥作用
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


if __name__ == '__main__':
    s=Solution()
    x="())"
    flag=s.longestValidParentheses(x)
    print(flag)