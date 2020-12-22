# -*- coding: utf-8 -*-
"""
@File    :   快乐数.py    
@Contact :   smilemilks@qq.com
@Author  :   haochen214934
@Create Time      @Version    @Desciption
------------      --------    -----------
2020/12/18 17:26    1.0         None
# 编写一个算法来判断一个数 n 是不是快乐数。
#
#  「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为 1，那么这个数就是快乐数。
#
#  如果 n 是快乐数就返回 True ；不是，则返回 False 。
#
#  示例：
#  输入：19
# 输出：true
# 解释：
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#
#  Related Topics 哈希表 数学
"""
__author__ = 'haochen214934'

class Solution:
    def bitSquareSum(self,n):#求整数每位数相加和
        sum=0
        while n>0:
            bit=n%10
            sum=sum+bit**2
            n=n//10
        return sum

    #双指针
    '''
    循环迭代地计算每一次输出的各位平方和，如果出现1，则输入数字是快乐数，
    此外，我们用一个临时列表sq记录已经出现过的各位平方和，查看每次计算出各位平方和是否在列表中出现过，
    若出现过，则之后的计算会循环下去，无法得到各位平方和为1的结果，不是快乐数
    '''
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=n
        while True:
            slow=self.bitSquareSum(slow)
            fast=self.bitSquareSum(fast)
            fast = self.bitSquareSum(fast)
            if fast==slow:
                break
        return slow==1




if __name__ == '__main__':
    s=Solution()
    n=171
    flag=s.isHappy(n)
    print(flag)