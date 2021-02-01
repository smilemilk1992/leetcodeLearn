# -*- coding: utf-8 -*-
"""
@File    :   5、最长无重复子串.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/2/1 17:09    1.0         None
"""
__author__ = 'haochen214934'

class Solution:
    def lengthOfLongestSubstring(self, strs):
        res=[]
        low=0
        high=1
        mx=0
        while low<high and low<len(strs) and high<len(strs):
            if strs[high] not in strs[low:high]:
                high = high + 1
            elif high-low==1:
                low=low+1
                high=high+1
            else:
                low = low + 1
            mx = max(mx, len(strs[low:high]))

        print(res,mx)



if __name__ == '__main__':
    s=Solution()
    strs="ababc"
    s.lengthOfLongestSubstring(strs)