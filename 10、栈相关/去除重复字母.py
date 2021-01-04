# -*- coding: utf-8 -*-
"""
@File    :   去除重复字母.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/4 15:33    1.0         None
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
#  示例 1：
# 输入：s = "bcabc"
# 输出："abc"
#
#  示例 2：
# 输入：s = "cbacdcbc"
# 输出："acdb"
#
#  提示：
#  1 <= s.length <= 104
#  s 由小写英文字母组成
#
#  Related Topics 栈 贪心算法 字符串
"""
__author__ = 'haochen214934'

class Solution:
    #栈
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        for i,k in enumerate(s):
            if k not in stack:
                while stack and k <stack[-1] and stack[-1] in s[i+1:]:#比前一个字母的字母序小且后面还有重复的就弹出
                    stack.pop()
                stack.append(k)
        print(stack)

if __name__ == '__main__':
    s=Solution()
    num="bcabc"
    s.removeDuplicateLetters(num)