# -*- coding: utf-8 -*-
"""
@File    :   最长公共前缀.py
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/10/24 10:28    1.0         None
"""

'''
编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，则返回""
示例1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释:

输入不存在公共前缀。
说明：

所有输入只包含小写字母 a-z
'''

__author__ = 'haochen214934'

'''
当字符串数组长度为 0 时则公共前缀为空，直接返回
令最长公共前缀 ans 的值为第一个字符串，进行初始化
遍历后面的字符串，依次将其与 ans 进行比较，两两找出公共前缀，最终结果即为最长公共前缀
如果查找过程中出现了 ans 为空的情况，则公共前缀不存在直接返回
时间复杂度：O(s)O(s)，s 为所有字符串的长度之和
'''
class Solution:
    #得到基准元素
    def getFlag(self,x,x1):
        if x1.startswith(x):
            return x
        while not x1.startswith(x):
            x = x[:-1]
            if len(x1)>=len(x) and x1.startswith(x):
                return x
        return None

    def twoArray(self, strs):
        if not strs:
            return ""
        x=strs[0]
        for i in strs:
            if x!=i:
                x=self.getFlag(x,i)
                if not x:
                    break
        return x if x else ""


if __name__ == '__main__':
    strs = ["aaa","aa","aaa"]
    a = Solution()
    result = a.twoArray(strs)
    print(result)
    # print(a.getFlag("flower","flow"))