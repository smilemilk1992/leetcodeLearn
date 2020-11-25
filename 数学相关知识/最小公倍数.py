# -*- coding: utf-8 -*-
"""
@File    :   最小公倍数.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/11/20 14:02    1.0         None
"""
__author__ = 'haochen214934'

class Solution1:
    def mcd(self, a,b):
        res=1
        for i in range(1,a*b+1):
            if i%a==0 and i%b==0 :
                res=i
                break
        return res

class Solution2:
    def exchange(self,a,b):
        a,b=b,a
        return a,b

    def mcd(self, a,b):
        if a<b:
            a,b=self.exchange(a,b)
        if a % b == 0:
            return a
        flag=a%b
        T=a/flag
        return int(T*b)

if __name__ == '__main__':
    s=Solution1()
    a = 24
    b = 32
    print(s.mcd(a,b))