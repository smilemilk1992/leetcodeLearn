# -*- coding: utf-8 -*-
"""
@File    :   各位相加.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/23 16:29    1.0         None
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
#
#  示例:
#  输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
#
#  进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
#  Related Topics 数学
"""
__author__ = 'haochen214934'
class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            x=num//10
            y=num%10
            num=x+y
        return num

    def addDigits1(self, num: int) -> int:
        if num%9==0 and num!=0:
            num=9
        else:
            num=num%9
        return num

if __name__ == '__main__':
    s=Solution()
    num=12345
    flag=s.addDigits1(num)
    print(flag)