# -*- coding: utf-8 -*-
"""
@File    :   Z字形变换.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/22 15:11    1.0         None
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
#  比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#  L   C   I   R
# E T O E S I I G
# E   D   H   N
#
#
#  之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#  请你实现这个将字符串进行指定行数变换的函数：
#  string convert(string s, int numRows);
#
#  示例 1:
#  输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#
#
#  示例 2:
#  输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
#  Related Topics 字符串
"""
__author__ = 'haochen214934'
class Solution:
    '''
    使用两个标记和一个方向来确定。
    两个标记：第一行和最后一行
    一个方向：方向向量走到第一行就开始改变方向往下走（-1）；走到最后一行就开始改变方向往上走（+1）
    利用列表实现每一个字符串位置存储一行的所有字符
    依次存储，第0行的注定要在第一行前，第一行注定要在第二行前……使用join进行合并即可。
    本题解题时间复杂度为O(n)，其中n=len(s)
    ['', '', '', '']
    ['L', '', '', '']
    ['L', 'E', '', '']
    ['L', 'E', 'E', '']
    ['L', 'E', 'E', 'T']
    ['L', 'E', 'EC', 'T']
    ['L', 'EO', 'EC', 'T']
    ['LD', 'EO', 'EC', 'T']
    ['LD', 'EOE', 'EC', 'T']
    ['LD', 'EOE', 'ECI', 'T']
    ['LD', 'EOE', 'ECI', 'TS']
    ['LD', 'EOE', 'ECIH', 'TS']
    ['LD', 'EOEI', 'ECIH', 'TS']
    ['LDR', 'EOEI', 'ECIH', 'TS']
    ['LDR', 'EOEII', 'ECIH', 'TS']
    ['LDR', 'EOEII', 'ECIHN', 'TS']
    ['LDR', 'EOEII', 'ECIHN', 'TSG']
    '''
    def convert(self, s: str, numRows: int) -> str:
        result = [''] * min(numRows, len(s))
        current_row = 0
        go_up_down = 0
        if len(s) <= 1 or numRows <= 1:
            return s
        else:
            for i in range(len(s)):
                result[current_row] = result[current_row] + s[i]
                if current_row == 0: #头
                    go_up_down = 1 #向下
                elif current_row == numRows - 1:#尾
                    go_up_down = -1 #向上
                current_row = current_row + go_up_down
        return ''.join(result)

    def convert1(self, s: str, numRows: int) -> str:
        result = [''] * min(numRows, len(s))
        cur_row=0
        flag=0
        if len(s)<=1 or numRows<=1:
            return s
        for i in range(len(s)):
            result[cur_row]=result[cur_row]+s[i]
            if cur_row==0:
                flag=1
            if cur_row==numRows-1:
                flag=-1
            cur_row=cur_row+flag
        return result


if __name__ == '__main__':
    S=Solution()
    s = "LEETCODEISHIRING"
    numRows = 4
    S.convert1(s,numRows)