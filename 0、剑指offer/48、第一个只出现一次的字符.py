# -*- coding: utf-8 -*-
"""
@File    :   48、第一个只出现一次的字符.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/18 18:01    1.0         None
# 在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
#
#  示例:
#
#  s = "abaccdeff"
# 返回 "b"
#
# s = ""
# 返回 " "
#
#  限制：
#  0 <= s 的长度 <= 50000
#  Related Topics 哈希表
"""
__author__ = 'haochen214934'

class Solution:
    def firstUniqChar(self, s: str) -> str:
        res=[]
        if not s:
            return " "
        for i,k in enumerate(s):
            if k in s[i+1:]:
                res.append(k)
                continue
            if k not in res and k not in s[i+1:]:
                return k
        return " "



if __name__ == '__main__':
    s=Solution()
    x = "abaccdeff"
    f=s.firstUniqChar(x)
    print(f)