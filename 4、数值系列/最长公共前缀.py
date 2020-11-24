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


from typing import List


#无序 hash映射 为什么可以这样看呢，因为我们需找出两个数组的交集元素，同时应与两个数组中出现的次数一致。这样就导致了我们需要知道每个值出现的次数，所以映射关系就成了<元素,出现次数>。剩下的就是顺利成章的解题。
class Solution:
    def twoArray(self, strs):
        result=[]
        i=1
        while i>=1:
            flag=strs[0][:1]
            for s in strs:
                if flag!=s[:i]:
                    break

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    a = Solution()
    result = a.twoArray(strs)
    print(result)