# -*- coding: utf-8 -*-
"""
@File    :   整数反转.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/22 17:15    1.0         None
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
#  示例 1:
#  输入: 123
# 输出: 321
#
#
#  示例 2:
#  输入: -123
# 输出: -321
#
#  示例 3:
#  输入: 120
# 输出: 21
#
#  注意:
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
#  Related Topics 数学
"""
__author__ = 'haochen214934'

class Solution:

    #队列
    def reverse(self, x: int) -> int:
        res=""
        lists=[]
        for i in str(x):
            lists.append(i)
        while lists:
            flag=lists.pop()
            if not lists and flag=="-":
                res="-"+res
            else:
                res=res+flag
        res=int(res)
        if res<(-2)**31 or res>(2**31-1):
            return 0
        return res

    def reverse1(self, x: int) -> int:
        strs=str(x)
        reversed=strs[::-1]
        if reversed.endswith("-"):
            reversed="-"+str(reversed.rstrip("-"))
        reversed=int(reversed)
        if reversed<(-2)**31 or reversed>(2**31-1):
            return 0
        return int(reversed)

    def reverse2(self, x: int) -> int:
        if x >= 0:
            reversed_x = int(str(x)[::-1])
        else:
            reversed_x = -int(str(x)[:0:-1])

        if -2 ** 31 < reversed_x < 2 ** 31 - 1:
            return reversed_x
        else:
            return 0

if __name__ == '__main__':
    s=Solution()
    f=-15638474120
    flag=s.reverse2(f)
    print(flag)