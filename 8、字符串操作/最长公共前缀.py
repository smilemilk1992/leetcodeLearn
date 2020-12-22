# -*- coding: utf-8 -*-
"""
@File    :   最长公共前缀.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/22 15:50    1.0         None
# 编写一个函数来查找字符串数组中的最长公共前缀。
#  如果不存在公共前缀，返回空字符串 ""。
#
#  示例 1:
#  输入: ["flower","flow","flight"]
# 输出: "fl"
#
#  示例 2:
#  输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#  说明:
#  所有输入只包含小写字母 a-z 。
#  Related Topics 字符串
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def prefix(self,x,y):
        while not y.startswith(x):
            x=x[:-1]
        return x

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        flag = self.prefix(strs[0], strs[1])
        if not flag:
            return ""
        for i in range(2,len(strs)):
            flag = self.prefix(flag, strs[i])
        return flag if flag else ""



if __name__ == '__main__':
    strs=["dog","racecar","car"]
    s=Solution()
    flag=s.longestCommonPrefix(strs)
    print(flag)
