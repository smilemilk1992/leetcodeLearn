# -*- coding: utf-8 -*-
"""
@File    :   36、二意字符串的判断.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/3/2 16:36    1.0         None
算法题：定义一种字符串为二意字符串，给定两个字符串，判断其是否为二意字符串，二意字符串的定义为：字符串中包含的字符全部相同，但是字符的顺序可能不同。

示例：act和tca互为二意字符串，因为他们包含的字母一样；
actt和act不是二意字符串，因为他们长度不同；
"""
__author__ = 'haochen214934'

class Solution:
    def isValid(self,str1,str2):
        if len(str1)!=len(str2):
            return False
        l1,l2=self.insertSort(str1),self.insertSort(str2)
        if l1 == l2:
            return True
        else:
            return False

    def insertSort(self,strs):
        length=len(strs)
        lists=list(strs)
        for i in range(1,length):
            current=lists[i]
            j=i-1
            while j>=0 and current<=lists[j]:
                lists[j+1]=lists[j]
                j=j-1
            lists[j+1]=current
        return lists

    def quickSort(self,strs,start,end):
        low=start
        high=end
        mid=strs[start]
        while low<high:
            pass

if __name__ == '__main__':
    str1="acttadcrwqqrqwre"
    str2="tcatadcerqwerwee"
    s=Solution()
    f=s.isValid(str1,str2)
    print(f)