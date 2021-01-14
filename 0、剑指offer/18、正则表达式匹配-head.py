# -*- coding: utf-8 -*-
"""
@File    :   18、正则表达式匹配-head.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/13 17:22    1.0         None
# 请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配
# 是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。
#
#  示例 1:
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#  示例 2:
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#  示例 3:
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#  示例 4:
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#
#  示例 5:
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#  s 可能为空，且只包含从 a-z 的小写字母。
#  p 可能为空，且只包含从 a-z 的小写字母以及字符 . 和 *，无连续的 '*'。
#
#  注意：本题与主站 10 题相同：https://leetcode-cn.com/problems/regular-expression-matching/
#  Related Topics 动态规划
"""
__author__ = 'haochen214934'
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
# 递归写法
        # s已被匹配且p已耗完
        if not s and not p:  # not比len()==0和s==[]或s==""更简便
            return True
        # p已耗完但s未被完全匹配
        if len(s) > 0 and len(p) == 0:  # 或if not p
            return False
        # 如果模式第二个字符是*
        if len(p) > 1 and p[1] == '*':
            if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                # 如果第一个字符匹配，三种可能1、模式后移两位；2、字符串移1位
                return self.isMatch(s, p[2:]) or self.isMatch(s[1:], p)
            else:
                # 如果第一个字符不匹配，模式往后移2位，相当于忽略x*
                return self.isMatch(s, p[2:])
        # 如果模式第二个字符不是*
        if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
            return self.isMatch(s[1:], p[1:])
        else:
            return False

if __name__ == '__main__':
    S=Solution()
    s = "mississippi"
    p = "mis*is*p*."
    f=S.isMatch(s,p)
    print(f)