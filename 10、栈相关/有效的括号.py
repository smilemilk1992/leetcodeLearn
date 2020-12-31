# -*- coding: utf-8 -*-
"""
@File    :   有效的括号.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/31 14:49    1.0         None
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#  有效字符串需满足：
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#  注意空字符串可被认为是有效字符串。
#
#  示例 1:
#  输入: "()"
# 输出: true
#
#  示例 2:
#  输入: "()[]{}"
# 输出: true
#
#  示例 3:
#  输入: "(]"
# 输出: false
#
#  示例 4:
#  输入: "([)]"
# 输出: false
#
#  示例 5:
#  输入: "{[]}"
# 输出: true
#  Related Topics 栈 字符串
"""
__author__ = 'haochen214934'

class Solution:
    def isValid(self, s: str) -> bool:
        lists=[]
        for i in s:
            if i=="{" or i=="[" or i=="(":
                lists.append(i)
            else:
                if not lists:
                    return False
                if i=="]":
                    if lists.pop()!="[":
                        return False
                elif i=="}":
                    if lists.pop()!="{":
                        return False
                else:
                    if lists.pop()!="(":
                        return False
        return False if lists else True



if __name__ == '__main__':
    A=Solution()
    s="{[]}"
    flag=A.isValid(s)
    print(flag)
