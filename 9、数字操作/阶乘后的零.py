# -*- coding: utf-8 -*-
"""
@File    :   阶乘后的零.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/23 16:05    1.0         None
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
#  示例 1:
#  输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
#
#  示例 2:
#  输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
#
#  说明: 你算法的时间复杂度应为 O(log n) 。
#  Related Topics 数学
"""
__author__ = 'haochen214934'

class Solution:
    def factorial(self,n):
        if n<=2:
            return n
        return n*self.factorial(n-1)

    def trailingZeroes(self, n: int) -> int:
        res=0
        result = self.factorial(n)
        if result==0:
            return 0
        flag=[x for x in str(result)]
        while flag:
            f=flag.pop()
            if f=="0":
                res=res+1
            else:
                break
        return res

    #基于方法一，寻找5出现的规律o(log(n))
    def trailingZeroes1(self, n: int) -> int:
        count=0
        while n>0:
            count=count+n//5
            n=n//5
        return count

    def trailingZeroes2(self, n: int) -> int:
        count=0
        for i in range(1,n+1):
            j=i
            while j%5==0:
                count=count+1
                j=j//5
        return count

if __name__ == '__main__':
    s=Solution()
    n=10
    flag=s.trailingZeroes2(n)
    print(flag)