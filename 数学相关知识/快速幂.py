# -*- coding: utf-8 -*-
"""
@File    :   快速幂.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/11/20 11:02    1.0         None

十进制就是「逢十进一」，而二进制就是「逢二进一」。
"""
__author__ = 'haochen214934'

'''
1. b 可能为负数

2. a 可能为 0
'''
class Solution1:
    #计算 a ^ b 2 -2
    def poww (self, a,b):
        if a==0 and b!=0:
            return 0
        if a==0 and b==0:
            return 1
        if b<0:
            a=1/a
            b=-b
        base =a
        ans=1
        while b:
            if b&1: #与
                ans=ans*base
            base=base*base
            b>>=1
        return ans

if __name__ == '__main__':
    s=Solution1()
    print(s.poww(2,-3))