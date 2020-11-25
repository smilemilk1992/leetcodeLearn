# -*- coding: utf-8 -*-
"""
@File    :   最大公约数.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/11/20 14:01    1.0         None
"""
__author__ = 'haochen214934'

#算法一：短除法
class Solution1:
    def gcd(self, a,b):
        res=1
        smaller=a if a<b else b
        for i in range(1,smaller+1):
            if a%i==0 and b%i==0:
                res=i
        return res


#算法二：辗转相减法
'''
辗转相减法是一种简便的求出两数最大公约数的方法。
（更相减损术）辗转相减法（求最大公约数），即尼考曼彻斯法，其特色是做一系列减法，从而求得最大公约数。
例如 ：两个自然数35和14，用大数减去小数，(35,14)->(21,14)->(7,14)，此时，7小于14，要做一次交换，把14作为被减数，即(14,7)->(7,7)，再做一次相减，结果为0，这样也就求出了最大公约数7
'''
class Solution2:
    def exchange(self,a,b):
        a,b=b,a
        return a,b

    def gcd(self, a,b):
        res=1
        if a<b:#初始化a>b
            a,b=self.exchange(a,b)
        while(a>b):
            a=a-b
            if a<b:
                a, b = self.exchange(a, b)
            if a==b:
                res=a
        return res




if __name__ == '__main__':
    s=Solution1()
    a=54
    b=24
    print(s.gcd(a,b))
