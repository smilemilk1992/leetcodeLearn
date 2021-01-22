# -*- coding: utf-8 -*-
"""
@File    :   61、左旋转字符串.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/22 17:40    1.0         None
# 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数
# 将返回左旋转两位得到的结果"cdefgab"。
#
#  示例 1：
#  输入: s = "abcdefg", k = 2
# 输出: "cdefgab"
#
#  示例 2：
#  输入: s = "lrloseumgh", k = 6
# 输出: "umghlrlose"
#
#  限制：
#  1 <= k < s.length <= 10000
#  Related Topics 字符串
"""
__author__ = 'haochen214934'
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:]+s[:n]



if __name__ == '__main__':
    s=Solution()
    strs = "lrloseumgh"
    k = 6
    f=s.reverseLeftWords(strs,k)
    print(f)
