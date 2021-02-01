# -*- coding: utf-8 -*-
"""
@File    :   6、给一个字符串表示的数字，通过移动字符串中的数字得到第一个大于原数的数字.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/1 17:33    1.0         None
"""
__author__ = 'haochen214934'

class Solution:
    def lengthOfLongestSubstring(self, strs):
        lists=list(strs)
        n=len(strs)
        for i in range(n-1):
            for j in range(i+1,n):
                if lists[j]>lists[i] and j-i==1:
                    lists[i],lists[j]=lists[j],lists[i]
                    return "".join(lists)


if __name__ == '__main__':
    s=Solution()
    strs="3215"
    f=s.lengthOfLongestSubstring(strs)
    print(f)