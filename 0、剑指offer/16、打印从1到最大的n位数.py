# -*- coding: utf-8 -*-
"""
@File    :   16、打印从1到最大的n位数.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2021/1/13 17:05    1.0         None
# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
#
#  示例 1:
#  输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
#
#  说明：
#  用返回一个整数列表来代替打印
#  n 为正整数
#  Related Topics 数学
"""
__author__ = 'haochen214934'

from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        res=[]
        n=10**n-1
        for i in range(1,n+1):
            res.append(i)
        return res

if __name__ == '__main__':
    s=Solution()
    n=2
    s.printNumbers(n)