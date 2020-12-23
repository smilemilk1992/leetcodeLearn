# -*- coding: utf-8 -*-
"""
@File    :   回文数.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/23 14:41    1.0         None
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
#  示例 1:
#  输入: 121
# 输出: true
#
#  示例 2:
#  输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#  示例 3:
#  输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#  进阶:
#  你能不将整数转为字符串来解决这个问题吗？
"""
__author__ = 'haochen214934'

class Solution:
    def isPalindrome(self, x: int) -> bool:
        strs=str(x)
        n=len(strs)
        mid=n//2
        for i in range(mid):
            left=strs[i]
            right=strs[n-i-1]
            if left!=right:
                return False
        return True

    def isPalindrome1(self, x: int) -> bool:
        if x<0:
            return False
        if x<10:
            return True
        if x%10==0:
            return False
        rs=0
        while rs<x//10:
            y=x%10
            x=x//10
            rs=rs*10+y
            if rs==x:
                return True
            elif x//10 == rs:
                return True
        return False

if __name__ == '__main__':
    s=Solution()
    x=121
    flag=s.isPalindrome1(x)
    print(flag)