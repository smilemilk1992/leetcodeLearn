# -*- coding: utf-8 -*-
"""
@File    :   19、表示数值的字符串-head.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/13 17:25    1.0         None
# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"012
# 3"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
#
#
#  Related Topics 数学

字符类型：

空格 「 」、数字「 0—90—9 」 、正负号 「 +-+− 」 、小数点 「 .. 」 、幂符号 「 eEeE 」 。

状态定义：
按照字符串从左到右的顺序，定义以下 9 种状态。
开始的空格
幂符号前的正负号
小数点前的数字
小数点、小数点后的数字
当小数点前为空格时，小数点、小数点后的数字
幂符号
幂符号后的正负号
幂符号后的数字
结尾的空格

结束状态：
合法的结束状态有 2, 3, 7, 8 。
"""
__author__ = 'haochen214934'
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        met_dot = met_e = met_digit = False
        for i, char in enumerate(s):
            if char in ('+', '-'):
                if i > 0 and s[i - 1] != 'e' and s[i - 1] != 'E':
                    return False
            elif char == '.':
                if met_dot or met_e:
                    return False
                met_dot = True
            elif char == 'e' or char == 'E':
                if met_e or not met_digit:
                    return False
                met_e, met_digit = True, False  # e后必须接，所以这时重置met_digit为False,以免e为最后一个char
            elif char.isdigit():
                met_digit = True
            else:
                return False
        return met_digit


if __name__ == '__main__':
    s=Solution()
    c=".1"
    f=s.isNumber(c)
    print(f)