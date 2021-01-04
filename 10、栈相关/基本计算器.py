# -*- coding: utf-8 -*-
"""
@File    :   基本计算器.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/31 16:55    1.0         None
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
#
#  示例 1：
# 输入：s = "1 + 1"
# 输出：2
#
#  示例 2：
# 输入：s = " 2-1 + 2 "
# 输出：3
#
#  示例 3：
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
#
#  提示：
#  1 <= s.length <= 3 * 105
#  s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
#  s 表示一个有效的表达式
#
#  Related Topics 栈 数学
"""
__author__ = 'haochen214934'

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1
        for ch in s:
            if ch.isdigit():#(1+(4+5+2)-3)+(6+8)
                operand = (operand * 10) + int(ch)
            elif ch == '+':
                res += sign * operand
                sign = 1
                operand = 0
            elif ch == '-':
                res += sign * operand
                sign = -1
                operand = 0
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif ch == ')':
                res += sign * operand
                res *= stack.pop()  # stack pop 1, sign
                res += stack.pop()  # stack pop 2, res
                # Reset the operand
                operand = 0

        return res + sign * operand

if __name__ == '__main__':
    s=Solution()
    x="(1+(4+5+2)-3)+(6+8)"
    flag=s.calculate(x)
    print(flag)