# -*- coding: utf-8 -*-
"""
@File    :   爬楼梯.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/7 16:48    1.0         None
"""
__author__ = 'haochen214934'

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)

if __name__ == '__main__':
    s=Solution()
    n=3
    s.climbStairs(n)