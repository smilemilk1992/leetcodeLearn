# -*- coding: utf-8 -*-
"""
@File    :   正则表达式匹配.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/11 13:49    1.0         None
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
#  '.' 匹配任意单个字符
#  '*' 匹配零个或多个前面的那一个元素
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
#  示例 1：
# 输入：s = "aa" p = "a"
# 输出：false
# 解释："a" 无法匹配 "aa" 整个字符串。
#
#  示例 2:
# 输入：s = "aa" p = "a*"
# 输出：true
# 解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#  示例 3：
# 输入：s = "ab" p = ".*"
# 输出：true
# 解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#  示例 4：
# 输入：s = "aab" p = "c*a*b"
# 输出：true
# 解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#
#  示例 5：
# 输入：s = "mississippi" p = "mis*is*p*."
# 输出：false
#
#  提示：
#  0 <= s.length <= 20
#  0 <= p.length <= 30
#  s 可能为空，且只包含从 a-z 的小写字母。
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
#  保证每次出现字符 * 时，前面都匹配到有效的字符
#
#  Related Topics 字符串 动态规划 回溯算法
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